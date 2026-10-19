"""Generated from Smithy shape ``com.amazonaws.textract#GetAdapterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_id


class GetAdapterRequest(TypedDict, closed=True):
    adapter_id: "capo_textract.types.adapter_id.AdapterId"
    """<p>A string containing a unique ID for the adapter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdapterRequest) -> dict:
    out: dict = {}
    out["AdapterId"] = value["adapter_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdapterRequest:
    out: GetAdapterRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdapterId") is not None:
        out["adapter_id"] = data["AdapterId"]
    else:
        out["adapter_id"] = ""
    return out
