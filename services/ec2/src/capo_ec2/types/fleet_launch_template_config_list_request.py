"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateConfigListRequest``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_launch_template_config_request

FleetLaunchTemplateConfigListRequest: TypeAlias = list[
    "capo_ec2.types.fleet_launch_template_config_request.FleetLaunchTemplateConfigRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateConfigListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.fleet_launch_template_config_request

        capo_ec2.types.fleet_launch_template_config_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> FleetLaunchTemplateConfigListRequest:
    import capo_ec2.types.fleet_launch_template_config_request

    out: FleetLaunchTemplateConfigListRequest = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.fleet_launch_template_config_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FleetLaunchTemplateConfigListRequest:
    import capo_ec2.types.fleet_launch_template_config_request

    out: FleetLaunchTemplateConfigListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.fleet_launch_template_config_request.deserialize_ec2_query(
                child
            )
        )
    return out


def redact_sensitive(value: FleetLaunchTemplateConfigListRequest) -> list[Any]:
    import capo_ec2.types.fleet_launch_template_config_request

    return [
        capo_ec2.types.fleet_launch_template_config_request.redact_sensitive(item)
        for item in value
    ]
