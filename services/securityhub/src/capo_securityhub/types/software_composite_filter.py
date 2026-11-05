"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareCompositeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.allowed_operators
    import capo_securityhub.types.software_composite_filter_list
    import capo_securityhub.types.software_string_filter_list


class SoftwareCompositeFilter(TypedDict, closed=True):
    string_filters: NotRequired[
        "capo_securityhub.types.software_string_filter_list.SoftwareStringFilterList"
    ]
    """<p>Enables filtering based on string field values.</p>"""
    nested_composite_filters: NotRequired[
        "capo_securityhub.types.software_composite_filter_list.SoftwareCompositeFilterList"
    ]
    """<p>Provides an additional level of filtering, creating a three-layer nested structure. The first layer is a <code>CompositeFilters</code> array with a <code>CompositeOperator</code> (<code>AND</code>/<code>OR</code>). The second layer is a <code>CompositeFilter</code> object that contains direct filters and <code>NestedCompositeFilters</code>. The third layer is <code>NestedCompositeFilters</code>, which contains additional filter conditions.</p>"""
    operator: NotRequired["capo_securityhub.types.allowed_operators.AllowedOperators"]
    """<p>The logical operator used to combine multiple filter conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareCompositeFilter) -> dict:
    out: dict = {}
    if "string_filters" in value:
        import capo_securityhub.types.software_string_filter_list

        out["StringFilters"] = (
            capo_securityhub.types.software_string_filter_list.serialize_json(
                value["string_filters"]
            )
        )
    if "nested_composite_filters" in value:
        import capo_securityhub.types.software_composite_filter_list

        out["NestedCompositeFilters"] = (
            capo_securityhub.types.software_composite_filter_list.serialize_json(
                value["nested_composite_filters"]
            )
        )
    if "operator" in value:
        import capo_securityhub.types.allowed_operators

        out["Operator"] = capo_securityhub.types.allowed_operators.serialize_json(
            value["operator"]
        )
    return out


def deserialize_json(data: dict) -> SoftwareCompositeFilter:
    out: SoftwareCompositeFilter = {}  # type: ignore[typeddict-item]
    if data.get("StringFilters") is not None:
        import capo_securityhub.types.software_string_filter_list

        out["string_filters"] = (
            capo_securityhub.types.software_string_filter_list.deserialize_json(
                data["StringFilters"]
            )
        )
    if data.get("NestedCompositeFilters") is not None:
        import capo_securityhub.types.software_composite_filter_list

        out["nested_composite_filters"] = (
            capo_securityhub.types.software_composite_filter_list.deserialize_json(
                data["NestedCompositeFilters"]
            )
        )
    if data.get("Operator") is not None:
        import capo_securityhub.types.allowed_operators

        out["operator"] = capo_securityhub.types.allowed_operators.deserialize_json(
            data["Operator"]
        )
    return out
