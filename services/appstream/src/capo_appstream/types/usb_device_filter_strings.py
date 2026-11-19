"""Generated from Smithy shape ``com.amazonaws.appstream#UsbDeviceFilterStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.usb_device_filter_string

UsbDeviceFilterStrings: TypeAlias = list[
    "capo_appstream.types.usb_device_filter_string.UsbDeviceFilterString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsbDeviceFilterStrings) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UsbDeviceFilterStrings:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UsbDeviceFilterStrings) -> list:
    return list(value)


def deserialize_cbor(data: list) -> UsbDeviceFilterStrings:
    return [item for item in data if item is not None]
