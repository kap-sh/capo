"""Generated from Smithy shape ``com.amazonaws.gamelift#VpcPeeringConnectionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string


class VpcPeeringConnectionStatus(TypedDict, closed=True):
    code: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>Code indicating the status of a VPC peering connection.</p>"""
    message: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Additional messaging associated with the connection status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcPeeringConnectionStatus) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcPeeringConnectionStatus:
    out: VpcPeeringConnectionStatus = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VpcPeeringConnectionStatus) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> VpcPeeringConnectionStatus:
    out: VpcPeeringConnectionStatus = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
