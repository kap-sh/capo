"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageMaximumSize``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.storage_maximum_size_unit
    import capo_iotfleetwise.types.storage_maximum_size_value


class StorageMaximumSize(TypedDict, closed=True):
    unit: "capo_iotfleetwise.types.storage_maximum_size_unit.StorageMaximumSizeUnit"
    """<p>The data type of the data to store.</p>"""
    value: "capo_iotfleetwise.types.storage_maximum_size_value.StorageMaximumSizeValue"
    """<p>The maximum amount of time to store data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageMaximumSize) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.storage_maximum_size_unit

    out["unit"] = (
        capo_iotfleetwise.types.storage_maximum_size_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StorageMaximumSize:
    out: StorageMaximumSize = {}  # type: ignore[typeddict-item]
    if data.get("unit") is not None:
        import capo_iotfleetwise.types.storage_maximum_size_unit

        out["unit"] = (
            capo_iotfleetwise.types.storage_maximum_size_unit.deserialize_aws_json_1_0(
                data["unit"]
            )
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_iotfleetwise.types.storage_maximum_size_unit.StorageMaximumSizeUnit",
            "",
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
