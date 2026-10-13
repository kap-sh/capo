"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedChunk``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotated_content_list


class AutomatedReasoningPolicyAnnotatedChunk(TypedDict, closed=True):
    page_number: NotRequired["int"]
    """<p>The page number where this chunk begins, if the document is divided into pages.</p>"""
    content: "capo_bedrock.types.automated_reasoning_policy_annotated_content_list.AutomatedReasoningPolicyAnnotatedContentList"
    """<p>The lines of text contained within this chunk, each annotated with its line number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedChunk) -> dict:
    out: dict = {}
    if "page_number" in value:
        out["pageNumber"] = value["page_number"]
    import capo_bedrock.types.automated_reasoning_policy_annotated_content_list

    out["content"] = (
        capo_bedrock.types.automated_reasoning_policy_annotated_content_list.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAnnotatedChunk:
    out: AutomatedReasoningPolicyAnnotatedChunk = {}  # type: ignore[typeddict-item]
    if data.get("pageNumber") is not None:
        out["page_number"] = data["pageNumber"]
    if data.get("content") is not None:
        import capo_bedrock.types.automated_reasoning_policy_annotated_content_list

        out["content"] = (
            capo_bedrock.types.automated_reasoning_policy_annotated_content_list.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAnnotatedChunk.content required"
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyAnnotatedChunk) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock.types.automated_reasoning_policy_annotated_content_list

        out["content"] = (
            capo_bedrock.types.automated_reasoning_policy_annotated_content_list.redact_sensitive(
                value["content"]
            )
        )
    return out
