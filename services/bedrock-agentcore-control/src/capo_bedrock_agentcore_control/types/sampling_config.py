"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SamplingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.sampling_percentage


class SamplingConfig(TypedDict, closed=True):
    sampling_percentage: (
        "capo_bedrock_agentcore_control.types.sampling_percentage.SamplingPercentage"
    )
    """<p> The percentage of agent traces to sample for evaluation, ranging from 0.01% to 100%. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingConfig) -> dict:
    out: dict = {}
    out["samplingPercentage"] = (
        "NaN"
        if value["sampling_percentage"] != value["sampling_percentage"]
        else "Infinity"
        if value["sampling_percentage"] == float("inf")
        else "-Infinity"
        if value["sampling_percentage"] == float("-inf")
        else value["sampling_percentage"]
    )
    return out


def deserialize_json(data: dict) -> SamplingConfig:
    out: SamplingConfig = {}  # type: ignore[typeddict-item]
    if data.get("samplingPercentage") is not None:
        out["sampling_percentage"] = float(data["samplingPercentage"])
    else:
        out["sampling_percentage"] = 0.0
    return out
