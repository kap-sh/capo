"""Generated from Smithy shape ``com.amazonaws.devicefarm#RemoteAccessSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.billing_method
    import capo_device_farm.types.date_time
    import capo_device_farm.types.device
    import capo_device_farm.types.device_minutes
    import capo_device_farm.types.device_proxy
    import capo_device_farm.types.execution_result
    import capo_device_farm.types.execution_status
    import capo_device_farm.types.interaction_mode
    import capo_device_farm.types.message
    import capo_device_farm.types.name
    import capo_device_farm.types.remote_access_endpoints
    import capo_device_farm.types.skip_app_resign
    import capo_device_farm.types.string
    import capo_device_farm.types.vpc_config


class RemoteAccessSession(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the remote access session.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The name of the remote access session.</p>"""
    created: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The date and time the remote access session was created.</p>"""
    status: NotRequired["capo_device_farm.types.execution_status.ExecutionStatus"]
    """<p>The status of the remote access session. Can be any of the following:</p> <ul> <li> <p>PENDING.</p> </li> <li> <p>PENDING_CONCURRENCY.</p> </li> <li> <p>PENDING_DEVICE.</p> </li> <li> <p>PROCESSING.</p> </li> <li> <p>SCHEDULING.</p> </li> <li> <p>PREPARING.</p> </li> <li> <p>RUNNING.</p> </li> <li> <p>COMPLETED.</p> </li> <li> <p>STOPPING.</p> </li> </ul>"""
    result: NotRequired["capo_device_farm.types.execution_result.ExecutionResult"]
    """<p>The result of the remote access session. Can be any of the following:</p> <ul> <li> <p>PENDING.</p> </li> <li> <p>PASSED.</p> </li> <li> <p>WARNED.</p> </li> <li> <p>FAILED.</p> </li> <li> <p>SKIPPED.</p> </li> <li> <p>ERRORED.</p> </li> <li> <p>STOPPED.</p> </li> </ul>"""
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>A message about the remote access session.</p>"""
    started: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The date and time the remote access session was started.</p>"""
    stopped: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The date and time the remote access session was stopped.</p>"""
    device: NotRequired["capo_device_farm.types.device.Device"]
    """<p>The device (phone or tablet) used in the remote access session.</p>"""
    instance_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the instance.</p>"""
    billing_method: NotRequired["capo_device_farm.types.billing_method.BillingMethod"]
    """<p>The billing method of the remote access session. Possible values include <code>METERED</code> or <code>UNMETERED</code>. For more information about metered devices, see <a href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology">AWS Device Farm terminology</a>.</p>"""
    device_minutes: NotRequired["capo_device_farm.types.device_minutes.DeviceMinutes"]
    """<p>The number of minutes a device is used in a remote access session (including setup and teardown minutes).</p>"""
    endpoint: NotRequired["capo_device_farm.types.string.String"]
    """<p>The endpoint for the remote access session. This field is deprecated, and is replaced by the new <code>endpoints.interactiveEndpoint</code> field.</p>"""
    device_udid: NotRequired["capo_device_farm.types.string.String"]
    """<p>Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.</p> <p>Remote debugging is <a href="https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html">no longer supported</a>.</p>"""
    interaction_mode: NotRequired[
        "capo_device_farm.types.interaction_mode.InteractionMode"
    ]
    """<p>The interaction mode of the remote access session. Changing the interactive mode of remote access sessions is no longer available.</p>"""
    skip_app_resign: NotRequired["capo_device_farm.types.skip_app_resign.SkipAppResign"]
    """<p>When set to <code>true</code>, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.</p> <p>For more information about how Device Farm re-signs your apps, see <a href="http://aws.amazon.com/device-farm/faqs/">Do you modify my app?</a> in the <i>AWS Device Farm FAQs</i>.</p>"""
    vpc_config: NotRequired["capo_device_farm.types.vpc_config.VpcConfig"]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""
    device_proxy: NotRequired["capo_device_farm.types.device_proxy.DeviceProxy"]
    """<p>The device proxy configured for the remote access session.</p>"""
    app_upload: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN for the app to be installed onto your device.</p>"""
    endpoints: NotRequired[
        "capo_device_farm.types.remote_access_endpoints.RemoteAccessEndpoints"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteAccessSession) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "created" in value:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "status" in value:
        import capo_device_farm.types.execution_status

        out["status"] = capo_device_farm.types.execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "result" in value:
        import capo_device_farm.types.execution_result

        out["result"] = capo_device_farm.types.execution_result.serialize_aws_json_1_1(
            value["result"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "started" in value:
        import capo_device_farm.types.date_time

        out["started"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["started"]
        )
    if "stopped" in value:
        import capo_device_farm.types.date_time

        out["stopped"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["stopped"]
        )
    if "device" in value:
        import capo_device_farm.types.device

        out["device"] = capo_device_farm.types.device.serialize_aws_json_1_1(
            value["device"]
        )
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "billing_method" in value:
        import capo_device_farm.types.billing_method

        out["billingMethod"] = (
            capo_device_farm.types.billing_method.serialize_aws_json_1_1(
                value["billing_method"]
            )
        )
    if "device_minutes" in value:
        import capo_device_farm.types.device_minutes

        out["deviceMinutes"] = (
            capo_device_farm.types.device_minutes.serialize_aws_json_1_1(
                value["device_minutes"]
            )
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "device_udid" in value:
        out["deviceUdid"] = value["device_udid"]
    if "interaction_mode" in value:
        import capo_device_farm.types.interaction_mode

        out["interactionMode"] = (
            capo_device_farm.types.interaction_mode.serialize_aws_json_1_1(
                value["interaction_mode"]
            )
        )
    if "skip_app_resign" in value:
        out["skipAppResign"] = value["skip_app_resign"]
    if "vpc_config" in value:
        import capo_device_farm.types.vpc_config

        out["vpcConfig"] = capo_device_farm.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "device_proxy" in value:
        import capo_device_farm.types.device_proxy

        out["deviceProxy"] = capo_device_farm.types.device_proxy.serialize_aws_json_1_1(
            value["device_proxy"]
        )
    if "app_upload" in value:
        out["appUpload"] = value["app_upload"]
    if "endpoints" in value:
        import capo_device_farm.types.remote_access_endpoints

        out["endpoints"] = (
            capo_device_farm.types.remote_access_endpoints.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoteAccessSession:
    out: RemoteAccessSession = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("created") is not None:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("status") is not None:
        import capo_device_farm.types.execution_status

        out["status"] = (
            capo_device_farm.types.execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("result") is not None:
        import capo_device_farm.types.execution_result

        out["result"] = (
            capo_device_farm.types.execution_result.deserialize_aws_json_1_1(
                data["result"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("started") is not None:
        import capo_device_farm.types.date_time

        out["started"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["started"]
        )
    if data.get("stopped") is not None:
        import capo_device_farm.types.date_time

        out["stopped"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["stopped"]
        )
    if data.get("device") is not None:
        import capo_device_farm.types.device

        out["device"] = capo_device_farm.types.device.deserialize_aws_json_1_1(
            data["device"]
        )
    if data.get("instanceArn") is not None:
        out["instance_arn"] = data["instanceArn"]
    if data.get("billingMethod") is not None:
        import capo_device_farm.types.billing_method

        out["billing_method"] = (
            capo_device_farm.types.billing_method.deserialize_aws_json_1_1(
                data["billingMethod"]
            )
        )
    if data.get("deviceMinutes") is not None:
        import capo_device_farm.types.device_minutes

        out["device_minutes"] = (
            capo_device_farm.types.device_minutes.deserialize_aws_json_1_1(
                data["deviceMinutes"]
            )
        )
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("deviceUdid") is not None:
        out["device_udid"] = data["deviceUdid"]
    if data.get("interactionMode") is not None:
        import capo_device_farm.types.interaction_mode

        out["interaction_mode"] = (
            capo_device_farm.types.interaction_mode.deserialize_aws_json_1_1(
                data["interactionMode"]
            )
        )
    if data.get("skipAppResign") is not None:
        out["skip_app_resign"] = data["skipAppResign"]
    if data.get("vpcConfig") is not None:
        import capo_device_farm.types.vpc_config

        out["vpc_config"] = capo_device_farm.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if data.get("deviceProxy") is not None:
        import capo_device_farm.types.device_proxy

        out["device_proxy"] = (
            capo_device_farm.types.device_proxy.deserialize_aws_json_1_1(
                data["deviceProxy"]
            )
        )
    if data.get("appUpload") is not None:
        out["app_upload"] = data["appUpload"]
    if data.get("endpoints") is not None:
        import capo_device_farm.types.remote_access_endpoints

        out["endpoints"] = (
            capo_device_farm.types.remote_access_endpoints.deserialize_aws_json_1_1(
                data["endpoints"]
            )
        )
    return out
