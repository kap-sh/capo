"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppPhoneNumberSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.iso_country_code
    import capo_socialmessaging.types.linked_whats_app_phone_number_arn
    import capo_socialmessaging.types.phone_number
    import capo_socialmessaging.types.whats_app_display_phone_number
    import capo_socialmessaging.types.whats_app_phone_number
    import capo_socialmessaging.types.whats_app_phone_number_id
    import capo_socialmessaging.types.whats_app_phone_number_name
    import capo_socialmessaging.types.whats_app_phone_number_quality_rating


class WhatsAppPhoneNumberSummary(TypedDict, closed=True):
    arn: "capo_socialmessaging.types.linked_whats_app_phone_number_arn.LinkedWhatsAppPhoneNumberArn"
    """<p>The full Amazon Resource Name (ARN) for the phone number.</p>"""
    phone_number: "capo_socialmessaging.types.phone_number.PhoneNumber"
    """<p>The phone number associated with the Linked WhatsApp Business Account.</p>"""
    phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The phone number ID. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. </p>"""
    meta_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number.WhatsAppPhoneNumber"
    )
    """<p>The phone number ID from Meta.</p>"""
    display_phone_number_name: (
        "capo_socialmessaging.types.whats_app_phone_number_name.WhatsAppPhoneNumberName"
    )
    """<p>The display name for this phone number.</p>"""
    display_phone_number: "capo_socialmessaging.types.whats_app_display_phone_number.WhatsAppDisplayPhoneNumber"
    """<p>The phone number that appears in the recipients display.</p>"""
    quality_rating: "capo_socialmessaging.types.whats_app_phone_number_quality_rating.WhatsAppPhoneNumberQualityRating"
    """<p>The quality rating of the phone number. This is from Meta.</p>"""
    data_localization_region: NotRequired[
        "capo_socialmessaging.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The geographic region where the WhatsApp phone number's data is stored and processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppPhoneNumberSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["phoneNumber"] = value["phone_number"]
    out["phoneNumberId"] = value["phone_number_id"]
    out["metaPhoneNumberId"] = value["meta_phone_number_id"]
    out["displayPhoneNumberName"] = value["display_phone_number_name"]
    out["displayPhoneNumber"] = value["display_phone_number"]
    out["qualityRating"] = value["quality_rating"]
    if "data_localization_region" in value:
        out["dataLocalizationRegion"] = value["data_localization_region"]
    return out


def deserialize_json(data: dict) -> WhatsAppPhoneNumberSummary:
    out: WhatsAppPhoneNumberSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("phoneNumber") is not None:
        out["phone_number"] = data["phoneNumber"]
    else:
        out["phone_number"] = ""
    if data.get("phoneNumberId") is not None:
        out["phone_number_id"] = data["phoneNumberId"]
    else:
        out["phone_number_id"] = ""
    if data.get("metaPhoneNumberId") is not None:
        out["meta_phone_number_id"] = data["metaPhoneNumberId"]
    else:
        out["meta_phone_number_id"] = ""
    if data.get("displayPhoneNumberName") is not None:
        out["display_phone_number_name"] = data["displayPhoneNumberName"]
    else:
        out["display_phone_number_name"] = ""
    if data.get("displayPhoneNumber") is not None:
        out["display_phone_number"] = data["displayPhoneNumber"]
    else:
        out["display_phone_number"] = ""
    if data.get("qualityRating") is not None:
        out["quality_rating"] = data["qualityRating"]
    else:
        out["quality_rating"] = ""
    if data.get("dataLocalizationRegion") is not None:
        out["data_localization_region"] = data["dataLocalizationRegion"]
    return out
