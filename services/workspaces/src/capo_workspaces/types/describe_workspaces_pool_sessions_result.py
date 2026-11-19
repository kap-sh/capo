"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolSessionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspaces_pool_sessions


class DescribeWorkspacesPoolSessionsResult(TypedDict, closed=True):
    sessions: NotRequired[
        "capo_workspaces.types.workspaces_pool_sessions.WorkspacesPoolSessions"
    ]
    """<p>Describes the pool sessions.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolSessionsResult) -> dict:
    out: dict = {}
    if "sessions" in value:
        import capo_workspaces.types.workspaces_pool_sessions

        out["Sessions"] = (
            capo_workspaces.types.workspaces_pool_sessions.serialize_aws_json_1_1(
                value["sessions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolSessionsResult:
    out: DescribeWorkspacesPoolSessionsResult = {}  # type: ignore[typeddict-item]
    if data.get("Sessions") is not None:
        import capo_workspaces.types.workspaces_pool_sessions

        out["sessions"] = (
            capo_workspaces.types.workspaces_pool_sessions.deserialize_aws_json_1_1(
                data["Sessions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspacesPoolSessionsResult) -> dict:
    out: dict = {}
    if "sessions" in value:
        import capo_workspaces.types.workspaces_pool_sessions

        out["Sessions"] = capo_workspaces.types.workspaces_pool_sessions.serialize_cbor(
            value["sessions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspacesPoolSessionsResult:
    out: DescribeWorkspacesPoolSessionsResult = {}  # type: ignore[typeddict-item]
    if data.get("Sessions") is not None:
        import capo_workspaces.types.workspaces_pool_sessions

        out["sessions"] = (
            capo_workspaces.types.workspaces_pool_sessions.deserialize_cbor(
                data["Sessions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
