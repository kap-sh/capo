"""Generated from Smithy shape ``com.amazonaws.quicksight#OverrideDatasetParameterOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dataset_parameter_name
    import capo_quicksight.types.new_default_values


class OverrideDatasetParameterOperation(TypedDict, closed=True):
    parameter_name: "capo_quicksight.types.dataset_parameter_name.DatasetParameterName"
    """<p>The name of the parameter to be overridden with different values.</p>"""
    new_parameter_name: NotRequired[
        "capo_quicksight.types.dataset_parameter_name.DatasetParameterName"
    ]
    """<p>The new name for the parameter.</p>"""
    new_default_values: NotRequired[
        "capo_quicksight.types.new_default_values.NewDefaultValues"
    ]
    """<p>The new default values for the parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverrideDatasetParameterOperation) -> dict:
    out: dict = {}
    out["ParameterName"] = value["parameter_name"]
    if "new_parameter_name" in value:
        out["NewParameterName"] = value["new_parameter_name"]
    if "new_default_values" in value:
        import capo_quicksight.types.new_default_values

        out["NewDefaultValues"] = (
            capo_quicksight.types.new_default_values.serialize_json(
                value["new_default_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> OverrideDatasetParameterOperation:
    out: OverrideDatasetParameterOperation = {}  # type: ignore[typeddict-item]
    if data.get("ParameterName") is not None:
        out["parameter_name"] = data["ParameterName"]
    else:
        out["parameter_name"] = ""
    if data.get("NewParameterName") is not None:
        out["new_parameter_name"] = data["NewParameterName"]
    if data.get("NewDefaultValues") is not None:
        import capo_quicksight.types.new_default_values

        out["new_default_values"] = (
            capo_quicksight.types.new_default_values.deserialize_json(
                data["NewDefaultValues"]
            )
        )
    return out
