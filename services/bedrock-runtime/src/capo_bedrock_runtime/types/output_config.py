"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#OutputConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.output_format


class OutputConfig(TypedDict, closed=True):
    text_format: NotRequired["capo_bedrock_runtime.types.output_format.OutputFormat"]
    """<p>Structured output parameters to control the model's text response. </p>"""
    effort: NotRequired["str"]
    """<p>The effort level for the model to use when generating a response. Higher effort levels allow the model to spend more time reasoning before responding. Supported values are <code>low</code>, <code>medium</code>, <code>high</code>, <code>xhigh</code>, and <code>max</code>.</p> <note> <p>When extended thinking is disabled, the effort level is capped at <code>high</code>. Use effort <code>high</code> or below, or enable thinking to use higher effort levels.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputConfig) -> dict:
    out: dict = {}
    if "text_format" in value:
        import capo_bedrock_runtime.types.output_format

        out["textFormat"] = capo_bedrock_runtime.types.output_format.serialize_json(
            value["text_format"]
        )
    if "effort" in value:
        out["effort"] = value["effort"]
    return out


def deserialize_json(data: dict) -> OutputConfig:
    out: OutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("textFormat") is not None:
        import capo_bedrock_runtime.types.output_format

        out["text_format"] = capo_bedrock_runtime.types.output_format.deserialize_json(
            data["textFormat"]
        )
    if data.get("effort") is not None:
        out["effort"] = data["effort"]
    return out


def redact_sensitive(value: OutputConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_format" in value:
        import capo_bedrock_runtime.types.output_format

        out["text_format"] = capo_bedrock_runtime.types.output_format.redact_sensitive(
            value["text_format"]
        )
    return out
