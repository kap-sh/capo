"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateMarketplaceModelEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.arn
    import capo_bedrock.types.endpoint_config
    import capo_bedrock.types.idempotency_token


class UpdateMarketplaceModelEndpointRequest(TypedDict, closed=True):
    endpoint_arn: "capo_bedrock.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the endpoint you want to update.</p>"""
    endpoint_config: "capo_bedrock.types.endpoint_config.EndpointConfig"
    """<p>The new configuration for the endpoint, including the number and type of instances to use.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMarketplaceModelEndpointRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.endpoint_config

    out["endpointConfig"] = capo_bedrock.types.endpoint_config.serialize_json(
        value["endpoint_config"]
    )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpdateMarketplaceModelEndpointRequest:
    out: UpdateMarketplaceModelEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("endpointConfig") is not None:
        import capo_bedrock.types.endpoint_config

        out["endpoint_config"] = capo_bedrock.types.endpoint_config.deserialize_json(
            data["endpointConfig"]
        )
    else:
        import capo_bedrock.types._unknown

        out["endpoint_config"] = capo_bedrock.types._unknown.UnknownUnionMember("")
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
