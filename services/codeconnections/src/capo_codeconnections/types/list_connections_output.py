"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListConnectionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.connection_list
    import capo_codeconnections.types.next_token


class ListConnectionsOutput(TypedDict, closed=True):
    connections: NotRequired[
        "capo_codeconnections.types.connection_list.ConnectionList"
    ]
    """<p>A list of connections and the details for each connection, such as status, owner, and provider type.</p>"""
    next_token: NotRequired["capo_codeconnections.types.next_token.NextToken"]
    """<p>A token that can be used in the next <code>ListConnections</code> call. To view all items in the list, continue to call this operation with each subsequent token until no more <code>nextToken</code> values are returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionsOutput) -> dict:
    out: dict = {}
    if "connections" in value:
        import capo_codeconnections.types.connection_list

        out["Connections"] = (
            capo_codeconnections.types.connection_list.serialize_aws_json_1_0(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionsOutput:
    out: ListConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Connections") is not None:
        import capo_codeconnections.types.connection_list

        out["connections"] = (
            capo_codeconnections.types.connection_list.deserialize_aws_json_1_0(
                data["Connections"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListConnectionsOutput) -> dict:
    out: dict = {}
    if "connections" in value:
        import capo_codeconnections.types.connection_list

        out["Connections"] = capo_codeconnections.types.connection_list.serialize_cbor(
            value["connections"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListConnectionsOutput:
    out: ListConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Connections") is not None:
        import capo_codeconnections.types.connection_list

        out["connections"] = (
            capo_codeconnections.types.connection_list.deserialize_cbor(
                data["Connections"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
