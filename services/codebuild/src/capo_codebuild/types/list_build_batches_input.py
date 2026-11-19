"""Generated from Smithy shape ``com.amazonaws.codebuild#ListBuildBatchesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_batch_filter
    import capo_codebuild.types.page_size
    import capo_codebuild.types.sort_order_type
    import capo_codebuild.types.string


class ListBuildBatchesInput(TypedDict, closed=True):
    filter: NotRequired["capo_codebuild.types.build_batch_filter.BuildBatchFilter"]
    """<p>A <code>BuildBatchFilter</code> object that specifies the filters for the search.</p>"""
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p>Specifies the sort order of the returned items. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List the batch build identifiers in ascending order by identifier.</p> </li> <li> <p> <code>DESCENDING</code>: List the batch build identifiers in descending order by identifier.</p> </li> </ul>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous call to <code>ListBuildBatches</code>. This specifies the next item to return. To return the beginning of the list, exclude this parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildBatchesInput) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_codebuild.types.build_batch_filter

        out["filter"] = capo_codebuild.types.build_batch_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildBatchesInput:
    out: ListBuildBatchesInput = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_codebuild.types.build_batch_filter

        out["filter"] = (
            capo_codebuild.types.build_batch_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = (
            capo_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListBuildBatchesInput) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_codebuild.types.build_batch_filter

        out["filter"] = capo_codebuild.types.build_batch_filter.serialize_cbor(
            value["filter"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_cbor(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListBuildBatchesInput:
    out: ListBuildBatchesInput = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_codebuild.types.build_batch_filter

        out["filter"] = capo_codebuild.types.build_batch_filter.deserialize_cbor(
            data["filter"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = capo_codebuild.types.sort_order_type.deserialize_cbor(
            data["sortOrder"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
