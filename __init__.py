from nautobot.apps.jobs import (
    register_jobs,
    StringVar,
    IPAddressVar,
    IntegerVar,
)
from nautobot_design_builder.design_job import DesignJob


class NxosVpcCoreDesign(DesignJob):
    """Generate config for an NX-OS vPC core switch pair."""

    hostname_core1 = StringVar(
        label="Core 1 hostname",
        description="Hostname of the first core switch",
    )

    hostname_core2 = StringVar(
        label="Core 2 hostname",
        description="Hostname of the second core switch",
    )

    domain_name = StringVar(
        label="Domain name",
        required=False,
        default="example.com",
    )

    mgmt_vrf = StringVar(
        label="Management VRF",
        required=False,
        default="management",
    )

    mgmt_ip_core1 = IPAddressVar(
        label="Core 1 management IP",
    )

    mgmt_ip_core2 = IPAddressVar(
        label="Core 2 management IP",
    )

    vpc_domain_id = IntegerVar(
        label="vPC domain ID",
        required=True,
        default=10,
    )

    vpc_peer_link_iface = StringVar(
        label="vPC peer-link port-channel",
        required=True,
        default="port-channel10",
    )

    vpc_keepalive_source = StringVar(
        label="vPC keepalive source interface",
        required=True,
        default="mgmt0",
    )

    vpc_keepalive_dest = IPAddressVar(
        label="vPC keepalive destination IP",
        required=True,
    )

    has_sensitive_variables = False

    class Meta:
        """Metadata for the NX-OS vPC core design."""

        name = "NX-OS vPC Core Pair"
        # Don’t commit by default; you can turn this on later if you want.
        commit_default = False

        # Path to your design file relative to the repo root:
        # adjust this if you use a different name/location.
        design_file = "designs/nxos_vpc_core.yaml"

        # If you don’t need extra context logic, just omit context_class entirely.
        nautobot_version = ">=2"


# This is what Nautobot shows in the Jobs UI as the "job group" name
name = "Nexus Designs"

# Register the job so Nautobot knows about it
register_jobs(NxosVpcCoreDesign)
