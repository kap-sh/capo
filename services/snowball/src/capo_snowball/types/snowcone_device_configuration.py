"""Generated from Smithy shape ``com.amazonaws.snowball#SnowconeDeviceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.wireless_connection


class SnowconeDeviceConfiguration(TypedDict, closed=True):
    wireless_connection: NotRequired[
        "capo_snowball.types.wireless_connection.WirelessConnection"
    ]
    """<p>Configures the wireless connection for the Snowball Edge device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowconeDeviceConfiguration) -> dict:
    out: dict = {}
    if "wireless_connection" in value:
        import capo_snowball.types.wireless_connection

        out["WirelessConnection"] = (
            capo_snowball.types.wireless_connection.serialize_aws_json_1_1(
                value["wireless_connection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowconeDeviceConfiguration:
    out: SnowconeDeviceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WirelessConnection") is not None:
        import capo_snowball.types.wireless_connection

        out["wireless_connection"] = (
            capo_snowball.types.wireless_connection.deserialize_aws_json_1_1(
                data["WirelessConnection"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SnowconeDeviceConfiguration) -> dict:
    out: dict = {}
    if "wireless_connection" in value:
        import capo_snowball.types.wireless_connection

        out["WirelessConnection"] = (
            capo_snowball.types.wireless_connection.serialize_cbor(
                value["wireless_connection"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SnowconeDeviceConfiguration:
    out: SnowconeDeviceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WirelessConnection") is not None:
        import capo_snowball.types.wireless_connection

        out["wireless_connection"] = (
            capo_snowball.types.wireless_connection.deserialize_cbor(
                data["WirelessConnection"]
            )
        )
    return out
