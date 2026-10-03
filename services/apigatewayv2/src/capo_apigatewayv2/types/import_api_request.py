"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ImportApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__boolean
    import capo_apigatewayv2.types.__string


class ImportApiRequest(TypedDict, closed=True):
    basepath: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html">Set the OpenAPI basePath Property</a>. Supported only for HTTP APIs.</p>"""
    body: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The OpenAPI definition. Supported only for HTTP APIs.</p>"""
    fail_on_warnings: NotRequired["capo_apigatewayv2.types.__boolean.__boolean"]
    """<p>Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportApiRequest) -> dict:
    out: dict = {}
    if "body" in value:
        out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> ImportApiRequest:
    out: ImportApiRequest = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        out["body"] = data["body"]
    return out
