"""Generated from Smithy shape ``com.amazonaws.odb#OdbPeeringConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.peered_cidr_list
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_status


class OdbPeeringConnection(TypedDict, closed=True):
    odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB peering connection. A sample ID is <code>odbpcx-abcdefgh12345678</code>.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the ODB peering connection.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The status of the ODB peering connection.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the ODB peering connection.</p>"""
    odb_peering_connection_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the ODB peering connection.</p> <p>Example: <code>arn:aws:odb:us-east-1:123456789012:odb-peering-connection/odbpcx-abcdefgh12345678</code> </p>"""
    odb_network_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the ODB network that initiated the peering connection.</p>"""
    peer_network_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the peer network.</p>"""
    odb_peering_connection_type: NotRequired["str"]
    """<p>The type of the ODB peering connection.</p> <p>Valid Values: <code>ODB-VPC | ODB-ODB</code> </p>"""
    peer_network_cidrs: NotRequired["capo_odb.types.peered_cidr_list.PeeredCidrList"]
    """<p>The CIDR blocks associated with the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the ODB peering connection was created.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The percentage progress of the ODB peering connection creation or deletion.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OdbPeeringConnection) -> dict:
    out: dict = {}
    out["odbPeeringConnectionId"] = value["odb_peering_connection_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "odb_peering_connection_arn" in value:
        out["odbPeeringConnectionArn"] = value["odb_peering_connection_arn"]
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
    if "peer_network_arn" in value:
        out["peerNetworkArn"] = value["peer_network_arn"]
    if "odb_peering_connection_type" in value:
        out["odbPeeringConnectionType"] = value["odb_peering_connection_type"]
    if "peer_network_cidrs" in value:
        import capo_odb.types.peered_cidr_list

        out["peerNetworkCidrs"] = (
            capo_odb.types.peered_cidr_list.serialize_aws_json_1_0(
                value["peer_network_cidrs"]
            )
        )
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "percent_progress" in value:
        out["percentProgress"] = (
            "NaN"
            if value["percent_progress"] != value["percent_progress"]
            else "Infinity"
            if value["percent_progress"] == float("inf")
            else "-Infinity"
            if value["percent_progress"] == float("-inf")
            else value["percent_progress"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OdbPeeringConnection:
    out: OdbPeeringConnection = {}  # type: ignore[typeddict-item]
    if data.get("odbPeeringConnectionId") is not None:
        out["odb_peering_connection_id"] = data["odbPeeringConnectionId"]
    else:
        out["odb_peering_connection_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("odbPeeringConnectionArn") is not None:
        out["odb_peering_connection_arn"] = data["odbPeeringConnectionArn"]
    if data.get("odbNetworkArn") is not None:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if data.get("peerNetworkArn") is not None:
        out["peer_network_arn"] = data["peerNetworkArn"]
    if data.get("odbPeeringConnectionType") is not None:
        out["odb_peering_connection_type"] = data["odbPeeringConnectionType"]
    if data.get("peerNetworkCidrs") is not None:
        import capo_odb.types.peered_cidr_list

        out["peer_network_cidrs"] = (
            capo_odb.types.peered_cidr_list.deserialize_aws_json_1_0(
                data["peerNetworkCidrs"]
            )
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("percentProgress") is not None:
        out["percent_progress"] = float(data["percentProgress"])
    return out
