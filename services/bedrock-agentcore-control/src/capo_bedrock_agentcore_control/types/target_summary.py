"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorization_data
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.listing_mode
    import capo_bedrock_agentcore_control.types.target_description
    import capo_bedrock_agentcore_control.types.target_id
    import capo_bedrock_agentcore_control.types.target_name
    import capo_bedrock_agentcore_control.types.target_resource_priority
    import capo_bedrock_agentcore_control.types.target_status
    import capo_bedrock_agentcore_control.types.target_type


class TargetSummary(TypedDict, closed=True):
    target_id: "capo_bedrock_agentcore_control.types.target_id.TargetId"
    """<p>The unique identifier of the target.</p>"""
    name: "capo_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the target.</p>"""
    status: "capo_bedrock_agentcore_control.types.target_status.TargetStatus"
    """<p>The current status of the target.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.target_description.TargetDescription"
    ]
    """<p>The description of the target.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the target was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the target was last updated.</p>"""
    resource_priority: NotRequired[
        "capo_bedrock_agentcore_control.types.target_resource_priority.TargetResourcePriority"
    ]
    """<p>Priority for resolving resource URI conflicts across targets. Lower values take precedence. Defaults to 1000 when not set.</p>"""
    last_synchronized_at: NotRequired[
        "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the target was last synchronized.</p>"""
    authorization_data: NotRequired[
        "capo_bedrock_agentcore_control.types.authorization_data.AuthorizationData"
    ]
    target_type: NotRequired[
        "capo_bedrock_agentcore_control.types.target_type.TargetType"
    ]
    """<p>The type of the target.</p>"""
    listing_mode: NotRequired[
        "capo_bedrock_agentcore_control.types.listing_mode.ListingMode"
    ]
    """<p>The listing mode for the target. MCP resources for <code>DEFAULT</code> targets are cached at the control plane for faster access. MCP resources for <code>DYNAMIC</code> targets are retrieved dynamically when listing tools.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummary) -> dict:
    out: dict = {}
    out["targetId"] = value["target_id"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.target_status

    out["status"] = capo_bedrock_agentcore_control.types.target_status.serialize_json(
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
    if "resource_priority" in value:
        out["resourcePriority"] = value["resource_priority"]
    if "last_synchronized_at" in value:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["lastSynchronizedAt"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["last_synchronized_at"]
            )
        )
    if "authorization_data" in value:
        import capo_bedrock_agentcore_control.types.authorization_data

        out["authorizationData"] = (
            capo_bedrock_agentcore_control.types.authorization_data.serialize_json(
                value["authorization_data"]
            )
        )
    if "target_type" in value:
        import capo_bedrock_agentcore_control.types.target_type

        out["targetType"] = (
            capo_bedrock_agentcore_control.types.target_type.serialize_json(
                value["target_type"]
            )
        )
    if "listing_mode" in value:
        import capo_bedrock_agentcore_control.types.listing_mode

        out["listingMode"] = (
            capo_bedrock_agentcore_control.types.listing_mode.serialize_json(
                value["listing_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> TargetSummary:
    out: TargetSummary = {}  # type: ignore[typeddict-item]
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError("TargetSummary.target_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TargetSummary.name required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.target_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.target_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("TargetSummary.status required")
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
        raise DeserializationError("TargetSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("TargetSummary.updated_at required")
    if data.get("resourcePriority") is not None:
        out["resource_priority"] = data["resourcePriority"]
    if data.get("lastSynchronizedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_synchronized_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastSynchronizedAt"]
            )
        )
    if data.get("authorizationData") is not None:
        import capo_bedrock_agentcore_control.types.authorization_data

        out["authorization_data"] = (
            capo_bedrock_agentcore_control.types.authorization_data.deserialize_json(
                data["authorizationData"]
            )
        )
    if data.get("targetType") is not None:
        import capo_bedrock_agentcore_control.types.target_type

        out["target_type"] = (
            capo_bedrock_agentcore_control.types.target_type.deserialize_json(
                data["targetType"]
            )
        )
    if data.get("listingMode") is not None:
        import capo_bedrock_agentcore_control.types.listing_mode

        out["listing_mode"] = (
            capo_bedrock_agentcore_control.types.listing_mode.deserialize_json(
                data["listingMode"]
            )
        )
    return out


def redact_sensitive(value: TargetSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
