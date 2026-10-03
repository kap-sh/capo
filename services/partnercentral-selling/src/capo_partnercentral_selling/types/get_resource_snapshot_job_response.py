"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetResourceSnapshotJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.resource_arn
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_arn
    import capo_partnercentral_selling.types.resource_snapshot_job_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_status
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type


class GetResourceSnapshotJobResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>The catalog in which the snapshot job was created. This will match the Catalog specified in the request. </p>"""
    id: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    ]
    """<p>The unique identifier of the snapshot job. This matches the ResourceSnapshotJobIdentifier provided in the request. </p>"""
    arn: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_job_arn.ResourceSnapshotJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the snapshot job. This globally unique identifier can be used for resource-specific operations across AWS services. </p>"""
    engagement_id: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The identifier of the engagement associated with this snapshot job. This links the job to a specific engagement context. </p>"""
    resource_type: NotRequired[
        "capo_partnercentral_selling.types.resource_type.ResourceType"
    ]
    """<p>The type of resource being snapshotted. This would have "Opportunity" as a value as it is dependent on the supported resource type.</p>"""
    resource_id: NotRequired[
        "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The identifier of the specific resource being snapshotted. The format might vary depending on the ResourceType. </p>"""
    resource_arn: NotRequired[
        "capo_partnercentral_selling.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource being snapshotted. This provides a globally unique identifier for the resource across AWS. </p>"""
    resource_snapshot_template_name: NotRequired[
        "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    ]
    """<p>The name of the template used for creating the snapshot. This is the same as the template name. It defines the structure and content of the snapshot.</p>"""
    created_at: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The date and time when the snapshot job was created in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z" </p>"""
    status: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
    ]
    """<p>The current status of the snapshot job. Valid values:</p> <ul> <li> <p>STOPPED: The job is not currently running.</p> </li> <li> <p>RUNNING: The job is actively executing.</p> </li> </ul>"""
    last_successful_execution_date: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>The date and time of the last successful execution of the job, in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z" </p>"""
    last_failure: NotRequired["str"]
    """<p>If the job has encountered any failures, this field contains the error message from the most recent failure. This can be useful for troubleshooting issues with the job. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceSnapshotJobResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "resource_type" in value:
        import capo_partnercentral_selling.types.resource_type

        out["ResourceType"] = (
            capo_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_snapshot_template_name" in value:
        out["ResourceSnapshotTemplateName"] = value["resource_snapshot_template_name"]
    if "created_at" in value:
        import capo_partnercentral_selling.types.date_time

        out["CreatedAt"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "status" in value:
        import capo_partnercentral_selling.types.resource_snapshot_job_status

        out["Status"] = (
            capo_partnercentral_selling.types.resource_snapshot_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "last_successful_execution_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["LastSuccessfulExecutionDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["last_successful_execution_date"]
            )
        )
    if "last_failure" in value:
        out["LastFailure"] = value["last_failure"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceSnapshotJobResponse:
    out: GetResourceSnapshotJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetResourceSnapshotJobResponse.catalog required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("EngagementId") is not None:
        out["engagement_id"] = data["EngagementId"]
    if data.get("ResourceType") is not None:
        import capo_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            capo_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("ResourceSnapshotTemplateName") is not None:
        out["resource_snapshot_template_name"] = data["ResourceSnapshotTemplateName"]
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_selling.types.date_time

        out["created_at"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("Status") is not None:
        import capo_partnercentral_selling.types.resource_snapshot_job_status

        out["status"] = (
            capo_partnercentral_selling.types.resource_snapshot_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("LastSuccessfulExecutionDate") is not None:
        import capo_partnercentral_selling.types.date_time

        out["last_successful_execution_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["LastSuccessfulExecutionDate"]
            )
        )
    if data.get("LastFailure") is not None:
        out["last_failure"] = data["LastFailure"]
    return out
