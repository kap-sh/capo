"""Generated from Smithy shape ``com.amazonaws.backupgateway#TestHypervisorConfigurationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_arn
    import capo_backup_gateway.types.host
    import capo_backup_gateway.types.password
    import capo_backup_gateway.types.username


class TestHypervisorConfigurationInput(TypedDict, closed=True):
    gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway to the hypervisor to test.</p>"""
    host: "capo_backup_gateway.types.host.Host"
    """<p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>"""
    username: NotRequired["capo_backup_gateway.types.username.Username"]
    """<p>The username for the hypervisor.</p>"""
    password: NotRequired["capo_backup_gateway.types.password.Password"]
    """<p>The password for the hypervisor.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestHypervisorConfigurationInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    out["Host"] = value["host"]
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TestHypervisorConfigurationInput:
    out: TestHypervisorConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        raise DeserializationError(
            "TestHypervisorConfigurationInput.gateway_arn required"
        )
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("TestHypervisorConfigurationInput.host required")
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    return out


def redact_sensitive(value: TestHypervisorConfigurationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
