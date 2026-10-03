"""Generated from Smithy shape ``com.amazonaws.snowball#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import capo_snowball.types.address_id
    import capo_snowball.types.boolean
    import capo_snowball.types.initial_cluster_size
    import capo_snowball.types.job_resource
    import capo_snowball.types.job_type
    import capo_snowball.types.kms_key_arn
    import capo_snowball.types.long_term_pricing_id_list
    import capo_snowball.types.notification
    import capo_snowball.types.on_device_service_configuration
    import capo_snowball.types.remote_management
    import capo_snowball.types.role_arn
    import capo_snowball.types.shipping_option
    import capo_snowball.types.snowball_capacity
    import capo_snowball.types.snowball_type
    import capo_snowball.types.string
    import capo_snowball.types.tax_documents


class CreateClusterRequest(TypedDict, closed=True):
    job_type: "capo_snowball.types.job_type.JobType"
    """<p>The type of job for this cluster. Currently, the only job type supported for clusters is <code>LOCAL_USE</code>.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""
    resources: NotRequired["capo_snowball.types.job_resource.JobResource"]
    """<p>The resources associated with the cluster job. These resources include Amazon S3 buckets and optional Lambda functions written in the Python language. </p>"""
    on_device_service_configuration: NotRequired[
        "capo_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
    ]
    """<p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family device clusters support Amazon S3 and NFS (Network File System).</p>"""
    description: NotRequired["capo_snowball.types.string.String"]
    """<p>An optional description of this specific cluster, for example <code>Environmental Data Cluster-01</code>.</p>"""
    address_id: "capo_snowball.types.address_id.AddressId"
    """<p>The ID for the address that you want the cluster shipped to.</p>"""
    kms_key_arn: NotRequired["capo_snowball.types.kms_key_arn.KmsKeyARN"]
    """<p>The <code>KmsKeyARN</code> value that you want to associate with this cluster. <code>KmsKeyARN</code> values are created by using the <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html">CreateKey</a> API action in Key Management Service (KMS). </p>"""
    role_arn: NotRequired["capo_snowball.types.role_arn.RoleARN"]
    """<p>The <code>RoleARN</code> that you want to associate with this cluster. <code>RoleArn</code> values are created by using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html">CreateRole</a> API action in Identity and Access Management (IAM).</p>"""
    snowball_type: "capo_snowball.types.snowball_type.SnowballType"
    """<p>The type of Snow Family devices to use for this cluster. </p> <note> <p>For cluster jobs, Amazon Web Services Snow Family currently supports only the <code>EDGE</code> device type.</p> </note> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""
    shipping_option: "capo_snowball.types.shipping_option.ShippingOption"
    """<p>The shipping speed for each node in this cluster. This speed doesn't dictate how soon you'll get each Snowball Edge device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows: </p> <ul> <li> <p>In Australia, you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day.</p> </li> <li> <p>In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.</p> </li> <li> <p>In India, Snow devices are delivered in one to seven days.</p> </li> <li> <p>In the United States of America (US), you have access to one-day shipping and two-day shipping.</p> </li> </ul> <ul> <li> <p>In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.</p> </li> <li> <p>In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.</p> </li> <li> <p>In India, Snow devices are delivered in one to seven days.</p> </li> <li> <p>In the US, you have access to one-day shipping and two-day shipping.</p> </li> </ul>"""
    notification: NotRequired["capo_snowball.types.notification.Notification"]
    """<p>The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.</p>"""
    forwarding_address_id: NotRequired["capo_snowball.types.address_id.AddressId"]
    """<p>The forwarding address ID for a cluster. This field is not supported in most regions.</p>"""
    tax_documents: NotRequired["capo_snowball.types.tax_documents.TaxDocuments"]
    """<p>The tax documents required in your Amazon Web Services Region.</p>"""
    remote_management: NotRequired[
        "capo_snowball.types.remote_management.RemoteManagement"
    ]
    """<p>Allows you to securely operate and manage Snow devices in a cluster remotely from outside of your internal network. When set to <code>INSTALLED_AUTOSTART</code>, remote management will automatically be available when the device arrives at your location. Otherwise, you need to use the Snowball Client to manage the device.</p>"""
    initial_cluster_size: NotRequired[
        "capo_snowball.types.initial_cluster_size.InitialClusterSize"
    ]
    """<p>If provided, each job will be automatically created and associated with the new cluster. If not provided, will be treated as 0.</p>"""
    force_create_jobs: "capo_snowball.types.boolean.Boolean"
    """<p>Force to create cluster when user attempts to overprovision or underprovision a cluster. A cluster is overprovisioned or underprovisioned if the initial size of the cluster is more (overprovisioned) or less (underprovisioned) than what needed to meet capacity requirement specified with <code>OnDeviceServiceConfiguration</code>.</p>"""
    long_term_pricing_ids: NotRequired[
        "capo_snowball.types.long_term_pricing_id_list.LongTermPricingIdList"
    ]
    """<p>Lists long-term pricing id that will be used to associate with jobs automatically created for the new cluster.</p>"""
    snowball_capacity_preference: NotRequired[
        "capo_snowball.types.snowball_capacity.SnowballCapacity"
    ]
    """<p>If your job is being created in one of the US regions, you have the option of specifying what size Snow device you'd like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterRequest) -> dict:
    out: dict = {}
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
    out["AddressId"] = value["address_id"]
    if "kms_key_arn" in value:
        out["KmsKeyARN"] = value["kms_key_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    import capo_snowball.types.snowball_type

    out["SnowballType"] = capo_snowball.types.snowball_type.serialize_aws_json_1_1(
        value["snowball_type"]
    )
    import capo_snowball.types.shipping_option

    out["ShippingOption"] = capo_snowball.types.shipping_option.serialize_aws_json_1_1(
        value["shipping_option"]
    )
    if "notification" in value:
        import capo_snowball.types.notification

        out["Notification"] = capo_snowball.types.notification.serialize_aws_json_1_1(
            value["notification"]
        )
    if "forwarding_address_id" in value:
        out["ForwardingAddressId"] = value["forwarding_address_id"]
    if "tax_documents" in value:
        import capo_snowball.types.tax_documents

        out["TaxDocuments"] = capo_snowball.types.tax_documents.serialize_aws_json_1_1(
            value["tax_documents"]
        )
    if "remote_management" in value:
        import capo_snowball.types.remote_management

        out["RemoteManagement"] = (
            capo_snowball.types.remote_management.serialize_aws_json_1_1(
                value["remote_management"]
            )
        )
    if "initial_cluster_size" in value:
        out["InitialClusterSize"] = value["initial_cluster_size"]
    out["ForceCreateJobs"] = value.get("force_create_jobs", False)
    if "long_term_pricing_ids" in value:
        import capo_snowball.types.long_term_pricing_id_list

        out["LongTermPricingIds"] = (
            capo_snowball.types.long_term_pricing_id_list.serialize_aws_json_1_1(
                value["long_term_pricing_ids"]
            )
        )
    if "snowball_capacity_preference" in value:
        import capo_snowball.types.snowball_capacity

        out["SnowballCapacityPreference"] = (
            capo_snowball.types.snowball_capacity.serialize_aws_json_1_1(
                value["snowball_capacity_preference"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobType") is not None:
        import capo_snowball.types.job_type

        out["job_type"] = capo_snowball.types.job_type.deserialize_aws_json_1_1(
            data["JobType"]
        )
    else:
        raise DeserializationError("CreateClusterRequest.job_type required")
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
    else:
        raise DeserializationError("CreateClusterRequest.address_id required")
    if data.get("KmsKeyARN") is not None:
        out["kms_key_arn"] = data["KmsKeyARN"]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    if data.get("SnowballType") is not None:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = (
            capo_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    else:
        raise DeserializationError("CreateClusterRequest.snowball_type required")
    if data.get("ShippingOption") is not None:
        import capo_snowball.types.shipping_option

        out["shipping_option"] = (
            capo_snowball.types.shipping_option.deserialize_aws_json_1_1(
                data["ShippingOption"]
            )
        )
    else:
        raise DeserializationError("CreateClusterRequest.shipping_option required")
    if data.get("Notification") is not None:
        import capo_snowball.types.notification

        out["notification"] = capo_snowball.types.notification.deserialize_aws_json_1_1(
            data["Notification"]
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
    if data.get("RemoteManagement") is not None:
        import capo_snowball.types.remote_management

        out["remote_management"] = (
            capo_snowball.types.remote_management.deserialize_aws_json_1_1(
                data["RemoteManagement"]
            )
        )
    if data.get("InitialClusterSize") is not None:
        out["initial_cluster_size"] = data["InitialClusterSize"]
    if data.get("ForceCreateJobs") is not None:
        out["force_create_jobs"] = data["ForceCreateJobs"]
    else:
        out["force_create_jobs"] = False
    if data.get("LongTermPricingIds") is not None:
        import capo_snowball.types.long_term_pricing_id_list

        out["long_term_pricing_ids"] = (
            capo_snowball.types.long_term_pricing_id_list.deserialize_aws_json_1_1(
                data["LongTermPricingIds"]
            )
        )
    if data.get("SnowballCapacityPreference") is not None:
        import capo_snowball.types.snowball_capacity

        out["snowball_capacity_preference"] = (
            capo_snowball.types.snowball_capacity.deserialize_aws_json_1_1(
                data["SnowballCapacityPreference"]
            )
        )
    return out
