"""Generated from Smithy shape ``com.amazonaws.transfer#ProtocolDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.as2_transports
    import capo_transfer.types.passive_ip
    import capo_transfer.types.proxy_config
    import capo_transfer.types.set_stat_option
    import capo_transfer.types.sftp_ports
    import capo_transfer.types.tls_session_resumption_mode


class ProtocolDetails(TypedDict, closed=True):
    passive_ip: NotRequired["capo_transfer.types.passive_ip.PassiveIp"]
    """<p> Indicates passive mode, for FTP and FTPS protocols. Enter a single IPv4 address, such as the public IP address of a firewall, router, or load balancer. For example: </p> <p> <code>aws transfer update-server --protocol-details PassiveIp=0.0.0.0</code> </p> <p>Replace <code>0.0.0.0</code> in the example above with the actual IP address you want to use.</p> <note> <p> If you change the <code>PassiveIp</code> value, you must stop and then restart your Transfer Family server for the change to take effect. For details on using passive mode (PASV) in a NAT environment, see <a href="http://aws.amazon.com/blogs/storage/configuring-your-ftps-server-behind-a-firewall-or-nat-with-aws-transfer-family/">Configuring your FTPS server behind a firewall or NAT with Transfer Family</a>. </p> <p>Additionally, avoid placing Network Load Balancers (NLBs) or NAT gateways in front of Transfer Family servers. This configuration increases costs and can cause performance issues. When NLBs or NATs are in the communication path, Transfer Family cannot accurately recognize client IP addresses, which impacts connection sharding and limits FTPS servers to only 300 simultaneous connections instead of 10,000. If you must use an NLB, use port 21 for health checks and enable TLS session resumption by setting <code>TlsSessionResumptionMode = ENFORCED</code>. For optimal performance, migrate to VPC endpoints with Elastic IP addresses instead of using NLBs. For more details, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations"> Avoid placing NLBs and NATs in front of Transfer Family</a>. </p> </note> <p> <i>Special values</i> </p> <p>The <code>AUTO</code> and <code>0.0.0.0</code> are special values for the <code>PassiveIp</code> parameter. The value <code>PassiveIp=AUTO</code> is assigned by default to FTP and FTPS type servers. In this case, the server automatically responds with one of the endpoint IPs within the PASV response. <code>PassiveIp=0.0.0.0</code> has a more unique application for its usage. For example, if you have a High Availability (HA) Network Load Balancer (NLB) environment, where you have 3 subnets, you can only specify a single IP address using the <code>PassiveIp</code> parameter. This reduces the effectiveness of having High Availability. In this case, you can specify <code>PassiveIp=0.0.0.0</code>. This tells the client to use the same IP address as the Control connection and utilize all AZs for their connections. Note, however, that not all FTP clients support the <code>PassiveIp=0.0.0.0</code> response. FileZilla and WinSCP do support it. If you are using other clients, check to see if your client supports the <code>PassiveIp=0.0.0.0</code> response.</p>"""
    tls_session_resumption_mode: NotRequired[
        "capo_transfer.types.tls_session_resumption_mode.TlsSessionResumptionMode"
    ]
    """<p>A property used with Transfer Family servers that use the FTPS protocol. TLS Session Resumption provides a mechanism to resume or share a negotiated secret key between the control and data connection for an FTPS session. <code>TlsSessionResumptionMode</code> determines whether or not the server resumes recent, negotiated sessions through a unique session ID. This property is available during <code>CreateServer</code> and <code>UpdateServer</code> calls. If a <code>TlsSessionResumptionMode</code> value is not specified during <code>CreateServer</code>, it is set to <code>ENFORCED</code> by default.</p> <ul> <li> <p> <code>DISABLED</code>: the server does not process TLS session resumption client requests and creates a new TLS session for each request. </p> </li> <li> <p> <code>ENABLED</code>: the server processes and accepts clients that are performing TLS session resumption. The server doesn't reject client data connections that do not perform the TLS session resumption client processing.</p> </li> <li> <p> <code>ENFORCED</code>: the server processes and accepts clients that are performing TLS session resumption. The server rejects client data connections that do not perform the TLS session resumption client processing. Before you set the value to <code>ENFORCED</code>, test your clients.</p> <note> <p>Not all FTPS clients perform TLS session resumption. So, if you choose to enforce TLS session resumption, you prevent any connections from FTPS clients that don't perform the protocol negotiation. To determine whether or not you can use the <code>ENFORCED</code> value, you need to test your clients.</p> </note> </li> </ul>"""
    set_stat_option: NotRequired["capo_transfer.types.set_stat_option.SetStatOption"]
    """<p>Use the <code>SetStatOption</code> to ignore the error that is generated when the client attempts to use <code>SETSTAT</code> on a file you are uploading to an S3 bucket.</p> <p>Some SFTP file transfer clients can attempt to change the attributes of remote files, including timestamp and permissions, using commands, such as <code>SETSTAT</code> when uploading the file. However, these commands are not compatible with object storage systems, such as Amazon S3. Due to this incompatibility, file uploads from these clients can result in errors even when the file is otherwise successfully uploaded.</p> <p>Set the value to <code>ENABLE_NO_OP</code> to have the Transfer Family server ignore the <code>SETSTAT</code> command, and upload files without needing to make any changes to your SFTP client. While the <code>SetStatOption</code> <code>ENABLE_NO_OP</code> setting ignores the error, it does generate a log entry in Amazon CloudWatch Logs, so you can determine when the client is making a <code>SETSTAT</code> call.</p> <note> <p>If you want to preserve the original timestamp for your file, and modify other file attributes using <code>SETSTAT</code>, you can use Amazon EFS as backend storage with Transfer Family.</p> </note>"""
    sftp_ports: NotRequired["capo_transfer.types.sftp_ports.SftpPorts"]
    """<p>A property used with Transfer Family servers that use the SFTP protocol and have <code>PUBLIC</code> endpoints. This property accepts a list of up to three port configurations that the service opens on the server endpoint.</p> <p>Each entry in the list consists of two parameters, the <code>SftpPort</code> and the <code>CommunicationMode</code>. The <code>SftpPort</code> takes any integer from 2000 to 65535, or 22. <code>CommunicationMode</code> can be one of the following options:</p> <ul> <li> <p> <code>SERVER_TALK_FIRST</code>: The server responds to initial TCP connections first. Many older clients expect that an SFTP server responds with its server string before starting SSH negotiations.</p> </li> <li> <p> <code>CLIENT_TALK_FIRST</code>: The server responds to the initial TCP connection only after receiving a data packet. Most modern clients support this behavior and send their client string along with the initial data packets for SSH negotiation. Additionally, this mode is more resilient to TCP retransmissions that can occur during the initial TCP connection.</p> </li> </ul> <p>The following is an <code>SftpPorts</code> example for port 2222 with <code>CLIENT_TALK_FIRST</code>.</p> <p> <code>[ { "SftpPort": 2222, "CommunicationMode": "CLIENT_TALK_FIRST" } ]</code> </p> <p>If you don't specify any configurations during <code>CreateServer</code>, the service uses port 22 with <code>SERVER_TALK_FIRST</code> by default.</p>"""
    as2_transports: NotRequired["capo_transfer.types.as2_transports.As2Transports"]
    """<p>Indicates the transport method for the AS2 messages. Currently, only HTTP is supported.</p>"""
    proxy_config: NotRequired["capo_transfer.types.proxy_config.ProxyConfig"]
    """<p>The configuration for PROXY protocol version 2 (PPv2) support on the Transfer Family server. For more information, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/working-with-nlb.html">Working with Network Load Balancers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolDetails) -> dict:
    out: dict = {}
    if "passive_ip" in value:
        out["PassiveIp"] = value["passive_ip"]
    if "tls_session_resumption_mode" in value:
        import capo_transfer.types.tls_session_resumption_mode

        out["TlsSessionResumptionMode"] = (
            capo_transfer.types.tls_session_resumption_mode.serialize_aws_json_1_1(
                value["tls_session_resumption_mode"]
            )
        )
    if "set_stat_option" in value:
        import capo_transfer.types.set_stat_option

        out["SetStatOption"] = (
            capo_transfer.types.set_stat_option.serialize_aws_json_1_1(
                value["set_stat_option"]
            )
        )
    if "sftp_ports" in value:
        import capo_transfer.types.sftp_ports

        out["SftpPorts"] = capo_transfer.types.sftp_ports.serialize_aws_json_1_1(
            value["sftp_ports"]
        )
    if "as2_transports" in value:
        import capo_transfer.types.as2_transports

        out["As2Transports"] = (
            capo_transfer.types.as2_transports.serialize_aws_json_1_1(
                value["as2_transports"]
            )
        )
    if "proxy_config" in value:
        import capo_transfer.types.proxy_config

        out["ProxyConfig"] = capo_transfer.types.proxy_config.serialize_aws_json_1_1(
            value["proxy_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtocolDetails:
    out: ProtocolDetails = {}  # type: ignore[typeddict-item]
    if data.get("PassiveIp") is not None:
        out["passive_ip"] = data["PassiveIp"]
    if data.get("TlsSessionResumptionMode") is not None:
        import capo_transfer.types.tls_session_resumption_mode

        out["tls_session_resumption_mode"] = (
            capo_transfer.types.tls_session_resumption_mode.deserialize_aws_json_1_1(
                data["TlsSessionResumptionMode"]
            )
        )
    if data.get("SetStatOption") is not None:
        import capo_transfer.types.set_stat_option

        out["set_stat_option"] = (
            capo_transfer.types.set_stat_option.deserialize_aws_json_1_1(
                data["SetStatOption"]
            )
        )
    if data.get("SftpPorts") is not None:
        import capo_transfer.types.sftp_ports

        out["sftp_ports"] = capo_transfer.types.sftp_ports.deserialize_aws_json_1_1(
            data["SftpPorts"]
        )
    if data.get("As2Transports") is not None:
        import capo_transfer.types.as2_transports

        out["as2_transports"] = (
            capo_transfer.types.as2_transports.deserialize_aws_json_1_1(
                data["As2Transports"]
            )
        )
    if data.get("ProxyConfig") is not None:
        import capo_transfer.types.proxy_config

        out["proxy_config"] = capo_transfer.types.proxy_config.deserialize_aws_json_1_1(
            data["ProxyConfig"]
        )
    return out
