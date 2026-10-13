"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disk_image

DiskImageList: TypeAlias = list["capo_ec2.types.disk_image.DiskImage"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskImageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.disk_image

        capo_ec2.types.disk_image.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> DiskImageList:
    import capo_ec2.types.disk_image

    out: DiskImageList = []
    for child in el.findall("member"):
        out.append(capo_ec2.types.disk_image.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> DiskImageList:
    import capo_ec2.types.disk_image

    out: DiskImageList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.disk_image.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: DiskImageList) -> list[Any]:
    import capo_ec2.types.disk_image

    return [capo_ec2.types.disk_image.redact_sensitive(item) for item in value]
