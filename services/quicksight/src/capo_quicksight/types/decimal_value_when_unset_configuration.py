"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalValueWhenUnsetConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_double
    import capo_quicksight.types.value_when_unset_option


class DecimalValueWhenUnsetConfiguration(TypedDict, closed=True):
    value_when_unset_option: NotRequired[
        "capo_quicksight.types.value_when_unset_option.ValueWhenUnsetOption"
    ]
    """<p>The built-in options for default values. The value can be one of the following:</p> <ul> <li> <p> <code>RECOMMENDED</code>: The recommended value.</p> </li> <li> <p> <code>NULL</code>: The <code>NULL</code> value.</p> </li> </ul>"""
    custom_value: NotRequired["capo_quicksight.types.sensitive_double.SensitiveDouble"]
    """<p>A custom value that's used when the value of a parameter isn't set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalValueWhenUnsetConfiguration) -> dict:
    out: dict = {}
    if "value_when_unset_option" in value:
        import capo_quicksight.types.value_when_unset_option

        out["ValueWhenUnsetOption"] = (
            capo_quicksight.types.value_when_unset_option.serialize_json(
                value["value_when_unset_option"]
            )
        )
    if "custom_value" in value:
        out["CustomValue"] = (
            "NaN"
            if value["custom_value"] != value["custom_value"]
            else "Infinity"
            if value["custom_value"] == float("inf")
            else "-Infinity"
            if value["custom_value"] == float("-inf")
            else value["custom_value"]
        )
    return out


def deserialize_json(data: dict) -> DecimalValueWhenUnsetConfiguration:
    out: DecimalValueWhenUnsetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ValueWhenUnsetOption") is not None:
        import capo_quicksight.types.value_when_unset_option

        out["value_when_unset_option"] = (
            capo_quicksight.types.value_when_unset_option.deserialize_json(
                data["ValueWhenUnsetOption"]
            )
        )
    if data.get("CustomValue") is not None:
        out["custom_value"] = float(data["CustomValue"])
    return out


def redact_sensitive(value: DecimalValueWhenUnsetConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_value" in value:
        out["custom_value"] = "*** Sensitive Data Redacted ***"
    return out
