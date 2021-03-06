from sklearn import metrics as skmetrics
#TODO: import metrics from other cool libraries for multilabel and multicass classfication and put it here.
#or you can implement your own meterics as you wish.

class ClassificationMetrics:
    def __init__(self):
        self.metrics = {
            "accuracy":self._accuracy,
            "auc": self._auc,
            "f1": self._f1,
            "recall": self._recall,
            "precision": self._precision,
            "logloss": self._logloss
            
        }

        #__init__ for class and __call__ for object.

    def __call__(self, metric, y_true, y_pred, y_proba=None):
        #statisfy predict probability condition
        #  for  logloss and auc score
        
        if metric not in self.metrics:
            raise NotImplementedError("metrics not implemented")

        if metric == "auc":
            if y_proba is not None:
                return self._auc(y_true=y_true, y_pred=y_proba)
            else:
                raise Exception('y_proba cannot be None for AUC')
        
        elif metric == "logloss":
            if y_proba is not None:
                return self._logloss(y_true=y_true, y_pred=y_proba)
            else:
                return Exception('y_proba cannot be none for logloss')
        else:
            return self.metrics[metric](y_true=y_true, y_pred=y_pred)
        
    
    @staticmethod
    def _accuracy(y_true, y_pred):
        return skmetrics.accuracy_score(y_true= y_true, y_pred = y_pred)

    @staticmethod
    def _auc(y_true, y_pred):
        return skmetrics.roc_auc_score(y_true = y_true, y_score = y_pred)
    
    @staticmethod
    def _f1(y_true, y_pred):
        return skmetrics.f1_score(y_true=y_true, y_pred=y_pred)
    
    @staticmethod
    def _recall (y_true, y_pred):
        return skmetrics.recall_score(y_true=y_true, y_pred=y_pred)

    @staticmethod
    def _precision (y_true, y_pred):
        return skmetrics.precision_score(y_true=y_true, y_pred=y_pred)
    
    @staticmethod
    def _logloss (y_true, y_pred):
        return skmetrics.log_loss(y_true=y_true, y_pred=y_pred)


    # @staticmethod
    # def some_cool_metric (*args):
    #     return metrics (*args)
    

    
    