"""Generated from Smithy shape ``com.amazonaws.connect#UpdateHoursOfOperationOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.common_human_readable_description
    import capo_connect.types.common_human_readable_name
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.hours_of_operation_override_config_list
    import capo_connect.types.hours_of_operation_override_id
    import capo_connect.types.hours_of_operation_override_year_month_day_date_format
    import capo_connect.types.instance_id
    import capo_connect.types.override_type
    import capo_connect.types.recurrence_config


class UpdateHoursOfOperationOverrideRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier for the hours of operation.</p>"""
    hours_of_operation_override_id: (
        "capo_connect.types.hours_of_operation_override_id.HoursOfOperationOverrideId"
    )
    """<p>The identifier for the hours of operation override.</p>"""
    name: NotRequired[
        "capo_connect.types.common_human_readable_name.CommonHumanReadableName"
    ]
    """<p>The name of the hours of operation override.</p>"""
    description: NotRequired[
        "capo_connect.types.common_human_readable_description.CommonHumanReadableDescription"
    ]
    """<p>The description of the hours of operation override.</p>"""
    config: NotRequired[
        "capo_connect.types.hours_of_operation_override_config_list.HoursOfOperationOverrideConfigList"
    ]
    """<p>Configuration information for the hours of operation override: day, start time, and end time.</p>"""
    effective_from: NotRequired[
        "capo_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    ]
    """<p>The date from when the hours of operation override would be effective.</p>"""
    effective_till: NotRequired[
        "capo_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    ]
    """<p>The date until the hours of operation override is effective.</p>"""
    recurrence_config: NotRequired[
        "capo_connect.types.recurrence_config.RecurrenceConfig"
    ]
    """<p>Configuration for a recurring event.</p>"""
    override_type: NotRequired["capo_connect.types.override_type.OverrideType"]
    """<p>Whether the override will be defined as a <i>standard</i> or as a <i>recurring event</i>.</p> <p>For more information about how override types are applied, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html">Build your list of overrides</a> in the <i> Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHoursOfOperationOverrideRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "config" in value:
        import capo_connect.types.hours_of_operation_override_config_list

        out["Config"] = (
            capo_connect.types.hours_of_operation_override_config_list.serialize_json(
                value["config"]
            )
        )
    if "effective_from" in value:
        out["EffectiveFrom"] = value["effective_from"]
    if "effective_till" in value:
        out["EffectiveTill"] = value["effective_till"]
    if "recurrence_config" in value:
        import capo_connect.types.recurrence_config

        out["RecurrenceConfig"] = capo_connect.types.recurrence_config.serialize_json(
            value["recurrence_config"]
        )
    if "override_type" in value:
        import capo_connect.types.override_type

        out["OverrideType"] = capo_connect.types.override_type.serialize_json(
            value["override_type"]
        )
    return out


def deserialize_json(data: dict) -> UpdateHoursOfOperationOverrideRequest:
    out: UpdateHoursOfOperationOverrideRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Config") is not None:
        import capo_connect.types.hours_of_operation_override_config_list

        out["config"] = (
            capo_connect.types.hours_of_operation_override_config_list.deserialize_json(
                data["Config"]
            )
        )
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    if data.get("EffectiveTill") is not None:
        out["effective_till"] = data["EffectiveTill"]
    if data.get("RecurrenceConfig") is not None:
        import capo_connect.types.recurrence_config

        out["recurrence_config"] = (
            capo_connect.types.recurrence_config.deserialize_json(
                data["RecurrenceConfig"]
            )
        )
    if data.get("OverrideType") is not None:
        import capo_connect.types.override_type

        out["override_type"] = capo_connect.types.override_type.deserialize_json(
            data["OverrideType"]
        )
    return out
