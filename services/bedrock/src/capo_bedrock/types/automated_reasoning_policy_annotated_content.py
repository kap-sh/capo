"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedContent``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotated_line


class AutomatedReasoningPolicyAnnotatedContentLineMember(TypedDict, closed=True):
    line: "capo_bedrock.types.automated_reasoning_policy_annotated_line.AutomatedReasoningPolicyAnnotatedLine"


AutomatedReasoningPolicyAnnotatedContent: TypeAlias = (
    AutomatedReasoningPolicyAnnotatedContentLineMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AutomatedReasoningPolicyAnnotatedContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "line" in value:
        import capo_bedrock.types.automated_reasoning_policy_annotated_line

        return {
            "line": capo_bedrock.types.automated_reasoning_policy_annotated_line.serialize_json(
                value["line"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyAnnotatedContent: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAnnotatedContent:
    if data.get("line") is not None:
        import capo_bedrock.types.automated_reasoning_policy_annotated_line

        return {
            "line": capo_bedrock.types.automated_reasoning_policy_annotated_line.deserialize_json(
                data["line"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AutomatedReasoningPolicyAnnotatedContent: no recognized variant key"
        )


def redact_sensitive(value: AutomatedReasoningPolicyAnnotatedContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "line" in value:
        import capo_bedrock.types.automated_reasoning_policy_annotated_line

        out["line"] = (
            capo_bedrock.types.automated_reasoning_policy_annotated_line.redact_sensitive(
                value["line"]
            )
        )
    return out
