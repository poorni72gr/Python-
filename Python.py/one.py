
import pandas as pd
import matplotlib.pyplot as plt
vehicles = pd.DataFrame({
    "Reg_No": ["KA01AB1234", "KA02CD5678", "KA03EF9012"],
    "Vehicle_Type": ["Car", "Truck", "Bike"],
    "Balance": [500, 800, 200]
})
toll_rates = {
    "Car": 100,
    "Truck": 200,
    "Bike": 50
}

print("Vehicle Database:")
print(vehicles)
print(toll_rates)
def process_vehicle(reg_no):
    global vehicles, transactions
    
    # Find vehicle
    vehicle = vehicles[vehicles["Reg_No"] == reg_no]
    
    if vehicle.empty:
        print("Vehicle not found!")
        return
    
    v_type = vehicle.iloc[0]["Vehicle_Type"]
    balance = vehicle.iloc[0]["Balance"]
    toll = toll_rates[v_type]
    
    # Check balance
    if balance >= toll:
        new_balance = balance - toll
        
        # Update balance
        vehicles.loc[vehicles["Reg_No"] == reg_no, "Balance"] = new_balance
        
        # Record transaction
        new_entry = pd.DataFrame([{
            "Reg_No": reg_no,
            "Vehicle_Type": v_type,
            "Toll_Amount": toll,
            "Remaining_Balance": new_balance
        }])
        
        transactions = pd.concat([transactions, new_entry], ignore_index=True)
        
        print(f"Toll deducted for {reg_no}. Remaining balance: {new_balance}")
    else:
        print(f"Insufficient balance for {reg_no}")


