"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImagesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.image_list
    import capo_appstream.types.string


class DescribeImagesResult(TypedDict, closed=True):
    images: NotRequired["capo_appstream.types.image_list.ImageList"]
    """<p>Information about the images.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagesResult) -> dict:
    out: dict = {}
    if "images" in value:
        import capo_appstream.types.image_list

        out["Images"] = capo_appstream.types.image_list.serialize_aws_json_1_1(
            value["images"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagesResult:
    out: DescribeImagesResult = {}  # type: ignore[typeddict-item]
    if data.get("Images") is not None:
        import capo_appstream.types.image_list

        out["images"] = capo_appstream.types.image_list.deserialize_aws_json_1_1(
            data["Images"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeImagesResult) -> dict:
    out: dict = {}
    if "images" in value:
        import capo_appstream.types.image_list

        out["Images"] = capo_appstream.types.image_list.serialize_cbor(value["images"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeImagesResult:
    out: DescribeImagesResult = {}  # type: ignore[typeddict-item]
    if data.get("Images") is not None:
        import capo_appstream.types.image_list

        out["images"] = capo_appstream.types.image_list.deserialize_cbor(data["Images"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
