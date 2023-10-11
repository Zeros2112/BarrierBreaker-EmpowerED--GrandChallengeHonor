import joblib 
import numpy as np
import numpy.ma as ma
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
import tabulate
from recsysNN_utils import * 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


pd.set_option("display.precision", 1)
item_train, user_train, y_train, item_features, user_features, item_vecs, movie_dict, user_to_genre = load_data()

num_user_features = user_train.shape[1] - 3  # remove userid, rating count and ave rating during training
num_item_features = item_train.shape[1] - 1  # remove movie id at train time
uvs = 3  # user genre vector start
ivs = 3  # item genre vector start
u_s = 3  # start of columns to use in training, user
i_s = 1  # start of columns to use in training, items
print(f"Number of training vectors: {len(item_train)}")

# scale training data
item_train_unscaled = item_train
user_train_unscaled = user_train
y_train_unscaled    = y_train

scalerItem = StandardScaler()
scalerItem.fit(item_train)
item_train = scalerItem.transform(item_train)

scalerUser = StandardScaler()
scalerUser.fit(user_train)
user_train = scalerUser.transform(user_train)

scalerTarget = MinMaxScaler((-1, 1))
scalerTarget.fit(y_train.reshape(-1, 1))
y_train = scalerTarget.transform(y_train.reshape(-1, 1))
#ynorm_test = scalerTarget.transform(y_test.reshape(-1, 1))

print(np.allclose(item_train_unscaled, scalerItem.inverse_transform(item_train)))
print(np.allclose(user_train_unscaled, scalerUser.inverse_transform(user_train)))

loaded_model = joblib.load('finalized_model.sav')
new_user_id = 5000
new_rating_ave = 0.0
new_Course_Difficulty = 0.0
new_Business_And_Management = 5.0
new_Design = 0.0
new_Environmental_Science = 0.0
new_Arts_And_Humanities = 5.0
new_Computer_Science = 0.0
new_Data_Science = 0.0
new_Math_And_Logic = 0.0
new_Language_Learning = 5.0
new_Health = 0.0
new_Social_science = 0.0
new_Electrical_And_Mechanical_Engineering = 0.0
new_Digital_Marketing = 0.0
new_Physics_And_Astronomy = 0.0
new_rating_count = 3

user_vec = np.array([[new_user_id, new_rating_count, new_rating_ave,
                      new_Course_Difficulty, new_Business_And_Management, new_Design, new_Environmental_Science,
                      new_Arts_And_Humanities, new_Computer_Science, new_Data_Science,
                      new_Math_And_Logic, new_Language_Learning, new_Health, new_Social_science ,
                      new_Electrical_And_Mechanical_Engineering, new_Digital_Marketing, new_Physics_And_Astronomy]])

# generate and replicate the user vector to match the number movies in the data set.
user_vecs = gen_user_vecs(user_vec,len(item_vecs))

# scale our user and item vectors
suser_vecs = scalerUser.transform(user_vecs)
sitem_vecs = scalerItem.transform(item_vecs)

# make a prediction
y_p = loaded_model.predict([suser_vecs[:, u_s:], sitem_vecs[:, i_s:]])

# unscale y prediction 
y_pu = scalerTarget.inverse_transform(y_p)

# sort the results, highest prediction first
sorted_index = np.argsort(-y_pu,axis=0).reshape(-1).tolist()  #negate to get largest rating first
sorted_ypu   = y_pu[sorted_index]
sorted_items = item_vecs[sorted_index]  #using unscaled vectors for display

print_pred_movies(sorted_ypu, sorted_items, movie_dict, maxcount = 10)