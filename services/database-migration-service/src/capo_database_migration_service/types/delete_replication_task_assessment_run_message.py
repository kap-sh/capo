"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteReplicationTaskAssessmentRunMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteReplicationTaskAssessmentRunMessage(TypedDict, closed=True):
    replication_task_assessment_run_arn: (
        "capo_database_migration_service.types.string.String"
    )
    """<p>Amazon Resource Name (ARN) of the premigration assessment run to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplicationTaskAssessmentRunMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskAssessmentRunArn"] = value[
        "replication_task_assessment_run_arn"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplicationTaskAssessmentRunMessage:
    out: DeleteReplicationTaskAssessmentRunMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskAssessmentRunArn") is not None:
        out["replication_task_assessment_run_arn"] = data[
            "ReplicationTaskAssessmentRunArn"
        ]
    else:
        out["replication_task_assessment_run_arn"] = ""
    return out
