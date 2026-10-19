"""Generated from Smithy shape ``com.amazonaws.migrationhub#DescribeMigrationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.migration_task_name
    import capo_migration_hub.types.progress_update_stream


class DescribeMigrationTaskRequest(TypedDict, closed=True):
    progress_update_stream: (
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream. </p>"""
    migration_task_name: (
        "capo_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>The identifier given to the MigrationTask. <i>Do not store personal data in this field.</i> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMigrationTaskRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMigrationTaskRequest:
    out: DescribeMigrationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProgressUpdateStream") is not None:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        out["progress_update_stream"] = ""
    if data.get("MigrationTaskName") is not None:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        out["migration_task_name"] = ""
    return out
