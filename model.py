import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import tensorflow
#from tensorflow.keras.models import load_model

from data_cleaning import calculateModelParameters

def createModelDataframe(username):
    
    user_dict = calculateModelParameters(username)

    user_parameters_df = pd.DataFrame(user_dict, index=[0])

    #print(user_parameters_df)
    return user_parameters_df

def modelIE(username):
    
    #Load user data
    test_df = createModelDataframe(username)

    #Determine if they're I or E
    model = tensorflow.keras.models.load_model('Models/NN_ie.h5')

    ie_predict = model.predict_classes(test_df)

    if ie_predict[0] == 0:
        ie_result = "I"
    else:
        ie_result = "E"

    return ie_result

def modelNS(username):
    
    #Load user data
    test_df = createModelDataframe(username)

    #Determine if they're N or S
    model = tensorflow.keras.models.load_model('Models/NN_ns.h5')

    ns_predict = model.predict_classes(test_df)

    if ns_predict[0] == 0:
        ns_result = "N"
    else:
        ns_result = "S"

    return ns_result

def modelFT(username):
    
    #Load user data
    test_df = createModelDataframe(username)

    #Determine if they're F or T
    model = tensorflow.keras.models.load_model('Models/NN_ft.h5')

    ft_predict = model.predict_classes(test_df)

    if ft_predict[0] == 0:
        ft_result = "F"
    else:
        ft_result = "T"

    return ft_result

def modelJP(username):

    #Load user data
    test_df = createModelDataframe(username)

    #Determine if they're J or P
    model = tensorflow.keras.models.load_model('Models/NN_jp.h5')

    jp_predict = model.predict_classes(test_df)

    if jp_predict[0] == 0:
        jp_result = "J"
    else:
        jp_result = "P"

    return jp_result

def personalityTypeResult(username):

    ie_result = modelIE(username)
    ns_result = modelNS(username)
    ft_result = modelFT(username)
    jp_result = modelJP(username)
   
    personality_result = (f'Your personality type is {ie_result[0]}{ns_result[0]}{ft_result[0]}{jp_result[0]}!')

    #print(personality_result)
    return(personality_result)


#username = input("Input username:")
#personalityTypeResult(username)
