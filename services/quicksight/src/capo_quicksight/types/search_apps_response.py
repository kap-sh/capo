"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAppsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.app_summary_list
    import capo_quicksight.types.next_token


class SearchAppsResponse(TypedDict, closed=True):
    app_summary_list: "capo_quicksight.types.app_summary_list.AppSummaryList"
    """<p>A list of app summaries that match the search criteria.</p>"""
    next_token: NotRequired["capo_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAppsResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.app_summary_list

    out["AppSummaryList"] = capo_quicksight.types.app_summary_list.serialize_json(
        value["app_summary_list"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchAppsResponse:
    out: SearchAppsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppSummaryList") is not None:
        import capo_quicksight.types.app_summary_list

        out["app_summary_list"] = (
            capo_quicksight.types.app_summary_list.deserialize_json(
                data["AppSummaryList"]
            )
        )
    else:
        out["app_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
