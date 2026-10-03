"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateRegistryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.approval_configuration
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.registry_authorizer_type
    import capo_bedrock_agentcore_control.types.registry_name


class CreateRegistryRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.registry_name.RegistryName"
    """<p>The name of the registry. The name must be unique within your account and can contain alphanumeric characters and underscores.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>A description of the registry.</p>"""
    authorizer_type: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"
    ]
    """<p>The type of authorizer to use for the registry. This controls the authorization method for the Search and Invoke APIs used by consumers, and does not affect the standard CRUDL APIs for registry and registry record management used by administrators.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the registry. Required if <code>authorizerType</code> is <code>CUSTOM_JWT</code>. For details, see the <code>AuthorizerConfiguration</code> data type.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    approval_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.approval_configuration.ApprovalConfiguration"
    ]
    """<p>The approval configuration for registry records. Controls whether records require explicit approval before becoming active. See the <code>ApprovalConfiguration</code> data type for supported configuration options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "authorizer_type" in value:
        import capo_bedrock_agentcore_control.types.registry_authorizer_type

        out["authorizerType"] = (
            capo_bedrock_agentcore_control.types.registry_authorizer_type.serialize_json(
                value["authorizer_type"]
            )
        )
    if "authorizer_configuration" in value:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "approval_configuration" in value:
        import capo_bedrock_agentcore_control.types.approval_configuration

        out["approvalConfiguration"] = (
            capo_bedrock_agentcore_control.types.approval_configuration.serialize_json(
                value["approval_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRegistryRequest:
    out: CreateRegistryRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRegistryRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("authorizerType") is not None:
        import capo_bedrock_agentcore_control.types.registry_authorizer_type

        out["authorizer_type"] = (
            capo_bedrock_agentcore_control.types.registry_authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    if data.get("authorizerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("approvalConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.approval_configuration

        out["approval_configuration"] = (
            capo_bedrock_agentcore_control.types.approval_configuration.deserialize_json(
                data["approvalConfiguration"]
            )
        )
    return out
