# demo_designs_testing/jobs/nexus_vpc/__init__.py

from nautobot.apps.jobs import register_jobs, StringVar, IPNetworkVar
from nautobot_design_builder.design_job import DesignJob

from .context import NexusVpcContext


class NexusVpcCoreDesign(DesignJob):
    """Design for a Nexus VPC core switch pair."""

    # Example vars - adjust to whatever you actually defined
    site_code = StringVar(
        label="Site code",
        description="Short site identifier, e.g. RIV01",
        regex=r"\w{3}\d+",
    )

    vpc_domain_id = StringVar(
        label="vPC Domain ID",
        description="Numeric vPC domain ID (e.g. 10)",
    )

    mgmt_prefix = IPNetworkVar(
        label="Management subnet",
        description="Subnet for mgmt SVI / loopbacks",
        min_prefix_length=24,
        max_prefix_length=30,
    )

    has_sensitive_variables = False

    class Meta:
        """Metadata for the Nexus VPC design."""

        name = "Nexus VPC Core Design"
        commit_default = False          # start in dry-run mode
        design_file = "designs/0001_design.yaml.j2"
        context_class = NexusVpcContext  # 🔑 this was missing
        nautobot_version = ">=2"


name = "Demo Designs"
register_jobs(NexusVpcCoreDesign)
