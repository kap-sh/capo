"""Generated from Smithy shape ``com.amazonaws.appstream#CreateImageBuilderStreamingURLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.long
    import capo_appstream.types.string


class CreateImageBuilderStreamingURLRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the image builder.</p>"""
    validity: NotRequired["capo_appstream.types.long.Long"]
    """<p>The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImageBuilderStreamingURLRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "validity" in value:
        out["Validity"] = value["validity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImageBuilderStreamingURLRequest:
    out: CreateImageBuilderStreamingURLRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Validity") is not None:
        out["validity"] = data["Validity"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateImageBuilderStreamingURLRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "validity" in value:
        out["Validity"] = value["validity"]
    return out


def deserialize_cbor(data: dict) -> CreateImageBuilderStreamingURLRequest:
    out: CreateImageBuilderStreamingURLRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Validity") is not None:
        out["validity"] = data["Validity"]
    return out
