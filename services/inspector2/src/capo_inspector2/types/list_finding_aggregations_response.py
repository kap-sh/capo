"""Generated from Smithy shape ``com.amazonaws.inspector2#ListFindingAggregationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.aggregation_response_list
    import capo_inspector2.types.aggregation_type
    import capo_inspector2.types.next_token


class ListFindingAggregationsResponse(TypedDict, closed=True):
    aggregation_type: "capo_inspector2.types.aggregation_type.AggregationType"
    """<p>The type of aggregation to perform.</p>"""
    responses: NotRequired[
        "capo_inspector2.types.aggregation_response_list.AggregationResponseList"
    ]
    """<p>Objects that contain the results of an aggregation operation.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingAggregationsResponse) -> dict:
    out: dict = {}
    out["aggregationType"] = value["aggregation_type"]
    if "responses" in value:
        import capo_inspector2.types.aggregation_response_list

        out["responses"] = (
            capo_inspector2.types.aggregation_response_list.serialize_json(
                value["responses"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingAggregationsResponse:
    out: ListFindingAggregationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("aggregationType") is not None:
        out["aggregation_type"] = data["aggregationType"]
    else:
        out["aggregation_type"] = ""
    if data.get("responses") is not None:
        import capo_inspector2.types.aggregation_response_list

        out["responses"] = (
            capo_inspector2.types.aggregation_response_list.deserialize_json(
                data["responses"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
