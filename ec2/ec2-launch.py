#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2',region_name='ap-southeast-1')
#for instance in ec2.instances.all():
#    print instance.id, instance.state

instance = ec2.create_instances(

   ImageId="ami-77af2014",
   MinCount=1,
   MaxCount=1,
   InstanceType="t2.micro")
print instance[0].id




