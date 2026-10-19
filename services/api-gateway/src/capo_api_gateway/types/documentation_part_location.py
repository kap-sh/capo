"""Generated from Smithy shape ``com.amazonaws.apigateway#DocumentationPartLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.documentation_part_location_status_code
    import capo_api_gateway.types.documentation_part_type
    import capo_api_gateway.types.string


class DocumentationPartLocation(TypedDict, closed=True):
    type: "capo_api_gateway.types.documentation_part_type.DocumentationPartType"
    """<p>The type of API entity to which the documentation content applies. Valid values are <code>API</code>, <code>AUTHORIZER</code>, <code>MODEL</code>, <code>RESOURCE</code>, <code>METHOD</code>, <code>PATH_PARAMETER</code>, <code>QUERY_PARAMETER</code>, <code>REQUEST_HEADER</code>, <code>REQUEST_BODY</code>, <code>RESPONSE</code>, <code>RESPONSE_HEADER</code>, and <code>RESPONSE_BODY</code>. Content inheritance does not apply to any entity of the <code>API</code>, <code>AUTHORIZER</code>, <code>METHOD</code>, <code>MODEL</code>, <code>REQUEST_BODY</code>, or <code>RESOURCE</code> type.</p>"""
    path: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The URL path of the target. It is a valid field for the API entity types of <code>RESOURCE</code>, <code>METHOD</code>, <code>PATH_PARAMETER</code>, <code>QUERY_PARAMETER</code>, <code>REQUEST_HEADER</code>, <code>REQUEST_BODY</code>, <code>RESPONSE</code>, <code>RESPONSE_HEADER</code>, and <code>RESPONSE_BODY</code>. The default value is <code>/</code> for the root resource. When an applicable child entity inherits the content of another entity of the same type with more general specifications of the other <code>location</code> attributes, the child entity's <code>path</code> attribute must match that of the parent entity as a prefix.</p>"""
    method: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The HTTP verb of a method. It is a valid field for the API entity types of <code>METHOD</code>, <code>PATH_PARAMETER</code>, <code>QUERY_PARAMETER</code>, <code>REQUEST_HEADER</code>, <code>REQUEST_BODY</code>, <code>RESPONSE</code>, <code>RESPONSE_HEADER</code>, and <code>RESPONSE_BODY</code>. The default value is <code>*</code> for any method. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other <code>location</code> attributes, the child entity's <code>method</code> attribute must match that of the parent entity exactly.</p>"""
    status_code: NotRequired[
        "capo_api_gateway.types.documentation_part_location_status_code.DocumentationPartLocationStatusCode"
    ]
    """<p>The HTTP status code of a response. It is a valid field for the API entity types of <code>RESPONSE</code>, <code>RESPONSE_HEADER</code>, and <code>RESPONSE_BODY</code>. The default value is <code>*</code> for any status code. When an applicable child entity inherits the content of an entity of the same type with more general specifications of the other <code>location</code> attributes, the child entity's <code>statusCode</code> attribute must match that of the parent entity exactly.</p>"""
    name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of the targeted API entity. It is a valid and required field for the API entity types of <code>AUTHORIZER</code>, <code>MODEL</code>, <code>PATH_PARAMETER</code>, <code>QUERY_PARAMETER</code>, <code>REQUEST_HEADER</code>, <code>REQUEST_BODY</code> and <code>RESPONSE_HEADER</code>. It is an invalid field for any other entity type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentationPartLocation) -> dict:
    out: dict = {}
    import capo_api_gateway.types.documentation_part_type

    out["type"] = capo_api_gateway.types.documentation_part_type.serialize_json(
        value["type"]
    )
    if "path" in value:
        out["path"] = value["path"]
    if "method" in value:
        out["method"] = value["method"]
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DocumentationPartLocation:
    out: DocumentationPartLocation = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_api_gateway.types.documentation_part_type

        out["type"] = capo_api_gateway.types.documentation_part_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_api_gateway.types.documentation_part_type.DocumentationPartType", ""
        )
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("method") is not None:
        out["method"] = data["method"]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
