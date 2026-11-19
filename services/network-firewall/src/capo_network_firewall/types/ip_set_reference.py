"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPSetReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn


class IPSetReference(TypedDict, closed=True):
    reference_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource that you are referencing in your rule group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IPSetReference) -> dict:
    out: dict = {}
    if "reference_arn" in value:
        out["ReferenceArn"] = value["reference_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IPSetReference:
    out: IPSetReference = {}  # type: ignore[typeddict-item]
    if data.get("ReferenceArn") is not None:
        out["reference_arn"] = data["ReferenceArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IPSetReference) -> dict:
    out: dict = {}
    if "reference_arn" in value:
        out["ReferenceArn"] = value["reference_arn"]
    return out


def deserialize_cbor(data: dict) -> IPSetReference:
    out: IPSetReference = {}  # type: ignore[typeddict-item]
    if data.get("ReferenceArn") is not None:
        out["reference_arn"] = data["ReferenceArn"]
    return out
