"""Generated from Smithy shape ``com.amazonaws.codebuild#GetResourcePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class GetResourcePolicyOutput(TypedDict, closed=True):
    policy: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The resource policy for the resource identified by the input ARN parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyOutput:
    out: GetResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetResourcePolicyOutput) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_cbor(data: dict) -> GetResourcePolicyOutput:
    out: GetResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    return out
