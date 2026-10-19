"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationTaskAssessmentMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class StartReplicationTaskAssessmentMessage(TypedDict, closed=True):
    replication_task_arn: "capo_database_migration_service.types.string.String"
    """<p> The Amazon Resource Name (ARN) of the replication task. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationTaskAssessmentMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplicationTaskAssessmentMessage:
    out: StartReplicationTaskAssessmentMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskArn") is not None:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        out["replication_task_arn"] = ""
    return out
