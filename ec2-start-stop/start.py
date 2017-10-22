
import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all stopped EC2 instances.
    filters = [{
            'Name': 'tag:AutoOff',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all stopped instances
    SelectedInstances = [instance.id for instance in instances]
    
    #print the instances for logging purposes
    print SelectedInstances 
    
    #make sure there are actually instances to start up. 
    if len(SelectedInstances) > 0:
        #perform the startup
        startingUp = ec2.instances.filter(InstanceIds=SelectedInstances).start()
        print startingUp
    else:
        print "Nothing to see here"
