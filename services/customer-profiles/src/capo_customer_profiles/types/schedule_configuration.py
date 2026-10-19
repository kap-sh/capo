"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ScheduleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.interval_value
    import capo_customer_profiles.types.schedule_configuration_unit


class ScheduleConfiguration(TypedDict, closed=True):
    interval: "capo_customer_profiles.types.interval_value.IntervalValue"
    """<p>The interval between scheduled executions. </p>"""
    unit: NotRequired[
        "capo_customer_profiles.types.schedule_configuration_unit.ScheduleConfigurationUnit"
    ]
    """<p>The unit for the interval. The following are valid values: </p> <ul> <li> <p> <b>HOURLY</b>: The interval is measured in hours. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    out["Interval"] = value["interval"]
    if "unit" in value:
        import capo_customer_profiles.types.schedule_configuration_unit

        out["Unit"] = (
            capo_customer_profiles.types.schedule_configuration_unit.serialize_json(
                value["unit"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Interval") is not None:
        out["interval"] = data["Interval"]
    else:
        out["interval"] = 0
    if data.get("Unit") is not None:
        import capo_customer_profiles.types.schedule_configuration_unit

        out["unit"] = (
            capo_customer_profiles.types.schedule_configuration_unit.deserialize_json(
                data["Unit"]
            )
        )
    return out
