"""Generated from Smithy shape ``com.amazonaws.connect#UserIdentityInfoLite``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_first_name
    import capo_connect.types.agent_last_name


class UserIdentityInfoLite(TypedDict, closed=True):
    first_name: NotRequired["capo_connect.types.agent_first_name.AgentFirstName"]
    """<p>The user's first name.</p>"""
    last_name: NotRequired["capo_connect.types.agent_last_name.AgentLastName"]
    """<p>The user's last name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentityInfoLite) -> dict:
    out: dict = {}
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    return out


def deserialize_json(data: dict) -> UserIdentityInfoLite:
    out: UserIdentityInfoLite = {}  # type: ignore[typeddict-item]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    return out


def redact_sensitive(value: UserIdentityInfoLite) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
