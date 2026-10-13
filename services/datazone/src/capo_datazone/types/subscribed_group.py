"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.group_profile_id
    import capo_datazone.types.group_profile_name


class SubscribedGroup(TypedDict, closed=True):
    id: NotRequired["capo_datazone.types.group_profile_id.GroupProfileId"]
    """<p>The ID of the subscribed group.</p>"""
    name: NotRequired["capo_datazone.types.group_profile_name.GroupProfileName"]
    """<p>The name of the subscribed group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SubscribedGroup:
    out: SubscribedGroup = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


def redact_sensitive(value: SubscribedGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
