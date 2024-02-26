import pulumi
from pulumi_oci import core

# Create a new Virtual Cloud Network
vcn = core.Vcn("k8s-vcn",
    cidr_blocks=["10.0.0.0/16"],
    compartment_id=config.require("compartmentId"),
    dns_label="k8s-vcn",
    display_name="k8s-vcn")

# Export the VCN's OCID
pulumi.export("vcn_id", vcn.id)
