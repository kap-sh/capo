"""Generated from Smithy shape ``com.amazonaws.snowball#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.address_id
    import capo_snowball.types.cluster_id
    import capo_snowball.types.device_configuration
    import capo_snowball.types.impact_level
    import capo_snowball.types.job_resource
    import capo_snowball.types.job_type
    import capo_snowball.types.kms_key_arn
    import capo_snowball.types.long_term_pricing_id
    import capo_snowball.types.notification
    import capo_snowball.types.on_device_service_configuration
    import capo_snowball.types.pickup_details
    import capo_snowball.types.remote_management
    import capo_snowball.types.role_arn
    import capo_snowball.types.shipping_option
    import capo_snowball.types.snowball_capacity
    import capo_snowball.types.snowball_type
    import capo_snowball.types.string
    import capo_snowball.types.tax_documents


class CreateJobRequest(TypedDict, closed=True):
    job_type: NotRequired["capo_snowball.types.job_type.JobType"]
    """<p>Defines the type of job that you're creating. </p>"""
    resources: NotRequired["capo_snowball.types.job_resource.JobResource"]
    """<p>Defines the Amazon S3 buckets associated with this job.</p> <p>With <code>IMPORT</code> jobs, you specify the bucket or buckets that your transferred data will be imported into.</p> <p>With <code>EXPORT</code> jobs, you specify the bucket or buckets that your transferred data will be exported from. Optionally, you can also specify a <code>KeyRange</code> value. If you choose to export a range, you define the length of the range by providing either an inclusive <code>BeginMarker</code> value, an inclusive <code>EndMarker</code> value, or both. Ranges are UTF-8 binary sorted.</p>"""
    on_device_service_configuration: NotRequired[
        "capo_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
    ]
    """<p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family supports Amazon S3 and NFS (Network File System) and the Amazon Web Services Storage Gateway service Tape Gateway type.</p>"""
    description: NotRequired["capo_snowball.types.string.String"]
    """<p>Defines an optional description of this specific job, for example <code>Important Photos 2016-08-11</code>.</p>"""
    address_id: NotRequired["capo_snowball.types.address_id.AddressId"]
    """<p>The ID for the address that you want the Snow device shipped to.</p>"""
    kms_key_arn: NotRequired["capo_snowball.types.kms_key_arn.KmsKeyARN"]
    """<p>The <code>KmsKeyARN</code> that you want to associate with this job. <code>KmsKeyARN</code>s are created using the <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html">CreateKey</a> Key Management Service (KMS) API action.</p>"""
    role_arn: NotRequired["capo_snowball.types.role_arn.RoleARN"]
    """<p>The <code>RoleARN</code> that you want to associate with this job. <code>RoleArn</code>s are created using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html">CreateRole</a> Identity and Access Management (IAM) API action.</p>"""
    snowball_capacity_preference: NotRequired[
        "capo_snowball.types.snowball_capacity.SnowballCapacity"
    ]
    """<p>If your job is being created in one of the US regions, you have the option of specifying what size Snow device you'd like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""
    shipping_option: NotRequired["capo_snowball.types.shipping_option.ShippingOption"]
    """<p>The shipping speed for this job. This speed doesn't dictate how soon you'll get the Snow device, rather it represents how quickly the Snow device moves to its destination while in transit. Regional shipping speeds are as follows:</p> <ul> <li> <p>In Australia, you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day.</p> </li> <li> <p>In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.</p> </li> <li> <p>In India, Snow devices are delivered in one to seven days.</p> </li> <li> <p>In the US, you have access to one-day shipping and two-day shipping.</p> </li> </ul>"""
    notification: NotRequired["capo_snowball.types.notification.Notification"]
    """<p>Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.</p>"""
    cluster_id: NotRequired["capo_snowball.types.cluster_id.ClusterId"]
    """<p>The ID of a cluster. If you're creating a job for a node in a cluster, you need to provide only this <code>clusterId</code> value. The other job attributes are inherited from the cluster.</p>"""
    snowball_type: NotRequired["capo_snowball.types.snowball_type.SnowballType"]
    """<p>The type of Snow Family devices to use for this job. </p> <note> <p>For cluster jobs, Amazon Web Services Snow Family currently supports only the <code>EDGE</code> device type.</p> </note> <p>The type of Amazon Web Services Snow device to use for this job. Currently, the only supported device type for cluster jobs is <code>EDGE</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html">Snowball Edge Device Options</a> in the Snowball Edge Developer Guide.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""
    forwarding_address_id: NotRequired["capo_snowball.types.address_id.AddressId"]
    """<p>The forwarding address ID for a job. This field is not supported in most Regions.</p>"""
    tax_documents: NotRequired["capo_snowball.types.tax_documents.TaxDocuments"]
    """<p>The tax documents required in your Amazon Web Services Region.</p>"""
    device_configuration: NotRequired[
        "capo_snowball.types.device_configuration.DeviceConfiguration"
    ]
    """<p>Defines the device configuration for an Snowball Edge job.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""
    remote_management: NotRequired[
        "capo_snowball.types.remote_management.RemoteManagement"
    ]
    """<p>Allows you to securely operate and manage Snowcone devices remotely from outside of your internal network. When set to <code>INSTALLED_AUTOSTART</code>, remote management will automatically be available when the device arrives at your location. Otherwise, you need to use the Snowball Edge client to manage the device. When set to <code>NOT_INSTALLED</code>, remote management will not be available on the device. </p>"""
    long_term_pricing_id: NotRequired[
        "capo_snowball.types.long_term_pricing_id.LongTermPricingId"
    ]
    """<p>The ID of the long-term pricing type for the device.</p>"""
    impact_level: NotRequired["capo_snowball.types.impact_level.ImpactLevel"]
    """<p>The highest impact level of data that will be stored or processed on the device, provided at job creation.</p>"""
    pickup_details: NotRequired["capo_snowball.types.pickup_details.PickupDetails"]
    """<p>Information identifying the person picking up the device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateJobRequest) -> dict:
    out: dict = {}
    if "job_type" in value:
        import capo_snowball.types.job_type

        out["JobType"] = capo_snowball.types.job_type.serialize_aws_json_1_1(
            value["job_type"]
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
    if "description" in value:
        out["Description"] = value["description"]
    if "address_id" in value:
        out["AddressId"] = value["address_id"]
    if "kms_key_arn" in value:
        out["KmsKeyARN"] = value["kms_key_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "snowball_capacity_preference" in value:
        import capo_snowball.types.snowball_capacity

        out["SnowballCapacityPreference"] = (
            capo_snowball.types.snowball_capacity.serialize_aws_json_1_1(
                value["snowball_capacity_preference"]
            )
        )
    if "shipping_option" in value:
        import capo_snowball.types.shipping_option

        out["ShippingOption"] = (
            capo_snowball.types.shipping_option.serialize_aws_json_1_1(
                value["shipping_option"]
            )
        )
    if "notification" in value:
        import capo_snowball.types.notification

        out["Notification"] = capo_snowball.types.notification.serialize_aws_json_1_1(
            value["notification"]
        )
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "snowball_type" in value:
        import capo_snowball.types.snowball_type

        out["SnowballType"] = capo_snowball.types.snowball_type.serialize_aws_json_1_1(
            value["snowball_type"]
        )
    if "forwarding_address_id" in value:
        out["ForwardingAddressId"] = value["forwarding_address_id"]
    if "tax_documents" in value:
        import capo_snowball.types.tax_documents

        out["TaxDocuments"] = capo_snowball.types.tax_documents.serialize_aws_json_1_1(
            value["tax_documents"]
        )
    if "device_configuration" in value:
        import capo_snowball.types.device_configuration

        out["DeviceConfiguration"] = (
            capo_snowball.types.device_configuration.serialize_aws_json_1_1(
                value["device_configuration"]
            )
        )
    if "remote_management" in value:
        import capo_snowball.types.remote_management

        out["RemoteManagement"] = (
            capo_snowball.types.remote_management.serialize_aws_json_1_1(
                value["remote_management"]
            )
        )
    if "long_term_pricing_id" in value:
        out["LongTermPricingId"] = value["long_term_pricing_id"]
    if "impact_level" in value:
        import capo_snowball.types.impact_level

        out["ImpactLevel"] = capo_snowball.types.impact_level.serialize_aws_json_1_1(
            value["impact_level"]
        )
    if "pickup_details" in value:
        import capo_snowball.types.pickup_details

        out["PickupDetails"] = (
            capo_snowball.types.pickup_details.serialize_aws_json_1_1(
                value["pickup_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobType") is not None:
        import capo_snowball.types.job_type

        out["job_type"] = capo_snowball.types.job_type.deserialize_aws_json_1_1(
            data["JobType"]
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
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AddressId") is not None:
        out["address_id"] = data["AddressId"]
    if data.get("KmsKeyARN") is not None:
        out["kms_key_arn"] = data["KmsKeyARN"]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    if data.get("SnowballCapacityPreference") is not None:
        import capo_snowball.types.snowball_capacity

        out["snowball_capacity_preference"] = (
            capo_snowball.types.snowball_capacity.deserialize_aws_json_1_1(
                data["SnowballCapacityPreference"]
            )
        )
    if data.get("ShippingOption") is not None:
        import capo_snowball.types.shipping_option

        out["shipping_option"] = (
            capo_snowball.types.shipping_option.deserialize_aws_json_1_1(
                data["ShippingOption"]
            )
        )
    if data.get("Notification") is not None:
        import capo_snowball.types.notification

        out["notification"] = capo_snowball.types.notification.deserialize_aws_json_1_1(
            data["Notification"]
        )
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    if data.get("SnowballType") is not None:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = (
            capo_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    if data.get("ForwardingAddressId") is not None:
        out["forwarding_address_id"] = data["ForwardingAddressId"]
    if data.get("TaxDocuments") is not None:
        import capo_snowball.types.tax_documents

        out["tax_documents"] = (
            capo_snowball.types.tax_documents.deserialize_aws_json_1_1(
                data["TaxDocuments"]
            )
        )
    if data.get("DeviceConfiguration") is not None:
        import capo_snowball.types.device_configuration

        out["device_configuration"] = (
            capo_snowball.types.device_configuration.deserialize_aws_json_1_1(
                data["DeviceConfiguration"]
            )
        )
    if data.get("RemoteManagement") is not None:
        import capo_snowball.types.remote_management

        out["remote_management"] = (
            capo_snowball.types.remote_management.deserialize_aws_json_1_1(
                data["RemoteManagement"]
            )
        )
    if data.get("LongTermPricingId") is not None:
        out["long_term_pricing_id"] = data["LongTermPricingId"]
    if data.get("ImpactLevel") is not None:
        import capo_snowball.types.impact_level

        out["impact_level"] = capo_snowball.types.impact_level.deserialize_aws_json_1_1(
            data["ImpactLevel"]
        )
    if data.get("PickupDetails") is not None:
        import capo_snowball.types.pickup_details

        out["pickup_details"] = (
            capo_snowball.types.pickup_details.deserialize_aws_json_1_1(
                data["PickupDetails"]
            )
        )
    return out
