"""Generated from Smithy shape ``com.amazonaws.connect#ListViewsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.views_next_token
    import capo_connect.types.views_summary_list


class ListViewsResponse(TypedDict, closed=True):
    views_summary_list: NotRequired[
        "capo_connect.types.views_summary_list.ViewsSummaryList"
    ]
    """<p>A list of view summaries.</p>"""
    next_token: NotRequired["capo_connect.types.views_next_token.ViewsNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListViewsResponse) -> dict:
    out: dict = {}
    if "views_summary_list" in value:
        import capo_connect.types.views_summary_list

        out["ViewsSummaryList"] = capo_connect.types.views_summary_list.serialize_json(
            value["views_summary_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListViewsResponse:
    out: ListViewsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ViewsSummaryList") is not None:
        import capo_connect.types.views_summary_list

        out["views_summary_list"] = (
            capo_connect.types.views_summary_list.deserialize_json(
                data["ViewsSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListViewsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "views_summary_list" in value:
        import capo_connect.types.views_summary_list

        out["views_summary_list"] = (
            capo_connect.types.views_summary_list.redact_sensitive(
                value["views_summary_list"]
            )
        )
    return out
