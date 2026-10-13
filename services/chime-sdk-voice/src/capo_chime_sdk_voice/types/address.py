"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Address``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_non_empty_string


class Address(TypedDict, closed=True):
    street_name: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The address street, such as <code>8th Avenue</code>.</p>"""
    street_suffix: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The address suffix, such as the <code>N</code> in <code>8th Avenue N</code>.</p>"""
    post_directional: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>An address suffix location, such as the <code>S. Unit A</code> in <code>Central Park S. Unit A</code>.</p>"""
    pre_directional: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>An address prefix location, such as the <code>N</code> in <code>N. Third St.</code> </p>"""
    street_number: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The numeric portion of an address.</p>"""
    city: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The city of an address.</p>"""
    state: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The state of an address.</p>"""
    postal_code: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The postal code of an address.</p>"""
    postal_code_plus4: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The zip + 4 or postal code + 4 of an address.</p>"""
    country: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The country of an address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Address) -> dict:
    out: dict = {}
    if "street_name" in value:
        out["streetName"] = value["street_name"]
    if "street_suffix" in value:
        out["streetSuffix"] = value["street_suffix"]
    if "post_directional" in value:
        out["postDirectional"] = value["post_directional"]
    if "pre_directional" in value:
        out["preDirectional"] = value["pre_directional"]
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


def deserialize_json(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if data.get("streetName") is not None:
        out["street_name"] = data["streetName"]
    if data.get("streetSuffix") is not None:
        out["street_suffix"] = data["streetSuffix"]
    if data.get("postDirectional") is not None:
        out["post_directional"] = data["postDirectional"]
    if data.get("preDirectional") is not None:
        out["pre_directional"] = data["preDirectional"]
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


def redact_sensitive(value: Address) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "street_name" in value:
        out["street_name"] = "*** Sensitive Data Redacted ***"
    if "street_suffix" in value:
        out["street_suffix"] = "*** Sensitive Data Redacted ***"
    if "post_directional" in value:
        out["post_directional"] = "*** Sensitive Data Redacted ***"
    if "pre_directional" in value:
        out["pre_directional"] = "*** Sensitive Data Redacted ***"
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
