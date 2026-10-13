"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateGatewayResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.authorizer_type
    import capo_bedrock_agentcore_control.types.custom_transform_configuration
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.exception_level
    import capo_bedrock_agentcore_control.types.gateway_arn
    import capo_bedrock_agentcore_control.types.gateway_description
    import capo_bedrock_agentcore_control.types.gateway_id
    import capo_bedrock_agentcore_control.types.gateway_interceptor_configurations
    import capo_bedrock_agentcore_control.types.gateway_name
    import capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration
    import capo_bedrock_agentcore_control.types.gateway_protocol_configuration
    import capo_bedrock_agentcore_control.types.gateway_protocol_type
    import capo_bedrock_agentcore_control.types.gateway_status
    import capo_bedrock_agentcore_control.types.gateway_url
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.status_reasons
    import capo_bedrock_agentcore_control.types.waf_configuration
    import capo_bedrock_agentcore_control.types.web_acl_arn
    import capo_bedrock_agentcore_control.types.workload_identity_details


class CreateGatewayResponse(TypedDict, closed=True):
    gateway_arn: "capo_bedrock_agentcore_control.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the created gateway.</p>"""
    gateway_id: "capo_bedrock_agentcore_control.types.gateway_id.GatewayId"
    """<p>The unique identifier of the created gateway.</p>"""
    gateway_url: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_url.GatewayUrl"
    ]
    """<p>The URL endpoint for the created gateway.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway was last updated.</p>"""
    status: "capo_bedrock_agentcore_control.types.gateway_status.GatewayStatus"
    """<p>The current status of the gateway.</p>"""
    status_reasons: NotRequired[
        "capo_bedrock_agentcore_control.types.status_reasons.StatusReasons"
    ]
    """<p>The reasons for the current status of the gateway.</p>"""
    name: "capo_bedrock_agentcore_control.types.gateway_name.GatewayName"
    """<p>The name of the gateway.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
    ]
    """<p>The description of the gateway.</p>"""
    role_arn: NotRequired["capo_bedrock_agentcore_control.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the gateway.</p>"""
    protocol_type: (
        "capo_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
    )
    """<p>The protocol type of the gateway.</p>"""
    protocol_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
    ]
    """<p>The configuration settings for the protocol used by the gateway.</p>"""
    authorizer_type: (
        "capo_bedrock_agentcore_control.types.authorizer_type.AuthorizerType"
    )
    """<p>The type of authorizer used by the gateway.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the created gateway.</p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt data associated with the gateway.</p>"""
    custom_transform_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.custom_transform_configuration.CustomTransformConfiguration"
    ]
    """<p>The custom transformation configuration for the gateway. This configuration defines how the gateway transforms requests and responses.</p>"""
    interceptor_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
    ]
    """<p>The list of interceptor configurations for the created gateway.</p>"""
    policy_engine_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
    ]
    """<p>The policy engine configuration for the created gateway.</p>"""
    workload_identity_details: NotRequired[
        "capo_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]
    """<p>The workload identity details for the created gateway.</p>"""
    exception_level: NotRequired[
        "capo_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
    ]
    """<p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>"""
    web_acl_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.web_acl_arn.WebAclArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services WAF web ACL associated with the gateway.</p>"""
    waf_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.waf_configuration.WafConfiguration"
    ]
    """<p>The Amazon Web Services WAF configuration for the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayArn"] = value["gateway_arn"]
    out["gatewayId"] = value["gateway_id"]
    if "gateway_url" in value:
        out["gatewayUrl"] = value["gateway_url"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.gateway_status

    out["status"] = capo_bedrock_agentcore_control.types.gateway_status.serialize_json(
        value["status"]
    )
    if "status_reasons" in value:
        import capo_bedrock_agentcore_control.types.status_reasons

        out["statusReasons"] = (
            capo_bedrock_agentcore_control.types.status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    import capo_bedrock_agentcore_control.types.gateway_protocol_type

    out["protocolType"] = (
        capo_bedrock_agentcore_control.types.gateway_protocol_type.serialize_json(
            value.get("protocol_type", "MCP")
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
    if "workload_identity_details" in value:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workloadIdentityDetails"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.serialize_json(
                value["workload_identity_details"]
            )
        )
    if "exception_level" in value:
        import capo_bedrock_agentcore_control.types.exception_level

        out["exceptionLevel"] = (
            capo_bedrock_agentcore_control.types.exception_level.serialize_json(
                value["exception_level"]
            )
        )
    if "web_acl_arn" in value:
        out["webAclArn"] = value["web_acl_arn"]
    if "waf_configuration" in value:
        import capo_bedrock_agentcore_control.types.waf_configuration

        out["wafConfiguration"] = (
            capo_bedrock_agentcore_control.types.waf_configuration.serialize_json(
                value["waf_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGatewayResponse:
    out: CreateGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("CreateGatewayResponse.gateway_arn required")
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("CreateGatewayResponse.gateway_id required")
    if data.get("gatewayUrl") is not None:
        out["gateway_url"] = data["gatewayUrl"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayResponse.updated_at required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.gateway_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.gateway_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayResponse.status required")
    if data.get("statusReasons") is not None:
        import capo_bedrock_agentcore_control.types.status_reasons

        out["status_reasons"] = (
            capo_bedrock_agentcore_control.types.status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGatewayResponse.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("protocolType") is not None:
        import capo_bedrock_agentcore_control.types.gateway_protocol_type

        out["protocol_type"] = (
            capo_bedrock_agentcore_control.types.gateway_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    else:
        out["protocol_type"] = "MCP"
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
        raise DeserializationError("CreateGatewayResponse.authorizer_type required")
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
    if data.get("workloadIdentityDetails") is not None:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workload_identity_details"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    if data.get("exceptionLevel") is not None:
        import capo_bedrock_agentcore_control.types.exception_level

        out["exception_level"] = (
            capo_bedrock_agentcore_control.types.exception_level.deserialize_json(
                data["exceptionLevel"]
            )
        )
    if data.get("webAclArn") is not None:
        out["web_acl_arn"] = data["webAclArn"]
    if data.get("wafConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.waf_configuration

        out["waf_configuration"] = (
            capo_bedrock_agentcore_control.types.waf_configuration.deserialize_json(
                data["wafConfiguration"]
            )
        )
    return out


def redact_sensitive(value: CreateGatewayResponse) -> dict[str, Any]:
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
