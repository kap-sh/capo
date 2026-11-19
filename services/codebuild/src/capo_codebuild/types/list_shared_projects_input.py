"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSharedProjectsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.page_size
    import capo_codebuild.types.shared_resource_sort_by_type
    import capo_codebuild.types.sort_order_type


class ListSharedProjectsInput(TypedDict, closed=True):
    sort_by: NotRequired[
        "capo_codebuild.types.shared_resource_sort_by_type.SharedResourceSortByType"
    ]
    """<p> The criterion to be used to list build projects shared with the current Amazon Web Services account or user. Valid values include: </p> <ul> <li> <p> <code>ARN</code>: List based on the ARN. </p> </li> <li> <p> <code>MODIFIED_TIME</code>: List based on when information about the shared project was last changed. </p> </li> </ul>"""
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which to list shared build projects. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List in ascending order.</p> </li> <li> <p> <code>DESCENDING</code>: List in descending order.</p> </li> </ul>"""
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p> The maximum number of paginated shared build projects returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>Project</code> objects. The default value is 100. </p>"""
    next_token: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSharedProjectsInput) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_codebuild.types.shared_resource_sort_by_type

        out["sortBy"] = (
            capo_codebuild.types.shared_resource_sort_by_type.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSharedProjectsInput:
    out: ListSharedProjectsInput = {}  # type: ignore[typeddict-item]
    if data.get("sortBy") is not None:
        import capo_codebuild.types.shared_resource_sort_by_type

        out["sort_by"] = (
            capo_codebuild.types.shared_resource_sort_by_type.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = (
            capo_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSharedProjectsInput) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_codebuild.types.shared_resource_sort_by_type

        out["sortBy"] = (
            capo_codebuild.types.shared_resource_sort_by_type.serialize_cbor(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_cbor(
            value["sort_order"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListSharedProjectsInput:
    out: ListSharedProjectsInput = {}  # type: ignore[typeddict-item]
    if data.get("sortBy") is not None:
        import capo_codebuild.types.shared_resource_sort_by_type

        out["sort_by"] = (
            capo_codebuild.types.shared_resource_sort_by_type.deserialize_cbor(
                data["sortBy"]
            )
        )
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = capo_codebuild.types.sort_order_type.deserialize_cbor(
            data["sortOrder"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
