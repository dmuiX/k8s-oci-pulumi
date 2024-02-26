"""A OCI Python Pulumi program"""

import pulumi
import pulumi_oci as oci
from pulumi import Output
from pprint import pprint

myCompartment = oci.identity.Compartment("myCompartment", name="my-compartment", description="my-compartment",
                                         enable_delete=True)

namespace = Output.all(myCompartment.id).apply(
    lambda args: oci.objectstorage.get_namespace(compartment_id=args[0]))

myBucket = oci.objectstorage.Bucket("my-bucket", name="my-bucket", namespace=namespace.namespace,
                                     compartment_id=myCompartment.id)

# config = pulumi.Config()
oci_config = pulumi.Config("oci")
oci_region = oci_config.require("region")
pprint(oci_region)
pprint(pulumi.Config("oci:tenancyOcid"))
# pprint(vars(pulumi.Config()))

# Export the Instance label of the instance
# pulumi.export('name', myBucket.name)
