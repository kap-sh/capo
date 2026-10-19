"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_arn
    import capo_lambda.types.capacity_provider_permissions_config
    import capo_lambda.types.capacity_provider_scaling_config
    import capo_lambda.types.capacity_provider_state
    import capo_lambda.types.capacity_provider_telemetry_config
    import capo_lambda.types.capacity_provider_vpc_config
    import capo_lambda.types.instance_requirements
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.propagate_tags
    import capo_lambda.types.timestamp


class CapacityProvider(TypedDict, closed=True):
    capacity_provider_arn: "capo_lambda.types.capacity_provider_arn.CapacityProviderArn"
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    state: "capo_lambda.types.capacity_provider_state.CapacityProviderState"
    """<p>The current state of the capacity provider.</p>"""
    vpc_config: (
        "capo_lambda.types.capacity_provider_vpc_config.CapacityProviderVpcConfig"
    )
    """<p>The VPC configuration for the capacity provider.</p>"""
    permissions_config: "capo_lambda.types.capacity_provider_permissions_config.CapacityProviderPermissionsConfig"
    """<p>The permissions configuration for the capacity provider.</p>"""
    instance_requirements: NotRequired[
        "capo_lambda.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The instance requirements for compute resources managed by the capacity provider.</p>"""
    capacity_provider_scaling_config: NotRequired[
        "capo_lambda.types.capacity_provider_scaling_config.CapacityProviderScalingConfig"
    ]
    """<p>The scaling configuration for the capacity provider.</p>"""
    kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the KMS key used to encrypt the capacity provider's resources.</p>"""
    last_modified: NotRequired["capo_lambda.types.timestamp.Timestamp"]
    """<p>The date and time when the capacity provider was last modified.</p>"""
    propagate_tags: NotRequired["capo_lambda.types.propagate_tags.PropagateTags"]
    telemetry_config: NotRequired[
        "capo_lambda.types.capacity_provider_telemetry_config.CapacityProviderTelemetryConfig"
    ]
    """<p>The telemetry configuration for the capacity provider, including logging settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProvider) -> dict:
    out: dict = {}
    out["CapacityProviderArn"] = value["capacity_provider_arn"]
    import capo_lambda.types.capacity_provider_state

    out["State"] = capo_lambda.types.capacity_provider_state.serialize_json(
        value["state"]
    )
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
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
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


def deserialize_json(data: dict) -> CapacityProvider:
    out: CapacityProvider = {}  # type: ignore[typeddict-item]
    if data.get("CapacityProviderArn") is not None:
        out["capacity_provider_arn"] = data["CapacityProviderArn"]
    else:
        out["capacity_provider_arn"] = ""
    if data.get("State") is not None:
        import capo_lambda.types.capacity_provider_state

        out["state"] = capo_lambda.types.capacity_provider_state.deserialize_json(
            data["State"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_lambda.types.capacity_provider_state.CapacityProviderState", ""
        )
    if data.get("VpcConfig") is not None:
        import capo_lambda.types.capacity_provider_vpc_config

        out["vpc_config"] = (
            capo_lambda.types.capacity_provider_vpc_config.deserialize_json(
                data["VpcConfig"]
            )
        )
    else:
        raise DeserializationError("CapacityProvider.vpc_config required")
    if data.get("PermissionsConfig") is not None:
        import capo_lambda.types.capacity_provider_permissions_config

        out["permissions_config"] = (
            capo_lambda.types.capacity_provider_permissions_config.deserialize_json(
                data["PermissionsConfig"]
            )
        )
    else:
        raise DeserializationError("CapacityProvider.permissions_config required")
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
    if data.get("LastModified") is not None:
        out["last_modified"] = data["LastModified"]
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
