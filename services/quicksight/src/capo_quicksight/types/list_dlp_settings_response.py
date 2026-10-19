"""Generated from Smithy shape ``com.amazonaws.quicksight#ListDlpSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dlp_setting_summary_list
    import capo_quicksight.types.pagination_token


class ListDlpSettingsResponse(TypedDict, closed=True):
    dlp_setting_summaries: (
        "capo_quicksight.types.dlp_setting_summary_list.DlpSettingSummaryList"
    )
    """<p>A list of <code>DlpSettingSummary</code> objects for the DLP settings in the account. The list is empty if no DLP settings have been configured.</p>"""
    next_token: NotRequired["capo_quicksight.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDlpSettingsResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.dlp_setting_summary_list

    out["DlpSettingSummaries"] = (
        capo_quicksight.types.dlp_setting_summary_list.serialize_json(
            value["dlp_setting_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListDlpSettingsResponse:
    out: ListDlpSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DlpSettingSummaries") is not None:
        import capo_quicksight.types.dlp_setting_summary_list

        out["dlp_setting_summaries"] = (
            capo_quicksight.types.dlp_setting_summary_list.deserialize_json(
                data["DlpSettingSummaries"]
            )
        )
    else:
        out["dlp_setting_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
