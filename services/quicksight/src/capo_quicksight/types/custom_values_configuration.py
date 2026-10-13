"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomValuesConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.boolean_object
    import capo_quicksight.types.custom_parameter_values


class CustomValuesConfiguration(TypedDict, closed=True):
    include_null_value: NotRequired[
        "capo_quicksight.types.boolean_object.BooleanObject"
    ]
    """<p>Includes the null value in custom action parameter values.</p>"""
    custom_values: "capo_quicksight.types.custom_parameter_values.CustomParameterValues"


# --- restJson1 ser/de ---
def serialize_json(value: CustomValuesConfiguration) -> dict:
    out: dict = {}
    if "include_null_value" in value:
        out["IncludeNullValue"] = value["include_null_value"]
    import capo_quicksight.types.custom_parameter_values

    out["CustomValues"] = capo_quicksight.types.custom_parameter_values.serialize_json(
        value["custom_values"]
    )
    return out


def deserialize_json(data: dict) -> CustomValuesConfiguration:
    out: CustomValuesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IncludeNullValue") is not None:
        out["include_null_value"] = data["IncludeNullValue"]
    if data.get("CustomValues") is not None:
        import capo_quicksight.types.custom_parameter_values

        out["custom_values"] = (
            capo_quicksight.types.custom_parameter_values.deserialize_json(
                data["CustomValues"]
            )
        )
    else:
        raise DeserializationError("CustomValuesConfiguration.custom_values required")
    return out


def redact_sensitive(value: CustomValuesConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_values" in value:
        import capo_quicksight.types.custom_parameter_values

        out["custom_values"] = (
            capo_quicksight.types.custom_parameter_values.redact_sensitive(
                value["custom_values"]
            )
        )
    return out
