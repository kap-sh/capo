"""Generated from Smithy shape ``com.amazonaws.gamelift#PutScalingPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string


class PutScalingPolicyOutput(TypedDict, closed=True):
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutScalingPolicyOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutScalingPolicyOutput:
    out: PutScalingPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutScalingPolicyOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> PutScalingPolicyOutput:
    out: PutScalingPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
