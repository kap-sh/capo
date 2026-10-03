"""Generated from Smithy shape ``com.amazonaws.apigateway#GetDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.string


class GetDeploymentRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    deployment_id: "capo_api_gateway.types.string.String"
    """<p>The identifier of the Deployment resource to get information about.</p>"""
    embed: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>A query parameter to retrieve the specified embedded resources of the returned Deployment resource in the response. In a REST API call, this <code>embed</code> parameter value is a list of comma-separated strings, as in <code>GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=var1,var2</code>. The SDK and other platform-dependent libraries might use a different format for the list. Currently, this request supports only retrieval of the embedded API summary this way. Hence, the parameter value must be a single-valued list containing only the <code>"apisummary"</code> string. For example, <code>GET /restapis/{restapi_id}/deployments/{deployment_id}?embed=apisummary</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeploymentRequest:
    out: GetDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
