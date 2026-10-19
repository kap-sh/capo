"""Generated from Smithy shape ``com.amazonaws.lambda#CreateCapacityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_name
    import capo_lambda.types.capacity_provider_permissions_config
    import capo_lambda.types.capacity_provider_scaling_config
    import capo_lambda.types.capacity_provider_telemetry_config
    import capo_lambda.types.capacity_provider_vpc_config
    import capo_lambda.types.instance_requirements
    import capo_lambda.types.kms_key_arn_non_empty
    import capo_lambda.types.propagate_tags
    import capo_lambda.types.tags


class CreateCapacityProviderRequest(TypedDict, closed=True):
    capacity_provider_name: (
        "capo_lambda.types.capacity_provider_name.CapacityProviderName"
    )
    """<p>The name of the capacity provider. </p>"""
    vpc_config: (
        "capo_lambda.types.capacity_provider_vpc_config.CapacityProviderVpcConfig"
    )
    """<p>The VPC configuration for the capacity provider, including subnet IDs and security group IDs where compute instances will be launched.</p>"""
    permissions_config: "capo_lambda.types.capacity_provider_permissions_config.CapacityProviderPermissionsConfig"
    """<p>The permissions configuration that specifies the IAM role ARN used by the capacity provider to manage compute resources.</p>"""
    instance_requirements: NotRequired[
        "capo_lambda.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The instance requirements that specify the compute instance characteristics, including architectures and allowed or excluded instance types.</p>"""
    capacity_provider_scaling_config: NotRequired[
        "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
    ]
    """<p>The scaling configuration that defines how the capacity provider scales compute instances, including maximum vCPU count and scaling policies.</p>"""
    kms_key_arn: NotRequired[
        "capo_lambda.types.kms_key_arn_non_empty.KMSKeyArnNonEmpty"
    ]
    """<p>The ARN of the KMS key used to encrypt data associated with the capacity provider.</p>"""
    tags: NotRequired["capo_lambda.types.tags.Tags"]
    """<p>A list of tags to associate with the capacity provider.</p>"""
    propagate_tags: NotRequired["capo_lambda.types.propagate_tags.PropagateTags"]
    """<p>The tag propagation configuration for the capacity provider. Specifies tags to apply to managed resources at launch.</p>"""
    telemetry_config: NotRequired[
        "capo_lambda.types.capacity_provider_telemetry_config.CapacityProviderTelemetryConfig"
    ]
    """<p>The telemetry configuration for the capacity provider. Specifies logging settings for managed resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCapacityProviderRequest) -> dict:
    out: dict = {}
    out["CapacityProviderName"] = value["capacity_provider_name"]
    import capo_lambda.types.capacity_provider_vpc_config

    out["VpcConfig"] = capo_lambda.types.capacity_provider_vpc_config.serialize_json(
        value["vpc_config"]
    )
    import capo_lambda.types.capacity_provider_permissions_config

    out["PermissionsConfig"] = (
        capo_lambda.types.capacity_provider_permissions_config.serialize_json(
            value["permissions_config"]
        )
    )
    if "instance_requirements" in value:
        import capo_lambda.types.instance_requirements

        out["InstanceRequirements"] = (
            capo_lambda.types.instance_requirements.serialize_json(
                value["instance_requirements"]
            )
        )
    if "capacity_provider_scaling_config" in value:
        import capo_lambda.types.capacity_provider_scaling_config

        out["CapacityProviderScalingConfig"] = (
            capo_lambda.types.capacity_provider_scaling_config.serialize_json(
                value["capacity_provider_scaling_config"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_lambda.types.tags

        out["Tags"] = capo_lambda.types.tags.serialize_json(value["tags"])
    if "propagate_tags" in value:
        import capo_lambda.types.propagate_tags

        out["PropagateTags"] = capo_lambda.types.propagate_tags.serialize_json(
            value["propagate_tags"]
        )
    if "telemetry_config" in value:
        import capo_lambda.types.capacity_provider_telemetry_config

        out["TelemetryConfig"] = (
            capo_lambda.types.capacity_provider_telemetry_config.serialize_json(
                value["telemetry_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateCapacityProviderRequest:
    out: CreateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("CapacityProviderName") is not None:
        out["capacity_provider_name"] = data["CapacityProviderName"]
    else:
        out["capacity_provider_name"] = ""
    if data.get("VpcConfig") is not None:
        import capo_lambda.types.capacity_provider_vpc_config

        out["vpc_config"] = (
            capo_lambda.types.capacity_provider_vpc_config.deserialize_json(
                data["VpcConfig"]
            )
        )
    else:
        raise DeserializationError("CreateCapacityProviderRequest.vpc_config required")
    if data.get("PermissionsConfig") is not None:
        import capo_lambda.types.capacity_provider_permissions_config

        out["permissions_config"] = (
            capo_lambda.types.capacity_provider_permissions_config.deserialize_json(
                data["PermissionsConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCapacityProviderRequest.permissions_config required"
        )
    if data.get("InstanceRequirements") is not None:
        import capo_lambda.types.instance_requirements

        out["instance_requirements"] = (
            capo_lambda.types.instance_requirements.deserialize_json(
                data["InstanceRequirements"]
            )
        )
    if data.get("CapacityProviderScalingConfig") is not None:
        import capo_lambda.types.capacity_provider_scaling_config

        out["capacity_provider_scaling_config"] = (
            capo_lambda.types.capacity_provider_scaling_config.deserialize_json(
                data["CapacityProviderScalingConfig"]
            )
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("Tags") is not None:
        import capo_lambda.types.tags

        out["tags"] = capo_lambda.types.tags.deserialize_json(data["Tags"])
    if data.get("PropagateTags") is not None:
        import capo_lambda.types.propagate_tags

        out["propagate_tags"] = capo_lambda.types.propagate_tags.deserialize_json(
            data["PropagateTags"]
        )
    if data.get("TelemetryConfig") is not None:
        import capo_lambda.types.capacity_provider_telemetry_config

        out["telemetry_config"] = (
            capo_lambda.types.capacity_provider_telemetry_config.deserialize_json(
                data["TelemetryConfig"]
            )
        )
    return out
