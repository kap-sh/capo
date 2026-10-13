"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.email_address_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.password_type
    import capo_workdocs.types.storage_rule_type
    import capo_workdocs.types.time_zone_id_type
    import capo_workdocs.types.user_attribute_value_type
    import capo_workdocs.types.username_type


class CreateUserRequest(TypedDict, closed=True):
    organization_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization.</p>"""
    username: "capo_workdocs.types.username_type.UsernameType"
    """<p>The login name of the user.</p>"""
    email_address: NotRequired[
        "capo_workdocs.types.email_address_type.EmailAddressType"
    ]
    """<p>The email address of the user.</p>"""
    given_name: "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    """<p>The given name of the user.</p>"""
    surname: "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    """<p>The surname of the user.</p>"""
    password: "capo_workdocs.types.password_type.PasswordType"
    """<p>The password of the user.</p>"""
    time_zone_id: NotRequired["capo_workdocs.types.time_zone_id_type.TimeZoneIdType"]
    """<p>The time zone ID of the user.</p>"""
    storage_rule: NotRequired["capo_workdocs.types.storage_rule_type.StorageRuleType"]
    """<p>The amount of storage for the user.</p>"""
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserRequest) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    out["Username"] = value["username"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    out["GivenName"] = value["given_name"]
    out["Surname"] = value["surname"]
    out["Password"] = value["password"]
    if "time_zone_id" in value:
        out["TimeZoneId"] = value["time_zone_id"]
    if "storage_rule" in value:
        import capo_workdocs.types.storage_rule_type

        out["StorageRule"] = capo_workdocs.types.storage_rule_type.serialize_json(
            value["storage_rule"]
        )
    return out


def deserialize_json(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("CreateUserRequest.username required")
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("GivenName") is not None:
        out["given_name"] = data["GivenName"]
    else:
        raise DeserializationError("CreateUserRequest.given_name required")
    if data.get("Surname") is not None:
        out["surname"] = data["Surname"]
    else:
        raise DeserializationError("CreateUserRequest.surname required")
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("CreateUserRequest.password required")
    if data.get("TimeZoneId") is not None:
        out["time_zone_id"] = data["TimeZoneId"]
    if data.get("StorageRule") is not None:
        import capo_workdocs.types.storage_rule_type

        out["storage_rule"] = capo_workdocs.types.storage_rule_type.deserialize_json(
            data["StorageRule"]
        )
    return out


def redact_sensitive(value: CreateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "given_name" in value:
        out["given_name"] = "*** Sensitive Data Redacted ***"
    if "surname" in value:
        out["surname"] = "*** Sensitive Data Redacted ***"
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
