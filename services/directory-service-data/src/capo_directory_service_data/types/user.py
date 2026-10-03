"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.attributes
    import capo_directory_service_data.types.distinguished_name
    import capo_directory_service_data.types.email_address
    import capo_directory_service_data.types.given_name
    import capo_directory_service_data.types.sid
    import capo_directory_service_data.types.surname
    import capo_directory_service_data.types.user_name
    import capo_directory_service_data.types.user_principal_name


class User(TypedDict, closed=True):
    sid: NotRequired["capo_directory_service_data.types.sid.SID"]
    """<p> The unique security identifier (SID) of the user. </p>"""
    sam_account_name: "capo_directory_service_data.types.user_name.UserName"
    """<p> The name of the user. </p>"""
    distinguished_name: NotRequired[
        "capo_directory_service_data.types.distinguished_name.DistinguishedName"
    ]
    """<p> The <a href="https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name">distinguished name</a> of the object. </p>"""
    user_principal_name: NotRequired[
        "capo_directory_service_data.types.user_principal_name.UserPrincipalName"
    ]
    """<p> The UPN that is an internet-style login name for a user and based on the internet standard <a href="https://datatracker.ietf.org/doc/html/rfc822">RFC 822</a>. The UPN is shorter than the distinguished name and easier to remember. </p>"""
    email_address: NotRequired[
        "capo_directory_service_data.types.email_address.EmailAddress"
    ]
    """<p> The email address of the user. </p>"""
    given_name: NotRequired["capo_directory_service_data.types.given_name.GivenName"]
    """<p> The first name of the user. </p>"""
    surname: NotRequired["capo_directory_service_data.types.surname.Surname"]
    """<p> The last name of the user. </p>"""
    enabled: NotRequired["bool"]
    """<p> Indicates whether the user account is active. </p>"""
    other_attributes: NotRequired[
        "capo_directory_service_data.types.attributes.Attributes"
    ]
    """<p> An expression that includes one or more attributes, data types, and values of a user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    if "sid" in value:
        out["SID"] = value["sid"]
    out["SAMAccountName"] = value["sam_account_name"]
    if "distinguished_name" in value:
        out["DistinguishedName"] = value["distinguished_name"]
    if "user_principal_name" in value:
        out["UserPrincipalName"] = value["user_principal_name"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "other_attributes" in value:
        import capo_directory_service_data.types.attributes

        out["OtherAttributes"] = (
            capo_directory_service_data.types.attributes.serialize_json(
                value["other_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("User.sam_account_name required")
    if data.get("DistinguishedName") is not None:
        out["distinguished_name"] = data["DistinguishedName"]
    if data.get("UserPrincipalName") is not None:
        out["user_principal_name"] = data["UserPrincipalName"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("GivenName") is not None:
        out["given_name"] = data["GivenName"]
    if data.get("Surname") is not None:
        out["surname"] = data["Surname"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("OtherAttributes") is not None:
        import capo_directory_service_data.types.attributes

        out["other_attributes"] = (
            capo_directory_service_data.types.attributes.deserialize_json(
                data["OtherAttributes"]
            )
        )
    return out
