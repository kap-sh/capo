"""Generated from Smithy shape ``com.amazonaws.appstream#CreateAppBlockBuilderStreamingURLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.long
    import capo_appstream.types.name


class CreateAppBlockBuilderStreamingURLRequest(TypedDict, closed=True):
    app_block_builder_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the app block builder.</p>"""
    validity: NotRequired["capo_appstream.types.long.Long"]
    """<p>The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppBlockBuilderStreamingURLRequest) -> dict:
    out: dict = {}
    if "app_block_builder_name" in value:
        out["AppBlockBuilderName"] = value["app_block_builder_name"]
    if "validity" in value:
        out["Validity"] = value["validity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppBlockBuilderStreamingURLRequest:
    out: CreateAppBlockBuilderStreamingURLRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockBuilderName") is not None:
        out["app_block_builder_name"] = data["AppBlockBuilderName"]
    if data.get("Validity") is not None:
        out["validity"] = data["Validity"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAppBlockBuilderStreamingURLRequest) -> dict:
    out: dict = {}
    if "app_block_builder_name" in value:
        out["AppBlockBuilderName"] = value["app_block_builder_name"]
    if "validity" in value:
        out["Validity"] = value["validity"]
    return out


def deserialize_cbor(data: dict) -> CreateAppBlockBuilderStreamingURLRequest:
    out: CreateAppBlockBuilderStreamingURLRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockBuilderName") is not None:
        out["app_block_builder_name"] = data["AppBlockBuilderName"]
    if data.get("Validity") is not None:
        out["validity"] = data["Validity"]
    return out
