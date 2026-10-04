"""Generated from Smithy shape ``com.amazonaws.ecs#ResolvedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.service_revision_load_balancers
    import capo_ecs.types.service_revision_vpc_lattice_configurations


class ResolvedConfiguration(TypedDict, closed=True):
    load_balancers: NotRequired[
        "capo_ecs.types.service_revision_load_balancers.ServiceRevisionLoadBalancers"
    ]
    """<p>The resolved load balancer configuration for the service revision. This includes information about which target groups serve traffic and which listener rules direct traffic to them.</p>"""
    vpc_lattice_configurations: NotRequired[
        "capo_ecs.types.service_revision_vpc_lattice_configurations.ServiceRevisionVpcLatticeConfigurations"
    ]
    """<p>The resolved VPC Lattice configuration for the service revision. This includes information about which target groups serve traffic and which listener rules direct traffic to them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedConfiguration) -> dict:
    out: dict = {}
    if "load_balancers" in value:
        import capo_ecs.types.service_revision_load_balancers

        out["loadBalancers"] = (
            capo_ecs.types.service_revision_load_balancers.serialize_aws_json_1_1(
                value["load_balancers"]
            )
        )
    if "vpc_lattice_configurations" in value:
        import capo_ecs.types.service_revision_vpc_lattice_configurations

        out["vpcLatticeConfigurations"] = (
            capo_ecs.types.service_revision_vpc_lattice_configurations.serialize_aws_json_1_1(
                value["vpc_lattice_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedConfiguration:
    out: ResolvedConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("loadBalancers") is not None:
        import capo_ecs.types.service_revision_load_balancers

        out["load_balancers"] = (
            capo_ecs.types.service_revision_load_balancers.deserialize_aws_json_1_1(
                data["loadBalancers"]
            )
        )
    if data.get("vpcLatticeConfigurations") is not None:
        import capo_ecs.types.service_revision_vpc_lattice_configurations

        out["vpc_lattice_configurations"] = (
            capo_ecs.types.service_revision_vpc_lattice_configurations.deserialize_aws_json_1_1(
                data["vpcLatticeConfigurations"]
            )
        )
    return out
