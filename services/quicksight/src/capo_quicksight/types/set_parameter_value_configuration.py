"""Generated from Smithy shape ``com.amazonaws.quicksight#SetParameterValueConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.destination_parameter_value_configuration
    import capo_quicksight.types.parameter_name


class SetParameterValueConfiguration(TypedDict, closed=True):
    destination_parameter_name: "capo_quicksight.types.parameter_name.ParameterName"
    """<p>The destination parameter name of the <code>SetParameterValueConfiguration</code>.</p>"""
    value: "capo_quicksight.types.destination_parameter_value_configuration.DestinationParameterValueConfiguration"


# --- restJson1 ser/de ---
def serialize_json(value: SetParameterValueConfiguration) -> dict:
    out: dict = {}
    out["DestinationParameterName"] = value["destination_parameter_name"]
    import capo_quicksight.types.destination_parameter_value_configuration

    out["Value"] = (
        capo_quicksight.types.destination_parameter_value_configuration.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> SetParameterValueConfiguration:
    out: SetParameterValueConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DestinationParameterName") is not None:
        out["destination_parameter_name"] = data["DestinationParameterName"]
    else:
        raise DeserializationError(
            "SetParameterValueConfiguration.destination_parameter_name required"
        )
    if data.get("Value") is not None:
        import capo_quicksight.types.destination_parameter_value_configuration

        out["value"] = (
            capo_quicksight.types.destination_parameter_value_configuration.deserialize_json(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("SetParameterValueConfiguration.value required")
    return out


def redact_sensitive(value: SetParameterValueConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_quicksight.types.destination_parameter_value_configuration

        out["value"] = (
            capo_quicksight.types.destination_parameter_value_configuration.redact_sensitive(
                value["value"]
            )
        )
    return out
