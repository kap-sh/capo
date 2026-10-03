"""Generated from Smithy shape ``com.amazonaws.apigateway#GetResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.string


class GetResourceRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    resource_id: "capo_api_gateway.types.string.String"
    """<p>The identifier for the Resource resource.</p>"""
    embed: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>A query parameter to retrieve the specified resources embedded in the returned Resource representation in the response. This <code>embed</code> parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the <code>"methods"</code> string. For example, <code>GET /restapis/{restapi_id}/resources/{resource_id}?embed=methods</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceRequest:
    out: GetResourceRequest = {}  # type: ignore[typeddict-item]
    return out
