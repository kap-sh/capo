"""Generated from Smithy shape ``com.amazonaws.directconnect#Connections``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_list
    import capo_direct_connect.types.pagination_token


class Connections(TypedDict, closed=True):
    connections: NotRequired["capo_direct_connect.types.connection_list.ConnectionList"]
    """<p>The connections.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connections) -> dict:
    out: dict = {}
    if "connections" in value:
        import capo_direct_connect.types.connection_list

        out["connections"] = (
            capo_direct_connect.types.connection_list.serialize_aws_json_1_1(
                value["connections"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Connections:
    out: Connections = {}  # type: ignore[typeddict-item]
    if data.get("connections") is not None:
        import capo_direct_connect.types.connection_list

        out["connections"] = (
            capo_direct_connect.types.connection_list.deserialize_aws_json_1_1(
                data["connections"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Connections) -> dict:
    out: dict = {}
    if "connections" in value:
        import capo_direct_connect.types.connection_list

        out["connections"] = capo_direct_connect.types.connection_list.serialize_cbor(
            value["connections"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> Connections:
    out: Connections = {}  # type: ignore[typeddict-item]
    if data.get("connections") is not None:
        import capo_direct_connect.types.connection_list

        out["connections"] = capo_direct_connect.types.connection_list.deserialize_cbor(
            data["connections"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
