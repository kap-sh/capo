"""Generated from Smithy shape ``com.amazonaws.securityagent#ListPrivateConnectionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.next_token
    import capo_securityagent.types.private_connection_list


class ListPrivateConnectionsOutput(TypedDict, closed=True):
    private_connections: (
        "capo_securityagent.types.private_connection_list.PrivateConnectionList"
    )
    """<p>The list of private connections.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results, if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivateConnectionsOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.private_connection_list

    out["privateConnections"] = (
        capo_securityagent.types.private_connection_list.serialize_json(
            value["private_connections"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrivateConnectionsOutput:
    out: ListPrivateConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("privateConnections") is not None:
        import capo_securityagent.types.private_connection_list

        out["private_connections"] = (
            capo_securityagent.types.private_connection_list.deserialize_json(
                data["privateConnections"]
            )
        )
    else:
        out["private_connections"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
