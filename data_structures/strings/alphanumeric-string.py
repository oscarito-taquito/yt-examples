# Check for invalid VINs

vins = [
  '5ADK2L8PV*9BG3SF1'
 ,'RT4NS9YHMJ8QA6PW2'
 ,'X7KY3DZMP6TF9VG1'
 ,'L2JK9SV4H$5ND8BQ6'
 ,'E3UH5PZ1MC4WR7YS9'
]


for vin in vins:
	if vin.isalnum():
		print(f'{vin} is a VIN')
	else:
		print(f'{vin} is not a VIN')
