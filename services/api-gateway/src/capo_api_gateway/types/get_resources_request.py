"""Generated from Smithy shape ``com.amazonaws.apigateway#GetResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.string


class GetResourcesRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set.</p>"""
    limit: NotRequired["capo_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500.</p>"""
    embed: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>A query parameter used to retrieve the specified resources embedded in the returned Resources resource in the response. This <code>embed</code> parameter value is a list of comma-separated strings. Currently, the request supports only retrieval of the embedded Method resources this way. The query parameter value must be a single-valued list and contain the <code>"methods"</code> string. For example, <code>GET /restapis/{restapi_id}/resources?embed=methods</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcesRequest:
    out: GetResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
