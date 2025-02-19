# Property Tax Calculator for Jaffrey, NH
def calculate_tax(property_value, school_tax_rate):
    # Fixed tax components based on $32.80 total tax rate
    state_ed_rate = 32.80 * (6 / 100)
    municipal_rate = 32.80 * (32 / 100)
    county_rate = 32.80 * (12 / 100)
    
    # Calculate annual school tax based on school tax rate
    school_tax = (property_value / 1000) * school_tax_rate
    
    # Calculate total property tax correctly, ensuring fixed non-school components
    total_tax = (property_value / 1000) * (32.80 - 16.22 + school_tax_rate)
    
    return school_tax_rate, school_tax, total_tax

def calculate_distribution(school_tax, property_value):
    return {
        "School": school_tax,
        "State Ed": (property_value / 1000) * (32.80 * (6 / 100)),
        "Municipal": (property_value / 1000) * (32.80 * (32 / 100)),
        "County": (property_value / 1000) * (32.80 * (12 / 100))
    }

# Get user input
property_value = float(input("Enter your property value: "))

# Define three different school budget scenarios with their respective school tax rates
budgets = {
    "Current Budget": 16.22,  # Fixed school tax rate
    "Default Budget": 19.80,  # Adjusted default budget school tax rate
    "Cut Budget": 17.02  # Adjusted cut budget school tax rate
}

# Calculate current taxes
current_rate, current_school_tax, total_current_tax = calculate_tax(property_value, budgets["Current Budget"])
current_distribution = calculate_distribution(current_school_tax, property_value)

# Display results
print("\nProperty Tax Scenarios for Jaffrey, NH:")
print(f"Current Budget: School Tax Rate: ${current_rate:.2f} per $1000, Annual School Tax: ${current_school_tax:.2f}")
print("Breakdown:")
for category, amount in current_distribution.items():
    print(f"  {category}: ${amount:.2f}")
print(f"Total Property Tax: ${total_current_tax:.2f}")

for scenario, school_rate in budgets.items():
    if scenario == "Current Budget":
        continue
    new_rate, new_school_tax, total_new_tax = calculate_tax(property_value, school_rate)
    tax_difference = total_new_tax - total_current_tax
    new_distribution = calculate_distribution(new_school_tax, property_value)
    monthly_difference = tax_difference / 12
    print(f"\n{scenario}: School Tax Rate: ${new_rate:.2f} per $1000, Annual School Tax: ${new_school_tax:.2f}, Difference from Current: ${tax_difference:.2f}")
    print("Breakdown:")
    for category, amount in new_distribution.items():
        print(f"  {category}: ${amount:.2f}")
    print(f"Total Property Tax: ${total_new_tax:.2f}")
    print(f"Divided over 12 months: ${monthly_difference:.2f}/month")

print("\nThis calculator should be used for entertainment only. The projected tax is only an estimate based on the information gathered from the proposed warrant articles and the N.H. Department of Revenue Administration Municipal Tax Rates. The calculator is not sponsored and should not be considered 'Official' in any capacity.")

input("\nPress Enter to exit...")
