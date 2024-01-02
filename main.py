import tkinter as tk
from tkinter import messagebox

# Function to calculate tax based on given salary
def calculate_tax(salary):
    # Define tax-free allowance and tax rate thresholds
    tax_free_allowance = 12570
    basic_rate_threshold = 50270
    higher_rate_threshold = 125140
    x = 0

    if salary > 100000:
        x += (salary - 100000) / 2
        if x >= 12070:
            tax_free_allowance = 0
        else:
            tax_free_allowance = x

    # Tax calculation based on salary thresholds
    if salary <= tax_free_allowance:
        # No tax for salaries below or equal to tax-free allowance
        tax = 0
    elif salary <= basic_rate_threshold:
        # Calculate tax for salary within basic rate threshold
        taxable_income = salary - tax_free_allowance
        tax = taxable_income * 0.2  # 20% tax rate
    elif salary <= higher_rate_threshold:
        # Calculate tax for salary within higher rate threshold
        basic_tax = basic_rate_threshold * 0.2
        remaining_income = salary - basic_rate_threshold
        higher_tax = remaining_income * 0.4  # 40% tax rate
        tax = basic_tax + higher_tax
    else:
        # Calculate tax for salary exceeding higher rate threshold
        basic_tax = basic_rate_threshold * 0.2
        higher_tax = (higher_rate_threshold - basic_rate_threshold) * 0.4
        additional_tax = (salary - higher_rate_threshold) * 0.45  # 45% tax rate
        tax = basic_tax + higher_tax + additional_tax

    # Return the calculated tax rounded to 2 decimal places
    return round(tax, 2)

# Calculates national insurance contributions based on salary
def calculate_national_insurance(salary):
    # Define national insurance thresholds and rates
    ni_threshold = 12570
    ni_lower_limit = 50270
    ni_upper_limit = 50270
    lower_rate = 0.12
    upper_rate = 0.02

    # NI calculation based on salary thresholds
    if salary <= ni_threshold:
        # No NI for salaries below or equal to NI threshold
        ni = 0
    elif salary <= ni_lower_limit:
        # Calculate NI for salary within lower NI limit
        ni = (salary - ni_threshold) * lower_rate  # 12% NI rate
    elif salary <= ni_upper_limit:
        # Calculate NI for salary within upper NI limit
        ni = (ni_lower_limit - ni_threshold) * lower_rate
    else:
        # Calculate NI for salary exceeding upper NI limit
        ni = (ni_lower_limit - ni_threshold) * lower_rate + (salary - ni_upper_limit) * upper_rate  # Mixed rates

    # Return the calculated national insurance rounded to 2 decimal places
    return round(ni, 2)

# Calculates student loan repayment amount based on salary and plan
def calculate_student_loan(salary, plan=None):
    # Define plan-specific thresholds and repayment rates
    plan_thresholds = {
        "1": 22015,
        "2": 27295,
        "3": 21000,
        "4": 27660,
        "5": 25000
    }

    plan_repayment_rates = {
        "1": 0.09,
        "2": 0.09,
        "3": 0.06,
        "4": 0.09,
        "5": 0.09
    }

    # Checks if a valid plan is provided and calculates repayment amount accordingly
    if plan and plan in plan_thresholds:
        threshold = plan_thresholds[plan]
        if salary > threshold:
            repayment_rate = plan_repayment_rates[plan]
            repayment_amount = (salary - threshold) * repayment_rate
            return round(repayment_amount, 2)  # Calculate repayment amount and round to 2 decimal places

    return 0  # Return 0 if no valid plan or if salary is below the repayment threshold


# Formats large numbers to a currency format
def format_large_number(num):
    return f"{num:,.2f}"  # Format the number to have commas for thousands and two decimal places

# Calculates monthly deductions for tax, NI, student loan, and take-home pay
def calculate_monthly_deductions(salary, student_loan_plan=None):
    # Calculate tax, NI, and student loan deductions annually, then convert to monthly values
    tax = calculate_tax(salary) / 12  # Calculate annual tax, divide by 12 for monthly
    ni = calculate_national_insurance(salary) / 12  # Calculate annual NI, divide by 12 for monthly

    student_loan = calculate_student_loan(salary, student_loan_plan) / 12  # Calculate annual student loan, divide by 12 for monthly

    # Calculate monthly take-home pay after deductions
    take_home_pay_monthly = salary / 12 - tax - ni - student_loan  # Monthly salary after deductions

    # Return the monthly deductions for tax, NI, student loan, and take-home pay
    return tax, ni, student_loan, take_home_pay_monthly

# This function allows you to compare salaries
def compare_salaries():
    try:
        # Prompt the user to input details for Salary 1
        print("Enter details for Salary 1:")
        salary_1 = float(input("Enter the annual salary: £"))  # Get the annual salary for Salary 1 as input

        # Prompt the user to input details for Salary 2
        print("\nEnter details for Salary 2:")
        salary_2 = float(input("Enter the annual salary: £"))  # Get the annual salary for Salary 2 as input

        # Display deductions breakdown for Salary 1
        print("\nSalary 1 Deductions:")
        display_monthly_and_yearly_breakdown(salary_1)  # Call a function to display monthly and yearly deductions for Salary 1

        # Display deductions breakdown for Salary 2
        print("\nSalary 2 Deductions:")
        display_monthly_and_yearly_breakdown(salary_2)  # Call a function to display monthly and yearly deductions for Salary 2

    except ValueError:
        print("Please enter valid numerical salaries.")  # Handle an exception if non-numerical input is entered

# Displays monthly and yearly breakdown of deductions based on salary
def display_monthly_and_yearly_breakdown(salary):
    try:
        # Calculate yearly tax and national insurance
        tax_yearly = calculate_tax(salary)
        ni_yearly = calculate_national_insurance(salary)

        # Asks for the student loan plan and calculates monthly deductions
        student_loan_plan = input("\nDo you have a student loan plan?\n\nPlan 1 : if you Started your course / dergree before 2012 \nPlan 2 : If you started your course between the 1st of september 2012 and 31st july 2023 \nPlan 3 : Post Graduate Loan\nPlan 4 : If you applied to student awards agency scotland\nPlan 5 : If you started your course on or after august 1st 2023\n\nEnter (Plan 1/2/3/4/5 or leave empty: ")

        # Calculate monthly deductions for tax, national insurance, student loan, and take-home pay
        tax_monthly, ni_monthly, student_loan_monthly, take_home_pay_monthly = calculate_monthly_deductions(salary, student_loan_plan)

        # Format yearly numbers for display
        formatted_tax_yearly = format_large_number(tax_yearly)
        formatted_ni_yearly = format_large_number(ni_yearly)
        formatted_student_loan_yearly = format_large_number(student_loan_monthly * 12)

        # Format monthly numbers for display
        formatted_tax_monthly = format_large_number(tax_monthly)
        formatted_ni_monthly = format_large_number(ni_monthly)
        formatted_student_loan_monthly = format_large_number(student_loan_monthly)
        formatted_takehome_monthly = format_large_number(take_home_pay_monthly)

        total_yearly_deductions = tax_yearly + ni_yearly + (student_loan_monthly * 12)

        # Display breakdown of monthly and yearly deductions
        print ("\n\033[1m\033[3m(---------------------------------)")
        print("\nMonthly Breakdown:")
        print(f"Income Tax Paid Monthly: £{formatted_tax_monthly}")
        print(f"National Insurance Paid Monthly: £{formatted_ni_monthly}")
        print(f"Student Loan Repayment Monthly: £{formatted_student_loan_monthly}")
        print(f"Take Home pay Monthly: £{formatted_takehome_monthly}")

        print("\nYearly Deductions:")
        print(f"Total Income Tax Paid Yearly: £{formatted_tax_yearly}")
        print(f"Total National Insurance Paid Yearly: £{formatted_ni_yearly}")
        print(f"Total Student Loan Repayment Yearly: £{formatted_student_loan_yearly}")
        print(f"Total Take Home pay Yearly: £{format_large_number(salary - total_yearly_deductions)}")
        print ("\n(---------------------------------)\033[0m ")

    except ValueError:
        # Show an error message if a non-numeric value is entered for the salary
        print("Please enter a valid numerical salary.")


# Main function for user interaction and program execution
def calculate_button_clicked():
    try:
        # Get the salary entered in the GUI and convert it to a float
        salary = float(salary1_entry.get())

        # Check if entered salary is valid (not negative)
        if salary < 0:
            # Show an error message if the salary is negative and return
            messagebox.showerror("Error", "Please enter a valid salary amount.")
            return

        # Calculate monthly deductions based on the entered salary
        tax_monthly, ni_monthly, student_loan_monthly, take_home_pay_monthly = calculate_monthly_deductions(salary, student_loan_var1.get())

        # Calculate annual deductions based on monthly deductions
        tax_annual = tax_monthly * 12
        ni_annual = ni_monthly * 12
        student_loan_annual = student_loan_monthly * 12
        take_home_pay_annual = take_home_pay_monthly * 12

        # Update results in the GUI for the entered salary
        update_results(tax_monthly, ni_monthly, student_loan_monthly, take_home_pay_monthly, tax_annual, ni_annual, student_loan_annual, take_home_pay_annual, 1)

    except ValueError:
        # Show an error message if a non-numeric value is entered for the salary
        messagebox.showerror("Error", "Please enter a valid numerical salary.")

def compare_salaries():
    try:
        # Get the salary amounts entered in the GUI and convert them to floats
        salary_1 = float(salary1_entry.get())
        salary_2 = float(salary2_entry.get())

        # Check if entered salaries are valid (not negative)
        if salary_1 < 0 or salary_2 < 0:
            # Show an error message if salaries are negative and return
            messagebox.showerror("Error", "Please enter valid salary amounts.")
            return

        # Calculate monthly deductions for both salaries
        tax_1_monthly, ni_1_monthly, student_loan_1_monthly, take_home_1_monthly = calculate_monthly_deductions(salary_1, student_loan_var1.get())
        tax_2_monthly, ni_2_monthly, student_loan_2_monthly, take_home_2_monthly = calculate_monthly_deductions(salary_2, student_loan_var2.get())

        # Calculate annual deductions based on monthly deductions for both salaries
        tax_1_annual = tax_1_monthly * 12
        ni_1_annual = ni_1_monthly * 12
        student_loan_1_annual = student_loan_1_monthly * 12
        take_home_1_annual = take_home_1_monthly * 12

        tax_2_annual = tax_2_monthly * 12
        ni_2_annual = ni_2_monthly * 12
        student_loan_2_annual = student_loan_2_monthly * 12
        take_home_2_annual = take_home_2_monthly * 12

        # Update results for both salaries in the GUI
        update_results(tax_1_monthly, ni_1_monthly, student_loan_1_monthly, take_home_1_monthly, tax_1_annual, ni_1_annual, student_loan_1_annual, take_home_1_annual, 1)
        update_results(tax_2_monthly, ni_2_monthly, student_loan_2_monthly, take_home_2_monthly, tax_2_annual, ni_2_annual, student_loan_2_annual, take_home_2_annual, 2)

        # Update the comparison results in the GUI
        update_comparison_results(tax_1_monthly, ni_1_monthly, student_loan_1_monthly, take_home_1_monthly, tax_2_monthly, ni_2_monthly, student_loan_2_monthly, take_home_2_monthly)

    except ValueError:
        # Show an error message if non-numeric values are entered for salaries
        messagebox.showerror("Error", "Please enter valid numerical salaries.")

def update_results(tax_monthly, ni_monthly, student_loan_monthly, take_home_pay_monthly,
                   tax_annual, ni_annual, student_loan_annual, take_home_pay_annual, salary_number):
    # Check if it's the first or second salary to update the respective labels
    if salary_number == 1:
        # Assigning labels for the first salary
        tax_result_label = tax_result_label_1
        ni_result_label = ni_result_label_1
        student_loan_result_label = student_loan_result_label_1
        take_home_result_label = take_home_result_label_1
    else:
        # Assigning labels for the second salary
        tax_result_label = tax_result_label_2
        ni_result_label = ni_result_label_2
        student_loan_result_label = student_loan_result_label_2
        take_home_result_label = take_home_result_label_2

    # Updating the labels with the calculated results for each salary
    tax_result_label.config(text=f"Income Tax\n(Annual): £{format_large_number(tax_annual)}\n(Monthly): £{format_large_number(tax_monthly)}")
    ni_result_label.config(text=f"National Insurance\n(Annual): £{format_large_number(ni_annual)}\n(Monthly): £{format_large_number(ni_monthly)}")
    student_loan_result_label.config(text=f"Student Loan\n(Annual): £{format_large_number(student_loan_annual)}\n(Monthly): £{format_large_number(student_loan_monthly)}")
    take_home_result_label.config(text=f"Take Home Pay\n(Annual): £{format_large_number(take_home_pay_annual)}\n(Monthly): £{format_large_number(take_home_pay_monthly)}")

def update_comparison_results(tax_1_monthly, ni_1_monthly, student_loan_1_monthly, take_home_1_monthly,
                              tax_2_monthly, ni_2_monthly, student_loan_2_monthly, take_home_2_monthly):
    # Calculate the monthly differences between the two salaries
    tax_diff_monthly = tax_1_monthly - tax_2_monthly
    ni_diff_monthly = ni_1_monthly - ni_2_monthly
    student_loan_diff_monthly = student_loan_1_monthly - student_loan_2_monthly
    take_home_diff_monthly = take_home_1_monthly - take_home_2_monthly

    # Calculate the annual differences based on the monthly differences
    tax_diff_annual = tax_diff_monthly * 12
    ni_diff_annual = ni_diff_monthly * 12
    student_loan_diff_annual = student_loan_diff_monthly * 12
    take_home_diff_annual = take_home_diff_monthly * 12

    # Update the labels in the GUI with the calculated differences
    tax_diff_label.config(
        text=f"Income Tax Difference\n(Monthly): £{format_large_number(tax_diff_monthly)}\n(Annual): £{format_large_number(tax_diff_annual)}")
    ni_diff_label.config(
        text=f"National Insurance Difference\n(Monthly): £{format_large_number(ni_diff_monthly)}\n(Annual): £{format_large_number(ni_diff_annual)}")
    student_loan_diff_label.config(
         text=f"Student Loan Difference\n(Monthly): £{format_large_number(student_loan_diff_monthly)}\n(Annual): £{format_large_number(student_loan_diff_annual)}")
    take_home_diff_label.config(
        text=f"Take Home Pay Difference\n(Monthly): £{format_large_number(take_home_diff_monthly)}\n(Annual): £{format_large_number(take_home_diff_annual)}")

# Creating the main application window
root = tk.Tk()
root.title("Salary Deductions Calculator")  # Setting the window title

# First Salary Section
salary1_frame = tk.Frame(root)  # Creating a frame for the first salary section
salary1_frame.pack(side=tk.LEFT, padx=10, pady=10)  # Packing the frame to the left with padding

# Widgets for the first salary section
salary1_label = tk.Label(salary1_frame, text="First Salary")  # Label for the first salary
salary1_label.pack()  # Packing the label into the frame

salary1_entry = tk.Entry(salary1_frame)  # Entry field for entering the first salary
salary1_entry.pack()  # Packing the entry field

student_loan_var1 = tk.StringVar()
student_loan_var1.set("None")  # Variable to store the selected student loan plan

student_loan1_label = tk.Label(salary1_frame, text="Student Loan Plan:")  # Label for student loan selection
student_loan1_label.pack()  # Packing the label

student_loan_menu1 = tk.OptionMenu(salary1_frame, student_loan_var1, "None", "1", "2", "3", "4", "5")
student_loan_menu1.pack()  # Packing the student loan menu

calculate_button = tk.Button(salary1_frame, text="Calculate", command=calculate_button_clicked)
calculate_button.pack()  # Packing the 'Calculate' button

# Labels to display calculated results
tax_result_label_1 = tk.Label(salary1_frame, text="Income Tax (Monthly): ")
tax_result_label_1.pack()

ni_result_label_1 = tk.Label(salary1_frame, text="National Insurance (Monthly): ")
ni_result_label_1.pack()

student_loan_result_label_1 = tk.Label(salary1_frame, text="Student Loan (Monthly): ")
student_loan_result_label_1.pack()

take_home_result_label_1 = tk.Label(salary1_frame, text="Take Home Pay (Monthly): ")
take_home_result_label_1.pack()

# Comparison and Second Salary Section
comparison_frame = tk.Frame(root)  # Frame for displaying the comparison between salaries
comparison_frame.pack(side=tk.LEFT, padx=10, pady=10)  # Packing the frame

# Labels for displaying differences between salaries
comparison_label = tk.Label(comparison_frame, text="Difference")
comparison_label.pack()

tax_diff_label = tk.Label(comparison_frame, text="Income Tax Difference (Monthly): ")
tax_diff_label.pack()

ni_diff_label = tk.Label(comparison_frame, text="National Insurance Difference (Monthly): ")
ni_diff_label.pack()

student_loan_diff_label = tk.Label(comparison_frame, text="Student Loan Difference (Monthly): ")
student_loan_diff_label.pack()

take_home_diff_label = tk.Label(comparison_frame, text="Take Home Pay Difference (Monthly): ")
take_home_diff_label.pack()

# Second Salary Section
salary2_frame = tk.Frame(root)  # Frame for the second salary section
salary2_frame.pack(side=tk.LEFT, padx=10, pady=10)  # Packing the frame

# Widgets for the second salary section
salary2_label = tk.Label(salary2_frame, text="Second Salary")  # Label for the second salary
salary2_label.pack()  # Packing the label

salary2_entry = tk.Entry(salary2_frame)  # Entry field for entering the second salary
salary2_entry.pack()  # Packing the entry field

student_loan_var2 = tk.StringVar()
student_loan_var2.set("None")  # Variable to store the selected student loan plan for the second salary

student_loan2_label = tk.Label(salary2_frame, text="Student Loan Plan:")  # Label for student loan selection
student_loan2_label.pack()  # Packing the label

student_loan_menu2 = tk.OptionMenu(salary2_frame, student_loan_var2, "None", "1", "2", "3", "4", "5")
student_loan_menu2.pack()  # Packing the student loan menu

compare_button = tk.Button(salary2_frame, text="Compare Salaries", command=compare_salaries)
compare_button.pack()  # Packing the 'Compare Salaries' button

# Labels to display calculated results for the second salary
tax_result_label_2 = tk.Label(salary2_frame, text="Income Tax (Monthly): ")
tax_result_label_2.pack()

ni_result_label_2 = tk.Label(salary2_frame, text="National Insurance (Monthly): ")
ni_result_label_2.pack()

student_loan_result_label_2 = tk.Label(salary2_frame, text="Student Loan (Monthly): ")
student_loan_result_label_2.pack()

take_home_result_label_2 = tk.Label(salary2_frame, text="Take Home Pay (Monthly): ")
take_home_result_label_2.pack()

root.mainloop()  # Running the main event loop for the application
