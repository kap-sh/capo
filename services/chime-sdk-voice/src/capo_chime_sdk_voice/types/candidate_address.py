"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CandidateAddress``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_non_empty_string


class CandidateAddress(TypedDict, closed=True):
    street_info: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The street information of the candidate address.</p>"""
    street_number: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The numeric portion of the candidate address.</p>"""
    city: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The city of the candidate address.</p>"""
    state: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The state of the candidate address.</p>"""
    postal_code: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The postal code of the candidate address.</p>"""
    postal_code_plus4: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The zip + 4 or postal code +4 of the candidate address.</p>"""
    country: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The country of the candidate address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CandidateAddress) -> dict:
    out: dict = {}
    if "street_info" in value:
        out["streetInfo"] = value["street_info"]
    if "street_number" in value:
        out["streetNumber"] = value["street_number"]
    if "city" in value:
        out["city"] = value["city"]
    if "state" in value:
        out["state"] = value["state"]
    if "postal_code" in value:
        out["postalCode"] = value["postal_code"]
    if "postal_code_plus4" in value:
        out["postalCodePlus4"] = value["postal_code_plus4"]
    if "country" in value:
        out["country"] = value["country"]
    return out


def deserialize_json(data: dict) -> CandidateAddress:
    out: CandidateAddress = {}  # type: ignore[typeddict-item]
    if data.get("streetInfo") is not None:
        out["street_info"] = data["streetInfo"]
    if data.get("streetNumber") is not None:
        out["street_number"] = data["streetNumber"]
    if data.get("city") is not None:
        out["city"] = data["city"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("postalCode") is not None:
        out["postal_code"] = data["postalCode"]
    if data.get("postalCodePlus4") is not None:
        out["postal_code_plus4"] = data["postalCodePlus4"]
    if data.get("country") is not None:
        out["country"] = data["country"]
    return out


def redact_sensitive(value: CandidateAddress) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "street_info" in value:
        out["street_info"] = "*** Sensitive Data Redacted ***"
    if "street_number" in value:
        out["street_number"] = "*** Sensitive Data Redacted ***"
    if "city" in value:
        out["city"] = "*** Sensitive Data Redacted ***"
    if "state" in value:
        out["state"] = "*** Sensitive Data Redacted ***"
    if "postal_code" in value:
        out["postal_code"] = "*** Sensitive Data Redacted ***"
    if "postal_code_plus4" in value:
        out["postal_code_plus4"] = "*** Sensitive Data Redacted ***"
    if "country" in value:
        out["country"] = "*** Sensitive Data Redacted ***"
    return out
