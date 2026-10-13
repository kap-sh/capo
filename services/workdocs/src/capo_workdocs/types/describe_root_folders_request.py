"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeRootFoldersRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.limit_type
    import capo_workdocs.types.page_marker_type


class DescribeRootFoldersRequest(TypedDict, closed=True):
    authentication_token: (
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    )
    """<p>Amazon WorkDocs authentication token.</p>"""
    limit: NotRequired["capo_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of items to return.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRootFoldersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRootFoldersRequest:
    out: DescribeRootFoldersRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DescribeRootFoldersRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    return out
