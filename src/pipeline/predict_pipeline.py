import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self, features):
        try:
            model_path = 'C:\\Users\\semwa\\OneDrive\\Desktop\\MLproject\\src\\components\\artifacts\\model.pkl'
            preprocessor_path = 'C:\\Users\\semwa\\OneDrive\\Desktop\\MLproject\\src\\components\\artifacts\\preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            raise CustomException(e, sys)
        
class CustomData:
    def __init__(self,
                 gender,
                 parental_level_of_education,
                 lunch,
                 race_ethnicity,
                 test_preparation_course,
                 reading_score,
                 writing_score):
        self.gender = gender
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.race_ethnicity = race_ethnicity
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    def get_data_as_dataframe(self):
      try:
        custom_data_input_dict = {
            "gender": [self.gender.lower()],
            "race_ethnicity": [self.race_ethnicity],  # FIXED
            "parental_level_of_education": [self.parental_level_of_education.lower()],  # FIXED
            "lunch": [self.lunch.lower()],  # FIXED
            "test_preparation_course": [self.test_preparation_course.lower()],  # FIXED
            "reading_score": [self.reading_score],  # FIXED
            "writing_score": [self.writing_score]   # FIXED
        }

        return pd.DataFrame(custom_data_input_dict)

      except Exception as e:
        raise CustomException(e, sys)

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            raise CustomException(e, sys)