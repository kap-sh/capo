"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateBasePathMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class CreateBasePathMappingRequest(TypedDict, closed=True):
    domain_name: "capo_api_gateway.types.string.String"
    """<p>The domain name of the BasePathMapping resource to create.</p>"""
    domain_name_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The identifier for the domain name resource. Required for private custom domain names.</p>"""
    base_path: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do not want callers to specify a base path name after the domain name.</p>"""
    rest_api_id: "capo_api_gateway.types.string.String"
    """<p>The string identifier of the associated RestApi.</p>"""
    stage: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of the API's stage that you want to use for this mapping. Specify '(none)' if you want callers to explicitly specify the stage name after any base path name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBasePathMappingRequest) -> dict:
    out: dict = {}
    if "base_path" in value:
        out["basePath"] = value["base_path"]
    out["restApiId"] = value["rest_api_id"]
    if "stage" in value:
        out["stage"] = value["stage"]
    return out


def deserialize_json(data: dict) -> CreateBasePathMappingRequest:
    out: CreateBasePathMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("basePath") is not None:
        out["base_path"] = data["basePath"]
    if data.get("restApiId") is not None:
        out["rest_api_id"] = data["restApiId"]
    else:
        out["rest_api_id"] = ""
    if data.get("stage") is not None:
        out["stage"] = data["stage"]
    return out
