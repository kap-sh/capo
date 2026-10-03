"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InferenceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.non_empty_string_list


class InferenceConfiguration(TypedDict, closed=True):
    max_tokens: NotRequired["int"]
    """<p>The maximum number of tokens to allow in the generated response. The default value is the maximum allowed value for the model that you are using. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters for foundation models</a>. </p>"""
    temperature: NotRequired["float"]
    """<p>The likelihood of the model selecting higher-probability options while generating a response. A lower value makes the model more likely to choose higher-probability options, while a higher value makes the model more likely to choose lower-probability options.</p> <p>The default value is the default value for the model that you are using. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters for foundation models</a>. </p>"""
    top_p: NotRequired["float"]
    """<p>The percentage of most-likely candidates that the model considers for the next token. For example, if you choose a value of 0.8 for <code>topP</code>, the model selects from the top 80% of the probability distribution of tokens that could be next in the sequence.</p> <p>The default value is the default value for the model that you are using. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters for foundation models</a>. </p>"""
    stop_sequences: NotRequired[
        "capo_bedrock_runtime.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConfiguration) -> dict:
    out: dict = {}
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
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
    if "stop_sequences" in value:
        import capo_bedrock_runtime.types.non_empty_string_list

        out["stopSequences"] = (
            capo_bedrock_runtime.types.non_empty_string_list.serialize_json(
                value["stop_sequences"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceConfiguration:
    out: InferenceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    if data.get("stopSequences") is not None:
        import capo_bedrock_runtime.types.non_empty_string_list

        out["stop_sequences"] = (
            capo_bedrock_runtime.types.non_empty_string_list.deserialize_json(
                data["stopSequences"]
            )
        )
    return out
