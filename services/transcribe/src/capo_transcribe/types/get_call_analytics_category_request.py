"""Generated from Smithy shape ``com.amazonaws.transcribe#GetCallAnalyticsCategoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.category_name


class GetCallAnalyticsCategoryRequest(TypedDict, closed=True):
    category_name: "capo_transcribe.types.category_name.CategoryName"
    """<p>The name of the Call Analytics category you want information about. Category names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCallAnalyticsCategoryRequest) -> dict:
    out: dict = {}
    out["CategoryName"] = value["category_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCallAnalyticsCategoryRequest:
    out: GetCallAnalyticsCategoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("CategoryName") is not None:
        out["category_name"] = data["CategoryName"]
    else:
        out["category_name"] = ""
    return out
