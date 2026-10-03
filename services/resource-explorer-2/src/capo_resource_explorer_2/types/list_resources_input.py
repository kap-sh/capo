"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.search_filter


class ListResourcesInput(TypedDict, closed=True):
    filters: NotRequired["capo_resource_explorer_2.types.search_filter.SearchFilter"]
    """<p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters">filter prefixes</a> with optional <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>"""
    view_arn: NotRequired["str"]
    """<p>Specifies the Amazon resource name (ARN) of the view to use for the query. If you don't specify a value for this parameter, then the operation automatically uses the default view for the Amazon Web Services Region in which you called this operation. If the Region either doesn't have a default view or if you don't have permission to use the default view, then the operation fails with a 401 Unauthorized exception.</p>"""
    next_token: NotRequired["str"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p> <note> <p>The <code>ListResources</code> operation does not generate a <code>NextToken</code> if you set <code>MaxResults</code> to 1000. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_resource_explorer_2.types.search_filter

        out["Filters"] = capo_resource_explorer_2.types.search_filter.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcesInput:
    out: ListResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_resource_explorer_2.types.search_filter

        out["filters"] = capo_resource_explorer_2.types.search_filter.deserialize_json(
            data["Filters"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
