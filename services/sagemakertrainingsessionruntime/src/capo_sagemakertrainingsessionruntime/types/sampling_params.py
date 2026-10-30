"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SamplingParams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.stop_sequence_list


class SamplingParams(TypedDict, closed=True):
    max_tokens: "int"
    """<p>The maximum number of tokens to generate per sample.</p>"""
    temperature: "float"
    """<p>The sampling temperature controlling randomness. Higher values produce more diverse outputs.</p>"""
    top_k: "int"
    """<p>The number of highest-probability vocabulary tokens to keep for top-k filtering. Set to -1 to disable.</p>"""
    top_p: "float"
    """<p>The cumulative probability threshold for nucleus (top-p) sampling. Only tokens with cumulative probability below this threshold are considered.</p>"""
    seed: NotRequired["int"]
    """<p>The random seed for reproducible sampling. When set, the same seed with the same input produces deterministic outputs.</p>"""
    stop: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.stop_sequence_list.StopSequenceList"
    ]
    """<p>The list of stop sequences that terminate generation when encountered in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingParams) -> dict:
    out: dict = {}
    out["maxTokens"] = value["max_tokens"]
    out["temperature"] = (
        "NaN"
        if value.get("temperature", 1) != value.get("temperature", 1)
        else "Infinity"
        if value.get("temperature", 1) == float("inf")
        else "-Infinity"
        if value.get("temperature", 1) == float("-inf")
        else value.get("temperature", 1)
    )
    out["topK"] = value.get("top_k", -1)
    out["topP"] = (
        "NaN"
        if value.get("top_p", 1) != value.get("top_p", 1)
        else "Infinity"
        if value.get("top_p", 1) == float("inf")
        else "-Infinity"
        if value.get("top_p", 1) == float("-inf")
        else value.get("top_p", 1)
    )
    if "seed" in value:
        out["seed"] = value["seed"]
    if "stop" in value:
        import capo_sagemakertrainingsessionruntime.types.stop_sequence_list

        out["stop"] = (
            capo_sagemakertrainingsessionruntime.types.stop_sequence_list.serialize_json(
                value["stop"]
            )
        )
    return out


def deserialize_json(data: dict) -> SamplingParams:
    out: SamplingParams = {}  # type: ignore[typeddict-item]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    else:
        out["max_tokens"] = 0
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    else:
        out["temperature"] = 1
    if data.get("topK") is not None:
        out["top_k"] = data["topK"]
    else:
        out["top_k"] = -1
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    else:
        out["top_p"] = 1
    if data.get("seed") is not None:
        out["seed"] = data["seed"]
    if data.get("stop") is not None:
        import capo_sagemakertrainingsessionruntime.types.stop_sequence_list

        out["stop"] = (
            capo_sagemakertrainingsessionruntime.types.stop_sequence_list.deserialize_json(
                data["stop"]
            )
        )
    return out
