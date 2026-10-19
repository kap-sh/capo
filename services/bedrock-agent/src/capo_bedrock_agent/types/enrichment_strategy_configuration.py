"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EnrichmentStrategyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.enrichment_strategy_method


class EnrichmentStrategyConfiguration(TypedDict, closed=True):
    method: (
        "capo_bedrock_agent.types.enrichment_strategy_method.EnrichmentStrategyMethod"
    )
    """<p>The method used for the context enrichment strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentStrategyConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.enrichment_strategy_method

    out["method"] = capo_bedrock_agent.types.enrichment_strategy_method.serialize_json(
        value["method"]
    )
    return out


def deserialize_json(data: dict) -> EnrichmentStrategyConfiguration:
    out: EnrichmentStrategyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("method") is not None:
        import capo_bedrock_agent.types.enrichment_strategy_method

        out["method"] = (
            capo_bedrock_agent.types.enrichment_strategy_method.deserialize_json(
                data["method"]
            )
        )
    else:
        import typing

        out["method"] = typing.cast(
            "capo_bedrock_agent.types.enrichment_strategy_method.EnrichmentStrategyMethod",
            "",
        )
    return out
