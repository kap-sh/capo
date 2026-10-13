"""Generated from Smithy shape ``com.amazonaws.quicksight#StringDefaultValues``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dynamic_default_value
    import capo_quicksight.types.string_default_value_list


class StringDefaultValues(TypedDict, closed=True):
    dynamic_value: NotRequired[
        "capo_quicksight.types.dynamic_default_value.DynamicDefaultValue"
    ]
    """<p>The dynamic value of the <code>StringDefaultValues</code>. Different defaults displayed according to users, groups, and values mapping.</p>"""
    static_values: NotRequired[
        "capo_quicksight.types.string_default_value_list.StringDefaultValueList"
    ]
    """<p>The static values of the <code>DecimalDefaultValues</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringDefaultValues) -> dict:
    out: dict = {}
    if "dynamic_value" in value:
        import capo_quicksight.types.dynamic_default_value

        out["DynamicValue"] = (
            capo_quicksight.types.dynamic_default_value.serialize_json(
                value["dynamic_value"]
            )
        )
    if "static_values" in value:
        import capo_quicksight.types.string_default_value_list

        out["StaticValues"] = (
            capo_quicksight.types.string_default_value_list.serialize_json(
                value["static_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> StringDefaultValues:
    out: StringDefaultValues = {}  # type: ignore[typeddict-item]
    if data.get("DynamicValue") is not None:
        import capo_quicksight.types.dynamic_default_value

        out["dynamic_value"] = (
            capo_quicksight.types.dynamic_default_value.deserialize_json(
                data["DynamicValue"]
            )
        )
    if data.get("StaticValues") is not None:
        import capo_quicksight.types.string_default_value_list

        out["static_values"] = (
            capo_quicksight.types.string_default_value_list.deserialize_json(
                data["StaticValues"]
            )
        )
    return out


def redact_sensitive(value: StringDefaultValues) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "static_values" in value:
        import capo_quicksight.types.string_default_value_list

        out["static_values"] = (
            capo_quicksight.types.string_default_value_list.redact_sensitive(
                value["static_values"]
            )
        )
    return out
