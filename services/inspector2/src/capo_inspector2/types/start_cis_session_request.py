"""Generated from Smithy shape ``com.amazonaws.inspector2#StartCisSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.start_cis_session_message
    import capo_inspector2.types.uuid


class StartCisSessionRequest(TypedDict, closed=True):
    scan_job_id: "capo_inspector2.types.uuid.UUID"
    """<p>A unique identifier for the scan job.</p>"""
    message: "capo_inspector2.types.start_cis_session_message.StartCisSessionMessage"
    """<p>The start CIS session message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCisSessionRequest) -> dict:
    out: dict = {}
    out["scanJobId"] = value["scan_job_id"]
    import capo_inspector2.types.start_cis_session_message

    out["message"] = capo_inspector2.types.start_cis_session_message.serialize_json(
        value["message"]
    )
    return out


def deserialize_json(data: dict) -> StartCisSessionRequest:
    out: StartCisSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanJobId") is not None:
        out["scan_job_id"] = data["scanJobId"]
    else:
        out["scan_job_id"] = ""
    if data.get("message") is not None:
        import capo_inspector2.types.start_cis_session_message

        out["message"] = (
            capo_inspector2.types.start_cis_session_message.deserialize_json(
                data["message"]
            )
        )
    else:
        raise DeserializationError("StartCisSessionRequest.message required")
    return out
