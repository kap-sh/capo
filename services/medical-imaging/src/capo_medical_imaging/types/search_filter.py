"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.operator
    import capo_medical_imaging.types.search_by_attribute_values


class SearchFilter(TypedDict, closed=True):
    values: (
        "capo_medical_imaging.types.search_by_attribute_values.SearchByAttributeValues"
    )
    """<p>The search filter values.</p>"""
    operator: "capo_medical_imaging.types.operator.Operator"
    """<p>The search filter operator for <code>imageSetDateTime</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilter) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.search_by_attribute_values

    out["values"] = (
        capo_medical_imaging.types.search_by_attribute_values.serialize_json(
            value["values"]
        )
    )
    import capo_medical_imaging.types.operator

    out["operator"] = capo_medical_imaging.types.operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> SearchFilter:
    out: SearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("values") is not None:
        import capo_medical_imaging.types.search_by_attribute_values

        out["values"] = (
            capo_medical_imaging.types.search_by_attribute_values.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("SearchFilter.values required")
    if data.get("operator") is not None:
        import capo_medical_imaging.types.operator

        out["operator"] = capo_medical_imaging.types.operator.deserialize_json(
            data["operator"]
        )
    else:
        raise DeserializationError("SearchFilter.operator required")
    return out


def redact_sensitive(value: SearchFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_medical_imaging.types.search_by_attribute_values

        out["values"] = (
            capo_medical_imaging.types.search_by_attribute_values.redact_sensitive(
                value["values"]
            )
        )
    return out
