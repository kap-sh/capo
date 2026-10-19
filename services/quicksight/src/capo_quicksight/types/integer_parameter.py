"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerParameter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.non_empty_string
    import capo_quicksight.types.sensitive_long_list


class IntegerParameter(TypedDict, closed=True):
    name: "capo_quicksight.types.non_empty_string.NonEmptyString"
    """<p>The name of the integer parameter.</p>"""
    values: "capo_quicksight.types.sensitive_long_list.SensitiveLongList"
    """<p>The values for the integer parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_quicksight.types.sensitive_long_list

    out["Values"] = capo_quicksight.types.sensitive_long_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> IntegerParameter:
    out: IntegerParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Values") is not None:
        import capo_quicksight.types.sensitive_long_list

        out["values"] = capo_quicksight.types.sensitive_long_list.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out


def redact_sensitive(value: IntegerParameter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_quicksight.types.sensitive_long_list

        out["values"] = capo_quicksight.types.sensitive_long_list.redact_sensitive(
            value["values"]
        )
    return out
