"""Generated from Smithy shape ``com.amazonaws.continuum#IntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.integration_arn
    import capo_continuum.types.integration_id
    import capo_continuum.types.integration_name
    import capo_continuum.types.integration_type
    import capo_continuum.types.provider_details


class IntegrationSummary(TypedDict, closed=True):
    integration_id: "capo_continuum.types.integration_id.IntegrationId"
    """The unique identifier of the integration."""
    integration_arn: "capo_continuum.types.integration_arn.IntegrationArn"
    """The ARN of the integration."""
    name: "capo_continuum.types.integration_name.IntegrationName"
    """The name of the integration."""
    integration_type: "capo_continuum.types.integration_type.IntegrationType"
    """The immutable provider type for the integration."""
    provider_details: "capo_continuum.types.provider_details.ProviderDetails"
    """Provider-specific details for the integration."""
    created_at: "datetime.datetime"
    """The timestamp when the integration was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the integration was last updated."""


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummary) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["integrationArn"] = value["integration_arn"]
    out["name"] = value["name"]
    import capo_continuum.types.integration_type

    out["integrationType"] = capo_continuum.types.integration_type.serialize_json(
        value["integration_type"]
    )
    import capo_continuum.types.provider_details

    out["providerDetails"] = capo_continuum.types.provider_details.serialize_json(
        value["provider_details"]
    )
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_continuum._protocol.serialize

    out["updatedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> IntegrationSummary:
    out: IntegrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    else:
        out["integration_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("integrationType") is not None:
        import capo_continuum.types.integration_type

        out["integration_type"] = (
            capo_continuum.types.integration_type.deserialize_json(
                data["integrationType"]
            )
        )
    else:
        import typing

        out["integration_type"] = typing.cast(
            "capo_continuum.types.integration_type.IntegrationType", ""
        )
    if data.get("providerDetails") is not None:
        import capo_continuum.types.provider_details

        out["provider_details"] = (
            capo_continuum.types.provider_details.deserialize_json(
                data["providerDetails"]
            )
        )
    else:
        out["provider_details"] = {"$unknown": {"name": ""}}
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
