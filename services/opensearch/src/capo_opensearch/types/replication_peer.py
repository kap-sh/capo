"""Generated from Smithy shape ``com.amazonaws.opensearch#ReplicationPeer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.replication_role
    import capo_opensearch.types.replication_status
    import capo_opensearch.types.replication_status_message


class ReplicationPeer(TypedDict, closed=True):
    peer_domain_arn: NotRequired["capo_opensearch.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the peer domain.</p>"""
    peer_role: NotRequired["capo_opensearch.types.replication_role.ReplicationRole"]
    """<p>The peer's role in the relationship, either <code>PRIMARY</code> or <code>SECONDARY</code>.</p>"""
    status: NotRequired["capo_opensearch.types.replication_status.ReplicationStatus"]
    """<p>The state of the relationship:</p> <ul> <li> <p> <code>PENDING_SETUP</code> - replication is being established.</p> </li> <li> <p> <code>ACTIVE</code> - replication is running.</p> </li> <li> <p> <code>SWITCHING_OVER</code> - a planned promotion is in progress.</p> </li> <li> <p> <code>FAILING_OVER</code> - an unplanned promotion is in progress.</p> </li> <li> <p> <code>PENDING_REMOVAL</code> - replication is being stopped.</p> </li> <li> <p> <code>DETACHED</code> - the relationship has ended.</p> </li> <li> <p> <code>EJECTED</code> - a failover promoted the other domain. The former primary keeps the data it had when it was ejected and stays read-only until you remove the peer, or discard that data and pair again.</p> </li> <li> <p> <code>FAILED</code> - setup or teardown could not complete. You can still remove the relationship.</p> </li> </ul> <p>A relationship that is removed successfully no longer appears in <code>Peers</code>.</p>"""
    status_message: NotRequired[
        "capo_opensearch.types.replication_status_message.ReplicationStatusMessage"
    ]
    """<p>An explanation of why the relationship is in its current state, when more detail is available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationPeer) -> dict:
    out: dict = {}
    if "peer_domain_arn" in value:
        out["PeerDomainArn"] = value["peer_domain_arn"]
    if "peer_role" in value:
        import capo_opensearch.types.replication_role

        out["PeerRole"] = capo_opensearch.types.replication_role.serialize_json(
            value["peer_role"]
        )
    if "status" in value:
        import capo_opensearch.types.replication_status

        out["Status"] = capo_opensearch.types.replication_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ReplicationPeer:
    out: ReplicationPeer = {}  # type: ignore[typeddict-item]
    if data.get("PeerDomainArn") is not None:
        out["peer_domain_arn"] = data["PeerDomainArn"]
    if data.get("PeerRole") is not None:
        import capo_opensearch.types.replication_role

        out["peer_role"] = capo_opensearch.types.replication_role.deserialize_json(
            data["PeerRole"]
        )
    if data.get("Status") is not None:
        import capo_opensearch.types.replication_status

        out["status"] = capo_opensearch.types.replication_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
