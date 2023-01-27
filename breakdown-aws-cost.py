import boto3
from datetime import datetime, timedelta

# Create a Cost Explorer client
ce = boto3.client('ce')

# Get the current date and the date one month ago
now = datetime.now()
start_date = (now - timedelta(days=0)).strftime('%Y-%m-01')
end_date = now.strftime('%Y-%m-%d')

# Get the cost and usage data for the last month
response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='MONTHLY',
    Metrics=['UnblendedCost'],
    GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
)

# Get the breakdown of costs by service
cost_breakdown = response['ResultsByTime'][0]['Groups']

# Print the breakdown of costs by service
for service in cost_breakdown:
    print(f'{service["Keys"][0]}: {service["Metrics"]["UnblendedCost"]["Amount"]}')