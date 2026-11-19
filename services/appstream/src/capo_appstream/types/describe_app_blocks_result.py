"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppBlocksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.app_blocks
    import capo_appstream.types.string


class DescribeAppBlocksResult(TypedDict, closed=True):
    app_blocks: NotRequired["capo_appstream.types.app_blocks.AppBlocks"]
    """<p>The app blocks in the list.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppBlocksResult) -> dict:
    out: dict = {}
    if "app_blocks" in value:
        import capo_appstream.types.app_blocks

        out["AppBlocks"] = capo_appstream.types.app_blocks.serialize_aws_json_1_1(
            value["app_blocks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppBlocksResult:
    out: DescribeAppBlocksResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlocks") is not None:
        import capo_appstream.types.app_blocks

        out["app_blocks"] = capo_appstream.types.app_blocks.deserialize_aws_json_1_1(
            data["AppBlocks"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAppBlocksResult) -> dict:
    out: dict = {}
    if "app_blocks" in value:
        import capo_appstream.types.app_blocks

        out["AppBlocks"] = capo_appstream.types.app_blocks.serialize_cbor(
            value["app_blocks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAppBlocksResult:
    out: DescribeAppBlocksResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlocks") is not None:
        import capo_appstream.types.app_blocks

        out["app_blocks"] = capo_appstream.types.app_blocks.deserialize_cbor(
            data["AppBlocks"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
