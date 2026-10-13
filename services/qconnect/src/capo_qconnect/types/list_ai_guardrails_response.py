"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIGuardrailsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_summaries_list
    import capo_qconnect.types.next_token


class ListAIGuardrailsResponse(TypedDict, closed=True):
    ai_guardrail_summaries: (
        "capo_qconnect.types.ai_guardrail_summaries_list.AIGuardrailSummariesList"
    )
    """<p>The summaries of the AI Guardrails.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIGuardrailsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.ai_guardrail_summaries_list

    out["aiGuardrailSummaries"] = (
        capo_qconnect.types.ai_guardrail_summaries_list.serialize_json(
            value["ai_guardrail_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIGuardrailsResponse:
    out: ListAIGuardrailsResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiGuardrailSummaries") is not None:
        import capo_qconnect.types.ai_guardrail_summaries_list

        out["ai_guardrail_summaries"] = (
            capo_qconnect.types.ai_guardrail_summaries_list.deserialize_json(
                data["aiGuardrailSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAIGuardrailsResponse.ai_guardrail_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAIGuardrailsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_guardrail_summaries" in value:
        import capo_qconnect.types.ai_guardrail_summaries_list

        out["ai_guardrail_summaries"] = (
            capo_qconnect.types.ai_guardrail_summaries_list.redact_sensitive(
                value["ai_guardrail_summaries"]
            )
        )
    return out
