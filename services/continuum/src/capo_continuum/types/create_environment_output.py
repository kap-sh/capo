"""Generated from Smithy shape ``com.amazonaws.continuum#CreateEnvironmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.environment_arn
    import capo_continuum.types.environment_id
    import capo_continuum.types.environment_status


class CreateEnvironmentOutput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier assigned to the environment."""
    environment_arn: "capo_continuum.types.environment_arn.EnvironmentArn"
    """The ARN of the created environment."""
    status: "capo_continuum.types.environment_status.EnvironmentStatus"
    """The initial status of the environment. Always ACTIVE on successful creation."""
    created_at: "datetime.datetime"
    """The timestamp when the environment was created."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentOutput) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["environmentArn"] = value["environment_arn"]
    import capo_continuum.types.environment_status

    out["status"] = capo_continuum.types.environment_status.serialize_json(
        value["status"]
    )
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateEnvironmentOutput:
    out: CreateEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("environmentArn") is not None:
        out["environment_arn"] = data["environmentArn"]
    else:
        out["environment_arn"] = ""
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
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
