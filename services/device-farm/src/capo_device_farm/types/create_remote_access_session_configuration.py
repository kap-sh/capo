"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateRemoteAccessSessionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_names
    import capo_device_farm.types.auxiliary_app_arn_list
    import capo_device_farm.types.billing_method
    import capo_device_farm.types.device_proxy
    import capo_device_farm.types.remote_access_parameters


class CreateRemoteAccessSessionConfiguration(TypedDict, closed=True):
    auxiliary_apps: NotRequired[
        "capo_device_farm.types.auxiliary_app_arn_list.AuxiliaryAppArnList"
    ]
    """<p>A list of upload ARNs for app packages to be installed onto your device. (Maximum 3)</p>"""
    billing_method: NotRequired["capo_device_farm.types.billing_method.BillingMethod"]
    """<p>The billing method for the remote access session.</p>"""
    vpce_configuration_arns: NotRequired[
        "capo_device_farm.types.amazon_resource_names.AmazonResourceNames"
    ]
    """<p>An array of ARNs included in the VPC endpoint configuration.</p>"""
    device_proxy: NotRequired["capo_device_farm.types.device_proxy.DeviceProxy"]
    """<p>The device proxy to be configured on the device for the remote access session.</p>"""
    parameters: NotRequired[
        "capo_device_farm.types.remote_access_parameters.RemoteAccessParameters"
    ]
    """<p>The name-value string pairs that specify additional settings for the remote access session.</p> <ul> <li> <p> <code>appium:version</code>: The major version of the Appium server to use for the session (for example, 2 or 3). The service might reject the selected version if it is not available for the selected device.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRemoteAccessSessionConfiguration) -> dict:
    out: dict = {}
    if "auxiliary_apps" in value:
        import capo_device_farm.types.auxiliary_app_arn_list

        out["auxiliaryApps"] = (
            capo_device_farm.types.auxiliary_app_arn_list.serialize_aws_json_1_1(
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
    if "parameters" in value:
        import capo_device_farm.types.remote_access_parameters

        out["parameters"] = (
            capo_device_farm.types.remote_access_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRemoteAccessSessionConfiguration:
    out: CreateRemoteAccessSessionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("auxiliaryApps") is not None:
        import capo_device_farm.types.auxiliary_app_arn_list

        out["auxiliary_apps"] = (
            capo_device_farm.types.auxiliary_app_arn_list.deserialize_aws_json_1_1(
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
    if data.get("parameters") is not None:
        import capo_device_farm.types.remote_access_parameters

        out["parameters"] = (
            capo_device_farm.types.remote_access_parameters.deserialize_aws_json_1_1(
                data["parameters"]
            )
        )
    return out
