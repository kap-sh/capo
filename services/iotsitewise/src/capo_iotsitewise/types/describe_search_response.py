"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeSearchResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.group_id
    import capo_iotsitewise.types.search_id
    import capo_iotsitewise.types.search_query_statement
    import capo_iotsitewise.types.search_status
    import capo_iotsitewise.types.search_type
    import capo_iotsitewise.types.workspace_name


class DescribeSearchResponse(TypedDict, closed=True):
    search_id: "capo_iotsitewise.types.search_id.SearchId"
    """<p>The unique identifier of the search.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace the search runs against.</p>"""
    status: "capo_iotsitewise.types.search_status.SearchStatus"
    """<p>The current status of the search.</p>"""
    query_statement: (
        "capo_iotsitewise.types.search_query_statement.SearchQueryStatement"
    )
    """<p>The natural-language query that was submitted for the search.</p>"""
    search_type: "capo_iotsitewise.types.search_type.SearchType"
    """<p>The search strategy used for the search.</p>"""
    status_reason: NotRequired["str"]
    """<p>A human-readable explanation of the current status. Populated when the search has <code>FAILED</code>.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The time at which the search was started.</p>"""
    group_id: NotRequired["capo_iotsitewise.types.group_id.GroupId"]
    """<p>The group identifier associated with the search, if one was supplied on the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSearchResponse) -> dict:
    out: dict = {}
    out["searchId"] = value["search_id"]
    out["workspaceName"] = value["workspace_name"]
    import capo_iotsitewise.types.search_status

    out["status"] = capo_iotsitewise.types.search_status.serialize_json(value["status"])
    out["queryStatement"] = value["query_statement"]
    import capo_iotsitewise.types.search_type

    out["searchType"] = capo_iotsitewise.types.search_type.serialize_json(
        value["search_type"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "started_at" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["startedAt"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> DescribeSearchResponse:
    out: DescribeSearchResponse = {}  # type: ignore[typeddict-item]
    if data.get("searchId") is not None:
        out["search_id"] = data["searchId"]
    else:
        raise DeserializationError("DescribeSearchResponse.search_id required")
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        raise DeserializationError("DescribeSearchResponse.workspace_name required")
    if data.get("status") is not None:
        import capo_iotsitewise.types.search_status

        out["status"] = capo_iotsitewise.types.search_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DescribeSearchResponse.status required")
    if data.get("queryStatement") is not None:
        out["query_statement"] = data["queryStatement"]
    else:
        raise DeserializationError("DescribeSearchResponse.query_statement required")
    if data.get("searchType") is not None:
        import capo_iotsitewise.types.search_type

        out["search_type"] = capo_iotsitewise.types.search_type.deserialize_json(
            data["searchType"]
        )
    else:
        raise DeserializationError("DescribeSearchResponse.search_type required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("startedAt") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["started_at"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    return out


def redact_sensitive(value: DescribeSearchResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_statement" in value:
        out["query_statement"] = "*** Sensitive Data Redacted ***"
    return out
