"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkAccountInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.amazon_id
    import capo_iot_wireless.types.app_server_private_key


class SidewalkAccountInfo(TypedDict, closed=True):
    amazon_id: NotRequired["capo_iot_wireless.types.amazon_id.AmazonId"]
    """<p>The Sidewalk Amazon ID.</p>"""
    app_server_private_key: NotRequired[
        "capo_iot_wireless.types.app_server_private_key.AppServerPrivateKey"
    ]
    """<p>The Sidewalk application server private key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkAccountInfo) -> dict:
    out: dict = {}
    if "amazon_id" in value:
        out["AmazonId"] = value["amazon_id"]
    if "app_server_private_key" in value:
        out["AppServerPrivateKey"] = value["app_server_private_key"]
    return out


def deserialize_json(data: dict) -> SidewalkAccountInfo:
    out: SidewalkAccountInfo = {}  # type: ignore[typeddict-item]
    if data.get("AmazonId") is not None:
        out["amazon_id"] = data["AmazonId"]
    if data.get("AppServerPrivateKey") is not None:
        out["app_server_private_key"] = data["AppServerPrivateKey"]
    return out


def redact_sensitive(value: SidewalkAccountInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_server_private_key" in value:
        out["app_server_private_key"] = "*** Sensitive Data Redacted ***"
    return out
