"""Generated from Smithy shape ``com.amazonaws.qconnect#ListMessageTemplatesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_summary_list
    import capo_qconnect.types.next_token


class ListMessageTemplatesResponse(TypedDict, closed=True):
    message_template_summaries: (
        "capo_qconnect.types.message_template_summary_list.MessageTemplateSummaryList"
    )
    """<p>Summary information about the message template.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMessageTemplatesResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.message_template_summary_list

    out["messageTemplateSummaries"] = (
        capo_qconnect.types.message_template_summary_list.serialize_json(
            value["message_template_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMessageTemplatesResponse:
    out: ListMessageTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("messageTemplateSummaries") is not None:
        import capo_qconnect.types.message_template_summary_list

        out["message_template_summaries"] = (
            capo_qconnect.types.message_template_summary_list.deserialize_json(
                data["messageTemplateSummaries"]
            )
        )
    else:
        out["message_template_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListMessageTemplatesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message_template_summaries" in value:
        import capo_qconnect.types.message_template_summary_list

        out["message_template_summaries"] = (
            capo_qconnect.types.message_template_summary_list.redact_sensitive(
                value["message_template_summaries"]
            )
        )
    return out
