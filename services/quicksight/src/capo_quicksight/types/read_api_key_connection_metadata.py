"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAPIKeyConnectionMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.email
    import capo_quicksight.types.endpoint


class ReadAPIKeyConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for API key authentication.</p>"""
    email: NotRequired["capo_quicksight.types.email.Email"]
    """<p>The email address associated with the API key authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadAPIKeyConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    if "email" in value:
        out["Email"] = value["email"]
    return out


def deserialize_json(data: dict) -> ReadAPIKeyConnectionMetadata:
    out: ReadAPIKeyConnectionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        out["base_endpoint"] = ""
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    return out


def redact_sensitive(value: ReadAPIKeyConnectionMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
