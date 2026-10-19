"""Generated from Smithy shape ``com.amazonaws.appfabric#ListAppAuthorizationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.app_authorization_summary_list
    import capo_appfabric.types.string2048


class ListAppAuthorizationsResponse(TypedDict, closed=True):
    app_authorization_summary_list: "capo_appfabric.types.app_authorization_summary_list.AppAuthorizationSummaryList"
    """<p>Contains a list of app authorization summaries.</p>"""
    next_token: NotRequired["capo_appfabric.types.string2048.String2048"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppAuthorizationsResponse) -> dict:
    out: dict = {}
    import capo_appfabric.types.app_authorization_summary_list

    out["appAuthorizationSummaryList"] = (
        capo_appfabric.types.app_authorization_summary_list.serialize_json(
            value["app_authorization_summary_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppAuthorizationsResponse:
    out: ListAppAuthorizationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("appAuthorizationSummaryList") is not None:
        import capo_appfabric.types.app_authorization_summary_list

        out["app_authorization_summary_list"] = (
            capo_appfabric.types.app_authorization_summary_list.deserialize_json(
                data["appAuthorizationSummaryList"]
            )
        )
    else:
        out["app_authorization_summary_list"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
