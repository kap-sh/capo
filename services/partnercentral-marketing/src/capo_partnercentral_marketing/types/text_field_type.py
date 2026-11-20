"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#TextFieldType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_body_content
    import capo_partnercentral_marketing.types.template_field_pattern


class TextFieldType(TypedDict, closed=True):
    min_length: NotRequired["int"]
    """Minimum accepted length."""
    max_length: NotRequired["int"]
    """Maximum accepted length."""
    pattern: NotRequired[
        "capo_partnercentral_marketing.types.template_field_pattern.TemplateFieldPattern"
    ]
    """Regular expression the value must match — used for URL, email, phone and hex-colour fields."""
    placeholder: NotRequired[
        "capo_partnercentral_marketing.types.asset_body_content.AssetBodyContent"
    ]
    """Example text shown where the field is empty in a preview of the asset. Never the asset's value: it is not set on the asset at create, does not fill a required field, and is never published."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TextFieldType) -> dict:
    out: dict = {}
    if "min_length" in value:
        out["MinLength"] = value["min_length"]
    if "max_length" in value:
        out["MaxLength"] = value["max_length"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    if "placeholder" in value:
        out["Placeholder"] = value["placeholder"]
    return out


def deserialize_cbor(data: dict) -> TextFieldType:
    out: TextFieldType = {}  # type: ignore[typeddict-item]
    if data.get("MinLength") is not None:
        out["min_length"] = data["MinLength"]
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("Placeholder") is not None:
        out["placeholder"] = data["Placeholder"]
    return out


def redact_sensitive(value: TextFieldType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "placeholder" in value:
        out["placeholder"] = "*** Sensitive Data Redacted ***"
    return out
