"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImageBuildersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.image_builder_list
    import capo_appstream.types.string


class DescribeImageBuildersResult(TypedDict, closed=True):
    image_builders: NotRequired[
        "capo_appstream.types.image_builder_list.ImageBuilderList"
    ]
    """<p>Information about the image builders.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageBuildersResult) -> dict:
    out: dict = {}
    if "image_builders" in value:
        import capo_appstream.types.image_builder_list

        out["ImageBuilders"] = (
            capo_appstream.types.image_builder_list.serialize_aws_json_1_1(
                value["image_builders"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageBuildersResult:
    out: DescribeImageBuildersResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilders") is not None:
        import capo_appstream.types.image_builder_list

        out["image_builders"] = (
            capo_appstream.types.image_builder_list.deserialize_aws_json_1_1(
                data["ImageBuilders"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeImageBuildersResult) -> dict:
    out: dict = {}
    if "image_builders" in value:
        import capo_appstream.types.image_builder_list

        out["ImageBuilders"] = capo_appstream.types.image_builder_list.serialize_cbor(
            value["image_builders"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeImageBuildersResult:
    out: DescribeImageBuildersResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilders") is not None:
        import capo_appstream.types.image_builder_list

        out["image_builders"] = (
            capo_appstream.types.image_builder_list.deserialize_cbor(
                data["ImageBuilders"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
