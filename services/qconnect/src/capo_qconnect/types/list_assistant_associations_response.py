"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAssistantAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.assistant_association_summary_list
    import capo_qconnect.types.next_token


class ListAssistantAssociationsResponse(TypedDict, closed=True):
    assistant_association_summaries: "capo_qconnect.types.assistant_association_summary_list.AssistantAssociationSummaryList"
    """<p>Summary information about assistant associations.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssistantAssociationsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.assistant_association_summary_list

    out["assistantAssociationSummaries"] = (
        capo_qconnect.types.assistant_association_summary_list.serialize_json(
            value["assistant_association_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssistantAssociationsResponse:
    out: ListAssistantAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assistantAssociationSummaries") is not None:
        import capo_qconnect.types.assistant_association_summary_list

        out["assistant_association_summaries"] = (
            capo_qconnect.types.assistant_association_summary_list.deserialize_json(
                data["assistantAssociationSummaries"]
            )
        )
    else:
        out["assistant_association_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
