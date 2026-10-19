"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StorageMinimumTimeToLive``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.storage_minimum_time_to_live_unit
    import capo_iotfleetwise.types.storage_minimum_time_to_live_value


class StorageMinimumTimeToLive(TypedDict, closed=True):
    unit: "capo_iotfleetwise.types.storage_minimum_time_to_live_unit.StorageMinimumTimeToLiveUnit"
    """<p>The time increment type.</p>"""
    value: "capo_iotfleetwise.types.storage_minimum_time_to_live_value.StorageMinimumTimeToLiveValue"
    """<p>The minimum amount of time to store the data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StorageMinimumTimeToLive) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.storage_minimum_time_to_live_unit

    out["unit"] = (
        capo_iotfleetwise.types.storage_minimum_time_to_live_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StorageMinimumTimeToLive:
    out: StorageMinimumTimeToLive = {}  # type: ignore[typeddict-item]
    if data.get("unit") is not None:
        import capo_iotfleetwise.types.storage_minimum_time_to_live_unit

        out["unit"] = (
            capo_iotfleetwise.types.storage_minimum_time_to_live_unit.deserialize_aws_json_1_0(
                data["unit"]
            )
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_iotfleetwise.types.storage_minimum_time_to_live_unit.StorageMinimumTimeToLiveUnit",
            "",
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
