"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileSystemAssociationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.audit_destination_arn
    import capo_storage_gateway.types.cache_attributes
    import capo_storage_gateway.types.endpoint_network_configuration
    import capo_storage_gateway.types.file_system_association_arn
    import capo_storage_gateway.types.file_system_association_status
    import capo_storage_gateway.types.file_system_association_status_details
    import capo_storage_gateway.types.file_system_location_arn
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.tags


class FileSystemAssociationInfo(TypedDict, closed=True):
    file_system_association_arn: NotRequired[
        "capo_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the file system association.</p>"""
    location_arn: NotRequired[
        "capo_storage_gateway.types.file_system_location_arn.FileSystemLocationARN"
    ]
    """<p>The ARN of the backend Amazon FSx file system used for storing file data. For information, see <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_FileSystem.html">FileSystem</a> in the <i>Amazon FSx API Reference</i>.</p>"""
    file_system_association_status: NotRequired[
        "capo_storage_gateway.types.file_system_association_status.FileSystemAssociationStatus"
    ]
    """<p>The status of the file system association. Valid Values: <code>AVAILABLE</code> | <code>CREATING</code> | <code>DELETING</code> | <code>FORCE_DELETING</code> | <code>UPDATING</code> | <code>ERROR</code> </p>"""
    audit_destination_arn: NotRequired[
        "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the storage used for the audit logs.</p>"""
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags assigned to the SMB file share, sorted alphabetically by key name. Each tag is a key-value pair.</p>"""
    cache_attributes: NotRequired[
        "capo_storage_gateway.types.cache_attributes.CacheAttributes"
    ]
    endpoint_network_configuration: NotRequired[
        "capo_storage_gateway.types.endpoint_network_configuration.EndpointNetworkConfiguration"
    ]
    """<p>Specifies network configuration information for the gateway associated with the Amazon FSx file system.</p> <note> <p>If multiple file systems are associated with this gateway, this parameter's <code>IpAddresses</code> field is required.</p> </note>"""
    file_system_association_status_details: NotRequired[
        "capo_storage_gateway.types.file_system_association_status_details.FileSystemAssociationStatusDetails"
    ]
    """<p>An array containing the FileSystemAssociationStatusDetail data type, which provides detailed information on file system association status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemAssociationInfo) -> dict:
    out: dict = {}
    if "file_system_association_arn" in value:
        out["FileSystemAssociationARN"] = value["file_system_association_arn"]
    if "location_arn" in value:
        out["LocationARN"] = value["location_arn"]
    if "file_system_association_status" in value:
        out["FileSystemAssociationStatus"] = value["file_system_association_status"]
    if "audit_destination_arn" in value:
        out["AuditDestinationARN"] = value["audit_destination_arn"]
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "cache_attributes" in value:
        import capo_storage_gateway.types.cache_attributes

        out["CacheAttributes"] = (
            capo_storage_gateway.types.cache_attributes.serialize_aws_json_1_1(
                value["cache_attributes"]
            )
        )
    if "endpoint_network_configuration" in value:
        import capo_storage_gateway.types.endpoint_network_configuration

        out["EndpointNetworkConfiguration"] = (
            capo_storage_gateway.types.endpoint_network_configuration.serialize_aws_json_1_1(
                value["endpoint_network_configuration"]
            )
        )
    if "file_system_association_status_details" in value:
        import capo_storage_gateway.types.file_system_association_status_details

        out["FileSystemAssociationStatusDetails"] = (
            capo_storage_gateway.types.file_system_association_status_details.serialize_aws_json_1_1(
                value["file_system_association_status_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemAssociationInfo:
    out: FileSystemAssociationInfo = {}  # type: ignore[typeddict-item]
    if data.get("FileSystemAssociationARN") is not None:
        out["file_system_association_arn"] = data["FileSystemAssociationARN"]
    if data.get("LocationARN") is not None:
        out["location_arn"] = data["LocationARN"]
    if data.get("FileSystemAssociationStatus") is not None:
        out["file_system_association_status"] = data["FileSystemAssociationStatus"]
    if data.get("AuditDestinationARN") is not None:
        out["audit_destination_arn"] = data["AuditDestinationARN"]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("CacheAttributes") is not None:
        import capo_storage_gateway.types.cache_attributes

        out["cache_attributes"] = (
            capo_storage_gateway.types.cache_attributes.deserialize_aws_json_1_1(
                data["CacheAttributes"]
            )
        )
    if data.get("EndpointNetworkConfiguration") is not None:
        import capo_storage_gateway.types.endpoint_network_configuration

        out["endpoint_network_configuration"] = (
            capo_storage_gateway.types.endpoint_network_configuration.deserialize_aws_json_1_1(
                data["EndpointNetworkConfiguration"]
            )
        )
    if data.get("FileSystemAssociationStatusDetails") is not None:
        import capo_storage_gateway.types.file_system_association_status_details

        out["file_system_association_status_details"] = (
            capo_storage_gateway.types.file_system_association_status_details.deserialize_aws_json_1_1(
                data["FileSystemAssociationStatusDetails"]
            )
        )
    return out
