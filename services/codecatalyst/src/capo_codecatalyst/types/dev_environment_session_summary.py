"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentSessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.timestamp
    import capo_codecatalyst.types.uuid


class DevEnvironmentSessionSummary(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    dev_environment_id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment.</p>"""
    started_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the session started, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a> </p>"""
    id: "str"
    """<p>The system-generated unique ID of the Dev Environment session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentSessionSummary) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["devEnvironmentId"] = value["dev_environment_id"]
    import capo_codecatalyst._protocol.serialize

    out["startedTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["started_time"]
    )
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DevEnvironmentSessionSummary:
    out: DevEnvironmentSessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("spaceName") is not None:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("DevEnvironmentSessionSummary.space_name required")
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("DevEnvironmentSessionSummary.project_name required")
    if data.get("devEnvironmentId") is not None:
        out["dev_environment_id"] = data["devEnvironmentId"]
    else:
        raise DeserializationError(
            "DevEnvironmentSessionSummary.dev_environment_id required"
        )
    if data.get("startedTime") is not None:
        import datetime

        out["started_time"] = datetime.datetime.fromisoformat(
            data["startedTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("DevEnvironmentSessionSummary.started_time required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DevEnvironmentSessionSummary.id required")
    return out
