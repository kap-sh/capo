"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListScopesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.scope_summary_list


class ListScopesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""
    scopes: "capo_network_security_manager.types.scope_summary_list.ScopeSummaryList"
    """<p>The list of scopes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScopesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_network_security_manager.types.scope_summary_list

    out["scopes"] = (
        capo_network_security_manager.types.scope_summary_list.serialize_json(
            value["scopes"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListScopesOutput:
    out: ListScopesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("scopes") is not None:
        import capo_network_security_manager.types.scope_summary_list

        out["scopes"] = (
            capo_network_security_manager.types.scope_summary_list.deserialize_json(
                data["scopes"]
            )
        )
    else:
        raise DeserializationError("ListScopesOutput.scopes required")
    return out
