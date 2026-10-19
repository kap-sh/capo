"""Generated from Smithy shape ``com.amazonaws.textract#GetAdapterVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_id
    import capo_textract.types.adapter_version


class GetAdapterVersionRequest(TypedDict, closed=True):
    adapter_id: "capo_textract.types.adapter_id.AdapterId"
    """<p>A string specifying a unique ID for the adapter version you want to retrieve information for.</p>"""
    adapter_version: "capo_textract.types.adapter_version.AdapterVersion"
    """<p>A string specifying the adapter version you want to retrieve information for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdapterVersionRequest) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    out["AdapterVersion"] = value["adapter_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdapterVersionRequest:
    out: GetAdapterVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    else:
        out["adapter_id"] = ""
    if data.get("AdapterVersion") is not None:
        out["adapter_version"] = data["AdapterVersion"]
    else:
        out["adapter_version"] = ""
    return out
