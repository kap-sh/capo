"""Generated from Smithy shape ``com.amazonaws.databrew#StartProjectSessionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.client_session_id
    import capo_databrew.types.project_name


class StartProjectSessionResponse(TypedDict, closed=True):
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The name of the project to be acted upon.</p>"""
    client_session_id: NotRequired[
        "capo_databrew.types.client_session_id.ClientSessionId"
    ]
    """<p>A system-generated identifier for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProjectSessionResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_session_id" in value:
        out["ClientSessionId"] = value["client_session_id"]
    return out


def deserialize_json(data: dict) -> StartProjectSessionResponse:
    out: StartProjectSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartProjectSessionResponse.name required")
    if data.get("ClientSessionId") is not None:
        out["client_session_id"] = data["ClientSessionId"]
    return out


def redact_sensitive(value: StartProjectSessionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_session_id" in value:
        out["client_session_id"] = "*** Sensitive Data Redacted ***"
    return out
