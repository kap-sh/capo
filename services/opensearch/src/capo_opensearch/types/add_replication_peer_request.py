"""Generated from Smithy shape ``com.amazonaws.opensearch#AddReplicationPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.domain_name


class AddReplicationPeerRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    peer_domain_arn: "capo_opensearch.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the domain to replicate to. The peer must be in a different Region from the domain you are calling, and in the same AWS account.</p>"""
    dry_run: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>When <code>true</code>, validates the request and reports whether replication could be established, without changing either domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddReplicationPeerRequest) -> dict:
    out: dict = {}
    out["PeerDomainArn"] = value["peer_domain_arn"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_json(data: dict) -> AddReplicationPeerRequest:
    out: AddReplicationPeerRequest = {}  # type: ignore[typeddict-item]
    if data.get("PeerDomainArn") is not None:
        out["peer_domain_arn"] = data["PeerDomainArn"]
    else:
        out["peer_domain_arn"] = ""
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
