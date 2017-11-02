import boto3
ec2 = boto3.resource('ec2')
cloudwatch = boto3.client('cloudwatch')
def createAlarm(tInstanceId):
    # Create alarm
    aname = tInstanceId + "_Server_CPU_Credit_Balance"
    cloudwatch.put_metric_alarm(
    AlarmName=aname,
    ComparisonOperator='LessThanThreshold',
    EvaluationPeriods=2,
    MetricName='CPUCreditBalance',
    Namespace='AWS/EC2',
    Period=1800,
    Statistic='Average',
    Threshold=100,
    ActionsEnabled=False,
    AlarmDescription=' Test Alarm when server CPU Credit',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': tInstanceId
        },
    ],
    Unit='Count'
    )
t2instances = []
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    if "t2" in instance.instance_type:
        print(instance.id, instance.instance_type)
        #t2instances.append(instance.id)
        #createAlarm(instance.id)
