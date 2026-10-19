"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetGatewayRateLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.dimension_keys
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_description
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_status
    import capo_bedrock_agentcore_control.types.limit_entries


class GetGatewayRateLimitResponse(TypedDict, closed=True):
    rate_limit_id: (
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
    )
    """<p>The unique identifier of the rate limit.</p>"""
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
    ]
    """<p>The human-readable description of the rate limit.</p>"""
    dimension_keys: "capo_bedrock_agentcore_control.types.dimension_keys.DimensionKeys"
    """<p>The ordered list of dimension key names that define the scope of this rate limit.</p>"""
    entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries"
    """<p>The list of rule entries that map dimension values to rate configurations.</p>"""
    status: "capo_bedrock_agentcore_control.types.gateway_rate_limit_status.GatewayRateLimitStatus"
    """<p>The current status of the rate limit.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the rate limit was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the rate limit was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayRateLimitResponse) -> dict:
    out: dict = {}
    out["rateLimitId"] = value["rate_limit_id"]
    out["gatewayIdentifier"] = value["gateway_identifier"]
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
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.gateway_rate_limit_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetGatewayRateLimitResponse:
    out: GetGatewayRateLimitResponse = {}  # type: ignore[typeddict-item]
    if data.get("rateLimitId") is not None:
        out["rate_limit_id"] = data["rateLimitId"]
    else:
        out["rate_limit_id"] = ""
    if data.get("gatewayIdentifier") is not None:
        out["gateway_identifier"] = data["gatewayIdentifier"]
    else:
        out["gateway_identifier"] = ""
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
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.gateway_rate_limit_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.gateway_rate_limit_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_status.GatewayRateLimitStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
