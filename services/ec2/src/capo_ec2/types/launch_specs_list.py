"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchSpecsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_fleet_launch_specification

LaunchSpecsList: TypeAlias = list[
    "capo_ec2.types.spot_fleet_launch_specification.SpotFleetLaunchSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchSpecsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.spot_fleet_launch_specification

        capo_ec2.types.spot_fleet_launch_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LaunchSpecsList:
    import capo_ec2.types.spot_fleet_launch_specification

    out: LaunchSpecsList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.spot_fleet_launch_specification.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LaunchSpecsList:
    import capo_ec2.types.spot_fleet_launch_specification

    out: LaunchSpecsList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.spot_fleet_launch_specification.deserialize_ec2_query(child)
        )
    return out


def redact_sensitive(value: LaunchSpecsList) -> list[Any]:
    import capo_ec2.types.spot_fleet_launch_specification

    return [
        capo_ec2.types.spot_fleet_launch_specification.redact_sensitive(item)
        for item in value
    ]
