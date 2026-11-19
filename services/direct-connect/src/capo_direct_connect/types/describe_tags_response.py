"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.resource_tag_list


class DescribeTagsResponse(TypedDict, closed=True):
    resource_tags: NotRequired[
        "capo_direct_connect.types.resource_tag_list.ResourceTagList"
    ]
    """<p>Information about the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import capo_direct_connect.types.resource_tag_list

        out["resourceTags"] = (
            capo_direct_connect.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsResponse:
    out: DescribeTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceTags") is not None:
        import capo_direct_connect.types.resource_tag_list

        out["resource_tags"] = (
            capo_direct_connect.types.resource_tag_list.deserialize_aws_json_1_1(
                data["resourceTags"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTagsResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import capo_direct_connect.types.resource_tag_list

        out["resourceTags"] = (
            capo_direct_connect.types.resource_tag_list.serialize_cbor(
                value["resource_tags"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeTagsResponse:
    out: DescribeTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceTags") is not None:
        import capo_direct_connect.types.resource_tag_list

        out["resource_tags"] = (
            capo_direct_connect.types.resource_tag_list.deserialize_cbor(
                data["resourceTags"]
            )
        )
    return out
