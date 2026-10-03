"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeDocumentVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.field_names_type
    import capo_workdocs.types.limit_type
    import capo_workdocs.types.page_marker_type
    import capo_workdocs.types.resource_id_type


class DescribeDocumentVersionsRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    limit: NotRequired["capo_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of versions to return with this call.</p>"""
    include: NotRequired["capo_workdocs.types.field_names_type.FieldNamesType"]
    """<p>A comma-separated list of values. Specify "INITIALIZED" to include incomplete versions.</p>"""
    fields: NotRequired["capo_workdocs.types.field_names_type.FieldNamesType"]
    """<p>Specify "SOURCE" to include initialized versions and a URL for the source document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDocumentVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDocumentVersionsRequest:
    out: DescribeDocumentVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
