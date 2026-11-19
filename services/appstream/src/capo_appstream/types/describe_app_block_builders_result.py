"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppBlockBuildersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.app_block_builder_list
    import capo_appstream.types.string


class DescribeAppBlockBuildersResult(TypedDict, closed=True):
    app_block_builders: NotRequired[
        "capo_appstream.types.app_block_builder_list.AppBlockBuilderList"
    ]
    """<p>The list that describes one or more app block builders.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppBlockBuildersResult) -> dict:
    out: dict = {}
    if "app_block_builders" in value:
        import capo_appstream.types.app_block_builder_list

        out["AppBlockBuilders"] = (
            capo_appstream.types.app_block_builder_list.serialize_aws_json_1_1(
                value["app_block_builders"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppBlockBuildersResult:
    out: DescribeAppBlockBuildersResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockBuilders") is not None:
        import capo_appstream.types.app_block_builder_list

        out["app_block_builders"] = (
            capo_appstream.types.app_block_builder_list.deserialize_aws_json_1_1(
                data["AppBlockBuilders"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAppBlockBuildersResult) -> dict:
    out: dict = {}
    if "app_block_builders" in value:
        import capo_appstream.types.app_block_builder_list

        out["AppBlockBuilders"] = (
            capo_appstream.types.app_block_builder_list.serialize_cbor(
                value["app_block_builders"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAppBlockBuildersResult:
    out: DescribeAppBlockBuildersResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockBuilders") is not None:
        import capo_appstream.types.app_block_builder_list

        out["app_block_builders"] = (
            capo_appstream.types.app_block_builder_list.deserialize_cbor(
                data["AppBlockBuilders"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
