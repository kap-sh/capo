"""Generated from Smithy shape ``com.amazonaws.qconnect#ListContentAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.content_association_summary_list
    import capo_qconnect.types.next_token


class ListContentAssociationsResponse(TypedDict, closed=True):
    content_association_summaries: "capo_qconnect.types.content_association_summary_list.ContentAssociationSummaryList"
    """<p>Summary information about content associations.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContentAssociationsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.content_association_summary_list

    out["contentAssociationSummaries"] = (
        capo_qconnect.types.content_association_summary_list.serialize_json(
            value["content_association_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContentAssociationsResponse:
    out: ListContentAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("contentAssociationSummaries") is not None:
        import capo_qconnect.types.content_association_summary_list

        out["content_association_summaries"] = (
            capo_qconnect.types.content_association_summary_list.deserialize_json(
                data["contentAssociationSummaries"]
            )
        )
    else:
        out["content_association_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
