"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfigRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_launch_template_overrides_list_request
    import capo_ec2.types.fleet_launch_template_specification_request


class FleetLaunchTemplateConfigRequest(TypedDict, closed=True):
    launch_template_specification: NotRequired[
        "capo_ec2.types.fleet_launch_template_specification_request.FleetLaunchTemplateSpecificationRequest"
    ]
    """<p>The launch template to use. You must specify either the launch template ID or launch template name in the request. </p>"""
    overrides: NotRequired[
        "capo_ec2.types.fleet_launch_template_overrides_list_request.FleetLaunchTemplateOverridesListRequest"
    ]
    """<p>Any parameters that you specify override the same parameters in the launch template.</p> <p>For fleets of type <code>request</code> and <code>maintain</code>, a maximum of 300 items is allowed across all launch templates.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateConfigRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_specification" in value:
        import capo_ec2.types.fleet_launch_template_specification_request

        capo_ec2.types.fleet_launch_template_specification_request.serialize_ec2_query(
            value["launch_template_specification"],
            pairs,
            f"{key_prefix}LaunchTemplateSpecification",
        )
    if "overrides" in value:
        import capo_ec2.types.fleet_launch_template_overrides_list_request

        capo_ec2.types.fleet_launch_template_overrides_list_request.serialize_ec2_query(
            value["overrides"], pairs, f"{key_prefix}Overrides"
        )


def deserialize_ec2_query(el: Element) -> FleetLaunchTemplateConfigRequest:
    out: FleetLaunchTemplateConfigRequest = {}  # type: ignore[typeddict-item]
    child_launch_template_specification = el.find("LaunchTemplateSpecification")
    if child_launch_template_specification is not None:
        import capo_ec2.types.fleet_launch_template_specification_request

        out["launch_template_specification"] = (
            capo_ec2.types.fleet_launch_template_specification_request.deserialize_ec2_query(
                child_launch_template_specification
            )
        )
    child_overrides = el.find("Overrides")
    if child_overrides is not None:
        import capo_ec2.types.fleet_launch_template_overrides_list_request

        out["overrides"] = (
            capo_ec2.types.fleet_launch_template_overrides_list_request.deserialize_ec2_query(
                child_overrides
            )
        )
    return out


def redact_sensitive(value: FleetLaunchTemplateConfigRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "launch_template_specification" in value:
        import capo_ec2.types.fleet_launch_template_specification_request

        out["launch_template_specification"] = (
            capo_ec2.types.fleet_launch_template_specification_request.redact_sensitive(
                value["launch_template_specification"]
            )
        )
    return out
