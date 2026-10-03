"""Generated from Smithy shape ``com.amazonaws.storagegateway#ActivateGatewayInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.activation_key
    import capo_storage_gateway.types.gateway_name
    import capo_storage_gateway.types.gateway_timezone
    import capo_storage_gateway.types.gateway_type
    import capo_storage_gateway.types.medium_changer_type
    import capo_storage_gateway.types.region_id
    import capo_storage_gateway.types.tags
    import capo_storage_gateway.types.tape_drive_type


class ActivateGatewayInput(TypedDict, closed=True):
    activation_key: "capo_storage_gateway.types.activation_key.ActivationKey"
    """<p>Your gateway activation key. You can obtain the activation key by sending an HTTP GET request with redirects enabled to the gateway IP address (port 80). The redirect URL returned in the response provides you the activation key for your gateway in the query string parameter <code>activationKey</code>. It may also include other activation-related parameters, however, these are merely defaults -- the arguments you pass to the <code>ActivateGateway</code> API call determine the actual configuration of your gateway.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html">Getting activation key</a> in the <i>Storage Gateway User Guide</i>.</p>"""
    gateway_name: "capo_storage_gateway.types.gateway_name.GatewayName"
    """<p>The name you configured for your gateway.</p>"""
    gateway_timezone: "capo_storage_gateway.types.gateway_timezone.GatewayTimezone"
    """<p>A value that indicates the time zone you want to set for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, GMT indicates Greenwich Mean Time without any offset. GMT-4:00 indicates the time is 4 hours behind GMT. GMT+2:00 indicates the time is 2 hours ahead of GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.</p>"""
    gateway_region: "capo_storage_gateway.types.region_id.RegionId"
    """<p>A value that indicates the Amazon Web Services Region where you want to store your data. The gateway Amazon Web Services Region specified must be the same Amazon Web Services Region as the Amazon Web Services Region in your <code>Host</code> header in the request. For more information about available Amazon Web Services Regions and endpoints for Storage Gateway, see <a href="https://docs.aws.amazon.com/general/latest/gr/sg.html"> Storage Gateway endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>Valid Values: See <a href="https://docs.aws.amazon.com/general/latest/gr/sg.html"> Storage Gateway endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>. </p>"""
    gateway_type: NotRequired["capo_storage_gateway.types.gateway_type.GatewayType"]
    """<p>A value that defines the type of gateway to activate. The type specified is critical to all later functions of the gateway and cannot be changed after activation. The default value is <code>CACHED</code>.</p> <important> <p>Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit <a href="https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/">this blog post</a>.</p> </important> <p>Valid Values: <code>STORED</code> | <code>CACHED</code> | <code>VTL</code> | <code>FILE_S3</code> | <code>FILE_FSX_SMB</code> </p>"""
    tape_drive_type: NotRequired[
        "capo_storage_gateway.types.tape_drive_type.TapeDriveType"
    ]
    """<p>The value that indicates the type of tape drive to use for tape gateway. This field is optional.</p> <p>Valid Values: <code>IBM-ULT3580-TD5</code> </p>"""
    medium_changer_type: NotRequired[
        "capo_storage_gateway.types.medium_changer_type.MediumChangerType"
    ]
    """<p>The value that indicates the type of medium changer to use for tape gateway. This field is optional.</p> <p>Valid Values: <code>STK-L700</code> | <code>AWS-Gateway-VTL</code> | <code>IBM-03584L32-0402</code> </p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that you can assign to the gateway. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers that can be represented in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256 characters.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivateGatewayInput) -> dict:
    out: dict = {}
    out["ActivationKey"] = value["activation_key"]
    out["GatewayName"] = value["gateway_name"]
    out["GatewayTimezone"] = value["gateway_timezone"]
    out["GatewayRegion"] = value["gateway_region"]
    if "gateway_type" in value:
        out["GatewayType"] = value["gateway_type"]
    if "tape_drive_type" in value:
        out["TapeDriveType"] = value["tape_drive_type"]
    if "medium_changer_type" in value:
        out["MediumChangerType"] = value["medium_changer_type"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActivateGatewayInput:
    out: ActivateGatewayInput = {}  # type: ignore[typeddict-item]
    if data.get("ActivationKey") is not None:
        out["activation_key"] = data["ActivationKey"]
    else:
        raise DeserializationError("ActivateGatewayInput.activation_key required")
    if data.get("GatewayName") is not None:
        out["gateway_name"] = data["GatewayName"]
    else:
        raise DeserializationError("ActivateGatewayInput.gateway_name required")
    if data.get("GatewayTimezone") is not None:
        out["gateway_timezone"] = data["GatewayTimezone"]
    else:
        raise DeserializationError("ActivateGatewayInput.gateway_timezone required")
    if data.get("GatewayRegion") is not None:
        out["gateway_region"] = data["GatewayRegion"]
    else:
        raise DeserializationError("ActivateGatewayInput.gateway_region required")
    if data.get("GatewayType") is not None:
        out["gateway_type"] = data["GatewayType"]
    if data.get("TapeDriveType") is not None:
        out["tape_drive_type"] = data["TapeDriveType"]
    if data.get("MediumChangerType") is not None:
        out["medium_changer_type"] = data["MediumChangerType"]
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
