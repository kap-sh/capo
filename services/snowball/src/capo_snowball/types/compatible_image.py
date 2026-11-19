"""Generated from Smithy shape ``com.amazonaws.snowball#CompatibleImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.string


class CompatibleImage(TypedDict, closed=True):
    ami_id: NotRequired["capo_snowball.types.string.String"]
    """<p>The unique identifier for an individual Snow device AMI.</p>"""
    name: NotRequired["capo_snowball.types.string.String"]
    """<p>The optional name of a compatible image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompatibleImage) -> dict:
    out: dict = {}
    if "ami_id" in value:
        out["AmiId"] = value["ami_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CompatibleImage:
    out: CompatibleImage = {}  # type: ignore[typeddict-item]
    if data.get("AmiId") is not None:
        out["ami_id"] = data["AmiId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CompatibleImage) -> dict:
    out: dict = {}
    if "ami_id" in value:
        out["AmiId"] = value["ami_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> CompatibleImage:
    out: CompatibleImage = {}  # type: ignore[typeddict-item]
    if data.get("AmiId") is not None:
        out["ami_id"] = data["AmiId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
