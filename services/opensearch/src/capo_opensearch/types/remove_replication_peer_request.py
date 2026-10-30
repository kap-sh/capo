"""Generated from Smithy shape ``com.amazonaws.opensearch#RemoveReplicationPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.domain_name


class RemoveReplicationPeerRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    peer_domain_arn: "capo_opensearch.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the peer to stop replicating with. Both domains are named so that the request identifies exactly one replication relationship.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveReplicationPeerRequest) -> dict:
    out: dict = {}
    out["PeerDomainArn"] = value["peer_domain_arn"]
    return out


def deserialize_json(data: dict) -> RemoveReplicationPeerRequest:
    out: RemoveReplicationPeerRequest = {}  # type: ignore[typeddict-item]
    if data.get("PeerDomainArn") is not None:
        out["peer_domain_arn"] = data["PeerDomainArn"]
    else:
        out["peer_domain_arn"] = ""
    return out
