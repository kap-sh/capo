"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CreateApplicationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input
    import capo_migration_hub_refactor_spaces.types.application_name
    import capo_migration_hub_refactor_spaces.types.client_token
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.proxy_type
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.vpc_id


class CreateApplicationRequest(TypedDict, closed=True):
    name: "capo_migration_hub_refactor_spaces.types.application_name.ApplicationName"
    """<p>The name to use for the application. </p>"""
    environment_identifier: (
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The unique identifier of the environment.</p>"""
    vpc_id: "capo_migration_hub_refactor_spaces.types.vpc_id.VpcId"
    """<p>The ID of the virtual private cloud (VPC).</p>"""
    proxy_type: "capo_migration_hub_refactor_spaces.types.proxy_type.ProxyType"
    """<p>The proxy type of the proxy created within the application. </p>"""
    api_gateway_proxy: NotRequired[
        "capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input.ApiGatewayProxyInput"
    ]
    """<p>A wrapper object holding the API Gateway endpoint type and stage name for the proxy. </p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags to assign to the application. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.</p>"""
    client_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["VpcId"] = value["vpc_id"]
    out["ProxyType"] = value["proxy_type"]
    if "api_gateway_proxy" in value:
        import capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input

        out["ApiGatewayProxy"] = (
            capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input.serialize_json(
                value["api_gateway_proxy"]
            )
        )
    if "tags" in value:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError("CreateApplicationRequest.vpc_id required")
    if data.get("ProxyType") is not None:
        out["proxy_type"] = data["ProxyType"]
    else:
        raise DeserializationError("CreateApplicationRequest.proxy_type required")
    if data.get("ApiGatewayProxy") is not None:
        import capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input

        out["api_gateway_proxy"] = (
            capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input.deserialize_json(
                data["ApiGatewayProxy"]
            )
        )
    if data.get("Tags") is not None:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CreateApplicationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
