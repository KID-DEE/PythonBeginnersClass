def calculate_material_cost():
    print("Welcome to D's Ventures what will you like to buy:\n1.Cement\n2.Sand\nGravel")
    choice=input("Enter here: ")
    cement=2500
    gravel=4500
    sand=3000
    if choice=="cement":
      bags=int(input("How many Bags will you buy: "))
      calc=bags*cement
      print(f"the price for {bags}bags of Cement is:{calc}")
    elif choice=="gravel":
       bags=int(input("How many Bags will you buy: "))
       calc=bags*gravel
       print(f"the price for {bags}bags of Cement is:{calc}")
    elif choice=="sand":
       bags=int(input("How many Bags will you buy: "))
       calc=bags*sand
       print(f"the price for {bags}bags of Cement is:{calc}")
    else:
       print("We do not have what you selected")
calculate_material_cost()  


print("\nno.2\n")


task_dict = {
    "Site Clearing": 12,
    "Foundation": 15,
    "Wall Construction": 24,
    "Roofing": 33,
    "Painting": 32
}
print(task_dict)
def estimate_project_days(task_dict):
    return sum(task_dict.values())
total_days = estimate_project_days(task_dict)
print("Total estimated project days:", total_days)
estimate_project_days(task_dict)


print("\nno.3\n")


def estimate_project_days():
   print("We have alot of tasks to do the total is: 160 tasks")
   ttask=160
   avworkers=int(input("please enter number of workers available: "))
   tpw=ttask/avworkers
   rtsks=ttask%avworkers
   print(f"total task per worker is:{tpw} ")
   if rtsks>=0:
      print("sufficiet workers")
   elif rtsks<0:
      print(f"Remaining tasks are:{rtsks}")
      print("insufficient workers")
estimate_project_days()



print("\nno.4\n")
def budget_summary():
   labour_cost=5000#per labourer
   material_cost=5500#per material
   equipment_rental=6500#per equipment
   date=150
   print("Welcome to D's")
   print("our prices are at:\nlabour_cost:5000 per labourer"\
   "\nmaterial_cost:5500 per material"\
   "\nequipment_rental:6500 per equipment"
   )
   l=int(input("How many labourers will you take:"))
   res=labour_cost*l
   print(f"The price for {l}labourers at:{labour_cost}per labourer is: {res} ")
   print("----------------------------")
   m=int(input("how many materials will you buy: " ))
   res2=material_cost*m
   print(f"The price for {m}labourers at:{material_cost}per labourer is: {res2} ")
   print("-----------------------------")
   e=int(input("how many equipments will you rent: " ))
   res3=equipment_rental*e
   days=int(input("For how many days will you rent each: "))
   print(f"The price for {e}equipments at:{equipment_rental}per equipment in {days*date}days is: {res3} ")
budget_summary()


print("\nno.5\n")
def check_safety_compliance():
    checklist_items = {
        "Fire Extinguisher": "",
        "First Aid Kit": "",
        "Safety Helmets": "",
        "Warning Signs": "",
        "Emergency Exit": ""
    }

    
    for item in checklist_items:
        status = input(f"Is '{item}' complete or incomplete? ").lower()
        checklist_items[item] = status


    for status in checklist_items.values():
        if status != "complete":
            print("Safety compliance check failed.")
            return False

    print("All safety checks are complete.")
    return True
check_safety_compliance()

print("\nno.6\n")
def track_equipment_usage():
    logs = [
        ("Excalator", 5),
        ("Crane", 3),
        ("Excavator", 2),
        ("Bulldozer", 4),
        ("Truck", 1)
    ]
    
    usage = {}
    for equipment, hours in logs:
        if equipment in usage:
            usage[equipment] += hours
        else:
            usage[equipment] = hours
    return usage
print(track_equipment_usage())
track_equipment_usage()

print("\n no.7\n")

def attendance_percentage():
    present_days=int(input("Please enter the number of days presesnt at work: "))
    total_days=200
    res=total_days-present_days
    percentage=present_days/total_days*100
    print(f"your work percentage is:{percentage}%")
attendance_percentage()

print("\nno.8\n")

def generate_invoice():
   print("Daliya's ventures")#this is no.1
   print("Good Day")
   name = input("please enter your full name:")
   print("welcome",name,"What will you like to buy:")
   print("here are what we offer:\nCakes:200/cake\nSoaps:150/soap\nBags:300/bag\nToothbrushes:100/toothbrush\nShoes:100/shoe")
   c=[
   ("cake",100,int(input("how many will you buy:")),
      "bread",200,int(input("how many will you buy:")),
      "wine",400,int(input("how many will you buy:")),
      )
   ]
    
   print(f"total invoice for: {name}")

print(generate_invoice())
generate_invoice()



print("\nno.9 \n") 
work_completed=int(input("how many works were completed"))
materials_used=int(input("how many materials were used"))
def efficiency_report(work_completed, materials_used):
        if materials_used == 0:
            return "Invalid: No materials used."
        
        efficiency = work_completed / materials_used

        if efficiency >= 1.0:
            efficiency = work_completed / materials_used
            return "Excellent"
        elif efficiency >= 0.75:
            efficiency = work_completed / materials_used
            return "Good"
        elif efficiency >= 0.5:
            efficiency = work_completed / materials_used
            return "Average"
        else:
         return "Poor"
        
