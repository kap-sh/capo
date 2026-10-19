"""Generated from Smithy shape ``com.amazonaws.apprunner#UpdateServiceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.health_check_configuration
    import capo_apprunner.types.instance_configuration
    import capo_apprunner.types.network_configuration
    import capo_apprunner.types.service_observability_configuration
    import capo_apprunner.types.source_configuration


class UpdateServiceRequest(TypedDict, closed=True):
    service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service that you want to update.</p>"""
    source_configuration: NotRequired[
        "capo_apprunner.types.source_configuration.SourceConfiguration"
    ]
    """<p>The source configuration to apply to the App Runner service.</p> <p>You can change the configuration of the code or image repository that the service uses. However, you can't switch from code to image or the other way around. This means that you must provide the same structure member of <code>SourceConfiguration</code> that you originally included when you created the service. Specifically, you can include either <code>CodeRepository</code> or <code>ImageRepository</code>. To update the source configuration, set the values to members of the structure that you include.</p>"""
    instance_configuration: NotRequired[
        "capo_apprunner.types.instance_configuration.InstanceConfiguration"
    ]
    """<p>The runtime configuration to apply to instances (scaling units) of your service.</p>"""
    auto_scaling_configuration_arn: NotRequired[
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with the App Runner service.</p>"""
    health_check_configuration: NotRequired[
        "capo_apprunner.types.health_check_configuration.HealthCheckConfiguration"
    ]
    """<p>The settings for the health check that App Runner performs to monitor the health of the App Runner service.</p>"""
    network_configuration: NotRequired[
        "capo_apprunner.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Configuration settings related to network traffic of the web application that the App Runner service runs.</p>"""
    observability_configuration: NotRequired[
        "capo_apprunner.types.service_observability_configuration.ServiceObservabilityConfiguration"
    ]
    """<p>The observability configuration of your service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    if "source_configuration" in value:
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
    if "auto_scaling_configuration_arn" in value:
        out["AutoScalingConfigurationArn"] = value["auto_scaling_configuration_arn"]
    if "health_check_configuration" in value:
        import capo_apprunner.types.health_check_configuration

        out["HealthCheckConfiguration"] = (
            capo_apprunner.types.health_check_configuration.serialize_aws_json_1_0(
                value["health_check_configuration"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceRequest:
    out: UpdateServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    else:
        out["service_arn"] = ""
    if data.get("SourceConfiguration") is not None:
        import capo_apprunner.types.source_configuration

        out["source_configuration"] = (
            capo_apprunner.types.source_configuration.deserialize_aws_json_1_0(
                data["SourceConfiguration"]
            )
        )
    if data.get("InstanceConfiguration") is not None:
        import capo_apprunner.types.instance_configuration

        out["instance_configuration"] = (
            capo_apprunner.types.instance_configuration.deserialize_aws_json_1_0(
                data["InstanceConfiguration"]
            )
        )
    if data.get("AutoScalingConfigurationArn") is not None:
        out["auto_scaling_configuration_arn"] = data["AutoScalingConfigurationArn"]
    if data.get("HealthCheckConfiguration") is not None:
        import capo_apprunner.types.health_check_configuration

        out["health_check_configuration"] = (
            capo_apprunner.types.health_check_configuration.deserialize_aws_json_1_0(
                data["HealthCheckConfiguration"]
            )
        )
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


def redact_sensitive(value: UpdateServiceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_configuration" in value:
        import capo_apprunner.types.source_configuration

        out["source_configuration"] = (
            capo_apprunner.types.source_configuration.redact_sensitive(
                value["source_configuration"]
            )
        )
    return out
