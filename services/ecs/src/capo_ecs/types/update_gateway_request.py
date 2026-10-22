"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.propagate_gateway_tags
    import capo_ecs.types.string
    import capo_ecs.types.update_gateway_configuration


class UpdateGatewayRequest(TypedDict, closed=True):
    gateway: "capo_ecs.types.string.String"
    """<p>The name or Amazon Resource Name (ARN) of the gateway to update.</p>"""
    infrastructure_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the gateway assumes to manage infrastructure on your behalf.</p>"""
    deletion_protection: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether to enable deletion protection for the gateway. When enabled, the gateway can't be deleted.</p>"""
    configuration: NotRequired[
        "capo_ecs.types.update_gateway_configuration.UpdateGatewayConfiguration"
    ]
    """<p>The updated type-specific configuration for the gateway. The configuration variant must match the gateway's existing type, and only mutable fields can be changed.</p>"""
    propagate_tags: NotRequired[
        "capo_ecs.types.propagate_gateway_tags.PropagateGatewayTags"
    ]
    """<p>Specifies whether to propagate the tags from the gateway to the infrastructure that the gateway manages. If you don't specify a value, the gateway's existing setting is unchanged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGatewayRequest) -> dict:
    out: dict = {}
    out["gateway"] = value["gateway"]
    if "infrastructure_role_arn" in value:
        out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "configuration" in value:
        import capo_ecs.types.update_gateway_configuration

        out["configuration"] = (
            capo_ecs.types.update_gateway_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_gateway_tags

        out["propagateTags"] = (
            capo_ecs.types.propagate_gateway_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGatewayRequest:
    out: UpdateGatewayRequest = {}  # type: ignore[typeddict-item]
    if data.get("gateway") is not None:
        out["gateway"] = data["gateway"]
    else:
        out["gateway"] = ""
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("configuration") is not None:
        import capo_ecs.types.update_gateway_configuration

        out["configuration"] = (
            capo_ecs.types.update_gateway_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("propagateTags") is not None:
        import capo_ecs.types.propagate_gateway_tags

        out["propagate_tags"] = (
            capo_ecs.types.propagate_gateway_tags.deserialize_aws_json_1_1(
                data["propagateTags"]
            )
        )
    return out
