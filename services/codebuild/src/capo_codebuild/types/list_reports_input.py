"""Generated from Smithy shape ``com.amazonaws.codebuild#ListReportsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.page_size
    import capo_codebuild.types.report_filter
    import capo_codebuild.types.sort_order_type
    import capo_codebuild.types.string


class ListReportsInput(TypedDict, closed=True):
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p> Specifies the sort order for the list of returned reports. Valid values are: </p> <ul> <li> <p> <code>ASCENDING</code>: return reports in chronological order based on their creation date. </p> </li> <li> <p> <code>DESCENDING</code>: return reports in the reverse chronological order based on their creation date. </p> </li> </ul>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p> The maximum number of paginated reports returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>Report</code> objects. The default value is 100. </p>"""
    filter: NotRequired["capo_codebuild.types.report_filter.ReportFilter"]
    """<p> A <code>ReportFilter</code> object used to filter the returned reports. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReportsInput) -> dict:
    out: dict = {}
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import capo_codebuild.types.report_filter

        out["filter"] = capo_codebuild.types.report_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReportsInput:
    out: ListReportsInput = {}  # type: ignore[typeddict-item]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = (
            capo_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filter") is not None:
        import capo_codebuild.types.report_filter

        out["filter"] = capo_codebuild.types.report_filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListReportsInput) -> dict:
    out: dict = {}
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_cbor(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import capo_codebuild.types.report_filter

        out["filter"] = capo_codebuild.types.report_filter.serialize_cbor(
            value["filter"]
        )
    return out


def deserialize_cbor(data: dict) -> ListReportsInput:
    out: ListReportsInput = {}  # type: ignore[typeddict-item]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = capo_codebuild.types.sort_order_type.deserialize_cbor(
            data["sortOrder"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filter") is not None:
        import capo_codebuild.types.report_filter

        out["filter"] = capo_codebuild.types.report_filter.deserialize_cbor(
            data["filter"]
        )
    return out
