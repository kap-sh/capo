"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationExportJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.creation_timestamp
    import capo_compute_optimizer.types.export_destination
    import capo_compute_optimizer.types.failure_reason
    import capo_compute_optimizer.types.job_id
    import capo_compute_optimizer.types.job_status
    import capo_compute_optimizer.types.last_updated_timestamp
    import capo_compute_optimizer.types.resource_type


class RecommendationExportJob(TypedDict, closed=True):
    job_id: NotRequired["capo_compute_optimizer.types.job_id.JobId"]
    """<p>The identification number of the export job.</p>"""
    destination: NotRequired[
        "capo_compute_optimizer.types.export_destination.ExportDestination"
    ]
    """<p>An object that describes the destination of the export file.</p>"""
    resource_type: NotRequired[
        "capo_compute_optimizer.types.resource_type.ResourceType"
    ]
    """<p>The resource type of the exported recommendations.</p>"""
    status: NotRequired["capo_compute_optimizer.types.job_status.JobStatus"]
    """<p>The status of the export job.</p>"""
    creation_timestamp: NotRequired[
        "capo_compute_optimizer.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>The timestamp of when the export job was created.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_updated_timestamp.LastUpdatedTimestamp"
    ]
    """<p>The timestamp of when the export job was last updated.</p>"""
    failure_reason: NotRequired[
        "capo_compute_optimizer.types.failure_reason.FailureReason"
    ]
    """<p>The reason for an export job failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationExportJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "destination" in value:
        import capo_compute_optimizer.types.export_destination

        out["destination"] = (
            capo_compute_optimizer.types.export_destination.serialize_aws_json_1_0(
                value["destination"]
            )
        )
    if "resource_type" in value:
        import capo_compute_optimizer.types.resource_type

        out["resourceType"] = (
            capo_compute_optimizer.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "status" in value:
        import capo_compute_optimizer.types.job_status

        out["status"] = capo_compute_optimizer.types.job_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "creation_timestamp" in value:
        import capo_compute_optimizer.types.creation_timestamp

        out["creationTimestamp"] = (
            capo_compute_optimizer.types.creation_timestamp.serialize_aws_json_1_0(
                value["creation_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationExportJob:
    out: RecommendationExportJob = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("destination") is not None:
        import capo_compute_optimizer.types.export_destination

        out["destination"] = (
            capo_compute_optimizer.types.export_destination.deserialize_aws_json_1_0(
                data["destination"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    if data.get("status") is not None:
        import capo_compute_optimizer.types.job_status

        out["status"] = (
            capo_compute_optimizer.types.job_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("creationTimestamp") is not None:
        import capo_compute_optimizer.types.creation_timestamp

        out["creation_timestamp"] = (
            capo_compute_optimizer.types.creation_timestamp.deserialize_aws_json_1_0(
                data["creationTimestamp"]
            )
        )
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationExportJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "destination" in value:
        import capo_compute_optimizer.types.export_destination

        out["destination"] = (
            capo_compute_optimizer.types.export_destination.serialize_cbor(
                value["destination"]
            )
        )
    if "resource_type" in value:
        import capo_compute_optimizer.types.resource_type

        out["resourceType"] = capo_compute_optimizer.types.resource_type.serialize_cbor(
            value["resource_type"]
        )
    if "status" in value:
        import capo_compute_optimizer.types.job_status

        out["status"] = capo_compute_optimizer.types.job_status.serialize_cbor(
            value["status"]
        )
    if "creation_timestamp" in value:
        import capo_compute_optimizer.types.creation_timestamp

        out["creationTimestamp"] = (
            capo_compute_optimizer.types.creation_timestamp.serialize_cbor(
                value["creation_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.serialize_cbor(
                value["last_updated_timestamp"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_cbor(data: dict) -> RecommendationExportJob:
    out: RecommendationExportJob = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("destination") is not None:
        import capo_compute_optimizer.types.export_destination

        out["destination"] = (
            capo_compute_optimizer.types.export_destination.deserialize_cbor(
                data["destination"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.resource_type.deserialize_cbor(
                data["resourceType"]
            )
        )
    if data.get("status") is not None:
        import capo_compute_optimizer.types.job_status

        out["status"] = capo_compute_optimizer.types.job_status.deserialize_cbor(
            data["status"]
        )
    if data.get("creationTimestamp") is not None:
        import capo_compute_optimizer.types.creation_timestamp

        out["creation_timestamp"] = (
            capo_compute_optimizer.types.creation_timestamp.deserialize_cbor(
                data["creationTimestamp"]
            )
        )
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.deserialize_cbor(
                data["lastUpdatedTimestamp"]
            )
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out
