"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationTaskAssessmentResultsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_task_assessment_result_list
    import capo_database_migration_service.types.string


class DescribeReplicationTaskAssessmentResultsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    bucket_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>- The Amazon S3 bucket where the task assessment report is located. </p>"""
    replication_task_assessment_results: NotRequired[
        "capo_database_migration_service.types.replication_task_assessment_result_list.ReplicationTaskAssessmentResultList"
    ]
    """<p> The task assessment report. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeReplicationTaskAssessmentResultsResponse,
) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "replication_task_assessment_results" in value:
        import capo_database_migration_service.types.replication_task_assessment_result_list

        out["ReplicationTaskAssessmentResults"] = (
            capo_database_migration_service.types.replication_task_assessment_result_list.serialize_aws_json_1_1(
                value["replication_task_assessment_results"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeReplicationTaskAssessmentResultsResponse:
    out: DescribeReplicationTaskAssessmentResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    if data.get("ReplicationTaskAssessmentResults") is not None:
        import capo_database_migration_service.types.replication_task_assessment_result_list

        out["replication_task_assessment_results"] = (
            capo_database_migration_service.types.replication_task_assessment_result_list.deserialize_aws_json_1_1(
                data["ReplicationTaskAssessmentResults"]
            )
        )
    return out


def redact_sensitive(
    value: DescribeReplicationTaskAssessmentResultsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "replication_task_assessment_results" in value:
        import capo_database_migration_service.types.replication_task_assessment_result_list

        out["replication_task_assessment_results"] = (
            capo_database_migration_service.types.replication_task_assessment_result_list.redact_sensitive(
                value["replication_task_assessment_results"]
            )
        )
    return out
