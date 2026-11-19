"""Generated from Smithy shape ``com.amazonaws.codebuild#ListReportGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.page_size
    import capo_codebuild.types.report_group_sort_by_type
    import capo_codebuild.types.sort_order_type
    import capo_codebuild.types.string


class ListReportGroupsInput(TypedDict, closed=True):
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p> Used to specify the order to sort the list of returned report groups. Valid values are <code>ASCENDING</code> and <code>DESCENDING</code>. </p>"""
    sort_by: NotRequired[
        "capo_codebuild.types.report_group_sort_by_type.ReportGroupSortByType"
    ]
    """<p> The criterion to be used to list build report groups. Valid values include: </p> <ul> <li> <p> <code>CREATED_TIME</code>: List based on when each report group was created.</p> </li> <li> <p> <code>LAST_MODIFIED_TIME</code>: List based on when each report group was last changed.</p> </li> <li> <p> <code>NAME</code>: List based on each report group's name.</p> </li> </ul>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p> The maximum number of paginated report groups returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>ReportGroup</code> objects. The default value is 100. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReportGroupsInput) -> dict:
    out: dict = {}
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "sort_by" in value:
        import capo_codebuild.types.report_group_sort_by_type

        out["sortBy"] = (
            capo_codebuild.types.report_group_sort_by_type.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReportGroupsInput:
    out: ListReportGroupsInput = {}  # type: ignore[typeddict-item]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = (
            capo_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if data.get("sortBy") is not None:
        import capo_codebuild.types.report_group_sort_by_type

        out["sort_by"] = (
            capo_codebuild.types.report_group_sort_by_type.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListReportGroupsInput) -> dict:
    out: dict = {}
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_cbor(
            value["sort_order"]
        )
    if "sort_by" in value:
        import capo_codebuild.types.report_group_sort_by_type

        out["sortBy"] = capo_codebuild.types.report_group_sort_by_type.serialize_cbor(
            value["sort_by"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListReportGroupsInput:
    out: ListReportGroupsInput = {}  # type: ignore[typeddict-item]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = capo_codebuild.types.sort_order_type.deserialize_cbor(
            data["sortOrder"]
        )
    if data.get("sortBy") is not None:
        import capo_codebuild.types.report_group_sort_by_type

        out["sort_by"] = (
            capo_codebuild.types.report_group_sort_by_type.deserialize_cbor(
                data["sortBy"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
