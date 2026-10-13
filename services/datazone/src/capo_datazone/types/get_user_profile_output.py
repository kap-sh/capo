"""Generated from Smithy shape ``com.amazonaws.datazone#GetUserProfileOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.user_profile_details
    import capo_datazone.types.user_profile_id
    import capo_datazone.types.user_profile_status
    import capo_datazone.types.user_profile_type


class GetUserProfileOutput(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>the identifier of the Amazon DataZone domain of which you want to get the user profile.</p>"""
    id: NotRequired["capo_datazone.types.user_profile_id.UserProfileId"]
    """<p>The identifier of the user profile.</p>"""
    type: NotRequired["capo_datazone.types.user_profile_type.UserProfileType"]
    """<p>The type of the user profile.</p>"""
    status: NotRequired["capo_datazone.types.user_profile_status.UserProfileStatus"]
    """<p>The status of the user profile.</p>"""
    details: NotRequired["capo_datazone.types.user_profile_details.UserProfileDetails"]
    """<p>The user profile details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserProfileOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_datazone.types.user_profile_type

        out["type"] = capo_datazone.types.user_profile_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import capo_datazone.types.user_profile_status

        out["status"] = capo_datazone.types.user_profile_status.serialize_json(
            value["status"]
        )
    if "details" in value:
        import capo_datazone.types.user_profile_details

        out["details"] = capo_datazone.types.user_profile_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> GetUserProfileOutput:
    out: GetUserProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("id") is not None:
        out["id"] = data["id"]
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
    if data.get("details") is not None:
        import capo_datazone.types.user_profile_details

        out["details"] = capo_datazone.types.user_profile_details.deserialize_json(
            data["details"]
        )
    return out


def redact_sensitive(value: GetUserProfileOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_datazone.types.user_profile_details

        out["details"] = capo_datazone.types.user_profile_details.redact_sensitive(
            value["details"]
        )
    return out
