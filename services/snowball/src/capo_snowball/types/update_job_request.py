"""Generated from Smithy shape ``com.amazonaws.snowball#UpdateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import capo_snowball.types.address_id
    import capo_snowball.types.job_id
    import capo_snowball.types.job_resource
    import capo_snowball.types.notification
    import capo_snowball.types.on_device_service_configuration
    import capo_snowball.types.pickup_details
    import capo_snowball.types.role_arn
    import capo_snowball.types.shipping_option
    import capo_snowball.types.snowball_capacity
    import capo_snowball.types.string


class UpdateJobRequest(TypedDict, closed=True):
    job_id: "capo_snowball.types.job_id.JobId"
    """<p>The job ID of the job that you want to update, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    role_arn: NotRequired["capo_snowball.types.role_arn.RoleARN"]
    """<p>The new role Amazon Resource Name (ARN) that you want to associate with this job. To create a role ARN, use the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html">CreateRole</a>Identity and Access Management (IAM) API action.</p>"""
    notification: NotRequired["capo_snowball.types.notification.Notification"]
    """<p>The new or updated <a>Notification</a> object.</p>"""
    resources: NotRequired["capo_snowball.types.job_resource.JobResource"]
    """<p>The updated <code>JobResource</code> object, or the updated <a>JobResource</a> object. </p>"""
    on_device_service_configuration: NotRequired[
        "capo_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
    ]
    """<p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family supports Amazon S3 and NFS (Network File System) and the Amazon Web Services Storage Gateway service Tape Gateway type.</p>"""
    address_id: NotRequired["capo_snowball.types.address_id.AddressId"]
    """<p>The ID of the updated <a>Address</a> object.</p>"""
    shipping_option: NotRequired["capo_snowball.types.shipping_option.ShippingOption"]
    """<p>The updated shipping option value of this job's <a>ShippingDetails</a> object.</p>"""
    description: NotRequired["capo_snowball.types.string.String"]
    """<p>The updated description of this job's <a>JobMetadata</a> object.</p>"""
    snowball_capacity_preference: NotRequired[
        "capo_snowball.types.snowball_capacity.SnowballCapacity"
    ]
    """<p>The updated <code>SnowballCapacityPreference</code> of this job's <a>JobMetadata</a> object. The 50 TB Snowballs are only available in the US regions.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""
    forwarding_address_id: NotRequired["capo_snowball.types.address_id.AddressId"]
    """<p>The updated ID for the forwarding address for a job. This field is not supported in most regions.</p>"""
    pickup_details: NotRequired["capo_snowball.types.pickup_details.PickupDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "notification" in value:
        import capo_snowball.types.notification

        out["Notification"] = capo_snowball.types.notification.serialize_aws_json_1_1(
            value["notification"]
        )
    if "resources" in value:
        import capo_snowball.types.job_resource

        out["Resources"] = capo_snowball.types.job_resource.serialize_aws_json_1_1(
            value["resources"]
        )
    if "on_device_service_configuration" in value:
        import capo_snowball.types.on_device_service_configuration

        out["OnDeviceServiceConfiguration"] = (
            capo_snowball.types.on_device_service_configuration.serialize_aws_json_1_1(
                value["on_device_service_configuration"]
            )
        )
    if "address_id" in value:
        out["AddressId"] = value["address_id"]
    if "shipping_option" in value:
        import capo_snowball.types.shipping_option

        out["ShippingOption"] = (
            capo_snowball.types.shipping_option.serialize_aws_json_1_1(
                value["shipping_option"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "snowball_capacity_preference" in value:
        import capo_snowball.types.snowball_capacity

        out["SnowballCapacityPreference"] = (
            capo_snowball.types.snowball_capacity.serialize_aws_json_1_1(
                value["snowball_capacity_preference"]
            )
        )
    if "forwarding_address_id" in value:
        out["ForwardingAddressId"] = value["forwarding_address_id"]
    if "pickup_details" in value:
        import capo_snowball.types.pickup_details

        out["PickupDetails"] = (
            capo_snowball.types.pickup_details.serialize_aws_json_1_1(
                value["pickup_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJobRequest:
    out: UpdateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("UpdateJobRequest.job_id required")
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    if data.get("Notification") is not None:
        import capo_snowball.types.notification

        out["notification"] = capo_snowball.types.notification.deserialize_aws_json_1_1(
            data["Notification"]
        )
    if data.get("Resources") is not None:
        import capo_snowball.types.job_resource

        out["resources"] = capo_snowball.types.job_resource.deserialize_aws_json_1_1(
            data["Resources"]
        )
    if data.get("OnDeviceServiceConfiguration") is not None:
        import capo_snowball.types.on_device_service_configuration

        out["on_device_service_configuration"] = (
            capo_snowball.types.on_device_service_configuration.deserialize_aws_json_1_1(
                data["OnDeviceServiceConfiguration"]
            )
        )
    if data.get("AddressId") is not None:
        out["address_id"] = data["AddressId"]
    if data.get("ShippingOption") is not None:
        import capo_snowball.types.shipping_option

        out["shipping_option"] = (
            capo_snowball.types.shipping_option.deserialize_aws_json_1_1(
                data["ShippingOption"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SnowballCapacityPreference") is not None:
        import capo_snowball.types.snowball_capacity

        out["snowball_capacity_preference"] = (
            capo_snowball.types.snowball_capacity.deserialize_aws_json_1_1(
                data["SnowballCapacityPreference"]
            )
        )
    if data.get("ForwardingAddressId") is not None:
        out["forwarding_address_id"] = data["ForwardingAddressId"]
    if data.get("PickupDetails") is not None:
        import capo_snowball.types.pickup_details

        out["pickup_details"] = (
            capo_snowball.types.pickup_details.deserialize_aws_json_1_1(
                data["PickupDetails"]
            )
        )
    return out
