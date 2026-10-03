"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ApiGatewayProxyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.api_gateway_endpoint_type
    import capo_migration_hub_refactor_spaces.types.stage_name


class ApiGatewayProxyInput(TypedDict, closed=True):
    endpoint_type: NotRequired[
        "capo_migration_hub_refactor_spaces.types.api_gateway_endpoint_type.ApiGatewayEndpointType"
    ]
    """<p>The type of endpoint to use for the API Gateway proxy. If no value is specified in the request, the value is set to <code>REGIONAL</code> by default.</p> <p>If the value is set to <code>PRIVATE</code> in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud (Amazon VPC) interface endpoints for the Amazon API Gateway that has been granted access. For more information about creating a private connection with Refactor Spaces and interface endpoint (Amazon Web Services PrivateLink) availability, see <a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/vpc-interface-endpoints.html">Access Refactor Spaces using an interface endpoint (Amazon Web Services PrivateLink)</a>.</p>"""
    stage_name: NotRequired[
        "capo_migration_hub_refactor_spaces.types.stage_name.StageName"
    ]
    """<p>The name of the API Gateway stage. The name defaults to <code>prod</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiGatewayProxyInput) -> dict:
    out: dict = {}
    if "endpoint_type" in value:
        out["EndpointType"] = value["endpoint_type"]
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    return out


def deserialize_json(data: dict) -> ApiGatewayProxyInput:
    out: ApiGatewayProxyInput = {}  # type: ignore[typeddict-item]
    if data.get("EndpointType") is not None:
        out["endpoint_type"] = data["EndpointType"]
    if data.get("StageName") is not None:
        out["stage_name"] = data["StageName"]
    return out
