"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateCapacityProviderOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_arn
    import capo_bedrock_agentcore_control.types.capacity_provider_id
    import capo_bedrock_agentcore_control.types.capacity_provider_name
    import capo_bedrock_agentcore_control.types.capacity_provider_status
    import capo_bedrock_agentcore_control.types.date_timestamp


class UpdateCapacityProviderOutput(TypedDict, closed=True):
    capacity_provider_id: (
        "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId"
    )
    """<p>The unique identifier of the capacity provider.</p>"""
    capacity_provider_arn: (
        "capo_bedrock_agentcore_control.types.capacity_provider_arn.CapacityProviderArn"
    )
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    name: "capo_bedrock_agentcore_control.types.capacity_provider_name.CapacityProviderName"
    """<p>The name of the capacity provider.</p>"""
    status: "capo_bedrock_agentcore_control.types.capacity_provider_status.CapacityProviderStatus"
    """<p>The current status of the capacity provider. For possible values, see <code>CapacityProviderStatus</code>.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the capacity provider was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the capacity provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCapacityProviderOutput) -> dict:
    out: dict = {}
    out["capacityProviderId"] = value["capacity_provider_id"]
    out["capacityProviderArn"] = value["capacity_provider_arn"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.capacity_provider_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.capacity_provider_status.serialize_json(
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

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateCapacityProviderOutput:
    out: UpdateCapacityProviderOutput = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviderId") is not None:
        out["capacity_provider_id"] = data["capacityProviderId"]
    else:
        out["capacity_provider_id"] = ""
    if data.get("capacityProviderArn") is not None:
        out["capacity_provider_arn"] = data["capacityProviderArn"]
    else:
        out["capacity_provider_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.capacity_provider_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.capacity_provider_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.capacity_provider_status.CapacityProviderStatus",
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
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
