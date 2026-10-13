"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshotTask``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.snapshot_task_detail
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ImportSnapshotTask(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the import snapshot task.</p>"""
    import_task_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the import snapshot task.</p>"""
    snapshot_task_detail: NotRequired[
        "capo_ec2.types.snapshot_task_detail.SnapshotTaskDetail"
    ]
    """<p>Describes an import snapshot task.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the import snapshot task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportSnapshotTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "import_task_id" in value:
        pairs.append((f"{key_prefix}ImportTaskId", str(value["import_task_id"])))
    if "snapshot_task_detail" in value:
        import capo_ec2.types.snapshot_task_detail

        capo_ec2.types.snapshot_task_detail.serialize_ec2_query(
            value["snapshot_task_detail"], pairs, f"{key_prefix}SnapshotTaskDetail"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> ImportSnapshotTask:
    out: ImportSnapshotTask = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_import_task_id = el.find("importTaskId")
    if child_import_task_id is not None:
        out["import_task_id"] = str(child_import_task_id.text or "")
    child_snapshot_task_detail = el.find("snapshotTaskDetail")
    if child_snapshot_task_detail is not None:
        import capo_ec2.types.snapshot_task_detail

        out["snapshot_task_detail"] = (
            capo_ec2.types.snapshot_task_detail.deserialize_ec2_query(
                child_snapshot_task_detail
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out


def redact_sensitive(value: ImportSnapshotTask) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "snapshot_task_detail" in value:
        import capo_ec2.types.snapshot_task_detail

        out["snapshot_task_detail"] = (
            capo_ec2.types.snapshot_task_detail.redact_sensitive(
                value["snapshot_task_detail"]
            )
        )
    return out
