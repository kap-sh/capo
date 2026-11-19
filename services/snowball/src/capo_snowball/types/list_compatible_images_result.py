"""Generated from Smithy shape ``com.amazonaws.snowball#ListCompatibleImagesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.compatible_image_list
    import capo_snowball.types.string


class ListCompatibleImagesResult(TypedDict, closed=True):
    compatible_images: NotRequired[
        "capo_snowball.types.compatible_image_list.CompatibleImageList"
    ]
    """<p>A JSON-formatted object that describes a compatible AMI, including the ID and name for a Snow device AMI.</p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point for your next list of returned images.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCompatibleImagesResult) -> dict:
    out: dict = {}
    if "compatible_images" in value:
        import capo_snowball.types.compatible_image_list

        out["CompatibleImages"] = (
            capo_snowball.types.compatible_image_list.serialize_aws_json_1_1(
                value["compatible_images"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCompatibleImagesResult:
    out: ListCompatibleImagesResult = {}  # type: ignore[typeddict-item]
    if data.get("CompatibleImages") is not None:
        import capo_snowball.types.compatible_image_list

        out["compatible_images"] = (
            capo_snowball.types.compatible_image_list.deserialize_aws_json_1_1(
                data["CompatibleImages"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCompatibleImagesResult) -> dict:
    out: dict = {}
    if "compatible_images" in value:
        import capo_snowball.types.compatible_image_list

        out["CompatibleImages"] = (
            capo_snowball.types.compatible_image_list.serialize_cbor(
                value["compatible_images"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListCompatibleImagesResult:
    out: ListCompatibleImagesResult = {}  # type: ignore[typeddict-item]
    if data.get("CompatibleImages") is not None:
        import capo_snowball.types.compatible_image_list

        out["compatible_images"] = (
            capo_snowball.types.compatible_image_list.deserialize_cbor(
                data["CompatibleImages"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
