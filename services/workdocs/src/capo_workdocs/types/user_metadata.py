"""Generated from Smithy shape ``com.amazonaws.workdocs#UserMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.email_address_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.user_attribute_value_type
    import capo_workdocs.types.username_type


class UserMetadata(TypedDict, closed=True):
    id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the user.</p>"""
    username: NotRequired["capo_workdocs.types.username_type.UsernameType"]
    """<p>The name of the user.</p>"""
    given_name: NotRequired[
        "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The given name of the user before a rename operation.</p>"""
    surname: NotRequired[
        "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The surname of the user.</p>"""
    email_address: NotRequired[
        "capo_workdocs.types.email_address_type.EmailAddressType"
    ]
    """<p>The email address of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "username" in value:
        out["Username"] = value["username"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> UserMetadata:
    out: UserMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("GivenName") is not None:
        out["given_name"] = data["GivenName"]
    if data.get("Surname") is not None:
        out["surname"] = data["Surname"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    return out


def redact_sensitive(value: UserMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "given_name" in value:
        out["given_name"] = "*** Sensitive Data Redacted ***"
    if "surname" in value:
        out["surname"] = "*** Sensitive Data Redacted ***"
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out
