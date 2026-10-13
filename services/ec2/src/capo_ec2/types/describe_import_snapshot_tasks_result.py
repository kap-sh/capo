"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImportSnapshotTasksResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.import_snapshot_task_list
    import capo_ec2.types.string


class DescribeImportSnapshotTasksResult(TypedDict, closed=True):
    import_snapshot_tasks: NotRequired[
        "capo_ec2.types.import_snapshot_task_list.ImportSnapshotTaskList"
    ]
    """<p>A list of zero or more import snapshot tasks that are currently active or were completed or canceled in the previous 7 days.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to get the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImportSnapshotTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "import_snapshot_tasks" in value:
        import capo_ec2.types.import_snapshot_task_list

        capo_ec2.types.import_snapshot_task_list.serialize_ec2_query(
            value["import_snapshot_tasks"], pairs, f"{key_prefix}ImportSnapshotTaskSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeImportSnapshotTasksResult:
    out: DescribeImportSnapshotTasksResult = {}  # type: ignore[typeddict-item]
    child_import_snapshot_tasks = el.find("importSnapshotTaskSet")
    if child_import_snapshot_tasks is not None:
        import capo_ec2.types.import_snapshot_task_list

        out["import_snapshot_tasks"] = (
            capo_ec2.types.import_snapshot_task_list.deserialize_ec2_query(
                child_import_snapshot_tasks
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


def redact_sensitive(value: DescribeImportSnapshotTasksResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "import_snapshot_tasks" in value:
        import capo_ec2.types.import_snapshot_task_list

        out["import_snapshot_tasks"] = (
            capo_ec2.types.import_snapshot_task_list.redact_sensitive(
                value["import_snapshot_tasks"]
            )
        )
    return out
