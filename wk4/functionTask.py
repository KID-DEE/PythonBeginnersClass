"""
1. Material Cost EstimatorWrite a function calculate_material_cost(material, quantity) that calculates the total 
cost of a material based on type (e.g., "cement", "sand", "gravel") and quantity. Use predefined unit prices.

2. Project Timeline EstimatorCreate a function estimate_project_days(task_dict) that takes a list of tasks with 
their estimated durations and returns the total number of days needed to complete the project.

3. Worker Allocation Calculator. Define a function allocate_workers(total_tasks, workers_available) that determines 
how many tasks each worker will handle and how many tasks will remain unassigned if not divisible.

4. Construction Budget PlannerWrite a function budget_summary(labor_cost, materials_cost, equipment_rental) that 
calculates the total project budget and breaks it down by category.

5. Site Safety Checklist ValidatorCreate a function check_safety_compliance(checklist) that returns True if all 
required safety items are marked as complete in a given dictionary, otherwise False.

6. Equipment Usage TrackerDefine a function track_equipment_usage(logs) where logs is a list of tuples 
(equipment_name, hours_used). Return a dictionary with total hours used per equipment.

7. Worker Attendance PercentageWrite a function attendance_percentage(present_days, total_days) that calculates and 
returns the attendance rate of a worker in percentage.

8. Invoice GeneratorCreate a function generate_invoice(client_name, items) where items is a list of tuples 
(description, unit_price, quantity). Return a detailed invoice summary as a dictionary or formatted string.

9. Resource Efficiency ReportDefine a function efficiency_report(work_completed, materials_used) that calculates 
how efficiently materials were used relative to the work done. Return a performance rating.

10. Permit Expiry Alert SystemWrite a function check_permit_expiry(permits) where permits is a dictionary of permit 
names and expiry dates. Return a list of permits expiring within the next 30 days.
"""