"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshotTaskList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.import_snapshot_task

ImportSnapshotTaskList: TypeAlias = list[
    "capo_ec2.types.import_snapshot_task.ImportSnapshotTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportSnapshotTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.import_snapshot_task

        capo_ec2.types.import_snapshot_task.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ImportSnapshotTaskList:
    import capo_ec2.types.import_snapshot_task

    out: ImportSnapshotTaskList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.import_snapshot_task.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ImportSnapshotTaskList:
    import capo_ec2.types.import_snapshot_task

    out: ImportSnapshotTaskList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.import_snapshot_task.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: ImportSnapshotTaskList) -> list[Any]:
    import capo_ec2.types.import_snapshot_task

    return [
        capo_ec2.types.import_snapshot_task.redact_sensitive(item) for item in value
    ]
