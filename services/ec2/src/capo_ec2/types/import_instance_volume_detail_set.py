"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceVolumeDetailSet``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.import_instance_volume_detail_item

ImportInstanceVolumeDetailSet: TypeAlias = list[
    "capo_ec2.types.import_instance_volume_detail_item.ImportInstanceVolumeDetailItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportInstanceVolumeDetailSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.import_instance_volume_detail_item

        capo_ec2.types.import_instance_volume_detail_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ImportInstanceVolumeDetailSet:
    import capo_ec2.types.import_instance_volume_detail_item

    out: ImportInstanceVolumeDetailSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.import_instance_volume_detail_item.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ImportInstanceVolumeDetailSet:
    import capo_ec2.types.import_instance_volume_detail_item

    out: ImportInstanceVolumeDetailSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.import_instance_volume_detail_item.deserialize_ec2_query(
                child
            )
        )
    return out


def redact_sensitive(value: ImportInstanceVolumeDetailSet) -> list[Any]:
    import capo_ec2.types.import_instance_volume_detail_item

    return [
        capo_ec2.types.import_instance_volume_detail_item.redact_sensitive(item)
        for item in value
    ]
