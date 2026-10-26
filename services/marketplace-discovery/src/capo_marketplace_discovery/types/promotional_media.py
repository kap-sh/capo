"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PromotionalMedia``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError, SerializationError
from capo_marketplace_discovery.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.promotional_embedded_image
    import capo_marketplace_discovery.types.promotional_embedded_video


class _PromotionalMedia_embeddedImage(TypedDict, closed=True):
    embeddedImage: "capo_marketplace_discovery.types.promotional_embedded_image.PromotionalEmbeddedImage"


class _PromotionalMedia_embeddedVideo(TypedDict, closed=True):
    embeddedVideo: "capo_marketplace_discovery.types.promotional_embedded_video.PromotionalEmbeddedVideo"


PromotionalMedia: TypeAlias = (
    _PromotionalMedia_embeddedImage
    | _PromotionalMedia_embeddedVideo
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PromotionalMedia) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PromotionalMedia: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "embeddedImage" in value:
        import capo_marketplace_discovery.types.promotional_embedded_image

        return {
            "embeddedImage": capo_marketplace_discovery.types.promotional_embedded_image.serialize_json(
                value["embeddedImage"]
            )
        }
    elif "embeddedVideo" in value:
        import capo_marketplace_discovery.types.promotional_embedded_video

        return {
            "embeddedVideo": capo_marketplace_discovery.types.promotional_embedded_video.serialize_json(
                value["embeddedVideo"]
            )
        }
    else:
        raise SerializationError("PromotionalMedia: no variant present")


def deserialize_json(data: dict) -> PromotionalMedia:
    if data.get("embeddedImage") is not None:
        import capo_marketplace_discovery.types.promotional_embedded_image

        return {
            "embeddedImage": capo_marketplace_discovery.types.promotional_embedded_image.deserialize_json(
                data["embeddedImage"]
            )
        }
    elif data.get("embeddedVideo") is not None:
        import capo_marketplace_discovery.types.promotional_embedded_video

        return {
            "embeddedVideo": capo_marketplace_discovery.types.promotional_embedded_video.deserialize_json(
                data["embeddedVideo"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PromotionalMedia: no recognized variant key")
