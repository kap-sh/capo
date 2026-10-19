"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.command_parameter_description
    import capo_iot.types.command_parameter_name
    import capo_iot.types.command_parameter_type
    import capo_iot.types.command_parameter_value
    import capo_iot.types.command_parameter_value_condition_list


class CommandParameter(TypedDict, closed=True):
    name: "capo_iot.types.command_parameter_name.CommandParameterName"
    """<p>The name of a specific parameter used in a command and command execution.</p>"""
    type: NotRequired["capo_iot.types.command_parameter_type.CommandParameterType"]
    """<p>The type of the command parameter.</p>"""
    value: NotRequired["capo_iot.types.command_parameter_value.CommandParameterValue"]
    """<p>Parameter value that overrides the default value, if set.</p>"""
    default_value: NotRequired[
        "capo_iot.types.command_parameter_value.CommandParameterValue"
    ]
    """<p>The default value used to describe the command. This is the value assumed by the parameter if no other value is assigned to it.</p>"""
    value_conditions: NotRequired[
        "capo_iot.types.command_parameter_value_condition_list.CommandParameterValueConditionList"
    ]
    """<p>The list of conditions that a command parameter value must satisfy to create a command execution.</p>"""
    description: NotRequired[
        "capo_iot.types.command_parameter_description.CommandParameterDescription"
    ]
    """<p>The description of the command parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "type" in value:
        import capo_iot.types.command_parameter_type

        out["type"] = capo_iot.types.command_parameter_type.serialize_json(
            value["type"]
        )
    if "value" in value:
        import capo_iot.types.command_parameter_value

        out["value"] = capo_iot.types.command_parameter_value.serialize_json(
            value["value"]
        )
    if "default_value" in value:
        import capo_iot.types.command_parameter_value

        out["defaultValue"] = capo_iot.types.command_parameter_value.serialize_json(
            value["default_value"]
        )
    if "value_conditions" in value:
        import capo_iot.types.command_parameter_value_condition_list

        out["valueConditions"] = (
            capo_iot.types.command_parameter_value_condition_list.serialize_json(
                value["value_conditions"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CommandParameter:
    out: CommandParameter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_iot.types.command_parameter_type

        out["type"] = capo_iot.types.command_parameter_type.deserialize_json(
            data["type"]
        )
    if data.get("value") is not None:
        import capo_iot.types.command_parameter_value

        out["value"] = capo_iot.types.command_parameter_value.deserialize_json(
            data["value"]
        )
    if data.get("defaultValue") is not None:
        import capo_iot.types.command_parameter_value

        out["default_value"] = capo_iot.types.command_parameter_value.deserialize_json(
            data["defaultValue"]
        )
    if data.get("valueConditions") is not None:
        import capo_iot.types.command_parameter_value_condition_list

        out["value_conditions"] = (
            capo_iot.types.command_parameter_value_condition_list.deserialize_json(
                data["valueConditions"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
