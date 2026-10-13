"""Generated from Smithy shape ``com.amazonaws.qconnect#CustomerProfileAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.custom_attributes
    import capo_qconnect.types.message_template_attribute_value


class CustomerProfileAttributes(TypedDict, closed=True):
    profile_id: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The unique identifier of a customer profile.</p>"""
    profile_arn: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The ARN of a customer profile.</p>"""
    first_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's first name.</p>"""
    middle_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's middle name.</p>"""
    last_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's last name.</p>"""
    account_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>A unique account number that you have given to the customer.</p>"""
    email_address: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's email address, which has not been specified as a personal or business address.</p>"""
    phone_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's phone number, which has not been specified as a mobile, home, or business number.</p>"""
    additional_information: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>Any additional information relevant to the customer's profile.</p>"""
    party_type: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's party type.</p>"""
    business_name: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The name of the customer's business.</p>"""
    birth_date: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's birth date.</p>"""
    gender: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's gender.</p>"""
    mobile_phone_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's mobile phone number.</p>"""
    home_phone_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's mobile phone number.</p>"""
    business_phone_number: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's business phone number.</p>"""
    business_email_address: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The customer's business email address.</p>"""
    address1: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The first line of a customer address.</p>"""
    address2: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The second line of a customer address.</p>"""
    address3: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The third line of a customer address.</p>"""
    address4: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The fourth line of a customer address.</p>"""
    city: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The city in which a customer lives.</p>"""
    county: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The county in which a customer lives.</p>"""
    country: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The country in which a customer lives.</p>"""
    postal_code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The postal code of a customer address.</p>"""
    province: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The province in which a customer lives.</p>"""
    state: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The state in which a customer lives.</p>"""
    shipping_address1: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The first line of a customer’s shipping address.</p>"""
    shipping_address2: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The second line of a customer’s shipping address.</p>"""
    shipping_address3: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The third line of a customer’s shipping address.</p>"""
    shipping_address4: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The fourth line of a customer’s shipping address.</p>"""
    shipping_city: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The city of a customer’s shipping address.</p>"""
    shipping_county: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The county of a customer’s shipping address.</p>"""
    shipping_country: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The country of a customer’s shipping address.</p>"""
    shipping_postal_code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The postal code of a customer’s shipping address.</p>"""
    shipping_province: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The province of a customer’s shipping address.</p>"""
    shipping_state: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The state of a customer’s shipping address.</p>"""
    mailing_address1: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The first line of a customer’s mailing address.</p>"""
    mailing_address2: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The second line of a customer’s mailing address.</p>"""
    mailing_address3: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The third line of a customer’s mailing address.</p>"""
    mailing_address4: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The fourth line of a customer’s mailing address.</p>"""
    mailing_city: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The city of a customer’s mailing address.</p>"""
    mailing_county: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The county of a customer’s mailing address.</p>"""
    mailing_country: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The country of a customer’s mailing address.</p>"""
    mailing_postal_code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The postal code of a customer’s mailing address.</p>"""
    mailing_province: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The province of a customer’s mailing address.</p>"""
    mailing_state: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The state of a customer’s mailing address.</p>"""
    billing_address1: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The first line of a customer’s billing address.</p>"""
    billing_address2: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The second line of a customer’s billing address.</p>"""
    billing_address3: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The third line of a customer’s billing address.</p>"""
    billing_address4: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The fourth line of a customer’s billing address.</p>"""
    billing_city: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The city of a customer’s billing address.</p>"""
    billing_county: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The county of a customer’s billing address.</p>"""
    billing_country: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The country of a customer’s billing address.</p>"""
    billing_postal_code: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The postal code of a customer’s billing address.</p>"""
    billing_province: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The province of a customer’s billing address.</p>"""
    billing_state: NotRequired[
        "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue"
    ]
    """<p>The state of a customer’s billing address.</p>"""
    custom: NotRequired["capo_qconnect.types.custom_attributes.CustomAttributes"]
    """<p>The custom attributes in customer profile attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerProfileAttributes) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["profileId"] = value["profile_id"]
    if "profile_arn" in value:
        out["profileARN"] = value["profile_arn"]
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "middle_name" in value:
        out["middleName"] = value["middle_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "account_number" in value:
        out["accountNumber"] = value["account_number"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "phone_number" in value:
        out["phoneNumber"] = value["phone_number"]
    if "additional_information" in value:
        out["additionalInformation"] = value["additional_information"]
    if "party_type" in value:
        out["partyType"] = value["party_type"]
    if "business_name" in value:
        out["businessName"] = value["business_name"]
    if "birth_date" in value:
        out["birthDate"] = value["birth_date"]
    if "gender" in value:
        out["gender"] = value["gender"]
    if "mobile_phone_number" in value:
        out["mobilePhoneNumber"] = value["mobile_phone_number"]
    if "home_phone_number" in value:
        out["homePhoneNumber"] = value["home_phone_number"]
    if "business_phone_number" in value:
        out["businessPhoneNumber"] = value["business_phone_number"]
    if "business_email_address" in value:
        out["businessEmailAddress"] = value["business_email_address"]
    if "address1" in value:
        out["address1"] = value["address1"]
    if "address2" in value:
        out["address2"] = value["address2"]
    if "address3" in value:
        out["address3"] = value["address3"]
    if "address4" in value:
        out["address4"] = value["address4"]
    if "city" in value:
        out["city"] = value["city"]
    if "county" in value:
        out["county"] = value["county"]
    if "country" in value:
        out["country"] = value["country"]
    if "postal_code" in value:
        out["postalCode"] = value["postal_code"]
    if "province" in value:
        out["province"] = value["province"]
    if "state" in value:
        out["state"] = value["state"]
    if "shipping_address1" in value:
        out["shippingAddress1"] = value["shipping_address1"]
    if "shipping_address2" in value:
        out["shippingAddress2"] = value["shipping_address2"]
    if "shipping_address3" in value:
        out["shippingAddress3"] = value["shipping_address3"]
    if "shipping_address4" in value:
        out["shippingAddress4"] = value["shipping_address4"]
    if "shipping_city" in value:
        out["shippingCity"] = value["shipping_city"]
    if "shipping_county" in value:
        out["shippingCounty"] = value["shipping_county"]
    if "shipping_country" in value:
        out["shippingCountry"] = value["shipping_country"]
    if "shipping_postal_code" in value:
        out["shippingPostalCode"] = value["shipping_postal_code"]
    if "shipping_province" in value:
        out["shippingProvince"] = value["shipping_province"]
    if "shipping_state" in value:
        out["shippingState"] = value["shipping_state"]
    if "mailing_address1" in value:
        out["mailingAddress1"] = value["mailing_address1"]
    if "mailing_address2" in value:
        out["mailingAddress2"] = value["mailing_address2"]
    if "mailing_address3" in value:
        out["mailingAddress3"] = value["mailing_address3"]
    if "mailing_address4" in value:
        out["mailingAddress4"] = value["mailing_address4"]
    if "mailing_city" in value:
        out["mailingCity"] = value["mailing_city"]
    if "mailing_county" in value:
        out["mailingCounty"] = value["mailing_county"]
    if "mailing_country" in value:
        out["mailingCountry"] = value["mailing_country"]
    if "mailing_postal_code" in value:
        out["mailingPostalCode"] = value["mailing_postal_code"]
    if "mailing_province" in value:
        out["mailingProvince"] = value["mailing_province"]
    if "mailing_state" in value:
        out["mailingState"] = value["mailing_state"]
    if "billing_address1" in value:
        out["billingAddress1"] = value["billing_address1"]
    if "billing_address2" in value:
        out["billingAddress2"] = value["billing_address2"]
    if "billing_address3" in value:
        out["billingAddress3"] = value["billing_address3"]
    if "billing_address4" in value:
        out["billingAddress4"] = value["billing_address4"]
    if "billing_city" in value:
        out["billingCity"] = value["billing_city"]
    if "billing_county" in value:
        out["billingCounty"] = value["billing_county"]
    if "billing_country" in value:
        out["billingCountry"] = value["billing_country"]
    if "billing_postal_code" in value:
        out["billingPostalCode"] = value["billing_postal_code"]
    if "billing_province" in value:
        out["billingProvince"] = value["billing_province"]
    if "billing_state" in value:
        out["billingState"] = value["billing_state"]
    if "custom" in value:
        import capo_qconnect.types.custom_attributes

        out["custom"] = capo_qconnect.types.custom_attributes.serialize_json(
            value["custom"]
        )
    return out


def deserialize_json(data: dict) -> CustomerProfileAttributes:
    out: CustomerProfileAttributes = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    if data.get("profileARN") is not None:
        out["profile_arn"] = data["profileARN"]
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("middleName") is not None:
        out["middle_name"] = data["middleName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    if data.get("accountNumber") is not None:
        out["account_number"] = data["accountNumber"]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    if data.get("phoneNumber") is not None:
        out["phone_number"] = data["phoneNumber"]
    if data.get("additionalInformation") is not None:
        out["additional_information"] = data["additionalInformation"]
    if data.get("partyType") is not None:
        out["party_type"] = data["partyType"]
    if data.get("businessName") is not None:
        out["business_name"] = data["businessName"]
    if data.get("birthDate") is not None:
        out["birth_date"] = data["birthDate"]
    if data.get("gender") is not None:
        out["gender"] = data["gender"]
    if data.get("mobilePhoneNumber") is not None:
        out["mobile_phone_number"] = data["mobilePhoneNumber"]
    if data.get("homePhoneNumber") is not None:
        out["home_phone_number"] = data["homePhoneNumber"]
    if data.get("businessPhoneNumber") is not None:
        out["business_phone_number"] = data["businessPhoneNumber"]
    if data.get("businessEmailAddress") is not None:
        out["business_email_address"] = data["businessEmailAddress"]
    if data.get("address1") is not None:
        out["address1"] = data["address1"]
    if data.get("address2") is not None:
        out["address2"] = data["address2"]
    if data.get("address3") is not None:
        out["address3"] = data["address3"]
    if data.get("address4") is not None:
        out["address4"] = data["address4"]
    if data.get("city") is not None:
        out["city"] = data["city"]
    if data.get("county") is not None:
        out["county"] = data["county"]
    if data.get("country") is not None:
        out["country"] = data["country"]
    if data.get("postalCode") is not None:
        out["postal_code"] = data["postalCode"]
    if data.get("province") is not None:
        out["province"] = data["province"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("shippingAddress1") is not None:
        out["shipping_address1"] = data["shippingAddress1"]
    if data.get("shippingAddress2") is not None:
        out["shipping_address2"] = data["shippingAddress2"]
    if data.get("shippingAddress3") is not None:
        out["shipping_address3"] = data["shippingAddress3"]
    if data.get("shippingAddress4") is not None:
        out["shipping_address4"] = data["shippingAddress4"]
    if data.get("shippingCity") is not None:
        out["shipping_city"] = data["shippingCity"]
    if data.get("shippingCounty") is not None:
        out["shipping_county"] = data["shippingCounty"]
    if data.get("shippingCountry") is not None:
        out["shipping_country"] = data["shippingCountry"]
    if data.get("shippingPostalCode") is not None:
        out["shipping_postal_code"] = data["shippingPostalCode"]
    if data.get("shippingProvince") is not None:
        out["shipping_province"] = data["shippingProvince"]
    if data.get("shippingState") is not None:
        out["shipping_state"] = data["shippingState"]
    if data.get("mailingAddress1") is not None:
        out["mailing_address1"] = data["mailingAddress1"]
    if data.get("mailingAddress2") is not None:
        out["mailing_address2"] = data["mailingAddress2"]
    if data.get("mailingAddress3") is not None:
        out["mailing_address3"] = data["mailingAddress3"]
    if data.get("mailingAddress4") is not None:
        out["mailing_address4"] = data["mailingAddress4"]
    if data.get("mailingCity") is not None:
        out["mailing_city"] = data["mailingCity"]
    if data.get("mailingCounty") is not None:
        out["mailing_county"] = data["mailingCounty"]
    if data.get("mailingCountry") is not None:
        out["mailing_country"] = data["mailingCountry"]
    if data.get("mailingPostalCode") is not None:
        out["mailing_postal_code"] = data["mailingPostalCode"]
    if data.get("mailingProvince") is not None:
        out["mailing_province"] = data["mailingProvince"]
    if data.get("mailingState") is not None:
        out["mailing_state"] = data["mailingState"]
    if data.get("billingAddress1") is not None:
        out["billing_address1"] = data["billingAddress1"]
    if data.get("billingAddress2") is not None:
        out["billing_address2"] = data["billingAddress2"]
    if data.get("billingAddress3") is not None:
        out["billing_address3"] = data["billingAddress3"]
    if data.get("billingAddress4") is not None:
        out["billing_address4"] = data["billingAddress4"]
    if data.get("billingCity") is not None:
        out["billing_city"] = data["billingCity"]
    if data.get("billingCounty") is not None:
        out["billing_county"] = data["billingCounty"]
    if data.get("billingCountry") is not None:
        out["billing_country"] = data["billingCountry"]
    if data.get("billingPostalCode") is not None:
        out["billing_postal_code"] = data["billingPostalCode"]
    if data.get("billingProvince") is not None:
        out["billing_province"] = data["billingProvince"]
    if data.get("billingState") is not None:
        out["billing_state"] = data["billingState"]
    if data.get("custom") is not None:
        import capo_qconnect.types.custom_attributes

        out["custom"] = capo_qconnect.types.custom_attributes.deserialize_json(
            data["custom"]
        )
    return out


def redact_sensitive(value: CustomerProfileAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "profile_id" in value:
        out["profile_id"] = "*** Sensitive Data Redacted ***"
    if "profile_arn" in value:
        out["profile_arn"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "middle_name" in value:
        out["middle_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "account_number" in value:
        out["account_number"] = "*** Sensitive Data Redacted ***"
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    if "additional_information" in value:
        out["additional_information"] = "*** Sensitive Data Redacted ***"
    if "party_type" in value:
        out["party_type"] = "*** Sensitive Data Redacted ***"
    if "business_name" in value:
        out["business_name"] = "*** Sensitive Data Redacted ***"
    if "birth_date" in value:
        out["birth_date"] = "*** Sensitive Data Redacted ***"
    if "gender" in value:
        out["gender"] = "*** Sensitive Data Redacted ***"
    if "mobile_phone_number" in value:
        out["mobile_phone_number"] = "*** Sensitive Data Redacted ***"
    if "home_phone_number" in value:
        out["home_phone_number"] = "*** Sensitive Data Redacted ***"
    if "business_phone_number" in value:
        out["business_phone_number"] = "*** Sensitive Data Redacted ***"
    if "business_email_address" in value:
        out["business_email_address"] = "*** Sensitive Data Redacted ***"
    if "address1" in value:
        out["address1"] = "*** Sensitive Data Redacted ***"
    if "address2" in value:
        out["address2"] = "*** Sensitive Data Redacted ***"
    if "address3" in value:
        out["address3"] = "*** Sensitive Data Redacted ***"
    if "address4" in value:
        out["address4"] = "*** Sensitive Data Redacted ***"
    if "city" in value:
        out["city"] = "*** Sensitive Data Redacted ***"
    if "county" in value:
        out["county"] = "*** Sensitive Data Redacted ***"
    if "country" in value:
        out["country"] = "*** Sensitive Data Redacted ***"
    if "postal_code" in value:
        out["postal_code"] = "*** Sensitive Data Redacted ***"
    if "province" in value:
        out["province"] = "*** Sensitive Data Redacted ***"
    if "state" in value:
        out["state"] = "*** Sensitive Data Redacted ***"
    if "shipping_address1" in value:
        out["shipping_address1"] = "*** Sensitive Data Redacted ***"
    if "shipping_address2" in value:
        out["shipping_address2"] = "*** Sensitive Data Redacted ***"
    if "shipping_address3" in value:
        out["shipping_address3"] = "*** Sensitive Data Redacted ***"
    if "shipping_address4" in value:
        out["shipping_address4"] = "*** Sensitive Data Redacted ***"
    if "shipping_city" in value:
        out["shipping_city"] = "*** Sensitive Data Redacted ***"
    if "shipping_county" in value:
        out["shipping_county"] = "*** Sensitive Data Redacted ***"
    if "shipping_country" in value:
        out["shipping_country"] = "*** Sensitive Data Redacted ***"
    if "shipping_postal_code" in value:
        out["shipping_postal_code"] = "*** Sensitive Data Redacted ***"
    if "shipping_province" in value:
        out["shipping_province"] = "*** Sensitive Data Redacted ***"
    if "shipping_state" in value:
        out["shipping_state"] = "*** Sensitive Data Redacted ***"
    if "mailing_address1" in value:
        out["mailing_address1"] = "*** Sensitive Data Redacted ***"
    if "mailing_address2" in value:
        out["mailing_address2"] = "*** Sensitive Data Redacted ***"
    if "mailing_address3" in value:
        out["mailing_address3"] = "*** Sensitive Data Redacted ***"
    if "mailing_address4" in value:
        out["mailing_address4"] = "*** Sensitive Data Redacted ***"
    if "mailing_city" in value:
        out["mailing_city"] = "*** Sensitive Data Redacted ***"
    if "mailing_county" in value:
        out["mailing_county"] = "*** Sensitive Data Redacted ***"
    if "mailing_country" in value:
        out["mailing_country"] = "*** Sensitive Data Redacted ***"
    if "mailing_postal_code" in value:
        out["mailing_postal_code"] = "*** Sensitive Data Redacted ***"
    if "mailing_province" in value:
        out["mailing_province"] = "*** Sensitive Data Redacted ***"
    if "mailing_state" in value:
        out["mailing_state"] = "*** Sensitive Data Redacted ***"
    if "billing_address1" in value:
        out["billing_address1"] = "*** Sensitive Data Redacted ***"
    if "billing_address2" in value:
        out["billing_address2"] = "*** Sensitive Data Redacted ***"
    if "billing_address3" in value:
        out["billing_address3"] = "*** Sensitive Data Redacted ***"
    if "billing_address4" in value:
        out["billing_address4"] = "*** Sensitive Data Redacted ***"
    if "billing_city" in value:
        out["billing_city"] = "*** Sensitive Data Redacted ***"
    if "billing_county" in value:
        out["billing_county"] = "*** Sensitive Data Redacted ***"
    if "billing_country" in value:
        out["billing_country"] = "*** Sensitive Data Redacted ***"
    if "billing_postal_code" in value:
        out["billing_postal_code"] = "*** Sensitive Data Redacted ***"
    if "billing_province" in value:
        out["billing_province"] = "*** Sensitive Data Redacted ***"
    if "billing_state" in value:
        out["billing_state"] = "*** Sensitive Data Redacted ***"
    if "custom" in value:
        out["custom"] = "*** Sensitive Data Redacted ***"
    return out
