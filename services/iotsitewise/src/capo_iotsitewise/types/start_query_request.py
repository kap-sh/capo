"""Generated from Smithy shape ``com.amazonaws.iotsitewise#StartQueryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.query_string
    import capo_iotsitewise.types.workspace_name


class StartQueryRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace to query.</p>"""
    query_statement: "capo_iotsitewise.types.query_string.QueryString"
    """<p>The SQL query to execute against the workspace telemetry, annotations, data segment, and dataset data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["queryStatement"] = value["query_statement"]
    return out


def deserialize_json(data: dict) -> StartQueryRequest:
    out: StartQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("queryStatement") is not None:
        out["query_statement"] = data["queryStatement"]
    else:
        out["query_statement"] = ""
    return out


def redact_sensitive(value: StartQueryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_statement" in value:
        out["query_statement"] = "*** Sensitive Data Redacted ***"
    return out
