"""Generated from Smithy shape ``com.amazonaws.codebuild#RetryBuildBatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.retry_build_batch_type
    import capo_codebuild.types.string


class RetryBuildBatchInput(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the identifier of the batch build to restart.</p>"""
    idempotency_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>A unique, case sensitive identifier you provide to ensure the idempotency of the <code>RetryBuildBatch</code> request. The token is included in the <code>RetryBuildBatch</code> request and is valid for five minutes. If you repeat the <code>RetryBuildBatch</code> request with the same token, but change a parameter, CodeBuild returns a parameter mismatch error.</p>"""
    retry_type: NotRequired[
        "capo_codebuild.types.retry_build_batch_type.RetryBuildBatchType"
    ]
    """<p>Specifies the type of retry to perform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryBuildBatchInput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    if "retry_type" in value:
        import capo_codebuild.types.retry_build_batch_type

        out["retryType"] = (
            capo_codebuild.types.retry_build_batch_type.serialize_aws_json_1_1(
                value["retry_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryBuildBatchInput:
    out: RetryBuildBatchInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("idempotencyToken") is not None:
        out["idempotency_token"] = data["idempotencyToken"]
    if data.get("retryType") is not None:
        import capo_codebuild.types.retry_build_batch_type

        out["retry_type"] = (
            capo_codebuild.types.retry_build_batch_type.deserialize_aws_json_1_1(
                data["retryType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryBuildBatchInput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    if "retry_type" in value:
        import capo_codebuild.types.retry_build_batch_type

        out["retryType"] = capo_codebuild.types.retry_build_batch_type.serialize_cbor(
            value["retry_type"]
        )
    return out


def deserialize_cbor(data: dict) -> RetryBuildBatchInput:
    out: RetryBuildBatchInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("idempotencyToken") is not None:
        out["idempotency_token"] = data["idempotencyToken"]
    if data.get("retryType") is not None:
        import capo_codebuild.types.retry_build_batch_type

        out["retry_type"] = (
            capo_codebuild.types.retry_build_batch_type.deserialize_cbor(
                data["retryType"]
            )
        )
    return out
