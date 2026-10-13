"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedUser``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.user_profile_details
    import capo_datazone.types.user_profile_id


class SubscribedUser(TypedDict, closed=True):
    id: NotRequired["capo_datazone.types.user_profile_id.UserProfileId"]
    """<p>The ID of the subscribed user.</p>"""
    details: NotRequired["capo_datazone.types.user_profile_details.UserProfileDetails"]
    """<p>The subscribed user details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedUser) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "details" in value:
        import capo_datazone.types.user_profile_details

        out["details"] = capo_datazone.types.user_profile_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> SubscribedUser:
    out: SubscribedUser = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("details") is not None:
        import capo_datazone.types.user_profile_details

        out["details"] = capo_datazone.types.user_profile_details.deserialize_json(
            data["details"]
        )
    return out


def redact_sensitive(value: SubscribedUser) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_datazone.types.user_profile_details

        out["details"] = capo_datazone.types.user_profile_details.redact_sensitive(
            value["details"]
        )
    return out
