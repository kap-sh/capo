"""Generated from Smithy shape ``com.amazonaws.snowball#ClusterMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.address_id
    import capo_snowball.types.cluster_state
    import capo_snowball.types.job_resource
    import capo_snowball.types.job_type
    import capo_snowball.types.kms_key_arn
    import capo_snowball.types.notification
    import capo_snowball.types.on_device_service_configuration
    import capo_snowball.types.role_arn
    import capo_snowball.types.shipping_option
    import capo_snowball.types.snowball_type
    import capo_snowball.types.string
    import capo_snowball.types.tax_documents
    import capo_snowball.types.timestamp


class ClusterMetadata(TypedDict, closed=True):
    cluster_id: NotRequired["capo_snowball.types.string.String"]
    """<p>The automatically generated ID for a cluster.</p>"""
    description: NotRequired["capo_snowball.types.string.String"]
    """<p>The optional description of the cluster.</p>"""
    kms_key_arn: NotRequired["capo_snowball.types.kms_key_arn.KmsKeyARN"]
    """<p>The <code>KmsKeyARN</code> Amazon Resource Name (ARN) associated with this cluster. This ARN was created using the <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html">CreateKey</a> API action in Key Management Service (KMS.</p>"""
    role_arn: NotRequired["capo_snowball.types.role_arn.RoleARN"]
    """<p>The role ARN associated with this cluster. This ARN was created using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html">CreateRole</a> API action in Identity and Access Management (IAM).</p>"""
    cluster_state: NotRequired["capo_snowball.types.cluster_state.ClusterState"]
    """<p>The current status of the cluster.</p>"""
    job_type: NotRequired["capo_snowball.types.job_type.JobType"]
    """<p>The type of job for this cluster. Currently, the only job type supported for clusters is <code>LOCAL_USE</code>.</p>"""
    snowball_type: NotRequired["capo_snowball.types.snowball_type.SnowballType"]
    """<p>The type of Snowball Edge device to use for this cluster. </p> <note> <p>For cluster jobs, Amazon Web Services Snow Family currently supports only the <code>EDGE</code> device type.</p> </note>"""
    creation_date: NotRequired["capo_snowball.types.timestamp.Timestamp"]
    """<p>The creation date for this cluster.</p>"""
    resources: NotRequired["capo_snowball.types.job_resource.JobResource"]
    """<p>The arrays of <a>JobResource</a> objects that can include updated <a>S3Resource</a> objects or <a>LambdaResource</a> objects.</p>"""
    address_id: NotRequired["capo_snowball.types.address_id.AddressId"]
    """<p>The automatically generated ID for a specific address.</p>"""
    shipping_option: NotRequired["capo_snowball.types.shipping_option.ShippingOption"]
    """<p>The shipping speed for each node in this cluster. This speed doesn't dictate how soon you'll get each device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows:</p> <ul> <li> <p>In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.</p> </li> <li> <p>In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.</p> </li> <li> <p>In India, Snow devices are delivered in one to seven days.</p> </li> <li> <p>In the US, you have access to one-day shipping and two-day shipping.</p> </li> </ul>"""
    notification: NotRequired["capo_snowball.types.notification.Notification"]
    """<p>The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.</p>"""
    forwarding_address_id: NotRequired["capo_snowball.types.address_id.AddressId"]
    """<p>The ID of the address that you want a cluster shipped to, after it will be shipped to its primary address. This field is not supported in most regions.</p>"""
    tax_documents: NotRequired["capo_snowball.types.tax_documents.TaxDocuments"]
    """<p>The tax documents required in your Amazon Web Services Region.</p>"""
    on_device_service_configuration: NotRequired[
        "capo_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
    ]
    """<p>Represents metadata and configuration settings for services on an Amazon Web Services Snow Family device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterMetadata) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key_arn" in value:
        out["KmsKeyARN"] = value["kms_key_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "cluster_state" in value:
        import capo_snowball.types.cluster_state

        out["ClusterState"] = capo_snowball.types.cluster_state.serialize_aws_json_1_1(
            value["cluster_state"]
        )
    if "job_type" in value:
        import capo_snowball.types.job_type

        out["JobType"] = capo_snowball.types.job_type.serialize_aws_json_1_1(
            value["job_type"]
        )
    if "snowball_type" in value:
        import capo_snowball.types.snowball_type

        out["SnowballType"] = capo_snowball.types.snowball_type.serialize_aws_json_1_1(
            value["snowball_type"]
        )
    if "creation_date" in value:
        import capo_snowball.types.timestamp

        out["CreationDate"] = capo_snowball.types.timestamp.serialize_aws_json_1_1(
            value["creation_date"]
        )
    if "resources" in value:
        import capo_snowball.types.job_resource

        out["Resources"] = capo_snowball.types.job_resource.serialize_aws_json_1_1(
            value["resources"]
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
    if "on_device_service_configuration" in value:
        import capo_snowball.types.on_device_service_configuration

        out["OnDeviceServiceConfiguration"] = (
            capo_snowball.types.on_device_service_configuration.serialize_aws_json_1_1(
                value["on_device_service_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterMetadata:
    out: ClusterMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KmsKeyARN") is not None:
        out["kms_key_arn"] = data["KmsKeyARN"]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    if data.get("ClusterState") is not None:
        import capo_snowball.types.cluster_state

        out["cluster_state"] = (
            capo_snowball.types.cluster_state.deserialize_aws_json_1_1(
                data["ClusterState"]
            )
        )
    if data.get("JobType") is not None:
        import capo_snowball.types.job_type

        out["job_type"] = capo_snowball.types.job_type.deserialize_aws_json_1_1(
            data["JobType"]
        )
    if data.get("SnowballType") is not None:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = (
            capo_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    if data.get("CreationDate") is not None:
        import capo_snowball.types.timestamp

        out["creation_date"] = capo_snowball.types.timestamp.deserialize_aws_json_1_1(
            data["CreationDate"]
        )
    if data.get("Resources") is not None:
        import capo_snowball.types.job_resource

        out["resources"] = capo_snowball.types.job_resource.deserialize_aws_json_1_1(
            data["Resources"]
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
    if data.get("OnDeviceServiceConfiguration") is not None:
        import capo_snowball.types.on_device_service_configuration

        out["on_device_service_configuration"] = (
            capo_snowball.types.on_device_service_configuration.deserialize_aws_json_1_1(
                data["OnDeviceServiceConfiguration"]
            )
        )
    return out
