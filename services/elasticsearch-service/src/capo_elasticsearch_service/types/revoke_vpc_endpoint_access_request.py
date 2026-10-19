"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#RevokeVpcEndpointAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.aws_account
    import capo_elasticsearch_service.types.domain_name


class RevokeVpcEndpointAccessRequest(TypedDict, closed=True):
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the OpenSearch Service domain.</p>"""
    account: "capo_elasticsearch_service.types.aws_account.AWSAccount"
    """<p>The account ID to revoke access from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeVpcEndpointAccessRequest) -> dict:
    out: dict = {}
    out["Account"] = value["account"]
    return out


def deserialize_json(data: dict) -> RevokeVpcEndpointAccessRequest:
    out: RevokeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("Account") is not None:
        out["account"] = data["Account"]
    else:
        out["account"] = ""
    return out
