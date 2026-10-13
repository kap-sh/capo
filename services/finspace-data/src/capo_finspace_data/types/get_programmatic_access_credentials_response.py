"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetProgrammaticAccessCredentialsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.credentials
    import capo_finspace_data.types.session_duration


class GetProgrammaticAccessCredentialsResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_finspace_data.types.credentials.Credentials"]
    """<p>Returns the programmatic credentials.</p>"""
    duration_in_minutes: NotRequired[
        "capo_finspace_data.types.session_duration.SessionDuration"
    ]
    """<p>Returns the duration in which the credentials will remain valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProgrammaticAccessCredentialsResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import capo_finspace_data.types.credentials

        out["credentials"] = capo_finspace_data.types.credentials.serialize_json(
            value["credentials"]
        )
    if "duration_in_minutes" in value:
        out["durationInMinutes"] = value["duration_in_minutes"]
    return out


def deserialize_json(data: dict) -> GetProgrammaticAccessCredentialsResponse:
    out: GetProgrammaticAccessCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("credentials") is not None:
        import capo_finspace_data.types.credentials

        out["credentials"] = capo_finspace_data.types.credentials.deserialize_json(
            data["credentials"]
        )
    if data.get("durationInMinutes") is not None:
        out["duration_in_minutes"] = data["durationInMinutes"]
    return out


def redact_sensitive(value: GetProgrammaticAccessCredentialsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        out["credentials"] = "*** Sensitive Data Redacted ***"
    return out
