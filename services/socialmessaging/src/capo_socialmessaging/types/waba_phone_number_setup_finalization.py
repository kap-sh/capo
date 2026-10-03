"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WabaPhoneNumberSetupFinalization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.iso_country_code
    import capo_socialmessaging.types.tag_list
    import capo_socialmessaging.types.two_factor_pin
    import capo_socialmessaging.types.whats_app_phone_number


class WabaPhoneNumberSetupFinalization(TypedDict, closed=True):
    id: "capo_socialmessaging.types.whats_app_phone_number.WhatsAppPhoneNumber"
    """<p>The unique identifier of the originating phone number associated with the media. Phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use the <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> API action to find a phone number's id.</p>"""
    two_factor_pin: "capo_socialmessaging.types.two_factor_pin.TwoFactorPin"
    """<p>The PIN to use for two-step verification. To reset your PIN follow the directions in <a href="https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification/#updating-pin">Updating PIN</a> in the <i>WhatsApp Business Platform Cloud API Reference</i>.</p>"""
    data_localization_region: NotRequired[
        "capo_socialmessaging.types.iso_country_code.IsoCountryCode"
    ]
    """<p>The two letter ISO region for the location of where Meta will store data.</p> <p class="title"> <b>Asia–Pacific (APAC)</b> </p> <ul> <li> <p>Australia <b>AU</b> </p> </li> <li> <p>Indonesia <b>ID</b> </p> </li> <li> <p>India <b>IN</b> </p> </li> <li> <p>Japan <b>JP</b> </p> </li> <li> <p>Singapore <b>SG</b> </p> </li> <li> <p>South Korea <b>KR</b> </p> </li> </ul> <p class="title"> <b>Europe</b> </p> <ul> <li> <p>Germany <b>DE</b> </p> </li> <li> <p>Switzerland <b>CH</b> </p> </li> <li> <p>United Kingdom <b>GB</b> </p> </li> </ul> <p class="title"> <b>Latin America (LATAM)</b> </p> <ul> <li> <p>Brazil <b>BR</b> </p> </li> </ul> <p class="title"> <b>Middle East and Africa (MEA)</b> </p> <ul> <li> <p>Bahrain <b>BH</b> </p> </li> <li> <p>South Africa <b>ZA</b> </p> </li> <li> <p>United Arab Emirates <b>AE</b> </p> </li> </ul> <p class="title"> <b>North America (NORAM)</b> </p> <ul> <li> <p>Canada <b>CA</b> </p> </li> </ul>"""
    tags: NotRequired["capo_socialmessaging.types.tag_list.TagList"]
    """<p>An array of key and value pair tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WabaPhoneNumberSetupFinalization) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["twoFactorPin"] = value["two_factor_pin"]
    if "data_localization_region" in value:
        out["dataLocalizationRegion"] = value["data_localization_region"]
    if "tags" in value:
        import capo_socialmessaging.types.tag_list

        out["tags"] = capo_socialmessaging.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> WabaPhoneNumberSetupFinalization:
    out: WabaPhoneNumberSetupFinalization = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("WabaPhoneNumberSetupFinalization.id required")
    if data.get("twoFactorPin") is not None:
        out["two_factor_pin"] = data["twoFactorPin"]
    else:
        raise DeserializationError(
            "WabaPhoneNumberSetupFinalization.two_factor_pin required"
        )
    if data.get("dataLocalizationRegion") is not None:
        out["data_localization_region"] = data["dataLocalizationRegion"]
    if data.get("tags") is not None:
        import capo_socialmessaging.types.tag_list

        out["tags"] = capo_socialmessaging.types.tag_list.deserialize_json(data["tags"])
    return out
