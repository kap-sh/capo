"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#FieldType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_marketing.errors import (
    DeserializationError,
    SerializationError,
)
from capo_partnercentral_marketing.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_link_field_type
    import capo_partnercentral_marketing.types.image_field_type
    import capo_partnercentral_marketing.types.rich_text_field_type
    import capo_partnercentral_marketing.types.text_field_type


class FieldTypeTextMember(TypedDict, closed=True):
    Text: "capo_partnercentral_marketing.types.text_field_type.TextFieldType"


class FieldTypeRichTextMember(TypedDict, closed=True):
    RichText: (
        "capo_partnercentral_marketing.types.rich_text_field_type.RichTextFieldType"
    )


class FieldTypeImageMember(TypedDict, closed=True):
    Image: "capo_partnercentral_marketing.types.image_field_type.ImageFieldType"


class FieldTypeAssetLinkMember(TypedDict, closed=True):
    AssetLink: (
        "capo_partnercentral_marketing.types.asset_link_field_type.AssetLinkFieldType"
    )


FieldType: TypeAlias = (
    FieldTypeTextMember
    | FieldTypeRichTextMember
    | FieldTypeImageMember
    | FieldTypeAssetLinkMember
    | UnknownUnionMember
)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FieldType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FieldType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Text" in value:
        import capo_partnercentral_marketing.types.text_field_type

        return {
            "Text": capo_partnercentral_marketing.types.text_field_type.serialize_cbor(
                value["Text"]
            )
        }
    elif "RichText" in value:
        import capo_partnercentral_marketing.types.rich_text_field_type

        return {
            "RichText": capo_partnercentral_marketing.types.rich_text_field_type.serialize_cbor(
                value["RichText"]
            )
        }
    elif "Image" in value:
        import capo_partnercentral_marketing.types.image_field_type

        return {
            "Image": capo_partnercentral_marketing.types.image_field_type.serialize_cbor(
                value["Image"]
            )
        }
    elif "AssetLink" in value:
        import capo_partnercentral_marketing.types.asset_link_field_type

        return {
            "AssetLink": capo_partnercentral_marketing.types.asset_link_field_type.serialize_cbor(
                value["AssetLink"]
            )
        }
    else:
        raise SerializationError("FieldType: no variant present")


def deserialize_cbor(data: dict) -> FieldType:
    if data.get("Text") is not None:
        import capo_partnercentral_marketing.types.text_field_type

        return {
            "Text": capo_partnercentral_marketing.types.text_field_type.deserialize_cbor(
                data["Text"]
            )
        }
    elif data.get("RichText") is not None:
        import capo_partnercentral_marketing.types.rich_text_field_type

        return {
            "RichText": capo_partnercentral_marketing.types.rich_text_field_type.deserialize_cbor(
                data["RichText"]
            )
        }
    elif data.get("Image") is not None:
        import capo_partnercentral_marketing.types.image_field_type

        return {
            "Image": capo_partnercentral_marketing.types.image_field_type.deserialize_cbor(
                data["Image"]
            )
        }
    elif data.get("AssetLink") is not None:
        import capo_partnercentral_marketing.types.asset_link_field_type

        return {
            "AssetLink": capo_partnercentral_marketing.types.asset_link_field_type.deserialize_cbor(
                data["AssetLink"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FieldType: no recognized variant key")


def redact_sensitive(value: FieldType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Text" in value:
        import capo_partnercentral_marketing.types.text_field_type

        out["Text"] = (
            capo_partnercentral_marketing.types.text_field_type.redact_sensitive(
                value["Text"]
            )
        )
    if "RichText" in value:
        import capo_partnercentral_marketing.types.rich_text_field_type

        out["RichText"] = (
            capo_partnercentral_marketing.types.rich_text_field_type.redact_sensitive(
                value["RichText"]
            )
        )
    return out
