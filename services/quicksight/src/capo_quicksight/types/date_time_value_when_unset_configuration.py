"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeValueWhenUnsetConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_timestamp
    import capo_quicksight.types.value_when_unset_option


class DateTimeValueWhenUnsetConfiguration(TypedDict, closed=True):
    value_when_unset_option: NotRequired[
        "capo_quicksight.types.value_when_unset_option.ValueWhenUnsetOption"
    ]
    """<p>The built-in options for default values. The value can be one of the following:</p> <ul> <li> <p> <code>RECOMMENDED</code>: The recommended value.</p> </li> <li> <p> <code>NULL</code>: The <code>NULL</code> value.</p> </li> </ul>"""
    custom_value: NotRequired[
        "capo_quicksight.types.sensitive_timestamp.SensitiveTimestamp"
    ]
    """<p>A custom value that's used when the value of a parameter isn't set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeValueWhenUnsetConfiguration) -> dict:
    out: dict = {}
    if "value_when_unset_option" in value:
        import capo_quicksight.types.value_when_unset_option

        out["ValueWhenUnsetOption"] = (
            capo_quicksight.types.value_when_unset_option.serialize_json(
                value["value_when_unset_option"]
            )
        )
    if "custom_value" in value:
        import capo_quicksight.types.sensitive_timestamp

        out["CustomValue"] = capo_quicksight.types.sensitive_timestamp.serialize_json(
            value["custom_value"]
        )
    return out


def deserialize_json(data: dict) -> DateTimeValueWhenUnsetConfiguration:
    out: DateTimeValueWhenUnsetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ValueWhenUnsetOption") is not None:
        import capo_quicksight.types.value_when_unset_option

        out["value_when_unset_option"] = (
            capo_quicksight.types.value_when_unset_option.deserialize_json(
                data["ValueWhenUnsetOption"]
            )
        )
    if data.get("CustomValue") is not None:
        import capo_quicksight.types.sensitive_timestamp

        out["custom_value"] = (
            capo_quicksight.types.sensitive_timestamp.deserialize_json(
                data["CustomValue"]
            )
        )
    return out


def redact_sensitive(value: DateTimeValueWhenUnsetConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_value" in value:
        out["custom_value"] = "*** Sensitive Data Redacted ***"
    return out
