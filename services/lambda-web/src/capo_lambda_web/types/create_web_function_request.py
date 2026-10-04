"""Generated from Smithy shape ``com.amazonaws.lambdaweb#CreateWebFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.endpoint_config
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.revision_config
    import capo_lambda_web.types.tags


class CreateWebFunctionRequest(TypedDict, closed=True):
    function_name: "capo_lambda_web.types.function_name.FunctionName"
    """<p>The name of the web function. The name can contain letters, numbers, hyphens (-), and underscores (_), and can't begin or end with a hyphen or an underscore. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    revision_config: NotRequired["capo_lambda_web.types.revision_config.RevisionConfig"]
    """<p>The configuration for the initial revision of the web function, including code and service settings.</p>"""
    endpoint_config: NotRequired["capo_lambda_web.types.endpoint_config.EndpointConfig"]
    """<p>The configuration for the initial endpoint of the web function.</p>"""
    tags: NotRequired["capo_lambda_web.types.tags.Tags"]
    """<p>A map of tag keys and values to apply to the web function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebFunctionRequest) -> dict:
    out: dict = {}
    out["functionName"] = value["function_name"]
    if "revision_config" in value:
        import capo_lambda_web.types.revision_config

        out["revisionConfig"] = capo_lambda_web.types.revision_config.serialize_json(
            value["revision_config"]
        )
    if "endpoint_config" in value:
        import capo_lambda_web.types.endpoint_config

        out["endpointConfig"] = capo_lambda_web.types.endpoint_config.serialize_json(
            value["endpoint_config"]
        )
    if "tags" in value:
        import capo_lambda_web.types.tags

        out["tags"] = capo_lambda_web.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWebFunctionRequest:
    out: CreateWebFunctionRequest = {}  # type: ignore[typeddict-item]
    if data.get("functionName") is not None:
        out["function_name"] = data["functionName"]
    else:
        raise DeserializationError("CreateWebFunctionRequest.function_name required")
    if data.get("revisionConfig") is not None:
        import capo_lambda_web.types.revision_config

        out["revision_config"] = capo_lambda_web.types.revision_config.deserialize_json(
            data["revisionConfig"]
        )
    if data.get("endpointConfig") is not None:
        import capo_lambda_web.types.endpoint_config

        out["endpoint_config"] = capo_lambda_web.types.endpoint_config.deserialize_json(
            data["endpointConfig"]
        )
    if data.get("tags") is not None:
        import capo_lambda_web.types.tags

        out["tags"] = capo_lambda_web.types.tags.deserialize_json(data["tags"])
    return out
