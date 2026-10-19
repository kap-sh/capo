"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateGatewayRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.authorizer_type
    import capo_bedrock_agentcore_control.types.custom_transform_configuration
    import capo_bedrock_agentcore_control.types.exception_level
    import capo_bedrock_agentcore_control.types.gateway_description
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_interceptor_configurations
    import capo_bedrock_agentcore_control.types.gateway_name
    import capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration
    import capo_bedrock_agentcore_control.types.gateway_protocol_configuration
    import capo_bedrock_agentcore_control.types.gateway_protocol_type
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.waf_configuration


class UpdateGatewayRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The identifier of the gateway to update.</p>"""
    name: "capo_bedrock_agentcore_control.types.gateway_name.GatewayName"
    """<p>The name of the gateway. This name must be the same as the one when the gateway was created.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
    ]
    """<p>The updated description for the gateway.</p>"""
    role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The updated IAM role ARN that provides permissions for the gateway.</p>"""
    protocol_type: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
    ]
    """<p>The updated protocol type for the gateway.</p>"""
    protocol_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
    ]
    authorizer_type: (
        "capo_bedrock_agentcore_control.types.authorizer_type.AuthorizerType"
    )
    """<p>The updated authorizer type for the gateway.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The updated authorizer configuration for the gateway.</p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The updated ARN of the KMS key used to encrypt the gateway.</p>"""
    custom_transform_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.custom_transform_configuration.CustomTransformConfiguration"
    ]
    """<p>The updated custom transformation configuration for the gateway. This configuration defines how the gateway transforms requests and responses.</p>"""
    interceptor_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
    ]
    """<p>The updated interceptor configurations for the gateway.</p>"""
    policy_engine_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
    ]
    """<p>The updated policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.</p>"""
    exception_level: NotRequired[
        "capo_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
    ]
    """<p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>"""
    waf_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.waf_configuration.WafConfiguration"
    ]
    """<p>The updated Amazon Web Services WAF configuration for the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["roleArn"] = value["role_arn"]
    if "protocol_type" in value:
        import capo_bedrock_agentcore_control.types.gateway_protocol_type

        out["protocolType"] = (
            capo_bedrock_agentcore_control.types.gateway_protocol_type.serialize_json(
                value["protocol_type"]
            )
        )
    if "protocol_configuration" in value:
        import capo_bedrock_agentcore_control.types.gateway_protocol_configuration

        out["protocolConfiguration"] = (
            capo_bedrock_agentcore_control.types.gateway_protocol_configuration.serialize_json(
                value["protocol_configuration"]
            )
        )
    import capo_bedrock_agentcore_control.types.authorizer_type

    out["authorizerType"] = (
        capo_bedrock_agentcore_control.types.authorizer_type.serialize_json(
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
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "custom_transform_configuration" in value:
        import capo_bedrock_agentcore_control.types.custom_transform_configuration

        out["customTransformConfiguration"] = (
            capo_bedrock_agentcore_control.types.custom_transform_configuration.serialize_json(
                value["custom_transform_configuration"]
            )
        )
    if "interceptor_configurations" in value:
        import capo_bedrock_agentcore_control.types.gateway_interceptor_configurations

        out["interceptorConfigurations"] = (
            capo_bedrock_agentcore_control.types.gateway_interceptor_configurations.serialize_json(
                value["interceptor_configurations"]
            )
        )
    if "policy_engine_configuration" in value:
        import capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration

        out["policyEngineConfiguration"] = (
            capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration.serialize_json(
                value["policy_engine_configuration"]
            )
        )
    if "exception_level" in value:
        import capo_bedrock_agentcore_control.types.exception_level

        out["exceptionLevel"] = (
            capo_bedrock_agentcore_control.types.exception_level.serialize_json(
                value["exception_level"]
            )
        )
    if "waf_configuration" in value:
        import capo_bedrock_agentcore_control.types.waf_configuration

        out["wafConfiguration"] = (
            capo_bedrock_agentcore_control.types.waf_configuration.serialize_json(
                value["waf_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGatewayRequest:
    out: UpdateGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateGatewayRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdateGatewayRequest.role_arn required")
    if data.get("protocolType") is not None:
        import capo_bedrock_agentcore_control.types.gateway_protocol_type

        out["protocol_type"] = (
            capo_bedrock_agentcore_control.types.gateway_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    if data.get("protocolConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.gateway_protocol_configuration

        out["protocol_configuration"] = (
            capo_bedrock_agentcore_control.types.gateway_protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    if data.get("authorizerType") is not None:
        import capo_bedrock_agentcore_control.types.authorizer_type

        out["authorizer_type"] = (
            capo_bedrock_agentcore_control.types.authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    else:
        raise DeserializationError("UpdateGatewayRequest.authorizer_type required")
    if data.get("authorizerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("customTransformConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.custom_transform_configuration

        out["custom_transform_configuration"] = (
            capo_bedrock_agentcore_control.types.custom_transform_configuration.deserialize_json(
                data["customTransformConfiguration"]
            )
        )
    if data.get("interceptorConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.gateway_interceptor_configurations

        out["interceptor_configurations"] = (
            capo_bedrock_agentcore_control.types.gateway_interceptor_configurations.deserialize_json(
                data["interceptorConfigurations"]
            )
        )
    if data.get("policyEngineConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration

        out["policy_engine_configuration"] = (
            capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration.deserialize_json(
                data["policyEngineConfiguration"]
            )
        )
    if data.get("exceptionLevel") is not None:
        import capo_bedrock_agentcore_control.types.exception_level

        out["exception_level"] = (
            capo_bedrock_agentcore_control.types.exception_level.deserialize_json(
                data["exceptionLevel"]
            )
        )
    if data.get("wafConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.waf_configuration

        out["waf_configuration"] = (
            capo_bedrock_agentcore_control.types.waf_configuration.deserialize_json(
                data["wafConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateGatewayRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "protocol_configuration" in value:
        import capo_bedrock_agentcore_control.types.gateway_protocol_configuration

        out["protocol_configuration"] = (
            capo_bedrock_agentcore_control.types.gateway_protocol_configuration.redact_sensitive(
                value["protocol_configuration"]
            )
        )
    return out
