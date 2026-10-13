"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkUpdateAccount``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.app_server_private_key


class SidewalkUpdateAccount(TypedDict, closed=True):
    app_server_private_key: NotRequired[
        "capo_iot_wireless.types.app_server_private_key.AppServerPrivateKey"
    ]
    """<p>The new Sidewalk application server private key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkUpdateAccount) -> dict:
    out: dict = {}
    if "app_server_private_key" in value:
        out["AppServerPrivateKey"] = value["app_server_private_key"]
    return out


def deserialize_json(data: dict) -> SidewalkUpdateAccount:
    out: SidewalkUpdateAccount = {}  # type: ignore[typeddict-item]
    if data.get("AppServerPrivateKey") is not None:
        out["app_server_private_key"] = data["AppServerPrivateKey"]
    return out


def redact_sensitive(value: SidewalkUpdateAccount) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_server_private_key" in value:
        out["app_server_private_key"] = "*** Sensitive Data Redacted ***"
    return out
