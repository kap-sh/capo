"""Generated from Smithy shape ``com.amazonaws.simpledbv2#StartDomainExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simpledbv2.types.aws_account_id
    import capo_simpledbv2.types.domain_name
    import capo_simpledbv2.types.idempotency_token
    import capo_simpledbv2.types.s3_bucket_name
    import capo_simpledbv2.types.s3_key_prefix
    import capo_simpledbv2.types.s3_sse_algorithm
    import capo_simpledbv2.types.s3_sse_kms_key_id


class StartDomainExportRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_simpledbv2.types.idempotency_token.IdempotencyToken"
    ]
    """Providing a ClientToken makes the call to StartDomainExport API idempotent, meaning that multiple identical calls have the same effect as one single call. A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent. If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, a ConflictException will be returned."""
    domain_name: "capo_simpledbv2.types.domain_name.DomainName"
    """The name of the domain to export."""
    s3_bucket: "capo_simpledbv2.types.s3_bucket_name.S3BucketName"
    """The name of the S3 bucket where the domain data will be exported."""
    s3_key_prefix: NotRequired["capo_simpledbv2.types.s3_key_prefix.S3KeyPrefix"]
    """The prefix string to be used to generate the S3 object keys for export artifacts."""
    s3_sse_algorithm: NotRequired[
        "capo_simpledbv2.types.s3_sse_algorithm.S3SseAlgorithm"
    ]
    """The server-side encryption algorithm to use for the exported data in S3. Valid values are: AES256 (SSE-S3) and KMS (SSE-KMS). If not specified, bucket's default encryption will apply."""
    s3_sse_kms_key_id: NotRequired[
        "capo_simpledbv2.types.s3_sse_kms_key_id.S3SseKmsKeyId"
    ]
    """The KMS key ID to use for server-side encryption with AWS KMS-managed keys (SSE-KMS). This parameter is only expected with KMS as the S3 SSE algorithm."""
    s3_bucket_owner: NotRequired["capo_simpledbv2.types.aws_account_id.AwsAccountId"]
    """The ID of the AWS account that owns the bucket the export will be stored in."""


# --- restJson1 ser/de ---
def serialize_json(value: StartDomainExportRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["domainName"] = value["domain_name"]
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
    return out


def deserialize_json(data: dict) -> StartDomainExportRequest:
    out: StartDomainExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
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
    return out
