

patient_name = input("📝 Enter name of patient: \n")
patient_age = int(input("🎂 Enter the patient age: \n"))
temperature = int(input("🌡 Enter the patient temp in celsius: \n"))

if temperature > 40:
    print("🔥 Critical condition! Immediate attention required for " + patient_name + "\n") 
elif patient_age < 12 or temperature >= 38:
    print("🚑 Admit " + patient_name + " to the hospital immediately. 🏥\n")
else:
    print("✅ " + patient_name + " is stable. No admission required. 😊")