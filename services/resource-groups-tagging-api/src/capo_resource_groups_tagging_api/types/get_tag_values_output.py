"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetTagValuesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.pagination_token
    import capo_resource_groups_tagging_api.types.tag_values_output_list


class GetTagValuesOutput(TypedDict, closed=True):
    pagination_token: NotRequired[
        "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the <code>PaginationToken</code> value in the request for the next page.</p>"""
    tag_values: NotRequired[
        "capo_resource_groups_tagging_api.types.tag_values_output_list.TagValuesOutputList"
    ]
    """<p>A list of all tag values for the specified key currently used in the specified Amazon Web Services Region for the calling account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagValuesOutput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "tag_values" in value:
        import capo_resource_groups_tagging_api.types.tag_values_output_list

        out["TagValues"] = (
            capo_resource_groups_tagging_api.types.tag_values_output_list.serialize_aws_json_1_1(
                value["tag_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagValuesOutput:
    out: GetTagValuesOutput = {}  # type: ignore[typeddict-item]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("TagValues") is not None:
        import capo_resource_groups_tagging_api.types.tag_values_output_list

        out["tag_values"] = (
            capo_resource_groups_tagging_api.types.tag_values_output_list.deserialize_aws_json_1_1(
                data["TagValues"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetTagValuesOutput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "tag_values" in value:
        import capo_resource_groups_tagging_api.types.tag_values_output_list

        out["TagValues"] = (
            capo_resource_groups_tagging_api.types.tag_values_output_list.serialize_cbor(
                value["tag_values"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetTagValuesOutput:
    out: GetTagValuesOutput = {}  # type: ignore[typeddict-item]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("TagValues") is not None:
        import capo_resource_groups_tagging_api.types.tag_values_output_list

        out["tag_values"] = (
            capo_resource_groups_tagging_api.types.tag_values_output_list.deserialize_cbor(
                data["TagValues"]
            )
        )
    return out
