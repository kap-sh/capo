"""Generated from Smithy shape ``com.amazonaws.migrationhub#Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.progress_percent
    import capo_migration_hub.types.status
    import capo_migration_hub.types.status_detail


class Task(TypedDict, closed=True):
    status: "capo_migration_hub.types.status.Status"
    """<p>Status of the task - Not Started, In-Progress, Complete.</p>"""
    status_detail: NotRequired["capo_migration_hub.types.status_detail.StatusDetail"]
    """<p>Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.</p>"""
    progress_percent: NotRequired[
        "capo_migration_hub.types.progress_percent.ProgressPercent"
    ]
    """<p>Indication of the percentage completion of the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Task) -> dict:
    out: dict = {}
    import capo_migration_hub.types.status

    out["Status"] = capo_migration_hub.types.status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_detail" in value:
        out["StatusDetail"] = value["status_detail"]
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Task:
    out: Task = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_migration_hub.types.status

        out["status"] = capo_migration_hub.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_migration_hub.types.status.Status", "")
    if data.get("StatusDetail") is not None:
        out["status_detail"] = data["StatusDetail"]
    if data.get("ProgressPercent") is not None:
        out["progress_percent"] = data["ProgressPercent"]
    return out
