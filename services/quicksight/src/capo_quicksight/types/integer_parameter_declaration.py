"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerParameterDeclaration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.integer_default_values
    import capo_quicksight.types.integer_value_when_unset_configuration
    import capo_quicksight.types.mapped_data_set_parameters
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.parameter_value_type


class IntegerParameterDeclaration(TypedDict, closed=True):
    parameter_value_type: (
        "capo_quicksight.types.parameter_value_type.ParameterValueType"
    )
    """<p>The value type determines whether the parameter is a single-value or multi-value parameter.</p>"""
    name: "capo_quicksight.types.parameter_name.ParameterName"
    """<p>The name of the parameter that is being declared.</p>"""
    default_values: NotRequired[
        "capo_quicksight.types.integer_default_values.IntegerDefaultValues"
    ]
    """<p>The default values of a parameter. If the parameter is a single-value parameter, a maximum of one default value can be provided.</p>"""
    value_when_unset: NotRequired[
        "capo_quicksight.types.integer_value_when_unset_configuration.IntegerValueWhenUnsetConfiguration"
    ]
    """<p>A parameter declaration for the <code>Integer</code> data type.</p>"""
    mapped_data_set_parameters: NotRequired[
        "capo_quicksight.types.mapped_data_set_parameters.MappedDataSetParameters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: IntegerParameterDeclaration) -> dict:
    out: dict = {}
    import capo_quicksight.types.parameter_value_type

    out["ParameterValueType"] = (
        capo_quicksight.types.parameter_value_type.serialize_json(
            value["parameter_value_type"]
        )
    )
    out["Name"] = value["name"]
    if "default_values" in value:
        import capo_quicksight.types.integer_default_values

        out["DefaultValues"] = (
            capo_quicksight.types.integer_default_values.serialize_json(
                value["default_values"]
            )
        )
    if "value_when_unset" in value:
        import capo_quicksight.types.integer_value_when_unset_configuration

        out["ValueWhenUnset"] = (
            capo_quicksight.types.integer_value_when_unset_configuration.serialize_json(
                value["value_when_unset"]
            )
        )
    if "mapped_data_set_parameters" in value:
        import capo_quicksight.types.mapped_data_set_parameters

        out["MappedDataSetParameters"] = (
            capo_quicksight.types.mapped_data_set_parameters.serialize_json(
                value["mapped_data_set_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegerParameterDeclaration:
    out: IntegerParameterDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("ParameterValueType") is not None:
        import capo_quicksight.types.parameter_value_type

        out["parameter_value_type"] = (
            capo_quicksight.types.parameter_value_type.deserialize_json(
                data["ParameterValueType"]
            )
        )
    else:
        import typing

        out["parameter_value_type"] = typing.cast(
            "capo_quicksight.types.parameter_value_type.ParameterValueType", ""
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DefaultValues") is not None:
        import capo_quicksight.types.integer_default_values

        out["default_values"] = (
            capo_quicksight.types.integer_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    if data.get("ValueWhenUnset") is not None:
        import capo_quicksight.types.integer_value_when_unset_configuration

        out["value_when_unset"] = (
            capo_quicksight.types.integer_value_when_unset_configuration.deserialize_json(
                data["ValueWhenUnset"]
            )
        )
    if data.get("MappedDataSetParameters") is not None:
        import capo_quicksight.types.mapped_data_set_parameters

        out["mapped_data_set_parameters"] = (
            capo_quicksight.types.mapped_data_set_parameters.deserialize_json(
                data["MappedDataSetParameters"]
            )
        )
    return out


def redact_sensitive(value: IntegerParameterDeclaration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "default_values" in value:
        import capo_quicksight.types.integer_default_values

        out["default_values"] = (
            capo_quicksight.types.integer_default_values.redact_sensitive(
                value["default_values"]
            )
        )
    if "value_when_unset" in value:
        import capo_quicksight.types.integer_value_when_unset_configuration

        out["value_when_unset"] = (
            capo_quicksight.types.integer_value_when_unset_configuration.redact_sensitive(
                value["value_when_unset"]
            )
        )
    return out
