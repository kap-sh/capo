"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.replication_peer_list
    import capo_opensearch.types.replication_role


class DescribeDomainReplicationResponse(TypedDict, closed=True):
    domain_arn: NotRequired["capo_opensearch.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the domain described.</p>"""
    role: NotRequired["capo_opensearch.types.replication_role.ReplicationRole"]
    """<p>The domain's role in the arrangement, either <code>PRIMARY</code> or <code>SECONDARY</code>. Absent when the domain is not replicating.</p>"""
    peers: NotRequired[
        "capo_opensearch.types.replication_peer_list.ReplicationPeerList"
    ]
    """<p>The domains that this domain replicates with. Each entry carries the state of that one relationship. Empty when the domain is not replicating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainReplicationResponse) -> dict:
    out: dict = {}
    if "domain_arn" in value:
        out["DomainArn"] = value["domain_arn"]
    if "role" in value:
        import capo_opensearch.types.replication_role

        out["Role"] = capo_opensearch.types.replication_role.serialize_json(
            value["role"]
        )
    if "peers" in value:
        import capo_opensearch.types.replication_peer_list

        out["Peers"] = capo_opensearch.types.replication_peer_list.serialize_json(
            value["peers"]
        )
    return out


def deserialize_json(data: dict) -> DescribeDomainReplicationResponse:
    out: DescribeDomainReplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainArn") is not None:
        out["domain_arn"] = data["DomainArn"]
    if data.get("Role") is not None:
        import capo_opensearch.types.replication_role

        out["role"] = capo_opensearch.types.replication_role.deserialize_json(
            data["Role"]
        )
    if data.get("Peers") is not None:
        import capo_opensearch.types.replication_peer_list

        out["peers"] = capo_opensearch.types.replication_peer_list.deserialize_json(
            data["Peers"]
        )
    return out
