"""Generated from Smithy shape ``com.amazonaws.opensearch#GetPackageVersionHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token
    import capo_opensearch.types.package_id


class GetPackageVersionHistoryRequest(TypedDict, closed=True):
    package_id: "capo_opensearch.types.package_id.PackageID"
    """<p>The unique identifier of the package.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>GetPackageVersionHistory</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>GetPackageVersionHistory</code> operations, which returns results in the next page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageVersionHistoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPackageVersionHistoryRequest:
    out: GetPackageVersionHistoryRequest = {}  # type: ignore[typeddict-item]
    return out
