"""Generated from Smithy shape ``com.amazonaws.codebuild#ListFleetsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.fleet_sort_by_type
    import capo_codebuild.types.page_size
    import capo_codebuild.types.sensitive_string
    import capo_codebuild.types.sort_order_type


class ListFleetsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_codebuild.types.sensitive_string.SensitiveString"]
    """<p>During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>"""
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of paginated compute fleets returned per response. Use <code>nextToken</code> to iterate pages in the list of returned compute fleets.</p>"""
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which to list compute fleets. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List in ascending order.</p> </li> <li> <p> <code>DESCENDING</code>: List in descending order.</p> </li> </ul> <p>Use <code>sortBy</code> to specify the criterion to be used to list compute fleet names.</p>"""
    sort_by: NotRequired["capo_codebuild.types.fleet_sort_by_type.FleetSortByType"]
    """<p>The criterion to be used to list compute fleet names. Valid values include:</p> <ul> <li> <p> <code>CREATED_TIME</code>: List based on when each compute fleet was created.</p> </li> <li> <p> <code>LAST_MODIFIED_TIME</code>: List based on when information about each compute fleet was last changed.</p> </li> <li> <p> <code>NAME</code>: List based on each compute fleet's name.</p> </li> </ul> <p>Use <code>sortOrder</code> to specify in what order to list the compute fleet names based on the preceding criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFleetsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "sort_by" in value:
        import capo_codebuild.types.fleet_sort_by_type

        out["sortBy"] = capo_codebuild.types.fleet_sort_by_type.serialize_aws_json_1_1(
            value["sort_by"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFleetsInput:
    out: ListFleetsInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = (
            capo_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if data.get("sortBy") is not None:
        import capo_codebuild.types.fleet_sort_by_type

        out["sort_by"] = (
            capo_codebuild.types.fleet_sort_by_type.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
    return out


def redact_sensitive(value: ListFleetsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
