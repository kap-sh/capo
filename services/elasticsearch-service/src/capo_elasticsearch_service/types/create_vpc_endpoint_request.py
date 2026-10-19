"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CreateVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.client_token
    import capo_elasticsearch_service.types.domain_arn
    import capo_elasticsearch_service.types.vpc_options


class CreateVpcEndpointRequest(TypedDict, closed=True):
    domain_arn: "capo_elasticsearch_service.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the domain to grant access to.</p>"""
    vpc_options: "capo_elasticsearch_service.types.vpc_options.VPCOptions"
    """<p>Options to specify the subnets and security groups for the endpoint.</p>"""
    client_token: NotRequired[
        "capo_elasticsearch_service.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcEndpointRequest) -> dict:
    out: dict = {}
    out["DomainArn"] = value["domain_arn"]
    import capo_elasticsearch_service.types.vpc_options

    out["VpcOptions"] = capo_elasticsearch_service.types.vpc_options.serialize_json(
        value["vpc_options"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateVpcEndpointRequest:
    out: CreateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainArn") is not None:
        out["domain_arn"] = data["DomainArn"]
    else:
        out["domain_arn"] = ""
    if data.get("VpcOptions") is not None:
        import capo_elasticsearch_service.types.vpc_options

        out["vpc_options"] = (
            capo_elasticsearch_service.types.vpc_options.deserialize_json(
                data["VpcOptions"]
            )
        )
    else:
        raise DeserializationError("CreateVpcEndpointRequest.vpc_options required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
