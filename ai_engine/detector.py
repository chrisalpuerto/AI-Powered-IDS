# Loading the trained model and classifying packets

import joblib

# load trained model 
model = joblib.load('model1.pkl')

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
        return "BENIGN" if prediction == 0 else "ATTACK"
    except Exception as e:
        print(f"Error in classification: {e}")
        return None