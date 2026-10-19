"""Generated from Smithy shape ``com.amazonaws.support#UploadRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.end_index
    import capo_support.types.start_index


class UploadRange(TypedDict, closed=True):
    start_index: "capo_support.types.start_index.StartIndex"
    """<p>The starting part index of the range, inclusive. Part indexes start at 1.</p>"""
    end_index: NotRequired["capo_support.types.end_index.EndIndex"]
    """<p>The ending part index of the range, exclusive. The range is half-open: <code>startIndex</code> is inclusive and <code>endIndex</code> is exclusive. For example, a range with <code>startIndex</code> of 1 and <code>endIndex</code> of 4 requests URLs for parts 1, 2, and 3. The range size (<code>endIndex</code> - <code>startIndex</code>) must not exceed 10. If you omit <code>endIndex</code>, the service defaults to <code>startIndex</code> + 10, capped by the total number of parts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadRange) -> dict:
    out: dict = {}
    out["startIndex"] = value["start_index"]
    if "end_index" in value:
        out["endIndex"] = value["end_index"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UploadRange:
    out: UploadRange = {}  # type: ignore[typeddict-item]
    if data.get("startIndex") is not None:
        out["start_index"] = data["startIndex"]
    else:
        out["start_index"] = 0
    if data.get("endIndex") is not None:
        out["end_index"] = data["endIndex"]
    return out
