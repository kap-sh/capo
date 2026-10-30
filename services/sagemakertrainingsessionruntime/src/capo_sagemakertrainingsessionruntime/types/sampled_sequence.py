"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampledSequence``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.double_list
    import capo_sagemakertrainingsessionruntime.types.integer_list
    import capo_sagemakertrainingsessionruntime.types.sample_token_usage
    import capo_sagemakertrainingsessionruntime.types.stop_reason


class SampledSequence(TypedDict, closed=True):
    stop_reason: "capo_sagemakertrainingsessionruntime.types.stop_reason.StopReason"
    """<p>The reason why generation stopped. A value of <code>stop</code> indicates a stop sequence was encountered. A value of <code>length</code> indicates the maximum token limit was reached.</p>"""
    tokens: "capo_sagemakertrainingsessionruntime.types.integer_list.IntegerList"
    """<p>The token IDs of the generated sequence.</p>"""
    logprobs: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.double_list.DoubleList"
    ]
    """<p>The per-token log-probabilities for the generated tokens.</p>"""
    token_usage: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.sample_token_usage.SampleTokenUsage"
    ]
    """<p>The token usage statistics for this individual sample.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampledSequence) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.stop_reason

    out["stopReason"] = (
        capo_sagemakertrainingsessionruntime.types.stop_reason.serialize_json(
            value["stop_reason"]
        )
    )
    import capo_sagemakertrainingsessionruntime.types.integer_list

    out["tokens"] = (
        capo_sagemakertrainingsessionruntime.types.integer_list.serialize_json(
            value["tokens"]
        )
    )
    if "logprobs" in value:
        import capo_sagemakertrainingsessionruntime.types.double_list

        out["logprobs"] = (
            capo_sagemakertrainingsessionruntime.types.double_list.serialize_json(
                value["logprobs"]
            )
        )
    if "token_usage" in value:
        import capo_sagemakertrainingsessionruntime.types.sample_token_usage

        out["tokenUsage"] = (
            capo_sagemakertrainingsessionruntime.types.sample_token_usage.serialize_json(
                value["token_usage"]
            )
        )
    return out


def deserialize_json(data: dict) -> SampledSequence:
    out: SampledSequence = {}  # type: ignore[typeddict-item]
    if data.get("stopReason") is not None:
        import capo_sagemakertrainingsessionruntime.types.stop_reason

        out["stop_reason"] = (
            capo_sagemakertrainingsessionruntime.types.stop_reason.deserialize_json(
                data["stopReason"]
            )
        )
    else:
        import typing

        out["stop_reason"] = typing.cast(
            "capo_sagemakertrainingsessionruntime.types.stop_reason.StopReason", ""
        )
    if data.get("tokens") is not None:
        import capo_sagemakertrainingsessionruntime.types.integer_list

        out["tokens"] = (
            capo_sagemakertrainingsessionruntime.types.integer_list.deserialize_json(
                data["tokens"]
            )
        )
    else:
        out["tokens"] = []
    if data.get("logprobs") is not None:
        import capo_sagemakertrainingsessionruntime.types.double_list

        out["logprobs"] = (
            capo_sagemakertrainingsessionruntime.types.double_list.deserialize_json(
                data["logprobs"]
            )
        )
    if data.get("tokenUsage") is not None:
        import capo_sagemakertrainingsessionruntime.types.sample_token_usage

        out["token_usage"] = (
            capo_sagemakertrainingsessionruntime.types.sample_token_usage.deserialize_json(
                data["tokenUsage"]
            )
        )
    return out
