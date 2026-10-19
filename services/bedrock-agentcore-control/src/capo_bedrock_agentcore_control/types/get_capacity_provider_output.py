"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetCapacityProviderOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_arn
    import capo_bedrock_agentcore_control.types.capacity_provider_id
    import capo_bedrock_agentcore_control.types.capacity_provider_name
    import capo_bedrock_agentcore_control.types.capacity_provider_status
    import capo_bedrock_agentcore_control.types.capacity_provider_status_code
    import capo_bedrock_agentcore_control.types.compute_configuration
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.permissions_configuration


class GetCapacityProviderOutput(TypedDict, closed=True):
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
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the capacity provider, if one was provided.</p>"""
    status_code: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_provider_status_code.CapacityProviderStatusCode"
    ]
    """<p>A reason code for a capacity provider that is not in the <code>READY</code> state. Use this code for programmatic error handling.</p>"""
    status_reason: NotRequired["str"]
    """<p>A human-readable message that describes why the capacity provider is not in the <code>READY</code> state. Because these messages can change, use <code>statusCode</code> for programmatic error handling.</p>"""
    permissions_configuration: "capo_bedrock_agentcore_control.types.permissions_configuration.PermissionsConfiguration"
    """<p>The permissions configuration for the capacity provider.</p>"""
    compute_configuration: "capo_bedrock_agentcore_control.types.compute_configuration.ComputeConfiguration"
    """<p>The compute configuration for the capacity provider.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the capacity provider was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the capacity provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCapacityProviderOutput) -> dict:
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
    if "description" in value:
        out["description"] = value["description"]
    if "status_code" in value:
        import capo_bedrock_agentcore_control.types.capacity_provider_status_code

        out["statusCode"] = (
            capo_bedrock_agentcore_control.types.capacity_provider_status_code.serialize_json(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_bedrock_agentcore_control.types.permissions_configuration

    out["permissionsConfiguration"] = (
        capo_bedrock_agentcore_control.types.permissions_configuration.serialize_json(
            value["permissions_configuration"]
        )
    )
    import capo_bedrock_agentcore_control.types.compute_configuration

    out["computeConfiguration"] = (
        capo_bedrock_agentcore_control.types.compute_configuration.serialize_json(
            value["compute_configuration"]
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


def deserialize_json(data: dict) -> GetCapacityProviderOutput:
    out: GetCapacityProviderOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("statusCode") is not None:
        import capo_bedrock_agentcore_control.types.capacity_provider_status_code

        out["status_code"] = (
            capo_bedrock_agentcore_control.types.capacity_provider_status_code.deserialize_json(
                data["statusCode"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("permissionsConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.permissions_configuration

        out["permissions_configuration"] = (
            capo_bedrock_agentcore_control.types.permissions_configuration.deserialize_json(
                data["permissionsConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetCapacityProviderOutput.permissions_configuration required"
        )
    if data.get("computeConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.compute_configuration

        out["compute_configuration"] = (
            capo_bedrock_agentcore_control.types.compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    else:
        import capo_bedrock_agentcore_control.types._unknown

        out["compute_configuration"] = (
            capo_bedrock_agentcore_control.types._unknown.UnknownUnionMember("")
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


def redact_sensitive(value: GetCapacityProviderOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
