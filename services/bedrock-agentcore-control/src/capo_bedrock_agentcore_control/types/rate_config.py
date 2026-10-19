"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.period


class RateConfig(TypedDict, closed=True):
    rate: "float"
    """<p>The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.</p>"""
    period: "capo_bedrock_agentcore_control.types.period.Period"
    """<p>The time period for the rate limit. Valid values:</p> <ul> <li> <p> <code>second</code>—Measures the rate limit over a one-second window.</p> </li> <li> <p> <code>minute</code>—Measures the rate limit over a one-minute window.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RateConfig) -> dict:
    out: dict = {}
    out["rate"] = (
        "NaN"
        if value["rate"] != value["rate"]
        else "Infinity"
        if value["rate"] == float("inf")
        else "-Infinity"
        if value["rate"] == float("-inf")
        else value["rate"]
    )
    import capo_bedrock_agentcore_control.types.period

    out["period"] = capo_bedrock_agentcore_control.types.period.serialize_json(
        value["period"]
    )
    return out


def deserialize_json(data: dict) -> RateConfig:
    out: RateConfig = {}  # type: ignore[typeddict-item]
    if data.get("rate") is not None:
        out["rate"] = float(data["rate"])
    else:
        out["rate"] = 0.0
    if data.get("period") is not None:
        import capo_bedrock_agentcore_control.types.period

        out["period"] = capo_bedrock_agentcore_control.types.period.deserialize_json(
            data["period"]
        )
    else:
        import typing

        out["period"] = typing.cast(
            "capo_bedrock_agentcore_control.types.period.Period", ""
        )
    return out
