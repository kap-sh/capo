"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyIngestContentAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation_ingest_content


class AutomatedReasoningPolicyIngestContentAnnotation(TypedDict, closed=True):
    content: "capo_bedrock.types.automated_reasoning_policy_annotation_ingest_content.AutomatedReasoningPolicyAnnotationIngestContent"
    """<p>The new content to be analyzed and incorporated into the policy, such as additional documents or rule descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyIngestContentAnnotation) -> dict:
    out: dict = {}
    out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyIngestContentAnnotation:
    out: AutomatedReasoningPolicyIngestContentAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyIngestContentAnnotation.content required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyIngestContentAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
