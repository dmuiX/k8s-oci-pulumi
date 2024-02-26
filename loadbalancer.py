import pulumi
import pulumi_oci as oci

k8s_load_balancer = oci.load_balancer.LoadBalancer("k8s-lb",
    compartment_id=var["compartment_id"],
    display_name=var["load_balancer_display_name"],
    shape=var["load_balancer_shape"],
    subnet_ids=var["load_balancer_subnet_ids"],
    defined_tags={
        "Operations.CostCenter": "42",
    },
    freeform_tags={
        "Department": "Finance",
    },
    ip_mode=var["load_balancer_ip_mode"],
    is_private=var["load_balancer_is_private"],
    network_security_group_ids=var["load_balancer_network_security_group_ids"],
    reserved_ips=[oci.load_balancer.LoadBalancerReservedIpArgs(
        id=var["load_balancer_reserved_ips_id"],
    )],
    )