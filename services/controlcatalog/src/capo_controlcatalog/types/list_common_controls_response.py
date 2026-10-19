"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListCommonControlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.common_control_summary_list
    import capo_controlcatalog.types.pagination_token


class ListCommonControlsResponse(TypedDict, closed=True):
    common_controls: (
        "capo_controlcatalog.types.common_control_summary_list.CommonControlSummaryList"
    )
    """<p>The list of common controls that the <code>ListCommonControls</code> API returns.</p>"""
    next_token: NotRequired[
        "capo_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommonControlsResponse) -> dict:
    out: dict = {}
    import capo_controlcatalog.types.common_control_summary_list

    out["CommonControls"] = (
        capo_controlcatalog.types.common_control_summary_list.serialize_json(
            value["common_controls"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCommonControlsResponse:
    out: ListCommonControlsResponse = {}  # type: ignore[typeddict-item]
    if data.get("CommonControls") is not None:
        import capo_controlcatalog.types.common_control_summary_list

        out["common_controls"] = (
            capo_controlcatalog.types.common_control_summary_list.deserialize_json(
                data["CommonControls"]
            )
        )
    else:
        out["common_controls"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
