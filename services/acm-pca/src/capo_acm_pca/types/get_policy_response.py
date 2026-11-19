"""Generated from Smithy shape ``com.amazonaws.acmpca#GetPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.aws_policy


class GetPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_acm_pca.types.aws_policy.AWSPolicy"]
    """<p>The policy attached to the private CA as a JSON document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_cbor(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out
