"""Generated from Smithy shape ``com.amazonaws.snowball#TGWOnDeviceServiceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.storage_limit
    import capo_snowball.types.storage_unit


class TGWOnDeviceServiceConfiguration(TypedDict, closed=True):
    storage_limit: "capo_snowball.types.storage_limit.StorageLimit"
    """<p>The maximum number of virtual tapes to store on one Snow Family device. Due to physical resource limitations, this value must be set to 80 for Snowball Edge.</p>"""
    storage_unit: NotRequired["capo_snowball.types.storage_unit.StorageUnit"]
    """<p>The scale unit of the virtual tapes on the device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TGWOnDeviceServiceConfiguration) -> dict:
    out: dict = {}
    out["StorageLimit"] = value.get("storage_limit", 0)
    if "storage_unit" in value:
        import capo_snowball.types.storage_unit

        out["StorageUnit"] = capo_snowball.types.storage_unit.serialize_aws_json_1_1(
            value["storage_unit"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TGWOnDeviceServiceConfiguration:
    out: TGWOnDeviceServiceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StorageLimit") is not None:
        out["storage_limit"] = data["StorageLimit"]
    else:
        out["storage_limit"] = 0
    if data.get("StorageUnit") is not None:
        import capo_snowball.types.storage_unit

        out["storage_unit"] = capo_snowball.types.storage_unit.deserialize_aws_json_1_1(
            data["StorageUnit"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TGWOnDeviceServiceConfiguration) -> dict:
    out: dict = {}
    out["StorageLimit"] = value.get("storage_limit", 0)
    if "storage_unit" in value:
        import capo_snowball.types.storage_unit

        out["StorageUnit"] = capo_snowball.types.storage_unit.serialize_cbor(
            value["storage_unit"]
        )
    return out


def deserialize_cbor(data: dict) -> TGWOnDeviceServiceConfiguration:
    out: TGWOnDeviceServiceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StorageLimit") is not None:
        out["storage_limit"] = data["StorageLimit"]
    else:
        out["storage_limit"] = 0
    if data.get("StorageUnit") is not None:
        import capo_snowball.types.storage_unit

        out["storage_unit"] = capo_snowball.types.storage_unit.deserialize_cbor(
            data["StorageUnit"]
        )
    return out
