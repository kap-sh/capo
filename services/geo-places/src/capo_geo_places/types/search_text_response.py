"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.search_text_result_item_list
    import capo_geo_places.types.token


class SearchTextResponse(TypedDict, closed=True):
    pricing_bucket: "str"
    """<p>The pricing bucket for which the query is charged at.</p> <p>For more information on pricing, please visit <a href="https://aws.amazon.com/location/pricing/">Amazon Location Service Pricing</a>.</p>"""
    result_items: NotRequired[
        "capo_geo_places.types.search_text_result_item_list.SearchTextResultItemList"
    ]
    """<p>List of places or results returned for a query. </p>"""
    next_token: NotRequired["capo_geo_places.types.token.Token"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextResponse) -> dict:
    out: dict = {}
    if "result_items" in value:
        import capo_geo_places.types.search_text_result_item_list

        out["ResultItems"] = (
            capo_geo_places.types.search_text_result_item_list.serialize_json(
                value["result_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchTextResponse:
    out: SearchTextResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResultItems") is not None:
        import capo_geo_places.types.search_text_result_item_list

        out["result_items"] = (
            capo_geo_places.types.search_text_result_item_list.deserialize_json(
                data["ResultItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
