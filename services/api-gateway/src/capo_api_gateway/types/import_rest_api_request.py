"""Generated from Smithy shape ``com.amazonaws.apigateway#ImportRestApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_api_gateway.types.blob
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.map_of_string_to_string


class ImportRestApiRequest(TypedDict, closed=True):
    fail_on_warnings: NotRequired["capo_api_gateway.types.boolean.Boolean"]
    """<p>A query parameter to indicate whether to rollback the API creation (<code>true</code>) or not (<code>false</code>) when a warning is encountered. The default value is <code>false</code>.</p>"""
    parameters: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>A key-value map of context-specific query string parameters specifying the behavior of different API importing operations. The following shows operation-specific parameters and their supported values.</p> <p> To exclude DocumentationParts from the import, set <code>parameters</code> as <code>ignore=documentation</code>.</p> <p> To configure the endpoint type, set <code>parameters</code> as <code>endpointConfigurationTypes=EDGE</code>, <code>endpointConfigurationTypes=REGIONAL</code>, or <code>endpointConfigurationTypes=PRIVATE</code>. The default endpoint type is <code>EDGE</code>.</p> <p> To handle imported <code>basepath</code>, set <code>parameters</code> as <code>basepath=ignore</code>, <code>basepath=prepend</code> or <code>basepath=split</code>.</p>"""
    body: "capo_api_gateway.types.blob.Blob"
    """<p>The POST request body containing external API definitions. Currently, only OpenAPI definition JSON/YAML files are supported. The maximum size of the API definition file is 6MB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportRestApiRequest) -> dict:
    out: dict = {}
    import capo_api_gateway.types.blob

    out["body"] = capo_api_gateway.types.blob.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> ImportRestApiRequest:
    out: ImportRestApiRequest = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_api_gateway.types.blob

        out["body"] = capo_api_gateway.types.blob.deserialize_json(data["body"])
    else:
        raise DeserializationError("ImportRestApiRequest.body required")
    return out
