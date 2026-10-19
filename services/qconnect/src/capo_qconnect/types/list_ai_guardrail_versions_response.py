"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIGuardrailVersionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_version_summaries_list
    import capo_qconnect.types.next_token


class ListAIGuardrailVersionsResponse(TypedDict, closed=True):
    ai_guardrail_version_summaries: "capo_qconnect.types.ai_guardrail_version_summaries_list.AIGuardrailVersionSummariesList"
    """<p>The summaries of the AI Guardrail versions.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIGuardrailVersionsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.ai_guardrail_version_summaries_list

    out["aiGuardrailVersionSummaries"] = (
        capo_qconnect.types.ai_guardrail_version_summaries_list.serialize_json(
            value["ai_guardrail_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIGuardrailVersionsResponse:
    out: ListAIGuardrailVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiGuardrailVersionSummaries") is not None:
        import capo_qconnect.types.ai_guardrail_version_summaries_list

        out["ai_guardrail_version_summaries"] = (
            capo_qconnect.types.ai_guardrail_version_summaries_list.deserialize_json(
                data["aiGuardrailVersionSummaries"]
            )
        )
    else:
        out["ai_guardrail_version_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAIGuardrailVersionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_guardrail_version_summaries" in value:
        import capo_qconnect.types.ai_guardrail_version_summaries_list

        out["ai_guardrail_version_summaries"] = (
            capo_qconnect.types.ai_guardrail_version_summaries_list.redact_sensitive(
                value["ai_guardrail_version_summaries"]
            )
        )
    return out
