"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountDetailsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.additional_contact_email_addresses
    import capo_sesv2.types.contact_language
    import capo_sesv2.types.enabled_wrapper
    import capo_sesv2.types.mail_type
    import capo_sesv2.types.use_case_description
    import capo_sesv2.types.website_url


class PutAccountDetailsRequest(TypedDict, closed=True):
    mail_type: "capo_sesv2.types.mail_type.MailType"
    """<p>The type of email your account will send.</p>"""
    website_url: "capo_sesv2.types.website_url.WebsiteURL"
    """<p>The URL of your website. This information helps us better understand the type of content that you plan to send.</p>"""
    contact_language: NotRequired["capo_sesv2.types.contact_language.ContactLanguage"]
    """<p>The language you would prefer to be contacted with.</p>"""
    use_case_description: NotRequired[
        "capo_sesv2.types.use_case_description.UseCaseDescription"
    ]
    """<p>A description of the types of email that you plan to send.</p>"""
    additional_contact_email_addresses: NotRequired[
        "capo_sesv2.types.additional_contact_email_addresses.AdditionalContactEmailAddresses"
    ]
    """<p>Additional email addresses that you would like to be notified regarding Amazon SES matters.</p>"""
    production_access_enabled: NotRequired[
        "capo_sesv2.types.enabled_wrapper.EnabledWrapper"
    ]
    """<p>Indicates whether or not your account should have production access in the current Amazon Web Services Region.</p> <p>If the value is <code>false</code>, then your account is in the <i>sandbox</i>. When your account is in the sandbox, you can only send email to verified identities. </p> <p>If the value is <code>true</code>, then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountDetailsRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.mail_type

    out["MailType"] = capo_sesv2.types.mail_type.serialize_json(value["mail_type"])
    out["WebsiteURL"] = value["website_url"]
    if "contact_language" in value:
        import capo_sesv2.types.contact_language

        out["ContactLanguage"] = capo_sesv2.types.contact_language.serialize_json(
            value["contact_language"]
        )
    if "use_case_description" in value:
        out["UseCaseDescription"] = value["use_case_description"]
    if "additional_contact_email_addresses" in value:
        import capo_sesv2.types.additional_contact_email_addresses

        out["AdditionalContactEmailAddresses"] = (
            capo_sesv2.types.additional_contact_email_addresses.serialize_json(
                value["additional_contact_email_addresses"]
            )
        )
    if "production_access_enabled" in value:
        out["ProductionAccessEnabled"] = value["production_access_enabled"]
    return out


def deserialize_json(data: dict) -> PutAccountDetailsRequest:
    out: PutAccountDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MailType") is not None:
        import capo_sesv2.types.mail_type

        out["mail_type"] = capo_sesv2.types.mail_type.deserialize_json(data["MailType"])
    else:
        raise DeserializationError("PutAccountDetailsRequest.mail_type required")
    if data.get("WebsiteURL") is not None:
        out["website_url"] = data["WebsiteURL"]
    else:
        raise DeserializationError("PutAccountDetailsRequest.website_url required")
    if data.get("ContactLanguage") is not None:
        import capo_sesv2.types.contact_language

        out["contact_language"] = capo_sesv2.types.contact_language.deserialize_json(
            data["ContactLanguage"]
        )
    if data.get("UseCaseDescription") is not None:
        out["use_case_description"] = data["UseCaseDescription"]
    if data.get("AdditionalContactEmailAddresses") is not None:
        import capo_sesv2.types.additional_contact_email_addresses

        out["additional_contact_email_addresses"] = (
            capo_sesv2.types.additional_contact_email_addresses.deserialize_json(
                data["AdditionalContactEmailAddresses"]
            )
        )
    if data.get("ProductionAccessEnabled") is not None:
        out["production_access_enabled"] = data["ProductionAccessEnabled"]
    return out


def redact_sensitive(value: PutAccountDetailsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "website_url" in value:
        out["website_url"] = "*** Sensitive Data Redacted ***"
    if "use_case_description" in value:
        out["use_case_description"] = "*** Sensitive Data Redacted ***"
    if "additional_contact_email_addresses" in value:
        out["additional_contact_email_addresses"] = "*** Sensitive Data Redacted ***"
    return out
