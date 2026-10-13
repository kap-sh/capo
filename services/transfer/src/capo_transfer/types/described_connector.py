"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedConnector``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.as2_connector_config
    import capo_transfer.types.connector_egress_type
    import capo_transfer.types.connector_error_message
    import capo_transfer.types.connector_id
    import capo_transfer.types.connector_security_policy_name
    import capo_transfer.types.connector_status
    import capo_transfer.types.connectors_ip_address_type
    import capo_transfer.types.described_connector_egress_config
    import capo_transfer.types.role
    import capo_transfer.types.service_managed_egress_ip_addresses
    import capo_transfer.types.sftp_connector_config
    import capo_transfer.types.tags
    import capo_transfer.types.url


class DescribedConnector(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>The unique Amazon Resource Name (ARN) for the connector.</p>"""
    connector_id: NotRequired["capo_transfer.types.connector_id.ConnectorId"]
    """<p>The unique identifier for the connector.</p>"""
    url: NotRequired["capo_transfer.types.url.Url"]
    """<p>The URL of the partner's AS2 or SFTP endpoint.</p> <p>When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.</p>"""
    as2_config: NotRequired[
        "capo_transfer.types.as2_connector_config.As2ConnectorConfig"
    ]
    """<p>A structure that contains the parameters for an AS2 connector object.</p>"""
    access_role: NotRequired["capo_transfer.types.role.Role"]
    """<p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>"""
    logging_role: NotRequired["capo_transfer.types.role.Role"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for connectors.</p>"""
    sftp_config: NotRequired[
        "capo_transfer.types.sftp_connector_config.SftpConnectorConfig"
    ]
    """<p>A structure that contains the parameters for an SFTP connector object.</p>"""
    service_managed_egress_ip_addresses: NotRequired[
        "capo_transfer.types.service_managed_egress_ip_addresses.ServiceManagedEgressIpAddresses"
    ]
    """<p>The list of egress IP addresses of this connector. These IP addresses are assigned automatically when you create the connector.</p>"""
    security_policy_name: NotRequired[
        "capo_transfer.types.connector_security_policy_name.ConnectorSecurityPolicyName"
    ]
    """<p>The text name of the security policy for the specified connector.</p>"""
    egress_config: NotRequired[
        "capo_transfer.types.described_connector_egress_config.DescribedConnectorEgressConfig"
    ]
    """<p>Current egress configuration of the connector, showing how traffic is routed to the SFTP server. Contains VPC Lattice settings when using VPC_LATTICE egress type.</p> <p>When using the VPC_LATTICE egress type, Transfer Family uses a managed Service Network to simplify the resource sharing process.</p>"""
    egress_type: "capo_transfer.types.connector_egress_type.ConnectorEgressType"
    """<p>Type of egress configuration for the connector. SERVICE_MANAGED uses Transfer Family managed NAT gateways, while VPC_LATTICE routes traffic through customer VPCs using VPC Lattice.</p>"""
    error_message: NotRequired[
        "capo_transfer.types.connector_error_message.ConnectorErrorMessage"
    ]
    """<p>Error message providing details when the connector is in ERRORED status. Contains information to help troubleshoot connector creation or operation failures.</p>"""
    status: "capo_transfer.types.connector_status.ConnectorStatus"
    """<p>Current status of the connector. PENDING indicates creation/update in progress, ACTIVE means ready for operations, and ERRORED indicates a failure requiring attention.</p>"""
    ip_address_type: NotRequired[
        "capo_transfer.types.connectors_ip_address_type.ConnectorsIpAddressType"
    ]
    """<p>IP address type for the connector's network connections. When set to <code>IPV4</code>, the connector uses IPv4 addresses only. When set to <code>DUALSTACK</code>, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedConnector) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "connector_id" in value:
        out["ConnectorId"] = value["connector_id"]
    if "url" in value:
        out["Url"] = value["url"]
    if "as2_config" in value:
        import capo_transfer.types.as2_connector_config

        out["As2Config"] = (
            capo_transfer.types.as2_connector_config.serialize_aws_json_1_1(
                value["as2_config"]
            )
        )
    if "access_role" in value:
        out["AccessRole"] = value["access_role"]
    if "logging_role" in value:
        out["LoggingRole"] = value["logging_role"]
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    if "sftp_config" in value:
        import capo_transfer.types.sftp_connector_config

        out["SftpConfig"] = (
            capo_transfer.types.sftp_connector_config.serialize_aws_json_1_1(
                value["sftp_config"]
            )
        )
    if "service_managed_egress_ip_addresses" in value:
        import capo_transfer.types.service_managed_egress_ip_addresses

        out["ServiceManagedEgressIpAddresses"] = (
            capo_transfer.types.service_managed_egress_ip_addresses.serialize_aws_json_1_1(
                value["service_managed_egress_ip_addresses"]
            )
        )
    if "security_policy_name" in value:
        out["SecurityPolicyName"] = value["security_policy_name"]
    if "egress_config" in value:
        import capo_transfer.types.described_connector_egress_config

        out["EgressConfig"] = (
            capo_transfer.types.described_connector_egress_config.serialize_aws_json_1_1(
                value["egress_config"]
            )
        )
    import capo_transfer.types.connector_egress_type

    out["EgressType"] = (
        capo_transfer.types.connector_egress_type.serialize_aws_json_1_1(
            value.get("egress_type", "SERVICE_MANAGED")
        )
    )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    import capo_transfer.types.connector_status

    out["Status"] = capo_transfer.types.connector_status.serialize_aws_json_1_1(
        value.get("status", "ACTIVE")
    )
    if "ip_address_type" in value:
        import capo_transfer.types.connectors_ip_address_type

        out["IpAddressType"] = (
            capo_transfer.types.connectors_ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedConnector:
    out: DescribedConnector = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedConnector.arn required")
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("As2Config") is not None:
        import capo_transfer.types.as2_connector_config

        out["as2_config"] = (
            capo_transfer.types.as2_connector_config.deserialize_aws_json_1_1(
                data["As2Config"]
            )
        )
    if data.get("AccessRole") is not None:
        out["access_role"] = data["AccessRole"]
    if data.get("LoggingRole") is not None:
        out["logging_role"] = data["LoggingRole"]
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("SftpConfig") is not None:
        import capo_transfer.types.sftp_connector_config

        out["sftp_config"] = (
            capo_transfer.types.sftp_connector_config.deserialize_aws_json_1_1(
                data["SftpConfig"]
            )
        )
    if data.get("ServiceManagedEgressIpAddresses") is not None:
        import capo_transfer.types.service_managed_egress_ip_addresses

        out["service_managed_egress_ip_addresses"] = (
            capo_transfer.types.service_managed_egress_ip_addresses.deserialize_aws_json_1_1(
                data["ServiceManagedEgressIpAddresses"]
            )
        )
    if data.get("SecurityPolicyName") is not None:
        out["security_policy_name"] = data["SecurityPolicyName"]
    if data.get("EgressConfig") is not None:
        import capo_transfer.types.described_connector_egress_config

        out["egress_config"] = (
            capo_transfer.types.described_connector_egress_config.deserialize_aws_json_1_1(
                data["EgressConfig"]
            )
        )
    if data.get("EgressType") is not None:
        import capo_transfer.types.connector_egress_type

        out["egress_type"] = (
            capo_transfer.types.connector_egress_type.deserialize_aws_json_1_1(
                data["EgressType"]
            )
        )
    else:
        out["egress_type"] = "SERVICE_MANAGED"
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("Status") is not None:
        import capo_transfer.types.connector_status

        out["status"] = capo_transfer.types.connector_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        out["status"] = "ACTIVE"
    if data.get("IpAddressType") is not None:
        import capo_transfer.types.connectors_ip_address_type

        out["ip_address_type"] = (
            capo_transfer.types.connectors_ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    return out


def redact_sensitive(value: DescribedConnector) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "as2_config" in value:
        import capo_transfer.types.as2_connector_config

        out["as2_config"] = capo_transfer.types.as2_connector_config.redact_sensitive(
            value["as2_config"]
        )
    return out
