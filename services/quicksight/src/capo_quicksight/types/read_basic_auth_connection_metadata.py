"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadBasicAuthConnectionMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.action_user_name
    import capo_quicksight.types.endpoint


class ReadBasicAuthConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for basic authentication.</p>"""
    username: "capo_quicksight.types.action_user_name.ActionUserName"
    """<p>The username used for basic authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadBasicAuthConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["Username"] = value["username"]
    return out


def deserialize_json(data: dict) -> ReadBasicAuthConnectionMetadata:
    out: ReadBasicAuthConnectionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        out["base_endpoint"] = ""
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    return out


def redact_sensitive(value: ReadBasicAuthConnectionMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
