# Loading the trained model and classifying packets

import joblib
import numpy as np

# load trained model 
try: 
    model = joblib.load('model1.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def classify_packet(features):
    try:
        # prediction using our model
        prediction = model.predict([features])

        # interpret prediction

        #FOR CONTEXT:
        '''
        when training ML model, BENIGN = good/normal traffic 
        DoS, BoT, Infiltration, PortScan = bad/attack traffic
        BENIGN = 0, Attack Types = 1
        '''

        features_array = np.array(features)
        prediction = model.predict(features_array.reshape(1, -1))[0]
        return "BENIGN" if prediction == 0 else "ATTACK"
    except Exception as e:
        print(f"Error in classification: {e}")
        return None