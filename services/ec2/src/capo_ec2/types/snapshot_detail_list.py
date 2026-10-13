"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotDetailList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.snapshot_detail

SnapshotDetailList: TypeAlias = list["capo_ec2.types.snapshot_detail.SnapshotDetail"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotDetailList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.snapshot_detail

        capo_ec2.types.snapshot_detail.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> SnapshotDetailList:
    import capo_ec2.types.snapshot_detail

    out: SnapshotDetailList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.snapshot_detail.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SnapshotDetailList:
    import capo_ec2.types.snapshot_detail

    out: SnapshotDetailList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.snapshot_detail.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: SnapshotDetailList) -> list[Any]:
    import capo_ec2.types.snapshot_detail

    return [capo_ec2.types.snapshot_detail.redact_sensitive(item) for item in value]
