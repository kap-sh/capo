"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclIcmpTypeCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.integer_object


class NetworkAclIcmpTypeCode(TypedDict, closed=True):
    code: NotRequired["capo_fms.types.integer_object.IntegerObject"]
    """<p>ICMP code. </p>"""
    type: NotRequired["capo_fms.types.integer_object.IntegerObject"]
    """<p>ICMP type. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclIcmpTypeCode) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAclIcmpTypeCode:
    out: NetworkAclIcmpTypeCode = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkAclIcmpTypeCode) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_cbor(data: dict) -> NetworkAclIcmpTypeCode:
    out: NetworkAclIcmpTypeCode = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
