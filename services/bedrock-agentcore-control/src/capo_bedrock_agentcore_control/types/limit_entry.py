"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LimitEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dimensions
    import capo_bedrock_agentcore_control.types.rate_configs


class LimitEntry(TypedDict, closed=True):
    dimensions: "capo_bedrock_agentcore_control.types.dimensions.Dimensions"
    """<p>A map of dimension names to dimension values for this rule entry. Keys must match the parent rate limit's dimension keys. Values may use <code>*</code> as a wildcard, but only in trailing positions based on the dimension keys ordering.</p>"""
    requests: NotRequired[
        "capo_bedrock_agentcore_control.types.rate_configs.RateConfigs"
    ]
    """<p>The request rate limit configuration. Specifies the maximum number of requests allowed per time period.</p>"""
    tokens: NotRequired["capo_bedrock_agentcore_control.types.rate_configs.RateConfigs"]
    """<p>The token rate limit configuration. Specifies the maximum number of tokens allowed per time period.</p>"""
    connections: NotRequired[
        "capo_bedrock_agentcore_control.types.rate_configs.RateConfigs"
    ]
    """<p>The connection rate limit configuration. Specifies the maximum number of concurrent connections allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitEntry) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.dimensions

    out["dimensions"] = capo_bedrock_agentcore_control.types.dimensions.serialize_json(
        value["dimensions"]
    )
    if "requests" in value:
        import capo_bedrock_agentcore_control.types.rate_configs

        out["requests"] = (
            capo_bedrock_agentcore_control.types.rate_configs.serialize_json(
                value["requests"]
            )
        )
    if "tokens" in value:
        import capo_bedrock_agentcore_control.types.rate_configs

        out["tokens"] = (
            capo_bedrock_agentcore_control.types.rate_configs.serialize_json(
                value["tokens"]
            )
        )
    if "connections" in value:
        import capo_bedrock_agentcore_control.types.rate_configs

        out["connections"] = (
            capo_bedrock_agentcore_control.types.rate_configs.serialize_json(
                value["connections"]
            )
        )
    return out


def deserialize_json(data: dict) -> LimitEntry:
    out: LimitEntry = {}  # type: ignore[typeddict-item]
    if data.get("dimensions") is not None:
        import capo_bedrock_agentcore_control.types.dimensions

        out["dimensions"] = (
            capo_bedrock_agentcore_control.types.dimensions.deserialize_json(
                data["dimensions"]
            )
        )
    else:
        out["dimensions"] = {}
    if data.get("requests") is not None:
        import capo_bedrock_agentcore_control.types.rate_configs

        out["requests"] = (
            capo_bedrock_agentcore_control.types.rate_configs.deserialize_json(
                data["requests"]
            )
        )
    if data.get("tokens") is not None:
        import capo_bedrock_agentcore_control.types.rate_configs

        out["tokens"] = (
            capo_bedrock_agentcore_control.types.rate_configs.deserialize_json(
                data["tokens"]
            )
        )
    if data.get("connections") is not None:
        import capo_bedrock_agentcore_control.types.rate_configs

        out["connections"] = (
            capo_bedrock_agentcore_control.types.rate_configs.deserialize_json(
                data["connections"]
            )
        )
    return out
