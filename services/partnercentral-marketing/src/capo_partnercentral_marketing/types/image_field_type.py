"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ImageFieldType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.image_format_list
    import capo_partnercentral_marketing.types.layout_preview


class ImageFieldType(TypedDict, closed=True):
    max_size_bytes: NotRequired["int"]
    """Maximum accepted file size in bytes."""
    allowed_formats: NotRequired[
        "capo_partnercentral_marketing.types.image_format_list.ImageFormatList"
    ]
    """Accepted image formats."""
    default_value: NotRequired[
        "capo_partnercentral_marketing.types.layout_preview.LayoutPreview"
    ]
    """The AWS-authored image the asset uses until the partner sets one: shown in previews and published in an empty slot of an email, landing page, banner ad or social post. It fills a required image field. A document leaves an empty image slot blank."""
    recommended_width_pixels: NotRequired["int"]
    """The image size, in pixels, that fills this slot and prints sharply, for example 1920 x 301 for a full-width header. Shown to the partner as "Recommended: W x H px". Present, together with `RecommendedHeightPixels`, on document (PDF) image slots only, where the slot is a fixed rectangle. Such a slot is always filled: the image is scaled to cover it, centred, and clipped to it, the same as CSS `object-fit: cover`. An image whose shape is too far from W:H is refused with `IMAGE_ASPECT_RATIO_MISMATCH`; one narrower than W is accepted. A slot showing the partner's logo or badge, and a slot without the two members (every slot from before sizes existed), fits the image inside instead (`object-fit: contain`): a logo or a badge is never cropped. Email and landing-page image slots are laid out by HTML and carry neither."""
    recommended_height_pixels: NotRequired["int"]
    """The image height, in pixels, that fills this slot. Present exactly when `RecommendedWidthPixels` is."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageFieldType) -> dict:
    out: dict = {}
    if "max_size_bytes" in value:
        out["MaxSizeBytes"] = value["max_size_bytes"]
    if "allowed_formats" in value:
        import capo_partnercentral_marketing.types.image_format_list

        out["AllowedFormats"] = (
            capo_partnercentral_marketing.types.image_format_list.serialize_cbor(
                value["allowed_formats"]
            )
        )
    if "default_value" in value:
        import capo_partnercentral_marketing.types.layout_preview

        out["DefaultValue"] = (
            capo_partnercentral_marketing.types.layout_preview.serialize_cbor(
                value["default_value"]
            )
        )
    if "recommended_width_pixels" in value:
        out["RecommendedWidthPixels"] = value["recommended_width_pixels"]
    if "recommended_height_pixels" in value:
        out["RecommendedHeightPixels"] = value["recommended_height_pixels"]
    return out


def deserialize_cbor(data: dict) -> ImageFieldType:
    out: ImageFieldType = {}  # type: ignore[typeddict-item]
    if data.get("MaxSizeBytes") is not None:
        out["max_size_bytes"] = data["MaxSizeBytes"]
    if data.get("AllowedFormats") is not None:
        import capo_partnercentral_marketing.types.image_format_list

        out["allowed_formats"] = (
            capo_partnercentral_marketing.types.image_format_list.deserialize_cbor(
                data["AllowedFormats"]
            )
        )
    if data.get("DefaultValue") is not None:
        import capo_partnercentral_marketing.types.layout_preview

        out["default_value"] = (
            capo_partnercentral_marketing.types.layout_preview.deserialize_cbor(
                data["DefaultValue"]
            )
        )
    if data.get("RecommendedWidthPixels") is not None:
        out["recommended_width_pixels"] = data["RecommendedWidthPixels"]
    if data.get("RecommendedHeightPixels") is not None:
        out["recommended_height_pixels"] = data["RecommendedHeightPixels"]
    return out
