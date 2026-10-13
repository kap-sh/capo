"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeResourcePermissionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.limit_type
    import capo_workdocs.types.page_marker_type
    import capo_workdocs.types.resource_id_type


class DescribeResourcePermissionsRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    principal_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the principal to filter permissions by.</p>"""
    limit: NotRequired["capo_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of items to return with this call.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. (You received this marker from a previous call)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourcePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeResourcePermissionsRequest:
    out: DescribeResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DescribeResourcePermissionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
