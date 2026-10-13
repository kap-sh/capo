"""Generated from Smithy shape ``com.amazonaws.mediapackage#IngestEndpoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.sensitive_string


class IngestEndpoint(TypedDict, closed=True):
    id: NotRequired["capo_mediapackage.types.__string.__string"]
    """The system generated unique identifier for the IngestEndpoint"""
    password: NotRequired["capo_mediapackage.types.sensitive_string.SensitiveString"]
    """The system generated password for ingest authentication."""
    url: NotRequired["capo_mediapackage.types.__string.__string"]
    """The ingest URL to which the source stream should be sent."""
    username: NotRequired["capo_mediapackage.types.sensitive_string.SensitiveString"]
    """The system generated username for ingest authentication."""


# --- restJson1 ser/de ---
def serialize_json(value: IngestEndpoint) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "password" in value:
        out["password"] = value["password"]
    if "url" in value:
        out["url"] = value["url"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> IngestEndpoint:
    out: IngestEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("password") is not None:
        out["password"] = data["password"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    return out


def redact_sensitive(value: IngestEndpoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
