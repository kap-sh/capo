"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#RichTextFieldType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.allowed_tag_list
    import capo_partnercentral_marketing.types.asset_body_content


class RichTextFieldType(TypedDict, closed=True):
    max_length: NotRequired["int"]
    """Maximum accepted length of the markup fragment."""
    allowed_tags: "capo_partnercentral_marketing.types.allowed_tag_list.AllowedTagList"
    """The HTML tags permitted in the value. Anything else is stripped."""
    placeholder: NotRequired[
        "capo_partnercentral_marketing.types.asset_body_content.AssetBodyContent"
    ]
    """Example markup shown where the field is empty in a preview of the asset, restricted to AllowedTags. Never the asset's value: it is not set on the asset at create, does not fill a required field, and is never published."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RichTextFieldType) -> dict:
    out: dict = {}
    if "max_length" in value:
        out["MaxLength"] = value["max_length"]
    import capo_partnercentral_marketing.types.allowed_tag_list

    out["AllowedTags"] = (
        capo_partnercentral_marketing.types.allowed_tag_list.serialize_cbor(
            value["allowed_tags"]
        )
    )
    if "placeholder" in value:
        out["Placeholder"] = value["placeholder"]
    return out


def deserialize_cbor(data: dict) -> RichTextFieldType:
    out: RichTextFieldType = {}  # type: ignore[typeddict-item]
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    if data.get("AllowedTags") is not None:
        import capo_partnercentral_marketing.types.allowed_tag_list

        out["allowed_tags"] = (
            capo_partnercentral_marketing.types.allowed_tag_list.deserialize_cbor(
                data["AllowedTags"]
            )
        )
    else:
        out["allowed_tags"] = []
    if data.get("Placeholder") is not None:
        out["placeholder"] = data["Placeholder"]
    return out


def redact_sensitive(value: RichTextFieldType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "placeholder" in value:
        out["placeholder"] = "*** Sensitive Data Redacted ***"
    return out
