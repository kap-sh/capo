"""Generated from Smithy shape ``com.amazonaws.codebuild#PutResourcePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class PutResourcePolicyOutput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The ARN of the <code>Project</code> or <code>ReportGroup</code> resource that is associated with a resource policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyOutput:
    out: PutResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutResourcePolicyOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_cbor(data: dict) -> PutResourcePolicyOutput:
    out: PutResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    return out
