"""Generated from Smithy shape ``com.amazonaws.transfer#ProxyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.proxy_mode


class ProxyConfig(TypedDict, closed=True):
    sftp_mode: NotRequired["capo_transfer.types.proxy_mode.ProxyMode"]
    """<p>Specifies whether the Transfer Family server requires or ignores a PPv2 header containing the original client IP address on incoming SFTP connections. If you don't specify a value, the default is <code>NONE</code> </p> <ul> <li> <p> <code>NONE</code>: the server reads and ignores any PPv2 header on incoming SFTP connections. This is the default value. Use this value when your SFTP server is not behind an NLB, or when you do not need to preserve client source IP addresses through an NLB.</p> </li> <li> <p> <code>PROXY_PROTOCOL_V2_ENFORCED</code>: the server requires a valid PPv2 header on every incoming SFTP connection. When a valid header is present, the server applies it and uses the client IP address from the header. If a connection arrives without a PPv2 header, the server refuses the connection and logs an error to Amazon CloudWatch Logs indicating that the expected PPv2 header was missing. Use this value when your SFTP server is behind an NLB with PPv2 enabled on the target group.</p> <important> <p>When you enable <code>PROXY_PROTOCOL_V2_ENFORCED</code>, the server trusts the source IP address in the PPv2 header. You must configure security groups on your server's VPC endpoint to restrict inbound traffic to only the NLB's private IP addresses. For the full requirements, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/working-with-nlb.html">Working with Network Load Balancers</a>.</p> </important> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyConfig) -> dict:
    out: dict = {}
    if "sftp_mode" in value:
        import capo_transfer.types.proxy_mode

        out["SftpMode"] = capo_transfer.types.proxy_mode.serialize_aws_json_1_1(
            value["sftp_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProxyConfig:
    out: ProxyConfig = {}  # type: ignore[typeddict-item]
    if data.get("SftpMode") is not None:
        import capo_transfer.types.proxy_mode

        out["sftp_mode"] = capo_transfer.types.proxy_mode.deserialize_aws_json_1_1(
            data["SftpMode"]
        )
    return out
