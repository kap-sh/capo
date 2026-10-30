"""Generated from Smithy shape ``com.amazonaws.continuum#UpdateEnvironmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_continuum.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.environment_arn
    import capo_continuum.types.environment_configuration_details
    import capo_continuum.types.environment_id
    import capo_continuum.types.environment_name
    import capo_continuum.types.environment_status
    import capo_continuum.types.environment_status_message


class UpdateEnvironmentOutput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier of the updated environment."""
    environment_arn: "capo_continuum.types.environment_arn.EnvironmentArn"
    """The ARN of the updated environment."""
    name: "capo_continuum.types.environment_name.EnvironmentName"
    """The current customer-visible name of the environment."""
    status: "capo_continuum.types.environment_status.EnvironmentStatus"
    """The current operational status of the environment."""
    status_message: NotRequired[
        "capo_continuum.types.environment_status_message.EnvironmentStatusMessage"
    ]
    """Human-readable details about the current status."""
    status_updated_at: "datetime.datetime"
    """The timestamp when the status last transitioned. Uses the existing GetEnvironment/ListEnvironments ISO-8601 wire format for this field."""
    created_at: "datetime.datetime"
    """The timestamp when the environment was created. Uses the existing GetEnvironment/ListEnvironments ISO-8601 wire format for this field."""
    configuration: "capo_continuum.types.environment_configuration_details.EnvironmentConfigurationDetails"
    """Type-specific state, including Collector details and the latest scan. Read source and operating-policy settings through GetEnvironment."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentOutput) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["environmentArn"] = value["environment_arn"]
    out["name"] = value["name"]
    import capo_continuum.types.environment_status

    out["status"] = capo_continuum.types.environment_status.serialize_json(
        value["status"]
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import capo_continuum._protocol.serialize

    out["statusUpdatedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["status_updated_at"]
    )
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_continuum.types.environment_configuration_details

    out["configuration"] = (
        capo_continuum.types.environment_configuration_details.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentOutput:
    out: UpdateEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("environmentArn") is not None:
        out["environment_arn"] = data["environmentArn"]
    else:
        out["environment_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_continuum.types.environment_status

        out["status"] = capo_continuum.types.environment_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_continuum.types.environment_status.EnvironmentStatus", ""
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("statusUpdatedAt") is not None:
        import datetime

        out["status_updated_at"] = datetime.datetime.fromisoformat(
            data["statusUpdatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["status_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("configuration") is not None:
        import capo_continuum.types.environment_configuration_details

        out["configuration"] = (
            capo_continuum.types.environment_configuration_details.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("UpdateEnvironmentOutput.configuration required")
    return out
