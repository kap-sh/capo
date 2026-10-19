"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedAttributeValueRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.range_mode
    import capo_clouddirectory.types.typed_attribute_value


class TypedAttributeValueRange(TypedDict, closed=True):
    start_mode: "capo_clouddirectory.types.range_mode.RangeMode"
    """<p>The inclusive or exclusive range start.</p>"""
    start_value: NotRequired[
        "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The value to start the range at.</p>"""
    end_mode: "capo_clouddirectory.types.range_mode.RangeMode"
    """<p>The inclusive or exclusive range end.</p>"""
    end_value: NotRequired[
        "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The attribute value to terminate the range at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedAttributeValueRange) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.range_mode

    out["StartMode"] = capo_clouddirectory.types.range_mode.serialize_json(
        value["start_mode"]
    )
    if "start_value" in value:
        import capo_clouddirectory.types.typed_attribute_value

        out["StartValue"] = (
            capo_clouddirectory.types.typed_attribute_value.serialize_json(
                value["start_value"]
            )
        )
    import capo_clouddirectory.types.range_mode

    out["EndMode"] = capo_clouddirectory.types.range_mode.serialize_json(
        value["end_mode"]
    )
    if "end_value" in value:
        import capo_clouddirectory.types.typed_attribute_value

        out["EndValue"] = (
            capo_clouddirectory.types.typed_attribute_value.serialize_json(
                value["end_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> TypedAttributeValueRange:
    out: TypedAttributeValueRange = {}  # type: ignore[typeddict-item]
    if data.get("StartMode") is not None:
        import capo_clouddirectory.types.range_mode

        out["start_mode"] = capo_clouddirectory.types.range_mode.deserialize_json(
            data["StartMode"]
        )
    else:
        import typing

        out["start_mode"] = typing.cast(
            "capo_clouddirectory.types.range_mode.RangeMode", ""
        )
    if data.get("StartValue") is not None:
        import capo_clouddirectory.types.typed_attribute_value

        out["start_value"] = (
            capo_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["StartValue"]
            )
        )
    if data.get("EndMode") is not None:
        import capo_clouddirectory.types.range_mode

        out["end_mode"] = capo_clouddirectory.types.range_mode.deserialize_json(
            data["EndMode"]
        )
    else:
        import typing

        out["end_mode"] = typing.cast(
            "capo_clouddirectory.types.range_mode.RangeMode", ""
        )
    if data.get("EndValue") is not None:
        import capo_clouddirectory.types.typed_attribute_value

        out["end_value"] = (
            capo_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["EndValue"]
            )
        )
    return out
