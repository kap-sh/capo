"""Generated from Smithy shape ``com.amazonaws.storagegateway#NFSFileShareInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.audit_destination_arn
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.cache_attributes
    import capo_storage_gateway.types.dns_host_name
    import capo_storage_gateway.types.encryption_type
    import capo_storage_gateway.types.file_share_arn
    import capo_storage_gateway.types.file_share_client_list
    import capo_storage_gateway.types.file_share_id
    import capo_storage_gateway.types.file_share_name
    import capo_storage_gateway.types.file_share_status
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.kms_key
    import capo_storage_gateway.types.location_arn
    import capo_storage_gateway.types.nfs_file_share_defaults
    import capo_storage_gateway.types.notification_policy
    import capo_storage_gateway.types.object_acl
    import capo_storage_gateway.types.path
    import capo_storage_gateway.types.region_id
    import capo_storage_gateway.types.role
    import capo_storage_gateway.types.squash
    import capo_storage_gateway.types.storage_class
    import capo_storage_gateway.types.tags


class NFSFileShareInfo(TypedDict, closed=True):
    nfs_file_share_defaults: NotRequired[
        "capo_storage_gateway.types.nfs_file_share_defaults.NFSFileShareDefaults"
    ]
    file_share_arn: NotRequired[
        "capo_storage_gateway.types.file_share_arn.FileShareARN"
    ]
    file_share_id: NotRequired["capo_storage_gateway.types.file_share_id.FileShareId"]
    file_share_status: NotRequired[
        "capo_storage_gateway.types.file_share_status.FileShareStatus"
    ]
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    encryption_type: NotRequired[
        "capo_storage_gateway.types.encryption_type.EncryptionType"
    ]
    """<p>A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note>"""
    kms_encrypted: "capo_storage_gateway.types.boolean2.Boolean2"
    """<p>Optional. Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key (SSE-KMS), or <code>false</code> to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the <code>EncryptionType</code> parameter instead.</p> <note> <p>We recommend using <code>EncryptionType</code> instead of <code>KMSEncrypted</code> to set the file share encryption method. You do not need to provide values for both parameters.</p> <p>If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if <code>EncryptionType</code> is <code>SseS3</code>, then <code>KMSEncrypted</code> must be <code>false</code>. If <code>EncryptionType</code> is <code>SseKms</code> or <code>DsseKms</code>, then <code>KMSEncrypted</code> must be <code>true</code>.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    kms_key: NotRequired["capo_storage_gateway.types.kms_key.KMSKey"]
    path: NotRequired["capo_storage_gateway.types.path.Path"]
    role: NotRequired["capo_storage_gateway.types.role.Role"]
    location_arn: NotRequired["capo_storage_gateway.types.location_arn.LocationARN"]
    default_storage_class: NotRequired[
        "capo_storage_gateway.types.storage_class.StorageClass"
    ]
    """<p>The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is <code>S3_STANDARD</code>. Optional.</p> <p>Valid Values: <code>S3_STANDARD</code> | <code>S3_INTELLIGENT_TIERING</code> | <code>S3_STANDARD_IA</code> | <code>S3_ONEZONE_IA</code> </p>"""
    object_acl: NotRequired["capo_storage_gateway.types.object_acl.ObjectACL"]
    client_list: NotRequired[
        "capo_storage_gateway.types.file_share_client_list.FileShareClientList"
    ]
    squash: NotRequired["capo_storage_gateway.types.squash.Squash"]
    read_only: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>A value that sets the write status of a file share. Set this value to <code>true</code> to set the write status to read-only, otherwise set to <code>false</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    guess_mime_type_enabled: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to <code>true</code> to enable MIME type guessing, otherwise set to <code>false</code>. The default value is <code>true</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    requester_pays: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to <code>true</code>, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.</p> <note> <p> <code>RequesterPays</code> is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.</p> </note> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags assigned to the NFS file share, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the <code>ListTagsForResource</code> API operation.</p>"""
    file_share_name: NotRequired[
        "capo_storage_gateway.types.file_share_name.FileShareName"
    ]
    """<p>The name of the file share. Optional.</p> <note> <p> <code>FileShareName</code> must be set if an S3 prefix name is set in <code>LocationARN</code>, or if an access point or access point alias is used.</p> </note>"""
    cache_attributes: NotRequired[
        "capo_storage_gateway.types.cache_attributes.CacheAttributes"
    ]
    """<p>Refresh cache information for the file share.</p>"""
    notification_policy: NotRequired[
        "capo_storage_gateway.types.notification_policy.NotificationPolicy"
    ]
    r"""<p>The notification policy of the file share. <code>SettlingTimeInSeconds</code> controls the number of seconds to wait after the last point in time a client wrote to a file before generating an <code>ObjectUploaded</code> notification. Because clients can make many small writes to files, it's best to set this parameter for as long as possible to avoid generating multiple notifications for the same file in a small time period.</p> <note> <p> <code>SettlingTimeInSeconds</code> has no effect on the timing of the object uploading to Amazon S3, only the timing of the notification.</p> <p>This setting is not meant to specify an exact time at which the notification will be sent. In some cases, the gateway might require more than the specified delay time to generate and send notifications.</p> </note> <p>The following example sets <code>NotificationPolicy</code> on with <code>SettlingTimeInSeconds</code> set to 60.</p> <p> <code>{\"Upload\": {\"SettlingTimeInSeconds\": 60}}</code> </p> <p>The following example sets <code>NotificationPolicy</code> off.</p> <p> <code>{}</code> </p>"""
    vpc_endpoint_dns_name: NotRequired[
        "capo_storage_gateway.types.dns_host_name.DNSHostName"
    ]
    """<p>Specifies the DNS name for the VPC endpoint that the NFS file share uses to connect to Amazon S3.</p> <note> <p>This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.</p> </note>"""
    bucket_region: NotRequired["capo_storage_gateway.types.region_id.RegionId"]
    """<p>Specifies the Region of the S3 bucket where the NFS file share stores files.</p> <note> <p>This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.</p> </note>"""
    audit_destination_arn: NotRequired[
        "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the storage used for audit logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NFSFileShareInfo) -> dict:
    out: dict = {}
    if "nfs_file_share_defaults" in value:
        import capo_storage_gateway.types.nfs_file_share_defaults

        out["NFSFileShareDefaults"] = (
            capo_storage_gateway.types.nfs_file_share_defaults.serialize_aws_json_1_1(
                value["nfs_file_share_defaults"]
            )
        )
    if "file_share_arn" in value:
        out["FileShareARN"] = value["file_share_arn"]
    if "file_share_id" in value:
        out["FileShareId"] = value["file_share_id"]
    if "file_share_status" in value:
        out["FileShareStatus"] = value["file_share_status"]
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "encryption_type" in value:
        import capo_storage_gateway.types.encryption_type

        out["EncryptionType"] = (
            capo_storage_gateway.types.encryption_type.serialize_aws_json_1_1(
                value["encryption_type"]
            )
        )
    out["KMSEncrypted"] = value.get("kms_encrypted", False)
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "path" in value:
        out["Path"] = value["path"]
    if "role" in value:
        out["Role"] = value["role"]
    if "location_arn" in value:
        out["LocationARN"] = value["location_arn"]
    if "default_storage_class" in value:
        out["DefaultStorageClass"] = value["default_storage_class"]
    if "object_acl" in value:
        import capo_storage_gateway.types.object_acl

        out["ObjectACL"] = capo_storage_gateway.types.object_acl.serialize_aws_json_1_1(
            value["object_acl"]
        )
    if "client_list" in value:
        import capo_storage_gateway.types.file_share_client_list

        out["ClientList"] = (
            capo_storage_gateway.types.file_share_client_list.serialize_aws_json_1_1(
                value["client_list"]
            )
        )
    if "squash" in value:
        out["Squash"] = value["squash"]
    if "read_only" in value:
        out["ReadOnly"] = value["read_only"]
    if "guess_mime_type_enabled" in value:
        out["GuessMIMETypeEnabled"] = value["guess_mime_type_enabled"]
    if "requester_pays" in value:
        out["RequesterPays"] = value["requester_pays"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "file_share_name" in value:
        out["FileShareName"] = value["file_share_name"]
    if "cache_attributes" in value:
        import capo_storage_gateway.types.cache_attributes

        out["CacheAttributes"] = (
            capo_storage_gateway.types.cache_attributes.serialize_aws_json_1_1(
                value["cache_attributes"]
            )
        )
    if "notification_policy" in value:
        out["NotificationPolicy"] = value["notification_policy"]
    if "vpc_endpoint_dns_name" in value:
        out["VPCEndpointDNSName"] = value["vpc_endpoint_dns_name"]
    if "bucket_region" in value:
        out["BucketRegion"] = value["bucket_region"]
    if "audit_destination_arn" in value:
        out["AuditDestinationARN"] = value["audit_destination_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NFSFileShareInfo:
    out: NFSFileShareInfo = {}  # type: ignore[typeddict-item]
    if data.get("NFSFileShareDefaults") is not None:
        import capo_storage_gateway.types.nfs_file_share_defaults

        out["nfs_file_share_defaults"] = (
            capo_storage_gateway.types.nfs_file_share_defaults.deserialize_aws_json_1_1(
                data["NFSFileShareDefaults"]
            )
        )
    if data.get("FileShareARN") is not None:
        out["file_share_arn"] = data["FileShareARN"]
    if data.get("FileShareId") is not None:
        out["file_share_id"] = data["FileShareId"]
    if data.get("FileShareStatus") is not None:
        out["file_share_status"] = data["FileShareStatus"]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    if data.get("EncryptionType") is not None:
        import capo_storage_gateway.types.encryption_type

        out["encryption_type"] = (
            capo_storage_gateway.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    if data.get("KMSEncrypted") is not None:
        out["kms_encrypted"] = data["KMSEncrypted"]
    else:
        out["kms_encrypted"] = False
    if data.get("KMSKey") is not None:
        out["kms_key"] = data["KMSKey"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    if data.get("LocationARN") is not None:
        out["location_arn"] = data["LocationARN"]
    if data.get("DefaultStorageClass") is not None:
        out["default_storage_class"] = data["DefaultStorageClass"]
    if data.get("ObjectACL") is not None:
        import capo_storage_gateway.types.object_acl

        out["object_acl"] = (
            capo_storage_gateway.types.object_acl.deserialize_aws_json_1_1(
                data["ObjectACL"]
            )
        )
    if data.get("ClientList") is not None:
        import capo_storage_gateway.types.file_share_client_list

        out["client_list"] = (
            capo_storage_gateway.types.file_share_client_list.deserialize_aws_json_1_1(
                data["ClientList"]
            )
        )
    if data.get("Squash") is not None:
        out["squash"] = data["Squash"]
    if data.get("ReadOnly") is not None:
        out["read_only"] = data["ReadOnly"]
    if data.get("GuessMIMETypeEnabled") is not None:
        out["guess_mime_type_enabled"] = data["GuessMIMETypeEnabled"]
    if data.get("RequesterPays") is not None:
        out["requester_pays"] = data["RequesterPays"]
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("FileShareName") is not None:
        out["file_share_name"] = data["FileShareName"]
    if data.get("CacheAttributes") is not None:
        import capo_storage_gateway.types.cache_attributes

        out["cache_attributes"] = (
            capo_storage_gateway.types.cache_attributes.deserialize_aws_json_1_1(
                data["CacheAttributes"]
            )
        )
    if data.get("NotificationPolicy") is not None:
        out["notification_policy"] = data["NotificationPolicy"]
    if data.get("VPCEndpointDNSName") is not None:
        out["vpc_endpoint_dns_name"] = data["VPCEndpointDNSName"]
    if data.get("BucketRegion") is not None:
        out["bucket_region"] = data["BucketRegion"]
    if data.get("AuditDestinationARN") is not None:
        out["audit_destination_arn"] = data["AuditDestinationARN"]
    return out
