"""Generated from Smithy shape ``com.amazonaws.simpledbv2#GetExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simpledbv2.types.aws_account_id
    import capo_simpledbv2.types.domain_name
    import capo_simpledbv2.types.export_arn
    import capo_simpledbv2.types.export_data_cutoff_time
    import capo_simpledbv2.types.export_manifest_summary
    import capo_simpledbv2.types.export_status
    import capo_simpledbv2.types.failure_code
    import capo_simpledbv2.types.failure_message
    import capo_simpledbv2.types.idempotency_token
    import capo_simpledbv2.types.items_count
    import capo_simpledbv2.types.requested_at
    import capo_simpledbv2.types.s3_bucket_name
    import capo_simpledbv2.types.s3_key_prefix
    import capo_simpledbv2.types.s3_sse_algorithm
    import capo_simpledbv2.types.s3_sse_kms_key_id


class GetExportResponse(TypedDict, closed=True):
    export_arn: "capo_simpledbv2.types.export_arn.ExportArn"
    """Unique ARN identifier of the export."""
    client_token: "capo_simpledbv2.types.idempotency_token.IdempotencyToken"
    """The client token provided for this export."""
    export_status: "capo_simpledbv2.types.export_status.ExportStatus"
    """The current state of the export. Current possible values include : PENDING - export request received, IN_PROGRESS - export is being processed, SUCCEEDED - export completed successfully, and FAILED - export encountered an error."""
    domain_name: "capo_simpledbv2.types.domain_name.DomainName"
    """The name of the domain that was exported."""
    requested_at: "capo_simpledbv2.types.requested_at.RequestedAt"
    """Timestamp when the export request was received by the service."""
    s3_bucket: "capo_simpledbv2.types.s3_bucket_name.S3BucketName"
    """The name of the S3 bucket for this export."""
    s3_key_prefix: NotRequired["capo_simpledbv2.types.s3_key_prefix.S3KeyPrefix"]
    """The S3 key prefix provided in the corresponding StartDomainExport request."""
    s3_sse_algorithm: NotRequired[
        "capo_simpledbv2.types.s3_sse_algorithm.S3SseAlgorithm"
    ]
    """The S3 SSE encryption algorithm for this export."""
    s3_sse_kms_key_id: NotRequired[
        "capo_simpledbv2.types.s3_sse_kms_key_id.S3SseKmsKeyId"
    ]
    """The KMS key ID for this export."""
    s3_bucket_owner: NotRequired["capo_simpledbv2.types.aws_account_id.AwsAccountId"]
    """The S3 bucket owner account ID for this export."""
    failure_code: NotRequired["capo_simpledbv2.types.failure_code.FailureCode"]
    """Failure code for the result of the failed export."""
    failure_message: NotRequired["capo_simpledbv2.types.failure_message.FailureMessage"]
    """Export failure reason description."""
    export_manifest: NotRequired[
        "capo_simpledbv2.types.export_manifest_summary.ExportManifestSummary"
    ]
    """The name of the manifest summary file for the export."""
    items_count: NotRequired["capo_simpledbv2.types.items_count.ItemsCount"]
    """Total number of exported items."""
    export_data_cutoff_time: NotRequired[
        "capo_simpledbv2.types.export_data_cutoff_time.ExportDataCutoffTime"
    ]
    """The timestamp indicating the cutoff point for data inclusion in the export. All data inserted or modified before this time will be present in the exported data. Data insertions or modifications after this timestamp may or may not be present in the export."""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportResponse) -> dict:
    out: dict = {}
    out["exportArn"] = value["export_arn"]
    out["clientToken"] = value["client_token"]
    import capo_simpledbv2.types.export_status

    out["exportStatus"] = capo_simpledbv2.types.export_status.serialize_json(
        value["export_status"]
    )
    out["domainName"] = value["domain_name"]
    import capo_simpledbv2.types.requested_at

    out["requestedAt"] = capo_simpledbv2.types.requested_at.serialize_json(
        value["requested_at"]
    )
    out["s3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    if "s3_sse_algorithm" in value:
        import capo_simpledbv2.types.s3_sse_algorithm

        out["s3SseAlgorithm"] = capo_simpledbv2.types.s3_sse_algorithm.serialize_json(
            value["s3_sse_algorithm"]
        )
    if "s3_sse_kms_key_id" in value:
        out["s3SseKmsKeyId"] = value["s3_sse_kms_key_id"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "export_manifest" in value:
        out["exportManifest"] = value["export_manifest"]
    if "items_count" in value:
        out["itemsCount"] = value["items_count"]
    if "export_data_cutoff_time" in value:
        import capo_simpledbv2.types.export_data_cutoff_time

        out["exportDataCutoffTime"] = (
            capo_simpledbv2.types.export_data_cutoff_time.serialize_json(
                value["export_data_cutoff_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetExportResponse:
    out: GetExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("exportArn") is not None:
        out["export_arn"] = data["exportArn"]
    else:
        out["export_arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("exportStatus") is not None:
        import capo_simpledbv2.types.export_status

        out["export_status"] = capo_simpledbv2.types.export_status.deserialize_json(
            data["exportStatus"]
        )
    else:
        import typing

        out["export_status"] = typing.cast(
            "capo_simpledbv2.types.export_status.ExportStatus", ""
        )
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("requestedAt") is not None:
        import capo_simpledbv2.types.requested_at

        out["requested_at"] = capo_simpledbv2.types.requested_at.deserialize_json(
            data["requestedAt"]
        )
    else:
        import datetime

        out["requested_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("s3Bucket") is not None:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("s3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    if data.get("s3SseAlgorithm") is not None:
        import capo_simpledbv2.types.s3_sse_algorithm

        out["s3_sse_algorithm"] = (
            capo_simpledbv2.types.s3_sse_algorithm.deserialize_json(
                data["s3SseAlgorithm"]
            )
        )
    if data.get("s3SseKmsKeyId") is not None:
        out["s3_sse_kms_key_id"] = data["s3SseKmsKeyId"]
    if data.get("s3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    if data.get("failureCode") is not None:
        out["failure_code"] = data["failureCode"]
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("exportManifest") is not None:
        out["export_manifest"] = data["exportManifest"]
    if data.get("itemsCount") is not None:
        out["items_count"] = data["itemsCount"]
    if data.get("exportDataCutoffTime") is not None:
        import capo_simpledbv2.types.export_data_cutoff_time

        out["export_data_cutoff_time"] = (
            capo_simpledbv2.types.export_data_cutoff_time.deserialize_json(
                data["exportDataCutoffTime"]
            )
        )
    return out
