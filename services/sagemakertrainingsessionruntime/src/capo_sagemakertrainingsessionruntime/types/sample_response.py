"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.double_list
    import capo_sagemakertrainingsessionruntime.types.sampled_sequence_list
    import capo_sagemakertrainingsessionruntime.types.topk_prompt_logprobs_list


class SampleResponse(TypedDict, closed=True):
    sequences: "capo_sagemakertrainingsessionruntime.types.sampled_sequence_list.SampledSequenceList"
    """<p>The list of generated sequences.</p>"""
    prompt_logprobs: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.double_list.DoubleList"
    ]
    """<p>The per-token log-probabilities for the input prompt. Populated only when <code>includePromptLogprobs</code> is true.</p>"""
    topk_prompt_logprobs: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.topk_prompt_logprobs_list.TopkPromptLogprobsList"
    ]
    """<p>The top-k log-probabilities per prompt token, as a list of lists. Populated only when <code>topkPromptLogprobs</code> is greater than 0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleResponse) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.sampled_sequence_list

    out["sequences"] = (
        capo_sagemakertrainingsessionruntime.types.sampled_sequence_list.serialize_json(
            value["sequences"]
        )
    )
    if "prompt_logprobs" in value:
        import capo_sagemakertrainingsessionruntime.types.double_list

        out["promptLogprobs"] = (
            capo_sagemakertrainingsessionruntime.types.double_list.serialize_json(
                value["prompt_logprobs"]
            )
        )
    if "topk_prompt_logprobs" in value:
        import capo_sagemakertrainingsessionruntime.types.topk_prompt_logprobs_list

        out["topkPromptLogprobs"] = (
            capo_sagemakertrainingsessionruntime.types.topk_prompt_logprobs_list.serialize_json(
                value["topk_prompt_logprobs"]
            )
        )
    return out


def deserialize_json(data: dict) -> SampleResponse:
    out: SampleResponse = {}  # type: ignore[typeddict-item]
    if data.get("sequences") is not None:
        import capo_sagemakertrainingsessionruntime.types.sampled_sequence_list

        out["sequences"] = (
            capo_sagemakertrainingsessionruntime.types.sampled_sequence_list.deserialize_json(
                data["sequences"]
            )
        )
    else:
        out["sequences"] = []
    if data.get("promptLogprobs") is not None:
        import capo_sagemakertrainingsessionruntime.types.double_list

        out["prompt_logprobs"] = (
            capo_sagemakertrainingsessionruntime.types.double_list.deserialize_json(
                data["promptLogprobs"]
            )
        )
    if data.get("topkPromptLogprobs") is not None:
        import capo_sagemakertrainingsessionruntime.types.topk_prompt_logprobs_list

        out["topk_prompt_logprobs"] = (
            capo_sagemakertrainingsessionruntime.types.topk_prompt_logprobs_list.deserialize_json(
                data["topkPromptLogprobs"]
            )
        )
    return out
