"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyFleetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.fleet_excess_capacity_termination_policy
    import capo_ec2.types.fleet_id
    import capo_ec2.types.fleet_launch_template_config_list_request
    import capo_ec2.types.string
    import capo_ec2.types.target_capacity_specification_request


class ModifyFleetRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    excess_capacity_termination_policy: NotRequired[
        "capo_ec2.types.fleet_excess_capacity_termination_policy.FleetExcessCapacityTerminationPolicy"
    ]
    """<p>Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet.</p> <p>Supported only for fleets of type <code>maintain</code>.</p>"""
    launch_template_configs: NotRequired[
        "capo_ec2.types.fleet_launch_template_config_list_request.FleetLaunchTemplateConfigListRequest"
    ]
    """<p>The launch template and overrides.</p>"""
    fleet_id: NotRequired["capo_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""
    target_capacity_specification: NotRequired[
        "capo_ec2.types.target_capacity_specification_request.TargetCapacitySpecificationRequest"
    ]
    """<p>The size of the EC2 Fleet.</p>"""
    context: NotRequired["capo_ec2.types.string.String"]
    """<p>Reserved.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyFleetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "excess_capacity_termination_policy" in value:
        import capo_ec2.types.fleet_excess_capacity_termination_policy

        capo_ec2.types.fleet_excess_capacity_termination_policy.serialize_ec2_query(
            value["excess_capacity_termination_policy"],
            pairs,
            f"{key_prefix}ExcessCapacityTerminationPolicy",
        )
    if "launch_template_configs" in value:
        import capo_ec2.types.fleet_launch_template_config_list_request

        capo_ec2.types.fleet_launch_template_config_list_request.serialize_ec2_query(
            value["launch_template_configs"], pairs, f"{key_prefix}LaunchTemplateConfig"
        )
    if "fleet_id" in value:
        pairs.append((f"{key_prefix}FleetId", str(value["fleet_id"])))
    if "target_capacity_specification" in value:
        import capo_ec2.types.target_capacity_specification_request

        capo_ec2.types.target_capacity_specification_request.serialize_ec2_query(
            value["target_capacity_specification"],
            pairs,
            f"{key_prefix}TargetCapacitySpecification",
        )
    if "context" in value:
        pairs.append((f"{key_prefix}Context", str(value["context"])))


def deserialize_ec2_query(el: Element) -> ModifyFleetRequest:
    out: ModifyFleetRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_excess_capacity_termination_policy = el.find(
        "ExcessCapacityTerminationPolicy"
    )
    if child_excess_capacity_termination_policy is not None:
        import capo_ec2.types.fleet_excess_capacity_termination_policy

        out["excess_capacity_termination_policy"] = (
            capo_ec2.types.fleet_excess_capacity_termination_policy.deserialize_ec2_query(
                child_excess_capacity_termination_policy
            )
        )
    child_launch_template_configs = el.find("LaunchTemplateConfig")
    if child_launch_template_configs is not None:
        import capo_ec2.types.fleet_launch_template_config_list_request

        out["launch_template_configs"] = (
            capo_ec2.types.fleet_launch_template_config_list_request.deserialize_ec2_query(
                child_launch_template_configs
            )
        )
    child_fleet_id = el.find("FleetId")
    if child_fleet_id is not None:
        out["fleet_id"] = str(child_fleet_id.text or "")
    child_target_capacity_specification = el.find("TargetCapacitySpecification")
    if child_target_capacity_specification is not None:
        import capo_ec2.types.target_capacity_specification_request

        out["target_capacity_specification"] = (
            capo_ec2.types.target_capacity_specification_request.deserialize_ec2_query(
                child_target_capacity_specification
            )
        )
    child_context = el.find("Context")
    if child_context is not None:
        out["context"] = str(child_context.text or "")
    return out


def redact_sensitive(value: ModifyFleetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "launch_template_configs" in value:
        import capo_ec2.types.fleet_launch_template_config_list_request

        out["launch_template_configs"] = (
            capo_ec2.types.fleet_launch_template_config_list_request.redact_sensitive(
                value["launch_template_configs"]
            )
        )
    return out
