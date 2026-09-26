"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListScopeSnapshotsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.scope_summary_list


class ListScopeSnapshotsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""
    snapshots: "capo_network_security_manager.types.scope_summary_list.ScopeSummaryList"
    """<p>The snapshots of the scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScopeSnapshotsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_network_security_manager.types.scope_summary_list

    out["snapshots"] = (
        capo_network_security_manager.types.scope_summary_list.serialize_json(
            value["snapshots"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListScopeSnapshotsOutput:
    out: ListScopeSnapshotsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("snapshots") is not None:
        import capo_network_security_manager.types.scope_summary_list

        out["snapshots"] = (
            capo_network_security_manager.types.scope_summary_list.deserialize_json(
                data["snapshots"]
            )
        )
    else:
        raise DeserializationError("ListScopeSnapshotsOutput.snapshots required")
    return out
