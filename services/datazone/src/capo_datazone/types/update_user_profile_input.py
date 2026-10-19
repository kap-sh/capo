"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateUserProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.user_identifier
    import capo_datazone.types.user_profile_status
    import capo_datazone.types.user_profile_type


class UpdateUserProfileInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a user profile is updated.</p>"""
    user_identifier: "capo_datazone.types.user_identifier.UserIdentifier"
    """<p>The identifier of the user whose user profile is to be updated.</p>"""
    type: NotRequired["capo_datazone.types.user_profile_type.UserProfileType"]
    """<p>The type of the user profile that are to be updated.</p>"""
    status: "capo_datazone.types.user_profile_status.UserProfileStatus"
    """<p>The status of the user profile that are to be updated.</p>"""
    session_name: NotRequired["str"]
    """<p>The session name for IAM role sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserProfileInput) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_datazone.types.user_profile_type

        out["type"] = capo_datazone.types.user_profile_type.serialize_json(
            value["type"]
        )
    import capo_datazone.types.user_profile_status

    out["status"] = capo_datazone.types.user_profile_status.serialize_json(
        value["status"]
    )
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    return out


def deserialize_json(data: dict) -> UpdateUserProfileInput:
    out: UpdateUserProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_datazone.types.user_profile_type

        out["type"] = capo_datazone.types.user_profile_type.deserialize_json(
            data["type"]
        )
    if data.get("status") is not None:
        import capo_datazone.types.user_profile_status

        out["status"] = capo_datazone.types.user_profile_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.user_profile_status.UserProfileStatus", ""
        )
    if data.get("sessionName") is not None:
        out["session_name"] = data["sessionName"]
    return out
