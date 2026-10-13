"""Generated from Smithy shape ``com.amazonaws.transfer#TestIdentityProviderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.protocol
    import capo_transfer.types.server_id
    import capo_transfer.types.source_ip
    import capo_transfer.types.user_name
    import capo_transfer.types.user_password


class TestIdentityProviderRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned identifier for a specific server. That server's user authentication method is tested with a user name and password.</p>"""
    server_protocol: NotRequired["capo_transfer.types.protocol.Protocol"]
    """<p>The type of file transfer protocol to be tested.</p> <p>The available protocols are:</p> <ul> <li> <p>Secure Shell (SSH) File Transfer Protocol (SFTP)</p> </li> <li> <p>File Transfer Protocol Secure (FTPS)</p> </li> <li> <p>File Transfer Protocol (FTP)</p> </li> <li> <p>Applicability Statement 2 (AS2)</p> </li> </ul>"""
    source_ip: NotRequired["capo_transfer.types.source_ip.SourceIp"]
    """<p>The source IP address of the account to be tested.</p>"""
    user_name: "capo_transfer.types.user_name.UserName"
    """<p>The name of the account to be tested.</p>"""
    user_password: NotRequired["capo_transfer.types.user_password.UserPassword"]
    """<p>The password of the account to be tested.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestIdentityProviderRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    if "server_protocol" in value:
        import capo_transfer.types.protocol

        out["ServerProtocol"] = capo_transfer.types.protocol.serialize_aws_json_1_1(
            value["server_protocol"]
        )
    if "source_ip" in value:
        out["SourceIp"] = value["source_ip"]
    out["UserName"] = value["user_name"]
    if "user_password" in value:
        out["UserPassword"] = value["user_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestIdentityProviderRequest:
    out: TestIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("TestIdentityProviderRequest.server_id required")
    if data.get("ServerProtocol") is not None:
        import capo_transfer.types.protocol

        out["server_protocol"] = capo_transfer.types.protocol.deserialize_aws_json_1_1(
            data["ServerProtocol"]
        )
    if data.get("SourceIp") is not None:
        out["source_ip"] = data["SourceIp"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("TestIdentityProviderRequest.user_name required")
    if data.get("UserPassword") is not None:
        out["user_password"] = data["UserPassword"]
    return out


def redact_sensitive(value: TestIdentityProviderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_password" in value:
        out["user_password"] = "*** Sensitive Data Redacted ***"
    return out
