"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomActionSetParametersOperation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.set_parameter_value_configuration_list


class CustomActionSetParametersOperation(TypedDict, closed=True):
    parameter_value_configurations: "capo_quicksight.types.set_parameter_value_configuration_list.SetParameterValueConfigurationList"
    """<p>The parameter that determines the value configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionSetParametersOperation) -> dict:
    out: dict = {}
    import capo_quicksight.types.set_parameter_value_configuration_list

    out["ParameterValueConfigurations"] = (
        capo_quicksight.types.set_parameter_value_configuration_list.serialize_json(
            value["parameter_value_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomActionSetParametersOperation:
    out: CustomActionSetParametersOperation = {}  # type: ignore[typeddict-item]
    if data.get("ParameterValueConfigurations") is not None:
        import capo_quicksight.types.set_parameter_value_configuration_list

        out["parameter_value_configurations"] = (
            capo_quicksight.types.set_parameter_value_configuration_list.deserialize_json(
                data["ParameterValueConfigurations"]
            )
        )
    else:
        out["parameter_value_configurations"] = []
    return out


def redact_sensitive(value: CustomActionSetParametersOperation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameter_value_configurations" in value:
        import capo_quicksight.types.set_parameter_value_configuration_list

        out["parameter_value_configurations"] = (
            capo_quicksight.types.set_parameter_value_configuration_list.redact_sensitive(
                value["parameter_value_configurations"]
            )
        )
    return out
