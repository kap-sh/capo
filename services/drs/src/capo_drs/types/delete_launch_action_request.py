"""Generated from Smithy shape ``com.amazonaws.drs#DeleteLaunchActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_action_id
    import capo_drs.types.launch_action_resource_id


class DeleteLaunchActionRequest(TypedDict, closed=True):
    resource_id: "capo_drs.types.launch_action_resource_id.LaunchActionResourceId"
    action_id: "capo_drs.types.launch_action_id.LaunchActionId"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLaunchActionRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    out["actionId"] = value["action_id"]
    return out


def deserialize_json(data: dict) -> DeleteLaunchActionRequest:
    out: DeleteLaunchActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        out["action_id"] = ""
    return out
