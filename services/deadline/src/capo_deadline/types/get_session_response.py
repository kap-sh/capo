"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.ended_at
    import capo_deadline.types.fleet_id
    import capo_deadline.types.host_properties_response
    import capo_deadline.types.log_configuration
    import capo_deadline.types.session_id
    import capo_deadline.types.session_lifecycle_status
    import capo_deadline.types.session_lifecycle_target_status
    import capo_deadline.types.started_at
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by
    import capo_deadline.types.worker_id


class GetSessionResponse(TypedDict, closed=True):
    session_id: "capo_deadline.types.session_id.SessionId"
    """<p>The session ID.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID for the session.</p>"""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The worker ID for the session.</p>"""
    started_at: "capo_deadline.types.started_at.StartedAt"
    """<p>The date and time the resource started running.</p>"""
    lifecycle_status: (
        "capo_deadline.types.session_lifecycle_status.SessionLifecycleStatus"
    )
    """<p>The life cycle status of the session.</p>"""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    target_lifecycle_status: NotRequired[
        "capo_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus"
    ]
    """<p>The life cycle status with which the session started.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    log: "capo_deadline.types.log_configuration.LogConfiguration"
    """<p>The session log.</p>"""
    host_properties: NotRequired[
        "capo_deadline.types.host_properties_response.HostPropertiesResponse"
    ]
    """<p>Provides the Amazon EC2 properties of the host.</p>"""
    worker_log: NotRequired["capo_deadline.types.log_configuration.LogConfiguration"]
    """<p>The worker log for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    import capo_deadline.types.started_at

    out["startedAt"] = capo_deadline.types.started_at.serialize_json(
        value["started_at"]
    )
    import capo_deadline.types.session_lifecycle_status

    out["lifecycleStatus"] = (
        capo_deadline.types.session_lifecycle_status.serialize_json(
            value["lifecycle_status"]
        )
    )
    if "ended_at" in value:
        import capo_deadline.types.ended_at

        out["endedAt"] = capo_deadline.types.ended_at.serialize_json(value["ended_at"])
    if "target_lifecycle_status" in value:
        import capo_deadline.types.session_lifecycle_target_status

        out["targetLifecycleStatus"] = (
            capo_deadline.types.session_lifecycle_target_status.serialize_json(
                value["target_lifecycle_status"]
            )
        )
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    import capo_deadline.types.log_configuration

    out["log"] = capo_deadline.types.log_configuration.serialize_json(value["log"])
    if "host_properties" in value:
        import capo_deadline.types.host_properties_response

        out["hostProperties"] = (
            capo_deadline.types.host_properties_response.serialize_json(
                value["host_properties"]
            )
        )
    if "worker_log" in value:
        import capo_deadline.types.log_configuration

        out["workerLog"] = capo_deadline.types.log_configuration.serialize_json(
            value["worker_log"]
        )
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    if data.get("workerId") is not None:
        out["worker_id"] = data["workerId"]
    else:
        out["worker_id"] = ""
    if data.get("startedAt") is not None:
        import capo_deadline.types.started_at

        out["started_at"] = capo_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lifecycleStatus") is not None:
        import capo_deadline.types.session_lifecycle_status

        out["lifecycle_status"] = (
            capo_deadline.types.session_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        import typing

        out["lifecycle_status"] = typing.cast(
            "capo_deadline.types.session_lifecycle_status.SessionLifecycleStatus", ""
        )
    if data.get("endedAt") is not None:
        import capo_deadline.types.ended_at

        out["ended_at"] = capo_deadline.types.ended_at.deserialize_json(data["endedAt"])
    if data.get("targetLifecycleStatus") is not None:
        import capo_deadline.types.session_lifecycle_target_status

        out["target_lifecycle_status"] = (
            capo_deadline.types.session_lifecycle_target_status.deserialize_json(
                data["targetLifecycleStatus"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("log") is not None:
        import capo_deadline.types.log_configuration

        out["log"] = capo_deadline.types.log_configuration.deserialize_json(data["log"])
    else:
        raise DeserializationError("GetSessionResponse.log required")
    if data.get("hostProperties") is not None:
        import capo_deadline.types.host_properties_response

        out["host_properties"] = (
            capo_deadline.types.host_properties_response.deserialize_json(
                data["hostProperties"]
            )
        )
    if data.get("workerLog") is not None:
        import capo_deadline.types.log_configuration

        out["worker_log"] = capo_deadline.types.log_configuration.deserialize_json(
            data["workerLog"]
        )
    return out
