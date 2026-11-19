"""Generated from Smithy shape ``com.amazonaws.codebuild#RetryBuildInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.string


class RetryBuildInput(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the identifier of the build to restart.</p>"""
    idempotency_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>A unique, case sensitive identifier you provide to ensure the idempotency of the <code>RetryBuild</code> request. The token is included in the <code>RetryBuild</code> request and is valid for five minutes. If you repeat the <code>RetryBuild</code> request with the same token, but change a parameter, CodeBuild returns a parameter mismatch error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryBuildInput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryBuildInput:
    out: RetryBuildInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("idempotencyToken") is not None:
        out["idempotency_token"] = data["idempotencyToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RetryBuildInput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_cbor(data: dict) -> RetryBuildInput:
    out: RetryBuildInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("idempotencyToken") is not None:
        out["idempotency_token"] = data["idempotencyToken"]
    return out
