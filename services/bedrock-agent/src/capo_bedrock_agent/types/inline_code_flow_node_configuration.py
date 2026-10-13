"""Generated from Smithy shape ``com.amazonaws.bedrockagent#InlineCodeFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.inline_code
    import capo_bedrock_agent.types.supported_languages


class InlineCodeFlowNodeConfiguration(TypedDict, closed=True):
    code: "capo_bedrock_agent.types.inline_code.InlineCode"
    """<p>The code that's executed in your inline code node. The code can access input data from previous nodes in the flow, perform operations on that data, and produce output that can be used by other nodes in your flow.</p> <p>The code must be valid in the programming <code>language</code> that you specify.</p>"""
    language: "capo_bedrock_agent.types.supported_languages.SupportedLanguages"
    """<p>The programming language used by your inline code node.</p> <p>The code must be valid in the programming <code>language</code> that you specify. Currently, only Python 3 (<code>Python_3</code>) is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineCodeFlowNodeConfiguration) -> dict:
    out: dict = {}
    out["code"] = value.get("code", "")
    import capo_bedrock_agent.types.supported_languages

    out["language"] = capo_bedrock_agent.types.supported_languages.serialize_json(
        value.get("language", "Python_3")
    )
    return out


def deserialize_json(data: dict) -> InlineCodeFlowNodeConfiguration:
    out: InlineCodeFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("language") is not None:
        import capo_bedrock_agent.types.supported_languages

        out["language"] = capo_bedrock_agent.types.supported_languages.deserialize_json(
            data["language"]
        )
    else:
        out["language"] = "Python_3"
    return out


def redact_sensitive(value: InlineCodeFlowNodeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    return out
