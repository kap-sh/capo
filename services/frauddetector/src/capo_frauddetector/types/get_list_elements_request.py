"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetListElementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.lists_elements_max_results
    import capo_frauddetector.types.next_token
    import capo_frauddetector.types.no_dash_identifier


class GetListElementsRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier"
    """<p> The name of the list. </p>"""
    next_token: NotRequired["capo_frauddetector.types.next_token.nextToken"]
    """<p> The next token for the subsequent request. </p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.lists_elements_max_results.ListsElementsMaxResults"
    ]
    """<p> The maximum number of objects to return for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetListElementsRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetListElementsRequest:
    out: GetListElementsRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
