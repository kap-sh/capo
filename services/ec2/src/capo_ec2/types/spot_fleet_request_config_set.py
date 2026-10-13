"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetRequestConfigSet``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_fleet_request_config

SpotFleetRequestConfigSet: TypeAlias = list[
    "capo_ec2.types.spot_fleet_request_config.SpotFleetRequestConfig"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetRequestConfigSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.spot_fleet_request_config

        capo_ec2.types.spot_fleet_request_config.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SpotFleetRequestConfigSet:
    import capo_ec2.types.spot_fleet_request_config

    out: SpotFleetRequestConfigSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.spot_fleet_request_config.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SpotFleetRequestConfigSet:
    import capo_ec2.types.spot_fleet_request_config

    out: SpotFleetRequestConfigSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.spot_fleet_request_config.deserialize_ec2_query(child)
        )
    return out


def redact_sensitive(value: SpotFleetRequestConfigSet) -> list[Any]:
    import capo_ec2.types.spot_fleet_request_config

    return [
        capo_ec2.types.spot_fleet_request_config.redact_sensitive(item)
        for item in value
    ]
