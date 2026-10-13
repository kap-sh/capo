"""Generated from Smithy shape ``com.amazonaws.workdocs#GetResourcesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.limit_type
    import capo_workdocs.types.page_marker_type
    import capo_workdocs.types.resource_collection_type


class GetResourcesRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>The Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    user_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The user ID for the resource collection. This is a required field for accessing the API operation using IAM credentials.</p>"""
    collection_type: NotRequired[
        "capo_workdocs.types.resource_collection_type.ResourceCollectionType"
    ]
    """<p>The collection type.</p>"""
    limit: NotRequired["capo_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of resources to return.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. This marker was received from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcesRequest:
    out: GetResourcesRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: GetResourcesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
