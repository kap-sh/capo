"""Generated from Smithy shape ``com.amazonaws.chime#User``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.alexa_for_business_metadata
    import capo_chime.types.email_address
    import capo_chime.types.invite_status
    import capo_chime.types.iso8601_timestamp
    import capo_chime.types.license
    import capo_chime.types.registration_status
    import capo_chime.types.sensitive_string
    import capo_chime.types.string
    import capo_chime.types.user_type


class User(TypedDict, closed=True):
    user_id: "capo_chime.types.string.String"
    """<p>The user ID.</p>"""
    account_id: NotRequired["capo_chime.types.string.String"]
    """<p>The Amazon Chime account ID.</p>"""
    primary_email: NotRequired["capo_chime.types.email_address.EmailAddress"]
    """<p>The primary email address of the user.</p>"""
    primary_provisioned_number: NotRequired[
        "capo_chime.types.sensitive_string.SensitiveString"
    ]
    """<p>The primary phone number associated with the user.</p>"""
    display_name: NotRequired["capo_chime.types.sensitive_string.SensitiveString"]
    """<p>The display name of the user.</p>"""
    license_type: NotRequired["capo_chime.types.license.License"]
    """<p>The license type for the user.</p>"""
    user_type: NotRequired["capo_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""
    user_registration_status: NotRequired[
        "capo_chime.types.registration_status.RegistrationStatus"
    ]
    """<p>The user registration status.</p>"""
    user_invitation_status: NotRequired["capo_chime.types.invite_status.InviteStatus"]
    """<p>The user invite status.</p>"""
    registered_on: NotRequired["capo_chime.types.iso8601_timestamp.Iso8601Timestamp"]
    """<p>Date and time when the user is registered, in ISO 8601 format.</p>"""
    invited_on: NotRequired["capo_chime.types.iso8601_timestamp.Iso8601Timestamp"]
    """<p>Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.</p>"""
    alexa_for_business_metadata: NotRequired[
        "capo_chime.types.alexa_for_business_metadata.AlexaForBusinessMetadata"
    ]
    """<p>The Alexa for Business metadata.</p>"""
    personal_pin: NotRequired["capo_chime.types.string.String"]
    """<p>The user's personal meeting PIN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "primary_email" in value:
        out["PrimaryEmail"] = value["primary_email"]
    if "primary_provisioned_number" in value:
        out["PrimaryProvisionedNumber"] = value["primary_provisioned_number"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "license_type" in value:
        import capo_chime.types.license

        out["LicenseType"] = capo_chime.types.license.serialize_json(
            value["license_type"]
        )
    if "user_type" in value:
        import capo_chime.types.user_type

        out["UserType"] = capo_chime.types.user_type.serialize_json(value["user_type"])
    if "user_registration_status" in value:
        import capo_chime.types.registration_status

        out["UserRegistrationStatus"] = (
            capo_chime.types.registration_status.serialize_json(
                value["user_registration_status"]
            )
        )
    if "user_invitation_status" in value:
        import capo_chime.types.invite_status

        out["UserInvitationStatus"] = capo_chime.types.invite_status.serialize_json(
            value["user_invitation_status"]
        )
    if "registered_on" in value:
        import capo_chime.types.iso8601_timestamp

        out["RegisteredOn"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["registered_on"]
        )
    if "invited_on" in value:
        import capo_chime.types.iso8601_timestamp

        out["InvitedOn"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["invited_on"]
        )
    if "alexa_for_business_metadata" in value:
        import capo_chime.types.alexa_for_business_metadata

        out["AlexaForBusinessMetadata"] = (
            capo_chime.types.alexa_for_business_metadata.serialize_json(
                value["alexa_for_business_metadata"]
            )
        )
    if "personal_pin" in value:
        out["PersonalPIN"] = value["personal_pin"]
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("User.user_id required")
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("PrimaryEmail") is not None:
        out["primary_email"] = data["PrimaryEmail"]
    if data.get("PrimaryProvisionedNumber") is not None:
        out["primary_provisioned_number"] = data["PrimaryProvisionedNumber"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("LicenseType") is not None:
        import capo_chime.types.license

        out["license_type"] = capo_chime.types.license.deserialize_json(
            data["LicenseType"]
        )
    if data.get("UserType") is not None:
        import capo_chime.types.user_type

        out["user_type"] = capo_chime.types.user_type.deserialize_json(data["UserType"])
    if data.get("UserRegistrationStatus") is not None:
        import capo_chime.types.registration_status

        out["user_registration_status"] = (
            capo_chime.types.registration_status.deserialize_json(
                data["UserRegistrationStatus"]
            )
        )
    if data.get("UserInvitationStatus") is not None:
        import capo_chime.types.invite_status

        out["user_invitation_status"] = capo_chime.types.invite_status.deserialize_json(
            data["UserInvitationStatus"]
        )
    if data.get("RegisteredOn") is not None:
        import capo_chime.types.iso8601_timestamp

        out["registered_on"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["RegisteredOn"]
        )
    if data.get("InvitedOn") is not None:
        import capo_chime.types.iso8601_timestamp

        out["invited_on"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["InvitedOn"]
        )
    if data.get("AlexaForBusinessMetadata") is not None:
        import capo_chime.types.alexa_for_business_metadata

        out["alexa_for_business_metadata"] = (
            capo_chime.types.alexa_for_business_metadata.deserialize_json(
                data["AlexaForBusinessMetadata"]
            )
        )
    if data.get("PersonalPIN") is not None:
        out["personal_pin"] = data["PersonalPIN"]
    return out


def redact_sensitive(value: User) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_email" in value:
        out["primary_email"] = "*** Sensitive Data Redacted ***"
    if "primary_provisioned_number" in value:
        out["primary_provisioned_number"] = "*** Sensitive Data Redacted ***"
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "alexa_for_business_metadata" in value:
        import capo_chime.types.alexa_for_business_metadata

        out["alexa_for_business_metadata"] = (
            capo_chime.types.alexa_for_business_metadata.redact_sensitive(
                value["alexa_for_business_metadata"]
            )
        )
    return out
