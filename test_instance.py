import pulumi
import pulumi_oci as oci

instance = ec2.Instance("myInstance", instance_type="t2.micro", ami="myAMI")