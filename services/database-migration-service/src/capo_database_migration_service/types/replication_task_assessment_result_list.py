"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskAssessmentResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_task_assessment_result

ReplicationTaskAssessmentResultList: TypeAlias = list[
    "capo_database_migration_service.types.replication_task_assessment_result.ReplicationTaskAssessmentResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskAssessmentResultList) -> list:
    import capo_database_migration_service.types.replication_task_assessment_result

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.replication_task_assessment_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationTaskAssessmentResultList:
    import capo_database_migration_service.types.replication_task_assessment_result

    out: ReplicationTaskAssessmentResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_database_migration_service.types.replication_task_assessment_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: ReplicationTaskAssessmentResultList) -> list[Any]:
    import capo_database_migration_service.types.replication_task_assessment_result

    return [
        capo_database_migration_service.types.replication_task_assessment_result.redact_sensitive(
            item
        )
        for item in value
    ]
