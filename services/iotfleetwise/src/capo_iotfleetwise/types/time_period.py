"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.positive_integer
    import capo_iotfleetwise.types.time_unit


class TimePeriod(TypedDict, closed=True):
    unit: "capo_iotfleetwise.types.time_unit.TimeUnit"
    """<p>A unit of time.</p>"""
    value: "capo_iotfleetwise.types.positive_integer.positiveInteger"
    """<p>A number of time units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimePeriod) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.time_unit

    out["unit"] = capo_iotfleetwise.types.time_unit.serialize_aws_json_1_0(
        value["unit"]
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if data.get("unit") is not None:
        import capo_iotfleetwise.types.time_unit

        out["unit"] = capo_iotfleetwise.types.time_unit.deserialize_aws_json_1_0(
            data["unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast("capo_iotfleetwise.types.time_unit.TimeUnit", "")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
