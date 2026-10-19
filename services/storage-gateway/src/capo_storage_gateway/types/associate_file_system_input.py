"""Generated from Smithy shape ``com.amazonaws.storagegateway#AssociateFileSystemInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.audit_destination_arn
    import capo_storage_gateway.types.cache_attributes
    import capo_storage_gateway.types.client_token
    import capo_storage_gateway.types.domain_user_name
    import capo_storage_gateway.types.domain_user_password
    import capo_storage_gateway.types.endpoint_network_configuration
    import capo_storage_gateway.types.file_system_location_arn
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.tags


class AssociateFileSystemInput(TypedDict, closed=True):
    user_name: "capo_storage_gateway.types.domain_user_name.DomainUserName"
    """<p>The user name of the user credential that has permission to access the root share D$ of the Amazon FSx file system. The user account must belong to the Amazon FSx delegated admin user group.</p>"""
    password: "capo_storage_gateway.types.domain_user_password.DomainUserPassword"
    """<p>The password of the user credential.</p>"""
    client_token: "capo_storage_gateway.types.client_token.ClientToken"
    """<p>A unique string value that you supply that is used by the FSx File Gateway to ensure idempotent file system association creation.</p>"""
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    location_arn: (
        "capo_storage_gateway.types.file_system_location_arn.FileSystemLocationARN"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon FSx file system to associate with the FSx File Gateway.</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that can be assigned to the file system association. Each tag is a key-value pair.</p>"""
    audit_destination_arn: NotRequired[
        "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the storage used for the audit logs.</p>"""
    cache_attributes: NotRequired[
        "capo_storage_gateway.types.cache_attributes.CacheAttributes"
    ]
    endpoint_network_configuration: NotRequired[
        "capo_storage_gateway.types.endpoint_network_configuration.EndpointNetworkConfiguration"
    ]
    """<p>Specifies the network configuration information for the gateway associated with the Amazon FSx file system.</p> <note> <p>If multiple file systems are associated with this gateway, this parameter's <code>IpAddresses</code> field is required.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFileSystemInput) -> dict:
    out: dict = {}
    out["UserName"] = value["user_name"]
    out["Password"] = value["password"]
    out["ClientToken"] = value["client_token"]
    out["GatewayARN"] = value["gateway_arn"]
    out["LocationARN"] = value["location_arn"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "audit_destination_arn" in value:
        out["AuditDestinationARN"] = value["audit_destination_arn"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFileSystemInput:
    out: AssociateFileSystemInput = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        out["user_name"] = ""
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        out["password"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("LocationARN") is not None:
        out["location_arn"] = data["LocationARN"]
    else:
        out["location_arn"] = ""
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("AuditDestinationARN") is not None:
        out["audit_destination_arn"] = data["AuditDestinationARN"]
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
    return out


def redact_sensitive(value: AssociateFileSystemInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
