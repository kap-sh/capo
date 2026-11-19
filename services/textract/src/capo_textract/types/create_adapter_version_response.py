"""Generated from Smithy shape ``com.amazonaws.textract#CreateAdapterVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_id
    import capo_textract.types.adapter_version


class CreateAdapterVersionResponse(TypedDict, closed=True):
    adapter_id: NotRequired["capo_textract.types.adapter_id.AdapterId"]
    """<p>A string containing the unique ID for the adapter that has received a new version.</p>"""
    adapter_version: NotRequired["capo_textract.types.adapter_version.AdapterVersion"]
    """<p>A string describing the new version of the adapter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAdapterVersionResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAdapterVersionResponse:
    out: CreateAdapterVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("AdapterVersion") is not None:
        out["adapter_version"] = data["AdapterVersion"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAdapterVersionResponse) -> dict:
    out: dict = {}
    if "adapter_id" in value:
        out["AdapterId"] = value["adapter_id"]
    if "adapter_version" in value:
        out["AdapterVersion"] = value["adapter_version"]
    return out


def deserialize_cbor(data: dict) -> CreateAdapterVersionResponse:
    out: CreateAdapterVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    if data.get("AdapterVersion") is not None:
        out["adapter_version"] = data["AdapterVersion"]
    return out
