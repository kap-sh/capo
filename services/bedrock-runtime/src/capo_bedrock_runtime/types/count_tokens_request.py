"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CountTokensRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.count_tokens_input
    import capo_bedrock_runtime.types.foundation_model_version_identifier


class CountTokensRequest(TypedDict, closed=True):
    model_id: "capo_bedrock_runtime.types.foundation_model_version_identifier.FoundationModelVersionIdentifier"
    """<p>The unique identifier or ARN of the foundation model to use for token counting. Each model processes tokens differently, so the token count is specific to the model you specify.</p>"""
    input: "capo_bedrock_runtime.types.count_tokens_input.CountTokensInput"
    """<p>The input for which to count tokens. The structure of this parameter depends on whether you're counting tokens for an <code>InvokeModel</code> or <code>Converse</code> request:</p> <ul> <li> <p>For <code>InvokeModel</code> requests, provide the request body in the <code>invokeModel</code> field</p> </li> <li> <p>For <code>Converse</code> requests, provide the messages and system content in the <code>converse</code> field</p> </li> </ul> <p>The input format must be compatible with the model specified in the <code>modelId</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CountTokensRequest) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.count_tokens_input

    out["input"] = capo_bedrock_runtime.types.count_tokens_input.serialize_json(
        value["input"]
    )
    return out


def deserialize_json(data: dict) -> CountTokensRequest:
    out: CountTokensRequest = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        import capo_bedrock_runtime.types.count_tokens_input

        out["input"] = capo_bedrock_runtime.types.count_tokens_input.deserialize_json(
            data["input"]
        )
    else:
        out["input"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: CountTokensRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        import capo_bedrock_runtime.types.count_tokens_input

        out["input"] = capo_bedrock_runtime.types.count_tokens_input.redact_sensitive(
            value["input"]
        )
    return out
