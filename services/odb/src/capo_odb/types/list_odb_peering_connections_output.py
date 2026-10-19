"""Generated from Smithy shape ``com.amazonaws.odb#ListOdbPeeringConnectionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.odb_peering_connection_list


class ListOdbPeeringConnectionsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The pagination token for the next page of ODB peering connections.</p>"""
    odb_peering_connections: (
        "capo_odb.types.odb_peering_connection_list.OdbPeeringConnectionList"
    )
    """<p>The list of ODB peering connections.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOdbPeeringConnectionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.odb_peering_connection_list

    out["odbPeeringConnections"] = (
        capo_odb.types.odb_peering_connection_list.serialize_aws_json_1_0(
            value["odb_peering_connections"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOdbPeeringConnectionsOutput:
    out: ListOdbPeeringConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("odbPeeringConnections") is not None:
        import capo_odb.types.odb_peering_connection_list

        out["odb_peering_connections"] = (
            capo_odb.types.odb_peering_connection_list.deserialize_aws_json_1_0(
                data["odbPeeringConnections"]
            )
        )
    else:
        out["odb_peering_connections"] = []
    return out
