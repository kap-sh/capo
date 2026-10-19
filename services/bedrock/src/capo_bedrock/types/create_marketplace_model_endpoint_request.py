"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.accept_eula
    import capo_bedrock.types.endpoint_config
    import capo_bedrock.types.endpoint_name
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.model_source_identifier
    import capo_bedrock.types.tag_list


class CreateMarketplaceModelEndpointRequest(TypedDict, closed=True):
    model_source_identifier: (
        "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier"
    )
    """<p>The ARN of the model from Amazon Bedrock Marketplace that you want to deploy to the endpoint.</p>"""
    endpoint_config: "capo_bedrock.types.endpoint_config.EndpointConfig"
    """<p>The configuration for the endpoint, including the number and type of instances to use.</p>"""
    accept_eula: NotRequired["capo_bedrock.types.accept_eula.AcceptEula"]
    """<p>Indicates whether you accept the end-user license agreement (EULA) for the model. Set to <code>true</code> to accept the EULA.</p>"""
    endpoint_name: "capo_bedrock.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint. This name must be unique within your Amazon Web Services account and region.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>"""
    tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply to the underlying Amazon SageMaker endpoint. You can use these tags to organize and identify your Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    out["modelSourceIdentifier"] = value["model_source_identifier"]
    import capo_bedrock.types.endpoint_config

    out["endpointConfig"] = capo_bedrock.types.endpoint_config.serialize_json(
        value["endpoint_config"]
    )
    if "accept_eula" in value:
        out["acceptEula"] = value["accept_eula"]
    out["endpointName"] = value["endpoint_name"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMarketplaceModelEndpointRequest:
    out: CreateMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelSourceIdentifier") is not None:
        out["model_source_identifier"] = data["modelSourceIdentifier"]
    else:
        out["model_source_identifier"] = ""
    if data.get("endpointConfig") is not None:
        import capo_bedrock.types.endpoint_config

        out["endpoint_config"] = capo_bedrock.types.endpoint_config.deserialize_json(
            data["endpointConfig"]
        )
    else:
        import capo_bedrock.types._unknown

        out["endpoint_config"] = capo_bedrock.types._unknown.UnknownUnionMember("")
    if data.get("acceptEula") is not None:
        out["accept_eula"] = data["acceptEula"]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        out["endpoint_name"] = ""
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("tags") is not None:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out
