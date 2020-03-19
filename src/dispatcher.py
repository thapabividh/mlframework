from sklearn import ensemble
import xgboost as xgb 

#ML MODELS
MODELS = {
    "randomforest": ensemble.RandomForestClassifier(
        n_estimators=200,
        n_jobs=-1,
        verbose=2),
    "extratrees": ensemble.ExtraTreesClassifier(
        n_estimators=200,
        n_jobs=-1,
        verbose=2),

    "xgboost": xgb.XGBRFClassifier(verbosity=2, 
        max_depth=4, 
        n_estimators=200, 
        n_jobs=-1)
}

#deep learning models:

DL_MODELS = {
    
}