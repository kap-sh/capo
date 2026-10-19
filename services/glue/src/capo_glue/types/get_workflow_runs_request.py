"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean
    import capo_glue.types.page_size


class GetWorkflowRunsRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>Name of the workflow whose metadata of runs should be returned.</p>"""
    include_graph: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to include the workflow graph in response or not.</p>"""
    next_token: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The maximum size of the response.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of workflow runs to be included in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunsRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "include_graph" in value:
        out["IncludeGraph"] = value["include_graph"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunsRequest:
    out: GetWorkflowRunsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("IncludeGraph") is not None:
        out["include_graph"] = data["IncludeGraph"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
