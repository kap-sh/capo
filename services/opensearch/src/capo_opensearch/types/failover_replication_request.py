"""Generated from Smithy shape ``com.amazonaws.opensearch#FailoverReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.domain_name


class FailoverReplicationRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    peer_domain_arn: "capo_opensearch.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the relationship's current primary. The request is rejected if this domain is no longer the peer of the domain you are calling.</p>"""
    allow_data_loss: "capo_opensearch.types.boolean.Boolean"
    """<p>Acknowledges that writes which had not yet replicated are lost. You must set this to <code>true</code>; the request is rejected otherwise.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverReplicationRequest) -> dict:
    out: dict = {}
    out["PeerDomainArn"] = value["peer_domain_arn"]
    out["AllowDataLoss"] = value["allow_data_loss"]
    return out


def deserialize_json(data: dict) -> FailoverReplicationRequest:
    out: FailoverReplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("PeerDomainArn") is not None:
        out["peer_domain_arn"] = data["PeerDomainArn"]
    else:
        out["peer_domain_arn"] = ""
    if data.get("AllowDataLoss") is not None:
        out["allow_data_loss"] = data["AllowDataLoss"]
    else:
        out["allow_data_loss"] = False
    return out
