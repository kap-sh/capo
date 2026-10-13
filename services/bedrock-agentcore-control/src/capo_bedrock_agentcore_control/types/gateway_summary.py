"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewaySummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_type
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.gateway_description
    import capo_bedrock_agentcore_control.types.gateway_id
    import capo_bedrock_agentcore_control.types.gateway_name
    import capo_bedrock_agentcore_control.types.gateway_protocol_type
    import capo_bedrock_agentcore_control.types.gateway_status


class GatewaySummary(TypedDict, closed=True):
    gateway_id: "capo_bedrock_agentcore_control.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    name: "capo_bedrock_agentcore_control.types.gateway_name.GatewayName"
    """<p>The name of the gateway.</p>"""
    status: "capo_bedrock_agentcore_control.types.gateway_status.GatewayStatus"
    """<p>The current status of the gateway.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
    ]
    """<p>The description of the gateway.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway was last updated.</p>"""
    authorizer_type: (
        "capo_bedrock_agentcore_control.types.authorizer_type.AuthorizerType"
    )
    """<p>The type of authorizer used by the gateway.</p>"""
    protocol_type: (
        "capo_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
    )
    """<p>The protocol type used by the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewaySummary) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.gateway_status

    out["status"] = capo_bedrock_agentcore_control.types.gateway_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
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
    import capo_bedrock_agentcore_control.types.authorizer_type

    out["authorizerType"] = (
        capo_bedrock_agentcore_control.types.authorizer_type.serialize_json(
            value["authorizer_type"]
        )
    )
    import capo_bedrock_agentcore_control.types.gateway_protocol_type

    out["protocolType"] = (
        capo_bedrock_agentcore_control.types.gateway_protocol_type.serialize_json(
            value.get("protocol_type", "MCP")
        )
    )
    return out


def deserialize_json(data: dict) -> GatewaySummary:
    out: GatewaySummary = {}  # type: ignore[typeddict-item]
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GatewaySummary.gateway_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GatewaySummary.name required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.gateway_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.gateway_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GatewaySummary.status required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GatewaySummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GatewaySummary.updated_at required")
    if data.get("authorizerType") is not None:
        import capo_bedrock_agentcore_control.types.authorizer_type

        out["authorizer_type"] = (
            capo_bedrock_agentcore_control.types.authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    else:
        raise DeserializationError("GatewaySummary.authorizer_type required")
    if data.get("protocolType") is not None:
        import capo_bedrock_agentcore_control.types.gateway_protocol_type

        out["protocol_type"] = (
            capo_bedrock_agentcore_control.types.gateway_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    else:
        out["protocol_type"] = "MCP"
    return out


def redact_sensitive(value: GatewaySummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
