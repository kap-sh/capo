"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BatchPutLimitEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dimension_keys
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_description
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id
    import capo_bedrock_agentcore_control.types.limit_entries


class BatchPutLimitEntry(TypedDict, closed=True):
    rate_limit_id: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
    ]
    """<p>The unique identifier of the rate limit. If provided, the service uses it for upsert matching against existing rate limits.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
    ]
    """<p>An optional human-readable description for this rate limit. If not provided, the rate limit is created without a description.</p>"""
    dimension_keys: "capo_bedrock_agentcore_control.types.dimension_keys.DimensionKeys"
    """<p>The ordered list of dimension key names that define the scope of this rate limit.</p>"""
    entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries"
    """<p>The list of rule entries that map dimension values to rate configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutLimitEntry) -> dict:
    out: dict = {}
    if "rate_limit_id" in value:
        out["rateLimitId"] = value["rate_limit_id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.dimension_keys

    out["dimensionKeys"] = (
        capo_bedrock_agentcore_control.types.dimension_keys.serialize_json(
            value["dimension_keys"]
        )
    )
    import capo_bedrock_agentcore_control.types.limit_entries

    out["entries"] = capo_bedrock_agentcore_control.types.limit_entries.serialize_json(
        value["entries"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutLimitEntry:
    out: BatchPutLimitEntry = {}  # type: ignore[typeddict-item]
    if data.get("rateLimitId") is not None:
        out["rate_limit_id"] = data["rateLimitId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("dimensionKeys") is not None:
        import capo_bedrock_agentcore_control.types.dimension_keys

        out["dimension_keys"] = (
            capo_bedrock_agentcore_control.types.dimension_keys.deserialize_json(
                data["dimensionKeys"]
            )
        )
    else:
        out["dimension_keys"] = []
    if data.get("entries") is not None:
        import capo_bedrock_agentcore_control.types.limit_entries

        out["entries"] = (
            capo_bedrock_agentcore_control.types.limit_entries.deserialize_json(
                data["entries"]
            )
        )
    else:
        out["entries"] = []
    return out
