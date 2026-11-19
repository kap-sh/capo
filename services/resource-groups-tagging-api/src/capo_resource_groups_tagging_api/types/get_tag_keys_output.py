"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetTagKeysOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.pagination_token
    import capo_resource_groups_tagging_api.types.tag_key_list


class GetTagKeysOutput(TypedDict, closed=True):
    pagination_token: NotRequired[
        "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the <code>PaginationToken</code> value in the request for the next page.</p>"""
    tag_keys: NotRequired[
        "capo_resource_groups_tagging_api.types.tag_key_list.TagKeyList"
    ]
    """<p>A list of all tag keys in the Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagKeysOutput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "tag_keys" in value:
        import capo_resource_groups_tagging_api.types.tag_key_list

        out["TagKeys"] = (
            capo_resource_groups_tagging_api.types.tag_key_list.serialize_aws_json_1_1(
                value["tag_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagKeysOutput:
    out: GetTagKeysOutput = {}  # type: ignore[typeddict-item]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("TagKeys") is not None:
        import capo_resource_groups_tagging_api.types.tag_key_list

        out["tag_keys"] = (
            capo_resource_groups_tagging_api.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetTagKeysOutput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "tag_keys" in value:
        import capo_resource_groups_tagging_api.types.tag_key_list

        out["TagKeys"] = (
            capo_resource_groups_tagging_api.types.tag_key_list.serialize_cbor(
                value["tag_keys"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetTagKeysOutput:
    out: GetTagKeysOutput = {}  # type: ignore[typeddict-item]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("TagKeys") is not None:
        import capo_resource_groups_tagging_api.types.tag_key_list

        out["tag_keys"] = (
            capo_resource_groups_tagging_api.types.tag_key_list.deserialize_cbor(
                data["TagKeys"]
            )
        )
    return out
