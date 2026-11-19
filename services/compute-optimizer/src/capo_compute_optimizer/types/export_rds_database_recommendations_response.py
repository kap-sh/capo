"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportRDSDatabaseRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.job_id
    import capo_compute_optimizer.types.s3_destination


class ExportRDSDatabaseRecommendationsResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_compute_optimizer.types.job_id.JobId"]
    """<p> The identification number of the export job. </p> <p>To view the status of an export job, use the <a>DescribeRecommendationExportJobs</a> action and specify the job ID. </p>"""
    s3_destination: NotRequired[
        "capo_compute_optimizer.types.s3_destination.S3Destination"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportRDSDatabaseRecommendationsResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "s3_destination" in value:
        import capo_compute_optimizer.types.s3_destination

        out["s3Destination"] = (
            capo_compute_optimizer.types.s3_destination.serialize_aws_json_1_0(
                value["s3_destination"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportRDSDatabaseRecommendationsResponse:
    out: ExportRDSDatabaseRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("s3Destination") is not None:
        import capo_compute_optimizer.types.s3_destination

        out["s3_destination"] = (
            capo_compute_optimizer.types.s3_destination.deserialize_aws_json_1_0(
                data["s3Destination"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportRDSDatabaseRecommendationsResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "s3_destination" in value:
        import capo_compute_optimizer.types.s3_destination

        out["s3Destination"] = (
            capo_compute_optimizer.types.s3_destination.serialize_cbor(
                value["s3_destination"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ExportRDSDatabaseRecommendationsResponse:
    out: ExportRDSDatabaseRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("s3Destination") is not None:
        import capo_compute_optimizer.types.s3_destination

        out["s3_destination"] = (
            capo_compute_optimizer.types.s3_destination.deserialize_cbor(
                data["s3Destination"]
            )
        )
    return out
