"""Generated from Smithy shape ``com.amazonaws.snowball#DeviceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.snowcone_device_configuration


class DeviceConfiguration(TypedDict, closed=True):
    snowcone_device_configuration: NotRequired[
        "capo_snowball.types.snowcone_device_configuration.SnowconeDeviceConfiguration"
    ]
    """<p>Returns information about the device configuration for an Snowball Edge job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceConfiguration) -> dict:
    out: dict = {}
    if "snowcone_device_configuration" in value:
        import capo_snowball.types.snowcone_device_configuration

        out["SnowconeDeviceConfiguration"] = (
            capo_snowball.types.snowcone_device_configuration.serialize_aws_json_1_1(
                value["snowcone_device_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceConfiguration:
    out: DeviceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SnowconeDeviceConfiguration") is not None:
        import capo_snowball.types.snowcone_device_configuration

        out["snowcone_device_configuration"] = (
            capo_snowball.types.snowcone_device_configuration.deserialize_aws_json_1_1(
                data["SnowconeDeviceConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeviceConfiguration) -> dict:
    out: dict = {}
    if "snowcone_device_configuration" in value:
        import capo_snowball.types.snowcone_device_configuration

        out["SnowconeDeviceConfiguration"] = (
            capo_snowball.types.snowcone_device_configuration.serialize_cbor(
                value["snowcone_device_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeviceConfiguration:
    out: DeviceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SnowconeDeviceConfiguration") is not None:
        import capo_snowball.types.snowcone_device_configuration

        out["snowcone_device_configuration"] = (
            capo_snowball.types.snowcone_device_configuration.deserialize_cbor(
                data["SnowconeDeviceConfiguration"]
            )
        )
    return out
