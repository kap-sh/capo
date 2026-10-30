"""Generated from Smithy shape ``com.amazonaws.continuum#CreateIntegrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.integration_arn
    import capo_continuum.types.integration_id


class CreateIntegrationOutput(TypedDict, closed=True):
    integration_id: "capo_continuum.types.integration_id.IntegrationId"
    """The unique identifier of the created integration."""
    integration_arn: "capo_continuum.types.integration_arn.IntegrationArn"
    """The ARN of the created integration."""
    created_at: "datetime.datetime"
    """The timestamp when the integration was created."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationOutput) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["integrationArn"] = value["integration_arn"]
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateIntegrationOutput:
    out: CreateIntegrationOutput = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    else:
        out["integration_arn"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
