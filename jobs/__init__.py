"""Design Builder job(s) for Nexus VPC core."""

from nautobot.apps.jobs import register_jobs
from nautobot_design_builder.design_job import DesignJob


class NxosVpcCoreDesign(DesignJob):
    """Generate base configuration for an NX-OS VPC core pair."""

    class Meta:
        name = "NXOS VPC Core Design"
        commit_default = False  # Just render configs; don't touch DB
        design_file = "designs/nxos_vpc_core.yaml.j2"
        nautobot_version = ">=2"


# This name is what shows up in the Job list grouping
name = "Demo Designs"

# Register this job with Nautobot
register_jobs(NxosVpcCoreDesign)
