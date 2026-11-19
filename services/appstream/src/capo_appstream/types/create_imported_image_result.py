"""Generated from Smithy shape ``com.amazonaws.appstream#CreateImportedImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.image


class CreateImportedImageResult(TypedDict, closed=True):
    image: NotRequired["capo_appstream.types.image.Image"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImportedImageResult) -> dict:
    out: dict = {}
    if "image" in value:
        import capo_appstream.types.image

        out["Image"] = capo_appstream.types.image.serialize_aws_json_1_1(value["image"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImportedImageResult:
    out: CreateImportedImageResult = {}  # type: ignore[typeddict-item]
    if data.get("Image") is not None:
        import capo_appstream.types.image

        out["image"] = capo_appstream.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateImportedImageResult) -> dict:
    out: dict = {}
    if "image" in value:
        import capo_appstream.types.image

        out["Image"] = capo_appstream.types.image.serialize_cbor(value["image"])
    return out


def deserialize_cbor(data: dict) -> CreateImportedImageResult:
    out: CreateImportedImageResult = {}  # type: ignore[typeddict-item]
    if data.get("Image") is not None:
        import capo_appstream.types.image

        out["image"] = capo_appstream.types.image.deserialize_cbor(data["Image"])
    return out
