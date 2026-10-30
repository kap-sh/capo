"""Generated from Smithy shape ``com.amazonaws.opensearch#SwitchoverReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.domain_name


class SwitchoverReplicationRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    peer_domain_arn: "capo_opensearch.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the relationship's current primary. The request is rejected if this domain is no longer the peer of the domain you are calling.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SwitchoverReplicationRequest) -> dict:
    out: dict = {}
    out["PeerDomainArn"] = value["peer_domain_arn"]
    return out


def deserialize_json(data: dict) -> SwitchoverReplicationRequest:
    out: SwitchoverReplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("PeerDomainArn") is not None:
        out["peer_domain_arn"] = data["PeerDomainArn"]
    else:
        out["peer_domain_arn"] = ""
    return out
