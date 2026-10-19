"""Generated from Smithy shape ``com.amazonaws.apigateway#GetModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.string


class GetModelRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The RestApi identifier under which the Model exists.</p>"""
    model_name: "capo_api_gateway.types.string.String"
    """<p>The name of the model as an identifier.</p>"""
    flatten: NotRequired["capo_api_gateway.types.boolean.Boolean"]
    """<p>A query parameter of a Boolean value to resolve (<code>true</code>) all external model references and returns a flattened model schema or not (<code>false</code>) The default is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelRequest:
    out: GetModelRequest = {}  # type: ignore[typeddict-item]
    return out
