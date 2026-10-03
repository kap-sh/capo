"""Generated from Smithy shape ``com.amazonaws.apigateway#PutRestApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_api_gateway.types.blob
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.put_mode
    import capo_api_gateway.types.string


class PutRestApiRequest(TypedDict, closed=True):
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    mode: NotRequired["capo_api_gateway.types.put_mode.PutMode"]
    """<p>The <code>mode</code> query parameter to specify the update mode. Valid values are "merge" and "overwrite". By default, the update mode is "merge".</p>"""
    fail_on_warnings: "capo_api_gateway.types.boolean.Boolean"
    """<p>A query parameter to indicate whether to rollback the API update (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.</p>"""
    parameters: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set <code>ignore=documentation</code> as a <code>parameters</code> value, as in the AWS CLI command of <code>aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json'</code>.</p>"""
    body: "capo_api_gateway.types.blob.Blob"
    """<p>The PUT request body containing external API definitions. Currently, only OpenAPI definition JSON/YAML files are supported. The maximum size of the API definition file is 6MB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRestApiRequest) -> dict:
    out: dict = {}
    import capo_api_gateway.types.blob

    out["body"] = capo_api_gateway.types.blob.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> PutRestApiRequest:
    out: PutRestApiRequest = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_api_gateway.types.blob

        out["body"] = capo_api_gateway.types.blob.deserialize_json(data["body"])
    else:
        raise DeserializationError("PutRestApiRequest.body required")
    return out
