"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#ComputeLogprobsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.double_list


class ComputeLogprobsResult(TypedDict, closed=True):
    logprobs: "capo_sagemakertrainingsessionruntime.types.double_list.DoubleList"
    """<p>The per-token log-probabilities for the input prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeLogprobsResult) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.double_list

    out["logprobs"] = (
        capo_sagemakertrainingsessionruntime.types.double_list.serialize_json(
            value["logprobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ComputeLogprobsResult:
    out: ComputeLogprobsResult = {}  # type: ignore[typeddict-item]
    if data.get("logprobs") is not None:
        import capo_sagemakertrainingsessionruntime.types.double_list

        out["logprobs"] = (
            capo_sagemakertrainingsessionruntime.types.double_list.deserialize_json(
                data["logprobs"]
            )
        )
    else:
        out["logprobs"] = []
    return out
