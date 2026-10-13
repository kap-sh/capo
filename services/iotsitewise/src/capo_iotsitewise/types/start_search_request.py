"""Generated from Smithy shape ``com.amazonaws.iotsitewise#StartSearchRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.group_id
    import capo_iotsitewise.types.search_filters
    import capo_iotsitewise.types.search_query_statement
    import capo_iotsitewise.types.search_type
    import capo_iotsitewise.types.workspace_name


class StartSearchRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace whose data is searched.</p>"""
    query_statement: (
        "capo_iotsitewise.types.search_query_statement.SearchQueryStatement"
    )
    """<p>The natural-language query describing the data to search for.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier you provide to ensure the request is idempotent. Repeating a StartSearch call with the same <code>clientToken</code> returns the original search rather than starting a new one. If omitted, the SDK autogenerates one.</p>"""
    search_type: NotRequired["capo_iotsitewise.types.search_type.SearchType"]
    """<p>The search strategy to use. Defaults to <code>QUICK</code> when omitted.</p>"""
    search_filters: NotRequired["capo_iotsitewise.types.search_filters.SearchFilters"]
    """<p>Optional filters that restrict the search to a subset of the workspace's data.</p>"""
    group_id: NotRequired["capo_iotsitewise.types.group_id.GroupId"]
    """<p>An optional caller-supplied identifier used to group related searches together.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSearchRequest) -> dict:
    out: dict = {}
    out["queryStatement"] = value["query_statement"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "search_type" in value:
        import capo_iotsitewise.types.search_type

        out["searchType"] = capo_iotsitewise.types.search_type.serialize_json(
            value["search_type"]
        )
    if "search_filters" in value:
        import capo_iotsitewise.types.search_filters

        out["searchFilters"] = capo_iotsitewise.types.search_filters.serialize_json(
            value["search_filters"]
        )
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> StartSearchRequest:
    out: StartSearchRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryStatement") is not None:
        out["query_statement"] = data["queryStatement"]
    else:
        raise DeserializationError("StartSearchRequest.query_statement required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("searchType") is not None:
        import capo_iotsitewise.types.search_type

        out["search_type"] = capo_iotsitewise.types.search_type.deserialize_json(
            data["searchType"]
        )
    if data.get("searchFilters") is not None:
        import capo_iotsitewise.types.search_filters

        out["search_filters"] = capo_iotsitewise.types.search_filters.deserialize_json(
            data["searchFilters"]
        )
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    return out


def redact_sensitive(value: StartSearchRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_statement" in value:
        out["query_statement"] = "*** Sensitive Data Redacted ***"
    return out
