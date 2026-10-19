"""Generated from Smithy shape ``com.amazonaws.datazone#CreateUserProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.user_identifier
    import capo_datazone.types.user_type


class CreateUserProfileInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a user profile is created.</p>"""
    user_identifier: "capo_datazone.types.user_identifier.UserIdentifier"
    """<p>The identifier of the user for which the user profile is created.</p>"""
    user_type: NotRequired["capo_datazone.types.user_type.UserType"]
    """<p>The user type of the user for which the user profile is created.</p>"""
    session_name: NotRequired["str"]
    """<p>The session name for IAM role sessions.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserProfileInput) -> dict:
    out: dict = {}
    out["userIdentifier"] = value["user_identifier"]
    if "user_type" in value:
        import capo_datazone.types.user_type

        out["userType"] = capo_datazone.types.user_type.serialize_json(
            value["user_type"]
        )
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateUserProfileInput:
    out: CreateUserProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("userIdentifier") is not None:
        out["user_identifier"] = data["userIdentifier"]
    else:
        out["user_identifier"] = ""
    if data.get("userType") is not None:
        import capo_datazone.types.user_type

        out["user_type"] = capo_datazone.types.user_type.deserialize_json(
            data["userType"]
        )
    if data.get("sessionName") is not None:
        out["session_name"] = data["sessionName"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
