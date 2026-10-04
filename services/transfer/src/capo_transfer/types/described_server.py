"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.certificate
    import capo_transfer.types.domain
    import capo_transfer.types.endpoint_details
    import capo_transfer.types.endpoint_type
    import capo_transfer.types.host_key_fingerprint
    import capo_transfer.types.identity_provider_details
    import capo_transfer.types.identity_provider_type
    import capo_transfer.types.ip_address_type
    import capo_transfer.types.nullable_role
    import capo_transfer.types.post_authentication_login_banner
    import capo_transfer.types.pre_authentication_login_banner
    import capo_transfer.types.protocol_details
    import capo_transfer.types.protocols
    import capo_transfer.types.s3_storage_options
    import capo_transfer.types.security_policy_name
    import capo_transfer.types.server_id
    import capo_transfer.types.service_managed_egress_ip_addresses
    import capo_transfer.types.state
    import capo_transfer.types.structured_log_destinations
    import capo_transfer.types.tags
    import capo_transfer.types.user_count
    import capo_transfer.types.workflow_details


class DescribedServer(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>Specifies the unique Amazon Resource Name (ARN) of the server.</p>"""
    certificate: NotRequired["capo_transfer.types.certificate.Certificate"]
    """<p>Specifies the ARN of the Amazon Web ServicesCertificate Manager (ACM) certificate. Required when <code>Protocols</code> is set to <code>FTPS</code>.</p>"""
    protocol_details: NotRequired[
        "capo_transfer.types.protocol_details.ProtocolDetails"
    ]
    """<p>The protocol settings that are configured for your server.</p> <note> <p>Avoid placing Network Load Balancers (NLBs) or NAT gateways in front of Transfer Family servers, as this increases costs and can cause performance issues, including reduced connection limits for FTPS. For more details, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations"> Avoid placing NLBs and NATs in front of Transfer Family</a>.</p> </note> <ul> <li> <p> To indicate passive mode (for FTP and FTPS protocols), use the <code>PassiveIp</code> parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. </p> </li> <li> <p>To ignore the error that is generated when the client attempts to use the <code>SETSTAT</code> command on a file that you are uploading to an Amazon S3 bucket, use the <code>SetStatOption</code> parameter. To have the Transfer Family server ignore the <code>SETSTAT</code> command and upload files without needing to make any changes to your SFTP client, set the value to <code>ENABLE_NO_OP</code>. If you set the <code>SetStatOption</code> parameter to <code>ENABLE_NO_OP</code>, Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a <code>SETSTAT</code> call.</p> </li> <li> <p>To specify which ports your Transfer Family server listens to, use the <code>SftpPorts</code> parameter.</p> </li> <li> <p>To determine whether your Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the <code>TlsSessionResumptionMode</code> parameter.</p> </li> <li> <p> <code>As2Transports</code> indicates the transport method for the AS2 messages. Currently, only HTTP is supported.</p> </li> </ul>"""
    domain: NotRequired["capo_transfer.types.domain.Domain"]
    """<p>Specifies the domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.</p>"""
    endpoint_details: NotRequired[
        "capo_transfer.types.endpoint_details.EndpointDetails"
    ]
    """<p>The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.</p>"""
    endpoint_type: NotRequired["capo_transfer.types.endpoint_type.EndpointType"]
    """<p>Defines the type of endpoint that your server is connected to. If your server is connected to a VPC endpoint, your server isn't accessible over the public internet.</p>"""
    host_key_fingerprint: NotRequired[
        "capo_transfer.types.host_key_fingerprint.HostKeyFingerprint"
    ]
    """<p>Specifies the Base64-encoded SHA256 fingerprint of the server's host key. This value is equivalent to the output of the <code>ssh-keygen -l -f my-new-server-key</code> command.</p>"""
    identity_provider_details: NotRequired[
        "capo_transfer.types.identity_provider_details.IdentityProviderDetails"
    ]
    """<p>Specifies information to call a customer-supplied authentication API. This field is not populated when the <code>IdentityProviderType</code> of a server is <code>AWS_DIRECTORY_SERVICE</code> or <code>SERVICE_MANAGED</code>.</p>"""
    identity_provider_type: NotRequired[
        "capo_transfer.types.identity_provider_type.IdentityProviderType"
    ]
    """<p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>"""
    logging_role: NotRequired["capo_transfer.types.nullable_role.NullableRole"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>"""
    post_authentication_login_banner: NotRequired[
        "capo_transfer.types.post_authentication_login_banner.PostAuthenticationLoginBanner"
    ]
    """<p>Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.</p> <note> <p>The SFTP protocol does not support post-authentication display banners.</p> </note>"""
    pre_authentication_login_banner: NotRequired[
        "capo_transfer.types.pre_authentication_login_banner.PreAuthenticationLoginBanner"
    ]
    """<p>Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:</p> <p> <code>This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.</code> </p>"""
    protocols: NotRequired["capo_transfer.types.protocols.Protocols"]
    """<p>Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:</p> <ul> <li> <p> <code>SFTP</code> (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH</p> </li> <li> <p> <code>FTPS</code> (File Transfer Protocol Secure): File transfer with TLS encryption</p> </li> <li> <p> <code>FTP</code> (File Transfer Protocol): Unencrypted file transfer</p> </li> <li> <p> <code>AS2</code> (Applicability Statement 2): used for transporting structured business-to-business data</p> </li> </ul> <note> <ul> <li> <p>If you select <code>FTPS</code>, you must choose a certificate stored in Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.</p> </li> <li> <p>If <code>Protocol</code> includes either <code>FTP</code> or <code>FTPS</code>, then the <code>EndpointType</code> must be <code>VPC</code> and the <code>IdentityProviderType</code> must be either <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>FTP</code>, then <code>AddressAllocationIds</code> cannot be associated.</p> </li> <li> <p>If <code>Protocol</code> is set only to <code>SFTP</code>, the <code>EndpointType</code> can be set to <code>PUBLIC</code> and the <code>IdentityProviderType</code> can be set any of the supported identity types: <code>SERVICE_MANAGED</code>, <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>AS2</code>, then the <code>EndpointType</code> must be <code>VPC</code>, and domain must be Amazon S3.</p> </li> </ul> </note>"""
    security_policy_name: NotRequired[
        "capo_transfer.types.security_policy_name.SecurityPolicyName"
    ]
    """<p>Specifies the name of the security policy for the server.</p>"""
    server_id: NotRequired["capo_transfer.types.server_id.ServerId"]
    """<p>Specifies the unique system-assigned identifier for a server that you instantiate.</p>"""
    state: NotRequired["capo_transfer.types.state.State"]
    """<p>The condition of the server that was described. A value of <code>ONLINE</code> indicates that the server can accept jobs and transfer files. A <code>State</code> value of <code>OFFLINE</code> means that the server cannot perform file transfer operations.</p> <p>The states of <code>STARTING</code> and <code>STOPPING</code> indicate that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of <code>START_FAILED</code> or <code>STOP_FAILED</code> can indicate an error condition.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Specifies the key-value pairs that you can use to search for and group servers that were assigned to the server that was described.</p>"""
    user_count: NotRequired["capo_transfer.types.user_count.UserCount"]
    """<p>Specifies the number of users that are assigned to a server you specified with the <code>ServerId</code>.</p>"""
    workflow_details: NotRequired[
        "capo_transfer.types.workflow_details.WorkflowDetails"
    ]
    """<p>Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.</p> <p>In addition to a workflow to execute when a file is uploaded completely, <code>WorkflowDetails</code> can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.</p>"""
    structured_log_destinations: NotRequired[
        "capo_transfer.types.structured_log_destinations.StructuredLogDestinations"
    ]
    """<p>Specifies the log groups to which your server logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:partition:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p> <p>If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an <code>update-server</code> call. For example:</p> <p> <code>update-server --server-id s-1234567890abcdef0 --structured-log-destinations</code> </p>"""
    s3_storage_options: NotRequired[
        "capo_transfer.types.s3_storage_options.S3StorageOptions"
    ]
    """<p>Specifies whether or not performance for your Amazon S3 directories is optimized.</p> <ul> <li> <p>If using the console, this is enabled by default.</p> </li> <li> <p>If using the API or CLI, this is disabled by default.</p> </li> </ul> <p>By default, home directory mappings have a <code>TYPE</code> of <code>DIRECTORY</code>. If you enable this option, you would then need to explicitly set the <code>HomeDirectoryMapEntry</code> <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p>"""
    as2_service_managed_egress_ip_addresses: NotRequired[
        "capo_transfer.types.service_managed_egress_ip_addresses.ServiceManagedEgressIpAddresses"
    ]
    """<p>The list of egress IP addresses of this server. These IP addresses are only relevant for servers that use the AS2 protocol. They are used for sending asynchronous MDNs.</p> <p>These IP addresses are assigned automatically when you create an AS2 server. Additionally, if you update an existing server and add the AS2 protocol, static IP addresses are assigned as well.</p>"""
    ip_address_type: NotRequired["capo_transfer.types.ip_address_type.IpAddressType"]
    """<p>Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your Transfer Family endpoint. The default value is <code>IPV4</code>.</p> <important> <p>The <code>IpAddressType</code> parameter has the following limitations:</p> <ul> <li> <p>It cannot be changed while the server is online. You must stop the server before modifying this parameter.</p> </li> <li> <p>It cannot be updated to <code>DUALSTACK</code> if the server has <code>AddressAllocationIds</code> specified.</p> </li> </ul> </important> <note> <p>When using <code>DUALSTACK</code> as the <code>IpAddressType</code>, you cannot set the <code>AddressAllocationIds</code> parameter for the <a href="https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html">EndpointDetails</a> for the server.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedServer) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "protocol_details" in value:
        import capo_transfer.types.protocol_details

        out["ProtocolDetails"] = (
            capo_transfer.types.protocol_details.serialize_aws_json_1_1(
                value["protocol_details"]
            )
        )
    if "domain" in value:
        import capo_transfer.types.domain

        out["Domain"] = capo_transfer.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    if "endpoint_details" in value:
        import capo_transfer.types.endpoint_details

        out["EndpointDetails"] = (
            capo_transfer.types.endpoint_details.serialize_aws_json_1_1(
                value["endpoint_details"]
            )
        )
    if "endpoint_type" in value:
        import capo_transfer.types.endpoint_type

        out["EndpointType"] = capo_transfer.types.endpoint_type.serialize_aws_json_1_1(
            value["endpoint_type"]
        )
    if "host_key_fingerprint" in value:
        out["HostKeyFingerprint"] = value["host_key_fingerprint"]
    if "identity_provider_details" in value:
        import capo_transfer.types.identity_provider_details

        out["IdentityProviderDetails"] = (
            capo_transfer.types.identity_provider_details.serialize_aws_json_1_1(
                value["identity_provider_details"]
            )
        )
    if "identity_provider_type" in value:
        import capo_transfer.types.identity_provider_type

        out["IdentityProviderType"] = (
            capo_transfer.types.identity_provider_type.serialize_aws_json_1_1(
                value["identity_provider_type"]
            )
        )
    if "logging_role" in value:
        out["LoggingRole"] = value["logging_role"]
    if "post_authentication_login_banner" in value:
        out["PostAuthenticationLoginBanner"] = value["post_authentication_login_banner"]
    if "pre_authentication_login_banner" in value:
        out["PreAuthenticationLoginBanner"] = value["pre_authentication_login_banner"]
    if "protocols" in value:
        import capo_transfer.types.protocols

        out["Protocols"] = capo_transfer.types.protocols.serialize_aws_json_1_1(
            value["protocols"]
        )
    if "security_policy_name" in value:
        out["SecurityPolicyName"] = value["security_policy_name"]
    if "server_id" in value:
        out["ServerId"] = value["server_id"]
    if "state" in value:
        import capo_transfer.types.state

        out["State"] = capo_transfer.types.state.serialize_aws_json_1_1(value["state"])
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    if "user_count" in value:
        out["UserCount"] = value["user_count"]
    if "workflow_details" in value:
        import capo_transfer.types.workflow_details

        out["WorkflowDetails"] = (
            capo_transfer.types.workflow_details.serialize_aws_json_1_1(
                value["workflow_details"]
            )
        )
    if "structured_log_destinations" in value:
        import capo_transfer.types.structured_log_destinations

        out["StructuredLogDestinations"] = (
            capo_transfer.types.structured_log_destinations.serialize_aws_json_1_1(
                value["structured_log_destinations"]
            )
        )
    if "s3_storage_options" in value:
        import capo_transfer.types.s3_storage_options

        out["S3StorageOptions"] = (
            capo_transfer.types.s3_storage_options.serialize_aws_json_1_1(
                value["s3_storage_options"]
            )
        )
    if "as2_service_managed_egress_ip_addresses" in value:
        import capo_transfer.types.service_managed_egress_ip_addresses

        out["As2ServiceManagedEgressIpAddresses"] = (
            capo_transfer.types.service_managed_egress_ip_addresses.serialize_aws_json_1_1(
                value["as2_service_managed_egress_ip_addresses"]
            )
        )
    if "ip_address_type" in value:
        import capo_transfer.types.ip_address_type

        out["IpAddressType"] = (
            capo_transfer.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedServer:
    out: DescribedServer = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedServer.arn required")
    if data.get("Certificate") is not None:
        out["certificate"] = data["Certificate"]
    if data.get("ProtocolDetails") is not None:
        import capo_transfer.types.protocol_details

        out["protocol_details"] = (
            capo_transfer.types.protocol_details.deserialize_aws_json_1_1(
                data["ProtocolDetails"]
            )
        )
    if data.get("Domain") is not None:
        import capo_transfer.types.domain

        out["domain"] = capo_transfer.types.domain.deserialize_aws_json_1_1(
            data["Domain"]
        )
    if data.get("EndpointDetails") is not None:
        import capo_transfer.types.endpoint_details

        out["endpoint_details"] = (
            capo_transfer.types.endpoint_details.deserialize_aws_json_1_1(
                data["EndpointDetails"]
            )
        )
    if data.get("EndpointType") is not None:
        import capo_transfer.types.endpoint_type

        out["endpoint_type"] = (
            capo_transfer.types.endpoint_type.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    if data.get("HostKeyFingerprint") is not None:
        out["host_key_fingerprint"] = data["HostKeyFingerprint"]
    if data.get("IdentityProviderDetails") is not None:
        import capo_transfer.types.identity_provider_details

        out["identity_provider_details"] = (
            capo_transfer.types.identity_provider_details.deserialize_aws_json_1_1(
                data["IdentityProviderDetails"]
            )
        )
    if data.get("IdentityProviderType") is not None:
        import capo_transfer.types.identity_provider_type

        out["identity_provider_type"] = (
            capo_transfer.types.identity_provider_type.deserialize_aws_json_1_1(
                data["IdentityProviderType"]
            )
        )
    if data.get("LoggingRole") is not None:
        out["logging_role"] = data["LoggingRole"]
    if data.get("PostAuthenticationLoginBanner") is not None:
        out["post_authentication_login_banner"] = data["PostAuthenticationLoginBanner"]
    if data.get("PreAuthenticationLoginBanner") is not None:
        out["pre_authentication_login_banner"] = data["PreAuthenticationLoginBanner"]
    if data.get("Protocols") is not None:
        import capo_transfer.types.protocols

        out["protocols"] = capo_transfer.types.protocols.deserialize_aws_json_1_1(
            data["Protocols"]
        )
    if data.get("SecurityPolicyName") is not None:
        out["security_policy_name"] = data["SecurityPolicyName"]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    if data.get("State") is not None:
        import capo_transfer.types.state

        out["state"] = capo_transfer.types.state.deserialize_aws_json_1_1(data["State"])
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("UserCount") is not None:
        out["user_count"] = data["UserCount"]
    if data.get("WorkflowDetails") is not None:
        import capo_transfer.types.workflow_details

        out["workflow_details"] = (
            capo_transfer.types.workflow_details.deserialize_aws_json_1_1(
                data["WorkflowDetails"]
            )
        )
    if data.get("StructuredLogDestinations") is not None:
        import capo_transfer.types.structured_log_destinations

        out["structured_log_destinations"] = (
            capo_transfer.types.structured_log_destinations.deserialize_aws_json_1_1(
                data["StructuredLogDestinations"]
            )
        )
    if data.get("S3StorageOptions") is not None:
        import capo_transfer.types.s3_storage_options

        out["s3_storage_options"] = (
            capo_transfer.types.s3_storage_options.deserialize_aws_json_1_1(
                data["S3StorageOptions"]
            )
        )
    if data.get("As2ServiceManagedEgressIpAddresses") is not None:
        import capo_transfer.types.service_managed_egress_ip_addresses

        out["as2_service_managed_egress_ip_addresses"] = (
            capo_transfer.types.service_managed_egress_ip_addresses.deserialize_aws_json_1_1(
                data["As2ServiceManagedEgressIpAddresses"]
            )
        )
    if data.get("IpAddressType") is not None:
        import capo_transfer.types.ip_address_type

        out["ip_address_type"] = (
            capo_transfer.types.ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    return out
