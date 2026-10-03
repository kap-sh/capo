"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#SearchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.query_string


class SearchInput(TypedDict, closed=True):
    query_string: "capo_resource_explorer_2.types.query_string.QueryString"
    """<p>A string that includes keywords and filters that specify the resources that you want to include in the results.</p> <p>For the complete syntax supported by the <code>QueryString</code> parameter, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html">Search query syntax reference for Resource Explorer</a>.</p> <p>The search is completely case insensitive. You can specify an empty string to return all results up to the limit of 1,000 total results.</p> <note> <p>The operation can return only the first 1,000 results. If the resource you want is not included, then use a different value for <code>QueryString</code> to refine the results.</p> </note>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>"""
    view_arn: NotRequired["str"]
    """<p>Specifies the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view to use for the query. If you don't specify a value for this parameter, then the operation automatically uses the default view for the Amazon Web Services Region in which you called this operation. If the Region either doesn't have a default view or if you don't have permission to use the default view, then the operation fails with a <code>401 Unauthorized</code> exception.</p>"""
    next_token: NotRequired["str"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchInput) -> dict:
    out: dict = {}
    out["QueryString"] = value["query_string"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchInput:
    out: SearchInput = {}  # type: ignore[typeddict-item]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        raise DeserializationError("SearchInput.query_string required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
