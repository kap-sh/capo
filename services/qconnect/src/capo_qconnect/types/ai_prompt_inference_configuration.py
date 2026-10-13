"""Generated from Smithy shape ``com.amazonaws.qconnect#AIPromptInferenceConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.max_tokens_to_sample
    import capo_qconnect.types.probability
    import capo_qconnect.types.top_k


class AIPromptInferenceConfiguration(TypedDict, closed=True):
    temperature: NotRequired["capo_qconnect.types.probability.Probability"]
    """<p>The temperature setting for controlling randomness in the generated response.</p>"""
    top_p: NotRequired["capo_qconnect.types.probability.Probability"]
    """<p>The top-P sampling parameter for nucleus sampling.</p>"""
    top_k: NotRequired["capo_qconnect.types.top_k.TopK"]
    """<p>The top-K sampling parameter for token selection.</p>"""
    max_tokens_to_sample: NotRequired[
        "capo_qconnect.types.max_tokens_to_sample.MaxTokensToSample"
    ]
    """<p>The maximum number of tokens to generate in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIPromptInferenceConfiguration) -> dict:
    out: dict = {}
    if "temperature" in value:
        out["temperature"] = (
            "NaN"
            if value["temperature"] != value["temperature"]
            else "Infinity"
            if value["temperature"] == float("inf")
            else "-Infinity"
            if value["temperature"] == float("-inf")
            else value["temperature"]
        )
    if "top_p" in value:
        out["topP"] = (
            "NaN"
            if value["top_p"] != value["top_p"]
            else "Infinity"
            if value["top_p"] == float("inf")
            else "-Infinity"
            if value["top_p"] == float("-inf")
            else value["top_p"]
        )
    if "top_k" in value:
        out["topK"] = value["top_k"]
    if "max_tokens_to_sample" in value:
        out["maxTokensToSample"] = value["max_tokens_to_sample"]
    return out


def deserialize_json(data: dict) -> AIPromptInferenceConfiguration:
    out: AIPromptInferenceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    if data.get("topK") is not None:
        out["top_k"] = data["topK"]
    if data.get("maxTokensToSample") is not None:
        out["max_tokens_to_sample"] = data["maxTokensToSample"]
    return out


def redact_sensitive(value: AIPromptInferenceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "temperature" in value:
        out["temperature"] = "*** Sensitive Data Redacted ***"
    if "top_p" in value:
        out["top_p"] = "*** Sensitive Data Redacted ***"
    if "top_k" in value:
        out["top_k"] = "*** Sensitive Data Redacted ***"
    if "max_tokens_to_sample" in value:
        out["max_tokens_to_sample"] = "*** Sensitive Data Redacted ***"
    return out
