"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceRequestList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_instance_request

SpotInstanceRequestList: TypeAlias = list[
    "capo_ec2.types.spot_instance_request.SpotInstanceRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotInstanceRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.spot_instance_request

        capo_ec2.types.spot_instance_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SpotInstanceRequestList:
    import capo_ec2.types.spot_instance_request

    out: SpotInstanceRequestList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.spot_instance_request.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SpotInstanceRequestList:
    import capo_ec2.types.spot_instance_request

    out: SpotInstanceRequestList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.spot_instance_request.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: SpotInstanceRequestList) -> list[Any]:
    import capo_ec2.types.spot_instance_request

    return [
        capo_ec2.types.spot_instance_request.redact_sensitive(item) for item in value
    ]
