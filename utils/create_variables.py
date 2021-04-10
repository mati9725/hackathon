def variables_generator(data):
    data['new_1'] = data['tGravityAcc-max()-Y'] * data['tGravityAcc-max()-Y']
    data['new_2'] = data['tGravityAcc-mean()-Y'] * data['tGravityAcc-mean()-Y']
    data['new_3'] = data['tGravityAcc-min()-Y'] * data['tGravityAcc-min()-Y']
    data['new_4'] = data['tGravityAcc-max()-Y'] * data['tGravityAcc-min()-Y']
    data['new_5'] = data['tGravityAcc-mean()-Y'] * data['tGravityAcc-mean()-Z']
    data['new_6'] = data['tGravityAcc-max()-Y'] - data['tGravityAcc-min()-Y']
    data['new_7'] = data['tGravityAcc-correlation()-X,Y'] * data['tGravityAcc-correlation()-X,Y'] * data['tGravityAcc-correlation()-X,Y']

    data['new_8'] = data['tGravityAcc-correlation()-X,Y'] + data['tGravityAcc-max()-Y']
    data['new_9'] = data['fBodyGyro-meanFreq()-Z'] + 2 * data['angle(Z,gravityMean)'] + data['angle(Y,gravityMean)']
    data['new_10'] = data['tGravityAcc-max()-Y'] + data['angle(Y,gravityMean)']
    data['new_11'] = data['tGravityAcc-mean()-Z'] * data['angle(Z,gravityMean)']
    data['new_12'] = data['angle(Y,gravityMean)'] + data['tGravityAcc-max()-Y']
    data['new_13'] = data['tGravityAcc-mean()-Z'] + data['tGravityAcc-min()-Y']
    data['new_14'] = data['angle(Y,gravityMean)'] + data['tBodyGyroJerk-arCoeff()-X,1']
    data['new_15'] = (data['fBodyGyro-entropy()-X'] * data['tGravityAcc-max()-Y']) + data['tGravityAcc-correlation()-X,Y']

    data['new_16'] = data['tGravityAcc-correlation()-X,Y'] * data['tGravityAcc-mean()-Y'] * data['tGravityAcc-min()-Y']
    data['new_17'] = data['tGravityAcc-mean()-Y'] * data['angle(Y,gravityMean)'] * data['fBodyGyro-mean()-X']
    data['new_18'] = data['tGravityAcc-max()-Y'] * data['tGravityAcc-mean()-Y'] * data['tGravityAcc-min()-Y']
    data['new_19'] = data['tGravityAcc-correlation()-X,Y'] * data['tGravityAcc-correlation()-X,Z']
    data['new_20'] = data['angle(Y,gravityMean)'] * data['angle(Y,gravityMean)'] * data['angle(Y,gravityMean)']
    data['new_21'] = data['tBodyGyro-arCoeff()-X,1'] * data['tBodyGyroJerk-arCoeff()-X,1'] 
    data['new_22'] = data['tGravityAcc-max()-Y'] - data['tGravityAcc-min()-Y']
    data['new_23'] = data['tGravityAcc-max()-Z'] - data['tGravityAcc-min()-Z']

    return data
