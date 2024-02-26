import pulumi
import pulumi_oci as oci

# Create Instance
example_instance = oci.core.Instance("test_instance",
    # compartment_id=# This is a placeholder, replace with your actual Compartment OCID
    availability_domain="AD1", # This is a placeholder, replace with your desired Availability Domain
    shape="VM.Standard.E2.1.Micro", # This is a placeholder, replace with your desired Shape
    #agent_config=oci.core.InstanceAgentConfigArgs(
    #     is_monitoring_disabled=False,
    # ),
    # source_details=oci.core.InstanceSourceDetailsArgs(
    #     source_type="image",
    #     source_id="ocid1.image.oc1..aaaaaaaahjkmmew2pjrcwq3n7h5xa6d2dnk3zgy43hel4h5y3jea3i3okena", # This is a placeholder, replace with your actual Image OCID
    # ),
    # display_name="example-instance",
    # metadata={"ssh_authorized_keys": "your_public_ssh_key"}, # This is a placeholder, replace with your actual Public SSH Key
    # create_vnic_details=oci.core.InstanceCreateVnicDetailsArgs(
    #     subnet_id="ocid1.subnet.oc1..aaaaaaaamaxfi5tnrddmetjkqk743otxnjdtlk75ym67xqka3xp6hjsm3bpq", # This is a placeholder, replace with your actual Subnet OCID
    #     assign_public_ip=False,
    # )
)

pulumi.export("instance_id", example_instance.id)