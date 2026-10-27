"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentEnterSessionActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.environment_id


class EnvironmentEnterSessionActionDefinition(TypedDict, closed=True):
    environment_id: "capo_deadline.types.environment_id.EnvironmentId"
    """The environment ID."""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentEnterSessionActionDefinition) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> EnvironmentEnterSessionActionDefinition:
    out: EnvironmentEnterSessionActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    return out
