def variables_generator(data):
    data['new_1'] = data['tGravityAcc-max()-Y'] * data['tGravityAcc-max()-Y']
    data['new_2'] = data['tGravityAcc-mean()-Y'] * data['tGravityAcc-mean()-Y']
    data['new_3'] = data['tGravityAcc-min()-Y'] * data['tGravityAcc-min()-Y']
    data['new_4'] = data['tGravityAcc-max()-Y'] * data['tGravityAcc-min()-Y']
    data['new_5'] = data['tGravityAcc-mean()-Y'] * data['tGravityAcc-mean()-Z']
    data['new_6'] = data['tGravityAcc-max()-Y'] - data['tGravityAcc-min()-Y']
    data['new_7'] = data['tGravityAcc-correlation()-X,Y'] * data['tGravityAcc-correlation()-X,Y'] * data['tGravityAcc-correlation()-X,Y']
    data['new_8'] = data['angle(Y,gravityMean)'] * data['angle(Y,gravityMean)'] * data['angle(Y,gravityMean)']
    return data
