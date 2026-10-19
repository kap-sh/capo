"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_summary_list
    import capo_resiliencehub.types.next_token


class ListAppsResponse(TypedDict, closed=True):
    app_summaries: "capo_resiliencehub.types.app_summary_list.AppSummaryList"
    """<p>Summaries for the Resilience Hub application.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app_summary_list

    out["appSummaries"] = capo_resiliencehub.types.app_summary_list.serialize_json(
        value["app_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppsResponse:
    out: ListAppsResponse = {}  # type: ignore[typeddict-item]
    if data.get("appSummaries") is not None:
        import capo_resiliencehub.types.app_summary_list

        out["app_summaries"] = (
            capo_resiliencehub.types.app_summary_list.deserialize_json(
                data["appSummaries"]
            )
        )
    else:
        out["app_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
