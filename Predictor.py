# Building AI Course Project
# Predicts dog or cat based on weight

print("Dog या Cat Predictor में आपका स्वागत है!")
weight = float(input("Pet का Weight kg में डालो: "))

# Simple AI rule: 5kg से कम = Cat, वरना = Dog
if weight < 5:
    print("Prediction: ये Cat है 🐱")
    print("Cats आमतौर पर हल्की होती हैं")
else:
    print("Prediction: ये Dog है 🐶")
    print("Dogs आमतौर पर भारी होते हैं")

print("Thanks for using my Building AI project!")
