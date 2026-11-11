"""Generated from Smithy shape ``com.amazonaws.devicefarm#ScheduleRunConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.amazon_resource_names
    import capo_device_farm.types.amazon_role_resource_name
    import capo_device_farm.types.billing_method
    import capo_device_farm.types.customer_artifact_paths
    import capo_device_farm.types.device_proxy
    import capo_device_farm.types.environment_variables
    import capo_device_farm.types.insights_types
    import capo_device_farm.types.location
    import capo_device_farm.types.radios
    import capo_device_farm.types.string


class ScheduleRunConfiguration(TypedDict, closed=True):
    extra_data_package_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm extracts to external data for Android or the app's sandbox for iOS.</p>"""
    network_profile_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Reserved for internal use.</p>"""
    locale: NotRequired["capo_device_farm.types.string.String"]
    """<p>Information about the locale that is used for the run.</p>"""
    location: NotRequired["capo_device_farm.types.location.Location"]
    """<p>Information about the location that is used for the run.</p>"""
    vpce_configuration_arns: NotRequired[
        "capo_device_farm.types.amazon_resource_names.AmazonResourceNames"
    ]
    """<p>An array of ARNs for your VPC endpoint configurations.</p>"""
    device_proxy: NotRequired["capo_device_farm.types.device_proxy.DeviceProxy"]
    """<p>The device proxy to be configured on the device for the run.</p>"""
    customer_artifact_paths: NotRequired[
        "capo_device_farm.types.customer_artifact_paths.CustomerArtifactPaths"
    ]
    """<p>Input <code>CustomerArtifactPaths</code> object for the scheduled run configuration.</p>"""
    radios: NotRequired["capo_device_farm.types.radios.Radios"]
    """<p>Information about the radio states for the run.</p>"""
    auxiliary_apps: NotRequired[
        "capo_device_farm.types.amazon_resource_names.AmazonResourceNames"
    ]
    """<p>A list of upload ARNs for app packages to be installed with your app.</p>"""
    billing_method: NotRequired["capo_device_farm.types.billing_method.BillingMethod"]
    """<p>Specifies the billing method for a test run: <code>metered</code> or <code>unmetered</code>. If the parameter is not specified, the default value is <code>metered</code>.</p> <note> <p>If you have purchased unmetered device slots, you must set this parameter to <code>unmetered</code> to make use of them. Otherwise, your run counts against your metered time.</p> </note>"""
    environment_variables: NotRequired[
        "capo_device_farm.types.environment_variables.EnvironmentVariables"
    ]
    """<p>Environment variables associated with the run.</p>"""
    execution_role_arn: NotRequired[
        "capo_device_farm.types.amazon_role_resource_name.AmazonRoleResourceName"
    ]
    """<p>An IAM role to be assumed by the test host for the run.</p>"""
    insights_types: NotRequired["capo_device_farm.types.insights_types.InsightsTypes"]
    """<p>The types of insights to generate for a run. If you do not specify a value, the default is <code>TEST_REPORT</code> for runs that support insights.</p> <p>Specify <code>NONE</code> if you do not want the service to generate insights for the run. You cannot combine <code>NONE</code> with any other value.</p> <p>Insights are supported for custom mode runs of all test types except Appium Ruby and Appium Web Ruby.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleRunConfiguration) -> dict:
    out: dict = {}
    if "extra_data_package_arn" in value:
        out["extraDataPackageArn"] = value["extra_data_package_arn"]
    if "network_profile_arn" in value:
        out["networkProfileArn"] = value["network_profile_arn"]
    if "locale" in value:
        out["locale"] = value["locale"]
    if "location" in value:
        import capo_device_farm.types.location

        out["location"] = capo_device_farm.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    if "vpce_configuration_arns" in value:
        import capo_device_farm.types.amazon_resource_names

        out["vpceConfigurationArns"] = (
            capo_device_farm.types.amazon_resource_names.serialize_aws_json_1_1(
                value["vpce_configuration_arns"]
            )
        )
    if "device_proxy" in value:
        import capo_device_farm.types.device_proxy

        out["deviceProxy"] = capo_device_farm.types.device_proxy.serialize_aws_json_1_1(
            value["device_proxy"]
        )
    if "customer_artifact_paths" in value:
        import capo_device_farm.types.customer_artifact_paths

        out["customerArtifactPaths"] = (
            capo_device_farm.types.customer_artifact_paths.serialize_aws_json_1_1(
                value["customer_artifact_paths"]
            )
        )
    if "radios" in value:
        import capo_device_farm.types.radios

        out["radios"] = capo_device_farm.types.radios.serialize_aws_json_1_1(
            value["radios"]
        )
    if "auxiliary_apps" in value:
        import capo_device_farm.types.amazon_resource_names

        out["auxiliaryApps"] = (
            capo_device_farm.types.amazon_resource_names.serialize_aws_json_1_1(
                value["auxiliary_apps"]
            )
        )
    if "billing_method" in value:
        import capo_device_farm.types.billing_method

        out["billingMethod"] = (
            capo_device_farm.types.billing_method.serialize_aws_json_1_1(
                value["billing_method"]
            )
        )
    if "environment_variables" in value:
        import capo_device_farm.types.environment_variables

        out["environmentVariables"] = (
            capo_device_farm.types.environment_variables.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "insights_types" in value:
        import capo_device_farm.types.insights_types

        out["insightsTypes"] = (
            capo_device_farm.types.insights_types.serialize_aws_json_1_1(
                value["insights_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduleRunConfiguration:
    out: ScheduleRunConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("extraDataPackageArn") is not None:
        out["extra_data_package_arn"] = data["extraDataPackageArn"]
    if data.get("networkProfileArn") is not None:
        out["network_profile_arn"] = data["networkProfileArn"]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("location") is not None:
        import capo_device_farm.types.location

        out["location"] = capo_device_farm.types.location.deserialize_aws_json_1_1(
            data["location"]
        )
    if data.get("vpceConfigurationArns") is not None:
        import capo_device_farm.types.amazon_resource_names

        out["vpce_configuration_arns"] = (
            capo_device_farm.types.amazon_resource_names.deserialize_aws_json_1_1(
                data["vpceConfigurationArns"]
            )
        )
    if data.get("deviceProxy") is not None:
        import capo_device_farm.types.device_proxy

        out["device_proxy"] = (
            capo_device_farm.types.device_proxy.deserialize_aws_json_1_1(
                data["deviceProxy"]
            )
        )
    if data.get("customerArtifactPaths") is not None:
        import capo_device_farm.types.customer_artifact_paths

        out["customer_artifact_paths"] = (
            capo_device_farm.types.customer_artifact_paths.deserialize_aws_json_1_1(
                data["customerArtifactPaths"]
            )
        )
    if data.get("radios") is not None:
        import capo_device_farm.types.radios

        out["radios"] = capo_device_farm.types.radios.deserialize_aws_json_1_1(
            data["radios"]
        )
    if data.get("auxiliaryApps") is not None:
        import capo_device_farm.types.amazon_resource_names

        out["auxiliary_apps"] = (
            capo_device_farm.types.amazon_resource_names.deserialize_aws_json_1_1(
                data["auxiliaryApps"]
            )
        )
    if data.get("billingMethod") is not None:
        import capo_device_farm.types.billing_method

        out["billing_method"] = (
            capo_device_farm.types.billing_method.deserialize_aws_json_1_1(
                data["billingMethod"]
            )
        )
    if data.get("environmentVariables") is not None:
        import capo_device_farm.types.environment_variables

        out["environment_variables"] = (
            capo_device_farm.types.environment_variables.deserialize_aws_json_1_1(
                data["environmentVariables"]
            )
        )
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("insightsTypes") is not None:
        import capo_device_farm.types.insights_types

        out["insights_types"] = (
            capo_device_farm.types.insights_types.deserialize_aws_json_1_1(
                data["insightsTypes"]
            )
        )
    return out
