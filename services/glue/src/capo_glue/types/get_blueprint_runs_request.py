"""Generated from Smithy shape ``com.amazonaws.glue#GetBlueprintRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string
    import capo_glue.types.name_string
    import capo_glue.types.page_size


class GetBlueprintRunsRequest(TypedDict, closed=True):
    blueprint_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the blueprint.</p>"""
    next_token: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if this is a continuation request.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum size of a list to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintRunsRequest) -> dict:
    out: dict = {}
    out["BlueprintName"] = value["blueprint_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintRunsRequest:
    out: GetBlueprintRunsRequest = {}  # type: ignore[typeddict-item]
    if data.get("BlueprintName") is not None:
        out["blueprint_name"] = data["BlueprintName"]
    else:
        out["blueprint_name"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
