"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTruncationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_truncation_strategy
    import capo_bedrock_agentcore_control.types.harness_truncation_strategy_configuration


class HarnessTruncationConfiguration(TypedDict, closed=True):
    strategy: "capo_bedrock_agentcore_control.types.harness_truncation_strategy.HarnessTruncationStrategy"
    """<p>The truncation strategy to use.</p>"""
    config: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_truncation_strategy_configuration.HarnessTruncationStrategyConfiguration"
    ]
    """<p>The strategy-specific configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTruncationConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.harness_truncation_strategy

    out["strategy"] = (
        capo_bedrock_agentcore_control.types.harness_truncation_strategy.serialize_json(
            value["strategy"]
        )
    )
    if "config" in value:
        import capo_bedrock_agentcore_control.types.harness_truncation_strategy_configuration

        out["config"] = (
            capo_bedrock_agentcore_control.types.harness_truncation_strategy_configuration.serialize_json(
                value["config"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessTruncationConfiguration:
    out: HarnessTruncationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("strategy") is not None:
        import capo_bedrock_agentcore_control.types.harness_truncation_strategy

        out["strategy"] = (
            capo_bedrock_agentcore_control.types.harness_truncation_strategy.deserialize_json(
                data["strategy"]
            )
        )
    else:
        import typing

        out["strategy"] = typing.cast(
            "capo_bedrock_agentcore_control.types.harness_truncation_strategy.HarnessTruncationStrategy",
            "",
        )
    if data.get("config") is not None:
        import capo_bedrock_agentcore_control.types.harness_truncation_strategy_configuration

        out["config"] = (
            capo_bedrock_agentcore_control.types.harness_truncation_strategy_configuration.deserialize_json(
                data["config"]
            )
        )
    return out
