"""Generated from Smithy shape ``com.amazonaws.connect#ListViewVersionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.view_version_summary_list
    import capo_connect.types.views_next_token


class ListViewVersionsResponse(TypedDict, closed=True):
    view_version_summary_list: NotRequired[
        "capo_connect.types.view_version_summary_list.ViewVersionSummaryList"
    ]
    """<p>A list of view version summaries.</p>"""
    next_token: NotRequired["capo_connect.types.views_next_token.ViewsNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListViewVersionsResponse) -> dict:
    out: dict = {}
    if "view_version_summary_list" in value:
        import capo_connect.types.view_version_summary_list

        out["ViewVersionSummaryList"] = (
            capo_connect.types.view_version_summary_list.serialize_json(
                value["view_version_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListViewVersionsResponse:
    out: ListViewVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ViewVersionSummaryList") is not None:
        import capo_connect.types.view_version_summary_list

        out["view_version_summary_list"] = (
            capo_connect.types.view_version_summary_list.deserialize_json(
                data["ViewVersionSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListViewVersionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "view_version_summary_list" in value:
        import capo_connect.types.view_version_summary_list

        out["view_version_summary_list"] = (
            capo_connect.types.view_version_summary_list.redact_sensitive(
                value["view_version_summary_list"]
            )
        )
    return out
