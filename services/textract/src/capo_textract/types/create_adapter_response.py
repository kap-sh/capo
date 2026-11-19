"""Generated from Smithy shape ``com.amazonaws.textract#CreateAdapterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_id


class CreateAdapterResponse(TypedDict, closed=True):
    adapter_id: NotRequired["capo_textract.types.adapter_id.AdapterId"]
    """<p>A string containing the unique ID for the adapter that has been created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAdapterResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAdapterResponse:
    out: CreateAdapterResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAdapterResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    return out


def deserialize_cbor(data: dict) -> CreateAdapterResponse:
    out: CreateAdapterResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    return out
