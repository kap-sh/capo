"""Generated from Smithy shape ``com.amazonaws.ecs#CreateGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.gateway_configuration
    import capo_ecs.types.propagate_gateway_tags
    import capo_ecs.types.string
    import capo_ecs.types.tags


class CreateGatewayRequest(TypedDict, closed=True):
    name: "capo_ecs.types.string.String"
    """<p>The name for the gateway. The name must be unique within your account and can be up to 255 characters.</p>"""
    infrastructure_role_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the gateway assumes to create and manage infrastructure on your behalf.</p>"""
    client_token: NotRequired["capo_ecs.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""
    deletion_protection: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether to enable deletion protection for the gateway. When enabled, the gateway can't be deleted, and the gateway propagates this setting to the load balancers it manages. The default is <code>true</code>.</p>"""
    configuration: "capo_ecs.types.gateway_configuration.GatewayConfiguration"
    """<p>The type-specific configuration for the gateway. Exactly one configuration variant must be set, and it determines the gateway type. For example, <code>hostSharedAlb</code> configures a gateway that uses Application Load Balancers with host-based routing.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the gateway to help you categorize and organize it. Each tag consists of a key and an optional value. Depending on <code>propagateTags</code>, these tags can be applied to the infrastructure the gateway manages.</p>"""
    propagate_tags: NotRequired[
        "capo_ecs.types.propagate_gateway_tags.PropagateGatewayTags"
    ]
    """<p>Specifies whether to propagate the tags from the gateway to the infrastructure that the gateway manages. The default is <code>GATEWAY</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGatewayRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    import capo_ecs.types.gateway_configuration

    out["configuration"] = capo_ecs.types.gateway_configuration.serialize_aws_json_1_1(
        value["configuration"]
    )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_gateway_tags

        out["propagateTags"] = (
            capo_ecs.types.propagate_gateway_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGatewayRequest:
    out: CreateGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    else:
        out["infrastructure_role_arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("configuration") is not None:
        import capo_ecs.types.gateway_configuration

        out["configuration"] = (
            capo_ecs.types.gateway_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    else:
        import capo_ecs.types._unknown

        out["configuration"] = capo_ecs.types._unknown.UnknownUnionMember("")
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("propagateTags") is not None:
        import capo_ecs.types.propagate_gateway_tags

        out["propagate_tags"] = (
            capo_ecs.types.propagate_gateway_tags.deserialize_aws_json_1_1(
                data["propagateTags"]
            )
        )
    return out
