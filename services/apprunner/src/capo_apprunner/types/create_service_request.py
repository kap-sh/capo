"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateServiceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.encryption_configuration
    import capo_apprunner.types.health_check_configuration
    import capo_apprunner.types.instance_configuration
    import capo_apprunner.types.network_configuration
    import capo_apprunner.types.service_name
    import capo_apprunner.types.service_observability_configuration
    import capo_apprunner.types.source_configuration
    import capo_apprunner.types.tag_list


class CreateServiceRequest(TypedDict, closed=True):
    service_name: "capo_apprunner.types.service_name.ServiceName"
    """<p>A name for the App Runner service. It must be unique across all the running App Runner services in your Amazon Web Services account in the Amazon Web Services Region.</p>"""
    source_configuration: (
        "capo_apprunner.types.source_configuration.SourceConfiguration"
    )
    """<p>The source to deploy to the App Runner service. It can be a code or an image repository.</p>"""
    instance_configuration: NotRequired[
        "capo_apprunner.types.instance_configuration.InstanceConfiguration"
    ]
    """<p>The runtime configuration of instances (scaling units) of your service.</p>"""
    tags: NotRequired["capo_apprunner.types.tag_list.TagList"]
    """<p>An optional list of metadata items that you can associate with the App Runner service resource. A tag is a key-value pair.</p>"""
    encryption_configuration: NotRequired[
        "capo_apprunner.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an Amazon Web Services managed key.</p>"""
    health_check_configuration: NotRequired[
        "capo_apprunner.types.health_check_configuration.HealthCheckConfiguration"
    ]
    """<p>The settings for the health check that App Runner performs to monitor the health of the App Runner service.</p>"""
    auto_scaling_configuration_arn: NotRequired[
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.</p> <p>Specify an ARN with a name and a revision number to associate that revision. For example: <code>arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3</code> </p> <p>Specify just the name to associate the latest revision. For example: <code>arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability</code> </p>"""
    network_configuration: NotRequired[
        "capo_apprunner.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Configuration settings related to network traffic of the web application that the App Runner service runs.</p>"""
    observability_configuration: NotRequired[
        "capo_apprunner.types.service_observability_configuration.ServiceObservabilityConfiguration"
    ]
    """<p>The observability configuration of your service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceRequest) -> dict:
    out: dict = {}
    out["ServiceName"] = value["service_name"]
    import capo_apprunner.types.source_configuration

    out["SourceConfiguration"] = (
        capo_apprunner.types.source_configuration.serialize_aws_json_1_0(
            value["source_configuration"]
        )
    )
    if "instance_configuration" in value:
        import capo_apprunner.types.instance_configuration

        out["InstanceConfiguration"] = (
            capo_apprunner.types.instance_configuration.serialize_aws_json_1_0(
                value["instance_configuration"]
            )
        )
    if "tags" in value:
        import capo_apprunner.types.tag_list

        out["Tags"] = capo_apprunner.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "encryption_configuration" in value:
        import capo_apprunner.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_apprunner.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "health_check_configuration" in value:
        import capo_apprunner.types.health_check_configuration

        out["HealthCheckConfiguration"] = (
            capo_apprunner.types.health_check_configuration.serialize_aws_json_1_0(
                value["health_check_configuration"]
            )
        )
    if "auto_scaling_configuration_arn" in value:
        out["AutoScalingConfigurationArn"] = value["auto_scaling_configuration_arn"]
    if "network_configuration" in value:
        import capo_apprunner.types.network_configuration

        out["NetworkConfiguration"] = (
            capo_apprunner.types.network_configuration.serialize_aws_json_1_0(
                value["network_configuration"]
            )
        )
    if "observability_configuration" in value:
        import capo_apprunner.types.service_observability_configuration

        out["ObservabilityConfiguration"] = (
            capo_apprunner.types.service_observability_configuration.serialize_aws_json_1_0(
                value["observability_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceRequest:
    out: CreateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    else:
        out["service_name"] = ""
    if data.get("SourceConfiguration") is not None:
        import capo_apprunner.types.source_configuration

        out["source_configuration"] = (
            capo_apprunner.types.source_configuration.deserialize_aws_json_1_0(
                data["SourceConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateServiceRequest.source_configuration required")
    if data.get("InstanceConfiguration") is not None:
        import capo_apprunner.types.instance_configuration

        out["instance_configuration"] = (
            capo_apprunner.types.instance_configuration.deserialize_aws_json_1_0(
                data["InstanceConfiguration"]
            )
        )
    if data.get("Tags") is not None:
        import capo_apprunner.types.tag_list

        out["tags"] = capo_apprunner.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_apprunner.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_apprunner.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("HealthCheckConfiguration") is not None:
        import capo_apprunner.types.health_check_configuration

        out["health_check_configuration"] = (
            capo_apprunner.types.health_check_configuration.deserialize_aws_json_1_0(
                data["HealthCheckConfiguration"]
            )
        )
    if data.get("AutoScalingConfigurationArn") is not None:
        out["auto_scaling_configuration_arn"] = data["AutoScalingConfigurationArn"]
    if data.get("NetworkConfiguration") is not None:
        import capo_apprunner.types.network_configuration

        out["network_configuration"] = (
            capo_apprunner.types.network_configuration.deserialize_aws_json_1_0(
                data["NetworkConfiguration"]
            )
        )
    if data.get("ObservabilityConfiguration") is not None:
        import capo_apprunner.types.service_observability_configuration

        out["observability_configuration"] = (
            capo_apprunner.types.service_observability_configuration.deserialize_aws_json_1_0(
                data["ObservabilityConfiguration"]
            )
        )
    return out


def redact_sensitive(value: CreateServiceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_configuration" in value:
        import capo_apprunner.types.source_configuration

        out["source_configuration"] = (
            capo_apprunner.types.source_configuration.redact_sensitive(
                value["source_configuration"]
            )
        )
    return out
