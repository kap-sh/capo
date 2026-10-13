"""Generated from Smithy shape ``com.amazonaws.storagegateway#SetLocalConsolePasswordInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.local_console_password


class SetLocalConsolePasswordInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    local_console_password: (
        "capo_storage_gateway.types.local_console_password.LocalConsolePassword"
    )
    """<p>The password you want to set for your VM local console.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetLocalConsolePasswordInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["LocalConsolePassword"] = value["local_console_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetLocalConsolePasswordInput:
    out: SetLocalConsolePasswordInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("SetLocalConsolePasswordInput.gateway_arn required")
    if data.get("LocalConsolePassword") is not None:
        out["local_console_password"] = data["LocalConsolePassword"]
    else:
        raise DeserializationError(
            "SetLocalConsolePasswordInput.local_console_password required"
        )
    return out


def redact_sensitive(value: SetLocalConsolePasswordInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "local_console_password" in value:
        out["local_console_password"] = "*** Sensitive Data Redacted ***"
    return out
