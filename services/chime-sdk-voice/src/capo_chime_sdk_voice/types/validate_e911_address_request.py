"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ValidateE911AddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.sensitive_non_empty_string


class ValidateE911AddressRequest(TypedDict, closed=True):
    aws_account_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The AWS account ID.</p>"""
    street_number: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The address street number, such as <code>200</code> or <code>2121</code>.</p>"""
    street_info: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The address street information, such as <code>8th Avenue</code>.</p>"""
    city: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The address city, such as <code>Portland</code>.</p>"""
    state: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The address state, such as <code>ME</code>.</p>"""
    country: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The country in the address being validated as two-letter country code in ISO 3166-1 alpha-2 format, such as <code>US</code>. For more information, see <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> in Wikipedia.</p>"""
    postal_code: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The dress postal code, such <code>04352</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateE911AddressRequest) -> dict:
    out: dict = {}
    out["AwsAccountId"] = value["aws_account_id"]
    out["StreetNumber"] = value["street_number"]
    out["StreetInfo"] = value["street_info"]
    out["City"] = value["city"]
    out["State"] = value["state"]
    out["Country"] = value["country"]
    out["PostalCode"] = value["postal_code"]
    return out


def deserialize_json(data: dict) -> ValidateE911AddressRequest:
    out: ValidateE911AddressRequest = {}  # type: ignore[typeddict-item]
    if data.get("AwsAccountId") is not None:
        out["aws_account_id"] = data["AwsAccountId"]
    else:
        raise DeserializationError("ValidateE911AddressRequest.aws_account_id required")
    if data.get("StreetNumber") is not None:
        out["street_number"] = data["StreetNumber"]
    else:
        raise DeserializationError("ValidateE911AddressRequest.street_number required")
    if data.get("StreetInfo") is not None:
        out["street_info"] = data["StreetInfo"]
    else:
        raise DeserializationError("ValidateE911AddressRequest.street_info required")
    if data.get("City") is not None:
        out["city"] = data["City"]
    else:
        raise DeserializationError("ValidateE911AddressRequest.city required")
    if data.get("State") is not None:
        out["state"] = data["State"]
    else:
        raise DeserializationError("ValidateE911AddressRequest.state required")
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    else:
        raise DeserializationError("ValidateE911AddressRequest.country required")
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    else:
        raise DeserializationError("ValidateE911AddressRequest.postal_code required")
    return out
