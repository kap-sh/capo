"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.network_id
    import capo_wickr.types.update_user_details
    import capo_wickr.types.user_id


class UpdateUserRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the user to update.</p>"""
    user_id: "capo_wickr.types.user_id.UserId"
    """<p>The unique identifier of the user to update.</p>"""
    user_details: NotRequired["capo_wickr.types.update_user_details.UpdateUserDetails"]
    """<p>An object containing the user details to be updated, such as name, password, security groups, and invite code settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    if "user_details" in value:
        import capo_wickr.types.update_user_details

        out["userDetails"] = capo_wickr.types.update_user_details.serialize_json(
            value["user_details"]
        )
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UpdateUserRequest.user_id required")
    if data.get("userDetails") is not None:
        import capo_wickr.types.update_user_details

        out["user_details"] = capo_wickr.types.update_user_details.deserialize_json(
            data["userDetails"]
        )
    return out


def redact_sensitive(value: UpdateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_details" in value:
        import capo_wickr.types.update_user_details

        out["user_details"] = capo_wickr.types.update_user_details.redact_sensitive(
            value["user_details"]
        )
    return out
