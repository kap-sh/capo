"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalParameter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.non_empty_string
    import capo_quicksight.types.sensitive_double_list


class DecimalParameter(TypedDict, closed=True):
    name: "capo_quicksight.types.non_empty_string.NonEmptyString"
    """<p>A display name for the decimal parameter.</p>"""
    values: "capo_quicksight.types.sensitive_double_list.SensitiveDoubleList"
    """<p>The values for the decimal parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_quicksight.types.sensitive_double_list

    out["Values"] = capo_quicksight.types.sensitive_double_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> DecimalParameter:
    out: DecimalParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DecimalParameter.name required")
    if data.get("Values") is not None:
        import capo_quicksight.types.sensitive_double_list

        out["values"] = capo_quicksight.types.sensitive_double_list.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("DecimalParameter.values required")
    return out


def redact_sensitive(value: DecimalParameter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_quicksight.types.sensitive_double_list

        out["values"] = capo_quicksight.types.sensitive_double_list.redact_sensitive(
            value["values"]
        )
    return out
