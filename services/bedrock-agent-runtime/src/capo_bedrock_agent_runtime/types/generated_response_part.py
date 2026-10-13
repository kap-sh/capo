"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GeneratedResponsePart``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.text_response_part


class GeneratedResponsePart(TypedDict, closed=True):
    text_response_part: NotRequired[
        "capo_bedrock_agent_runtime.types.text_response_part.TextResponsePart"
    ]
    """<p>Contains metadata about a textual part of the generated response that is accompanied by a citation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedResponsePart) -> dict:
    out: dict = {}
    if "text_response_part" in value:
        import capo_bedrock_agent_runtime.types.text_response_part

        out["textResponsePart"] = (
            capo_bedrock_agent_runtime.types.text_response_part.serialize_json(
                value["text_response_part"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeneratedResponsePart:
    out: GeneratedResponsePart = {}  # type: ignore[typeddict-item]
    if data.get("textResponsePart") is not None:
        import capo_bedrock_agent_runtime.types.text_response_part

        out["text_response_part"] = (
            capo_bedrock_agent_runtime.types.text_response_part.deserialize_json(
                data["textResponsePart"]
            )
        )
    return out


def redact_sensitive(value: GeneratedResponsePart) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_response_part" in value:
        out["text_response_part"] = "*** Sensitive Data Redacted ***"
    return out
