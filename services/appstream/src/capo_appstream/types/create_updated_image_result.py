"""Generated from Smithy shape ``com.amazonaws.appstream#CreateUpdatedImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.boolean
    import capo_appstream.types.image


class CreateUpdatedImageResult(TypedDict, closed=True):
    image: NotRequired["capo_appstream.types.image.Image"]
    can_update_image: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Indicates whether a new image can be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUpdatedImageResult) -> dict:
    out: dict = {}
    if "image" in value:
        import capo_appstream.types.image

        out["image"] = capo_appstream.types.image.serialize_aws_json_1_1(value["image"])
    if "can_update_image" in value:
        out["canUpdateImage"] = value["can_update_image"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUpdatedImageResult:
    out: CreateUpdatedImageResult = {}  # type: ignore[typeddict-item]
    if data.get("image") is not None:
        import capo_appstream.types.image

        out["image"] = capo_appstream.types.image.deserialize_aws_json_1_1(
            data["image"]
        )
    if data.get("canUpdateImage") is not None:
        out["can_update_image"] = data["canUpdateImage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateUpdatedImageResult) -> dict:
    out: dict = {}
    if "image" in value:
        import capo_appstream.types.image

        out["image"] = capo_appstream.types.image.serialize_cbor(value["image"])
    if "can_update_image" in value:
        out["canUpdateImage"] = value["can_update_image"]
    return out


def deserialize_cbor(data: dict) -> CreateUpdatedImageResult:
    out: CreateUpdatedImageResult = {}  # type: ignore[typeddict-item]
    if data.get("image") is not None:
        import capo_appstream.types.image

        out["image"] = capo_appstream.types.image.deserialize_cbor(data["image"])
    if data.get("canUpdateImage") is not None:
        out["can_update_image"] = data["canUpdateImage"]
    return out
