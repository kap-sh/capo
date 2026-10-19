"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeTypesSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.address_list
    import capo_customer_profiles.types.attribute_matching_model
    import capo_customer_profiles.types.email_list
    import capo_customer_profiles.types.phone_number_list


class AttributeTypesSelector(TypedDict, closed=True):
    attribute_matching_model: (
        "capo_customer_profiles.types.attribute_matching_model.AttributeMatchingModel"
    )
    """<p>Configures the <code>AttributeMatchingModel</code>, you can either choose <code>ONE_TO_ONE</code> or <code>MANY_TO_MANY</code>.</p>"""
    address: NotRequired["capo_customer_profiles.types.address_list.AddressList"]
    """<p>The <code>Address</code> type. You can choose from <code>Address</code>, <code>BusinessAddress</code>, <code>MaillingAddress</code>, and <code>ShippingAddress</code>.</p> <p>You only can use the Address type in the <code>MatchingRule</code>. For example, if you want to match profile based on <code>BusinessAddress.City</code> or <code>MaillingAddress.City</code>, you need to choose the <code>BusinessAddress</code> and the <code>MaillingAddress</code> to represent the Address type and specify the <code>Address.City</code> on the matching rule.</p>"""
    phone_number: NotRequired[
        "capo_customer_profiles.types.phone_number_list.PhoneNumberList"
    ]
    """<p>The <code>PhoneNumber</code> type. You can choose from <code>PhoneNumber</code>, <code>HomePhoneNumber</code>, and <code>MobilePhoneNumber</code>.</p> <p>You only can use the <code>PhoneNumber</code> type in the <code>MatchingRule</code>. For example, if you want to match a profile based on <code>Phone</code> or <code>HomePhone</code>, you need to choose the <code>Phone</code> and the <code>HomePhone</code> to represent the <code>PhoneNumber</code> type and only specify the <code>PhoneNumber</code> on the matching rule.</p>"""
    email_address: NotRequired["capo_customer_profiles.types.email_list.EmailList"]
    """<p>The <code>Email</code> type. You can choose from <code>EmailAddress</code>, <code>BusinessEmailAddress</code> and <code>PersonalEmailAddress</code>.</p> <p>You only can use the <code>EmailAddress</code> type in the <code>MatchingRule</code>. For example, if you want to match profile based on <code>PersonalEmailAddress</code> or <code>BusinessEmailAddress</code>, you need to choose the <code>PersonalEmailAddress</code> and the <code>BusinessEmailAddress</code> to represent the <code>EmailAddress</code> type and only specify the <code>EmailAddress</code> on the matching rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeTypesSelector) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.attribute_matching_model

    out["AttributeMatchingModel"] = (
        capo_customer_profiles.types.attribute_matching_model.serialize_json(
            value["attribute_matching_model"]
        )
    )
    if "address" in value:
        import capo_customer_profiles.types.address_list

        out["Address"] = capo_customer_profiles.types.address_list.serialize_json(
            value["address"]
        )
    if "phone_number" in value:
        import capo_customer_profiles.types.phone_number_list

        out["PhoneNumber"] = (
            capo_customer_profiles.types.phone_number_list.serialize_json(
                value["phone_number"]
            )
        )
    if "email_address" in value:
        import capo_customer_profiles.types.email_list

        out["EmailAddress"] = capo_customer_profiles.types.email_list.serialize_json(
            value["email_address"]
        )
    return out


def deserialize_json(data: dict) -> AttributeTypesSelector:
    out: AttributeTypesSelector = {}  # type: ignore[typeddict-item]
    if data.get("AttributeMatchingModel") is not None:
        import capo_customer_profiles.types.attribute_matching_model

        out["attribute_matching_model"] = (
            capo_customer_profiles.types.attribute_matching_model.deserialize_json(
                data["AttributeMatchingModel"]
            )
        )
    else:
        import typing

        out["attribute_matching_model"] = typing.cast(
            "capo_customer_profiles.types.attribute_matching_model.AttributeMatchingModel",
            "",
        )
    if data.get("Address") is not None:
        import capo_customer_profiles.types.address_list

        out["address"] = capo_customer_profiles.types.address_list.deserialize_json(
            data["Address"]
        )
    if data.get("PhoneNumber") is not None:
        import capo_customer_profiles.types.phone_number_list

        out["phone_number"] = (
            capo_customer_profiles.types.phone_number_list.deserialize_json(
                data["PhoneNumber"]
            )
        )
    if data.get("EmailAddress") is not None:
        import capo_customer_profiles.types.email_list

        out["email_address"] = capo_customer_profiles.types.email_list.deserialize_json(
            data["EmailAddress"]
        )
    return out
