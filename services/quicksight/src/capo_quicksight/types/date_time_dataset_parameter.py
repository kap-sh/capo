"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDatasetParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dataset_parameter_id
    import capo_quicksight.types.dataset_parameter_name
    import capo_quicksight.types.dataset_parameter_value_type
    import capo_quicksight.types.date_time_dataset_parameter_default_values
    import capo_quicksight.types.time_granularity


class DateTimeDatasetParameter(TypedDict, closed=True):
    id: "capo_quicksight.types.dataset_parameter_id.DatasetParameterId"
    """<p>An identifier for the parameter that is created in the dataset.</p>"""
    name: "capo_quicksight.types.dataset_parameter_name.DatasetParameterName"
    """<p>The name of the date time parameter that is created in the dataset.</p>"""
    value_type: (
        "capo_quicksight.types.dataset_parameter_value_type.DatasetParameterValueType"
    )
    """<p>The value type of the dataset parameter. Valid values are <code>single value</code> or <code>multi value</code>.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The time granularity of the date time parameter.</p>"""
    default_values: NotRequired[
        "capo_quicksight.types.date_time_dataset_parameter_default_values.DateTimeDatasetParameterDefaultValues"
    ]
    """<p>A list of default values for a given date time parameter. This structure only accepts static values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDatasetParameter) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    import capo_quicksight.types.dataset_parameter_value_type

    out["ValueType"] = (
        capo_quicksight.types.dataset_parameter_value_type.serialize_json(
            value["value_type"]
        )
    )
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    if "default_values" in value:
        import capo_quicksight.types.date_time_dataset_parameter_default_values

        out["DefaultValues"] = (
            capo_quicksight.types.date_time_dataset_parameter_default_values.serialize_json(
                value["default_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateTimeDatasetParameter:
    out: DateTimeDatasetParameter = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ValueType") is not None:
        import capo_quicksight.types.dataset_parameter_value_type

        out["value_type"] = (
            capo_quicksight.types.dataset_parameter_value_type.deserialize_json(
                data["ValueType"]
            )
        )
    else:
        import typing

        out["value_type"] = typing.cast(
            "capo_quicksight.types.dataset_parameter_value_type.DatasetParameterValueType",
            "",
        )
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if data.get("DefaultValues") is not None:
        import capo_quicksight.types.date_time_dataset_parameter_default_values

        out["default_values"] = (
            capo_quicksight.types.date_time_dataset_parameter_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    return out
