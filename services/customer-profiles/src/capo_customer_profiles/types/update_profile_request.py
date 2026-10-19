"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.engagement_preferences
    import capo_customer_profiles.types.gender
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.party_type
    import capo_customer_profiles.types.profile_type
    import capo_customer_profiles.types.sensitive_string0_to255
    import capo_customer_profiles.types.sensitive_string0_to1000
    import capo_customer_profiles.types.update_address
    import capo_customer_profiles.types.update_attributes
    import capo_customer_profiles.types.uuid


class UpdateProfileRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""
    additional_information: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to1000.sensitiveString0To1000"
    ]
    """<p>Any additional information relevant to the customer’s profile.</p>"""
    account_number: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>An account number that you have assigned to the customer.</p>"""
    party_type: NotRequired["capo_customer_profiles.types.party_type.PartyType"]
    """<p>The type of profile used to describe the customer.</p>"""
    business_name: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The name of the customer’s business.</p>"""
    first_name: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s first name.</p>"""
    middle_name: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s middle name.</p>"""
    last_name: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s last name.</p>"""
    birth_date: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s birth date. </p>"""
    gender: NotRequired["capo_customer_profiles.types.gender.Gender"]
    """<p>The gender with which the customer identifies. </p>"""
    phone_number: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s phone number, which has not been specified as a mobile, home, or business number. </p>"""
    mobile_phone_number: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s mobile phone number.</p>"""
    home_phone_number: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s home phone number.</p>"""
    business_phone_number: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s business phone number.</p>"""
    email_address: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s email address, which has not been specified as a personal or business address. </p>"""
    personal_email_address: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s personal email address.</p>"""
    business_email_address: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>The customer’s business email address.</p>"""
    address: NotRequired["capo_customer_profiles.types.update_address.UpdateAddress"]
    """<p>A generic address associated with the customer that is not mailing, shipping, or billing.</p>"""
    shipping_address: NotRequired[
        "capo_customer_profiles.types.update_address.UpdateAddress"
    ]
    """<p>The customer’s shipping address.</p>"""
    mailing_address: NotRequired[
        "capo_customer_profiles.types.update_address.UpdateAddress"
    ]
    """<p>The customer’s mailing address.</p>"""
    billing_address: NotRequired[
        "capo_customer_profiles.types.update_address.UpdateAddress"
    ]
    """<p>The customer’s billing address.</p>"""
    attributes: NotRequired[
        "capo_customer_profiles.types.update_attributes.UpdateAttributes"
    ]
    """<p>A key value pair of attributes of a customer profile.</p>"""
    party_type_string: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>An alternative to <code>PartyType</code> which accepts any string as input.</p>"""
    gender_string: NotRequired[
        "capo_customer_profiles.types.sensitive_string0_to255.sensitiveString0To255"
    ]
    """<p>An alternative to <code>Gender</code> which accepts any string as input.</p>"""
    profile_type: NotRequired["capo_customer_profiles.types.profile_type.ProfileType"]
    """<p>Determines the type of the profile.</p>"""
    engagement_preferences: NotRequired[
        "capo_customer_profiles.types.engagement_preferences.EngagementPreferences"
    ]
    """<p>Object that defines users preferred methods of engagement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    if "additional_information" in value:
        out["AdditionalInformation"] = value["additional_information"]
    if "account_number" in value:
        out["AccountNumber"] = value["account_number"]
    if "party_type" in value:
        import capo_customer_profiles.types.party_type

        out["PartyType"] = capo_customer_profiles.types.party_type.serialize_json(
            value["party_type"]
        )
    if "business_name" in value:
        out["BusinessName"] = value["business_name"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "middle_name" in value:
        out["MiddleName"] = value["middle_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "birth_date" in value:
        out["BirthDate"] = value["birth_date"]
    if "gender" in value:
        import capo_customer_profiles.types.gender

        out["Gender"] = capo_customer_profiles.types.gender.serialize_json(
            value["gender"]
        )
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "mobile_phone_number" in value:
        out["MobilePhoneNumber"] = value["mobile_phone_number"]
    if "home_phone_number" in value:
        out["HomePhoneNumber"] = value["home_phone_number"]
    if "business_phone_number" in value:
        out["BusinessPhoneNumber"] = value["business_phone_number"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "personal_email_address" in value:
        out["PersonalEmailAddress"] = value["personal_email_address"]
    if "business_email_address" in value:
        out["BusinessEmailAddress"] = value["business_email_address"]
    if "address" in value:
        import capo_customer_profiles.types.update_address

        out["Address"] = capo_customer_profiles.types.update_address.serialize_json(
            value["address"]
        )
    if "shipping_address" in value:
        import capo_customer_profiles.types.update_address

        out["ShippingAddress"] = (
            capo_customer_profiles.types.update_address.serialize_json(
                value["shipping_address"]
            )
        )
    if "mailing_address" in value:
        import capo_customer_profiles.types.update_address

        out["MailingAddress"] = (
            capo_customer_profiles.types.update_address.serialize_json(
                value["mailing_address"]
            )
        )
    if "billing_address" in value:
        import capo_customer_profiles.types.update_address

        out["BillingAddress"] = (
            capo_customer_profiles.types.update_address.serialize_json(
                value["billing_address"]
            )
        )
    if "attributes" in value:
        import capo_customer_profiles.types.update_attributes

        out["Attributes"] = (
            capo_customer_profiles.types.update_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "party_type_string" in value:
        out["PartyTypeString"] = value["party_type_string"]
    if "gender_string" in value:
        out["GenderString"] = value["gender_string"]
    if "profile_type" in value:
        import capo_customer_profiles.types.profile_type

        out["ProfileType"] = capo_customer_profiles.types.profile_type.serialize_json(
            value["profile_type"]
        )
    if "engagement_preferences" in value:
        import capo_customer_profiles.types.engagement_preferences

        out["EngagementPreferences"] = (
            capo_customer_profiles.types.engagement_preferences.serialize_json(
                value["engagement_preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateProfileRequest:
    out: UpdateProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("AdditionalInformation") is not None:
        out["additional_information"] = data["AdditionalInformation"]
    if data.get("AccountNumber") is not None:
        out["account_number"] = data["AccountNumber"]
    if data.get("PartyType") is not None:
        import capo_customer_profiles.types.party_type

        out["party_type"] = capo_customer_profiles.types.party_type.deserialize_json(
            data["PartyType"]
        )
    if data.get("BusinessName") is not None:
        out["business_name"] = data["BusinessName"]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("MiddleName") is not None:
        out["middle_name"] = data["MiddleName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("BirthDate") is not None:
        out["birth_date"] = data["BirthDate"]
    if data.get("Gender") is not None:
        import capo_customer_profiles.types.gender

        out["gender"] = capo_customer_profiles.types.gender.deserialize_json(
            data["Gender"]
        )
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("MobilePhoneNumber") is not None:
        out["mobile_phone_number"] = data["MobilePhoneNumber"]
    if data.get("HomePhoneNumber") is not None:
        out["home_phone_number"] = data["HomePhoneNumber"]
    if data.get("BusinessPhoneNumber") is not None:
        out["business_phone_number"] = data["BusinessPhoneNumber"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("PersonalEmailAddress") is not None:
        out["personal_email_address"] = data["PersonalEmailAddress"]
    if data.get("BusinessEmailAddress") is not None:
        out["business_email_address"] = data["BusinessEmailAddress"]
    if data.get("Address") is not None:
        import capo_customer_profiles.types.update_address

        out["address"] = capo_customer_profiles.types.update_address.deserialize_json(
            data["Address"]
        )
    if data.get("ShippingAddress") is not None:
        import capo_customer_profiles.types.update_address

        out["shipping_address"] = (
            capo_customer_profiles.types.update_address.deserialize_json(
                data["ShippingAddress"]
            )
        )
    if data.get("MailingAddress") is not None:
        import capo_customer_profiles.types.update_address

        out["mailing_address"] = (
            capo_customer_profiles.types.update_address.deserialize_json(
                data["MailingAddress"]
            )
        )
    if data.get("BillingAddress") is not None:
        import capo_customer_profiles.types.update_address

        out["billing_address"] = (
            capo_customer_profiles.types.update_address.deserialize_json(
                data["BillingAddress"]
            )
        )
    if data.get("Attributes") is not None:
        import capo_customer_profiles.types.update_attributes

        out["attributes"] = (
            capo_customer_profiles.types.update_attributes.deserialize_json(
                data["Attributes"]
            )
        )
    if data.get("PartyTypeString") is not None:
        out["party_type_string"] = data["PartyTypeString"]
    if data.get("GenderString") is not None:
        out["gender_string"] = data["GenderString"]
    if data.get("ProfileType") is not None:
        import capo_customer_profiles.types.profile_type

        out["profile_type"] = (
            capo_customer_profiles.types.profile_type.deserialize_json(
                data["ProfileType"]
            )
        )
    if data.get("EngagementPreferences") is not None:
        import capo_customer_profiles.types.engagement_preferences

        out["engagement_preferences"] = (
            capo_customer_profiles.types.engagement_preferences.deserialize_json(
                data["EngagementPreferences"]
            )
        )
    return out


def redact_sensitive(value: UpdateProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "additional_information" in value:
        out["additional_information"] = "*** Sensitive Data Redacted ***"
    if "account_number" in value:
        out["account_number"] = "*** Sensitive Data Redacted ***"
    if "party_type" in value:
        out["party_type"] = "*** Sensitive Data Redacted ***"
    if "business_name" in value:
        out["business_name"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "middle_name" in value:
        out["middle_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "birth_date" in value:
        out["birth_date"] = "*** Sensitive Data Redacted ***"
    if "gender" in value:
        out["gender"] = "*** Sensitive Data Redacted ***"
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    if "mobile_phone_number" in value:
        out["mobile_phone_number"] = "*** Sensitive Data Redacted ***"
    if "home_phone_number" in value:
        out["home_phone_number"] = "*** Sensitive Data Redacted ***"
    if "business_phone_number" in value:
        out["business_phone_number"] = "*** Sensitive Data Redacted ***"
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "personal_email_address" in value:
        out["personal_email_address"] = "*** Sensitive Data Redacted ***"
    if "business_email_address" in value:
        out["business_email_address"] = "*** Sensitive Data Redacted ***"
    if "address" in value:
        out["address"] = "*** Sensitive Data Redacted ***"
    if "shipping_address" in value:
        out["shipping_address"] = "*** Sensitive Data Redacted ***"
    if "mailing_address" in value:
        out["mailing_address"] = "*** Sensitive Data Redacted ***"
    if "billing_address" in value:
        out["billing_address"] = "*** Sensitive Data Redacted ***"
    if "attributes" in value:
        out["attributes"] = "*** Sensitive Data Redacted ***"
    if "party_type_string" in value:
        out["party_type_string"] = "*** Sensitive Data Redacted ***"
    if "gender_string" in value:
        out["gender_string"] = "*** Sensitive Data Redacted ***"
    if "profile_type" in value:
        out["profile_type"] = "*** Sensitive Data Redacted ***"
    if "engagement_preferences" in value:
        out["engagement_preferences"] = "*** Sensitive Data Redacted ***"
    return out
