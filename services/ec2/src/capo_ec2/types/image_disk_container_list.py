"""Generated from Smithy shape ``com.amazonaws.ec2#ImageDiskContainerList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_disk_container

ImageDiskContainerList: TypeAlias = list[
    "capo_ec2.types.image_disk_container.ImageDiskContainer"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageDiskContainerList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_disk_container

        capo_ec2.types.image_disk_container.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ImageDiskContainerList:
    import capo_ec2.types.image_disk_container

    out: ImageDiskContainerList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.image_disk_container.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ImageDiskContainerList:
    import capo_ec2.types.image_disk_container

    out: ImageDiskContainerList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.image_disk_container.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: ImageDiskContainerList) -> list[Any]:
    import capo_ec2.types.image_disk_container

    return [
        capo_ec2.types.image_disk_container.redact_sensitive(item) for item in value
    ]
