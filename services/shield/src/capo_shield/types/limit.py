"""Generated from Smithy shape ``com.amazonaws.shield#Limit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.long
    import capo_shield.types.string


class Limit(TypedDict, closed=True):
    type: NotRequired["capo_shield.types.string.String"]
    """<p>The type of protection.</p>"""
    max: "capo_shield.types.long.Long"
    """<p>The maximum number of protections that can be created for the specified <code>Type</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Limit) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    out["Max"] = value.get("max", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Limit:
    out: Limit = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Max") is not None:
        out["max"] = data["Max"]
    else:
        out["max"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Limit) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    out["Max"] = value.get("max", 0)
    return out


def deserialize_cbor(data: dict) -> Limit:
    out: Limit = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Max") is not None:
        out["max"] = data["Max"]
    else:
        out["max"] = 0
    return out
