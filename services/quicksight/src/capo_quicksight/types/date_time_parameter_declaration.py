"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeParameterDeclaration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_default_values
    import capo_quicksight.types.date_time_value_when_unset_configuration
    import capo_quicksight.types.mapped_data_set_parameters
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.time_granularity


class DateTimeParameterDeclaration(TypedDict, closed=True):
    name: "capo_quicksight.types.parameter_name.ParameterName"
    """<p>The name of the parameter that is being declared.</p>"""
    default_values: NotRequired[
        "capo_quicksight.types.date_time_default_values.DateTimeDefaultValues"
    ]
    """<p>The default values of a parameter. If the parameter is a single-value parameter, a maximum of one default value can be provided.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    value_when_unset: NotRequired[
        "capo_quicksight.types.date_time_value_when_unset_configuration.DateTimeValueWhenUnsetConfiguration"
    ]
    """<p>The configuration that defines the default value of a <code>DateTime</code> parameter when a value has not been set.</p>"""
    mapped_data_set_parameters: NotRequired[
        "capo_quicksight.types.mapped_data_set_parameters.MappedDataSetParameters"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeParameterDeclaration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "default_values" in value:
        import capo_quicksight.types.date_time_default_values

        out["DefaultValues"] = (
            capo_quicksight.types.date_time_default_values.serialize_json(
                value["default_values"]
            )
        )
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    if "value_when_unset" in value:
        import capo_quicksight.types.date_time_value_when_unset_configuration

        out["ValueWhenUnset"] = (
            capo_quicksight.types.date_time_value_when_unset_configuration.serialize_json(
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


def deserialize_json(data: dict) -> DateTimeParameterDeclaration:
    out: DateTimeParameterDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DateTimeParameterDeclaration.name required")
    if data.get("DefaultValues") is not None:
        import capo_quicksight.types.date_time_default_values

        out["default_values"] = (
            capo_quicksight.types.date_time_default_values.deserialize_json(
                data["DefaultValues"]
            )
        )
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if data.get("ValueWhenUnset") is not None:
        import capo_quicksight.types.date_time_value_when_unset_configuration

        out["value_when_unset"] = (
            capo_quicksight.types.date_time_value_when_unset_configuration.deserialize_json(
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


def redact_sensitive(value: DateTimeParameterDeclaration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "default_values" in value:
        import capo_quicksight.types.date_time_default_values

        out["default_values"] = (
            capo_quicksight.types.date_time_default_values.redact_sensitive(
                value["default_values"]
            )
        )
    if "value_when_unset" in value:
        import capo_quicksight.types.date_time_value_when_unset_configuration

        out["value_when_unset"] = (
            capo_quicksight.types.date_time_value_when_unset_configuration.redact_sensitive(
                value["value_when_unset"]
            )
        )
    return out
