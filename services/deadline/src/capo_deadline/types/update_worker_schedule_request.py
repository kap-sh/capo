"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateWorkerScheduleRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.updated_session_actions
    import capo_deadline.types.worker_id


class UpdateWorkerScheduleRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID to update."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID to update."""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """The worker ID to update."""
    updated_session_actions: NotRequired[
        "capo_deadline.types.updated_session_actions.UpdatedSessionActions"
    ]
    """The session actions associated with the worker schedule to update."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkerScheduleRequest) -> dict:
    out: dict = {}
    if "updated_session_actions" in value:
        import capo_deadline.types.updated_session_actions

        out["updatedSessionActions"] = (
            capo_deadline.types.updated_session_actions.serialize_json(
                value["updated_session_actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkerScheduleRequest:
    out: UpdateWorkerScheduleRequest = {}  # type: ignore[typeddict-item]
    if data.get("updatedSessionActions") is not None:
        import capo_deadline.types.updated_session_actions

        out["updated_session_actions"] = (
            capo_deadline.types.updated_session_actions.deserialize_json(
                data["updatedSessionActions"]
            )
        )
    return out


def redact_sensitive(value: UpdateWorkerScheduleRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "updated_session_actions" in value:
        import capo_deadline.types.updated_session_actions

        out["updated_session_actions"] = (
            capo_deadline.types.updated_session_actions.redact_sensitive(
                value["updated_session_actions"]
            )
        )
    return out
