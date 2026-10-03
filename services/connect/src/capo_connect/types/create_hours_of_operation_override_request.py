"""Generated from Smithy shape ``com.amazonaws.connect#CreateHoursOfOperationOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.common_human_readable_description
    import capo_connect.types.common_human_readable_name
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.hours_of_operation_override_config_list
    import capo_connect.types.hours_of_operation_override_year_month_day_date_format
    import capo_connect.types.instance_id
    import capo_connect.types.override_type
    import capo_connect.types.recurrence_config


class CreateHoursOfOperationOverrideRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier for the hours of operation</p>"""
    name: "capo_connect.types.common_human_readable_name.CommonHumanReadableName"
    """<p>The name of the hours of operation override.</p>"""
    description: NotRequired[
        "capo_connect.types.common_human_readable_description.CommonHumanReadableDescription"
    ]
    """<p>The description of the hours of operation override.</p>"""
    config: "capo_connect.types.hours_of_operation_override_config_list.HoursOfOperationOverrideConfigList"
    """<p>Configuration information for the hours of operation override: day, start time, and end time.</p>"""
    effective_from: "capo_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    """<p>The date from when the hours of operation override is effective.</p>"""
    effective_till: "capo_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    """<p>The date until when the hours of operation override is effective.</p>"""
    recurrence_config: NotRequired[
        "capo_connect.types.recurrence_config.RecurrenceConfig"
    ]
    """<p>Configuration for a recurring event.</p>"""
    override_type: NotRequired["capo_connect.types.override_type.OverrideType"]
    """<p>Whether the override will be defined as a <i>standard</i> or as a <i>recurring event</i>.</p> <p>For more information about how override types are applied, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html">Build your list of overrides</a> in the <i> Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHoursOfOperationOverrideRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_connect.types.hours_of_operation_override_config_list

    out["Config"] = (
        capo_connect.types.hours_of_operation_override_config_list.serialize_json(
            value["config"]
        )
    )
    out["EffectiveFrom"] = value["effective_from"]
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


def deserialize_json(data: dict) -> CreateHoursOfOperationOverrideRequest:
    out: CreateHoursOfOperationOverrideRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "CreateHoursOfOperationOverrideRequest.name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Config") is not None:
        import capo_connect.types.hours_of_operation_override_config_list

        out["config"] = (
            capo_connect.types.hours_of_operation_override_config_list.deserialize_json(
                data["Config"]
            )
        )
    else:
        raise DeserializationError(
            "CreateHoursOfOperationOverrideRequest.config required"
        )
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    else:
        raise DeserializationError(
            "CreateHoursOfOperationOverrideRequest.effective_from required"
        )
    if data.get("EffectiveTill") is not None:
        out["effective_till"] = data["EffectiveTill"]
    else:
        raise DeserializationError(
            "CreateHoursOfOperationOverrideRequest.effective_till required"
        )
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
