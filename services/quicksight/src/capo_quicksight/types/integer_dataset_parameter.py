"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerDatasetParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dataset_parameter_id
    import capo_quicksight.types.dataset_parameter_name
    import capo_quicksight.types.dataset_parameter_value_type
    import capo_quicksight.types.integer_dataset_parameter_default_values


class IntegerDatasetParameter(TypedDict, closed=True):
    id: "capo_quicksight.types.dataset_parameter_id.DatasetParameterId"
    """<p>An identifier for the integer parameter created in the dataset.</p>"""
    name: "capo_quicksight.types.dataset_parameter_name.DatasetParameterName"
    """<p>The name of the integer parameter that is created in the dataset.</p>"""
    value_type: (
        "capo_quicksight.types.dataset_parameter_value_type.DatasetParameterValueType"
    )
    """<p>The value type of the dataset parameter. Valid values are <code>single value</code> or <code>multi value</code>.</p>"""
    default_values: NotRequired[
        "capo_quicksight.types.integer_dataset_parameter_default_values.IntegerDatasetParameterDefaultValues"
    ]
    """<p>A list of default values for a given integer parameter. This structure only accepts static values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerDatasetParameter) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    import capo_quicksight.types.dataset_parameter_value_type

    out["ValueType"] = (
        capo_quicksight.types.dataset_parameter_value_type.serialize_json(
            value["value_type"]
        )
    )
    if "default_values" in value:
        import capo_quicksight.types.integer_dataset_parameter_default_values

        out["DefaultValues"] = (
            capo_quicksight.types.integer_dataset_parameter_default_values.serialize_json(
                value["default_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegerDatasetParameter:
    out: IntegerDatasetParameter = {}  # type: ignore[typeddict-item]
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
    if data.get("DefaultValues") is not None:
        import capo_quicksight.types.integer_dataset_parameter_default_values

        out["default_values"] = (
            capo_quicksight.types.integer_dataset_parameter_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    return out
