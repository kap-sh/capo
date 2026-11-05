"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.software_string_field
    import capo_securityhub.types.string_filter


class SoftwareStringFilter(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_securityhub.types.software_string_field.SoftwareStringField"
    ]
    """<p>The name of the field.</p>"""
    filter: NotRequired["capo_securityhub.types.string_filter.StringFilter"]
    """<p>The string value and comparison operator to filter on. Supported comparisons are <code>EQUALS</code>, <code>NOT_EQUALS</code>, <code>PREFIX</code>, and <code>PREFIX_NOT_EQUALS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareStringFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_securityhub.types.software_string_field

        out["FieldName"] = capo_securityhub.types.software_string_field.serialize_json(
            value["field_name"]
        )
    if "filter" in value:
        import capo_securityhub.types.string_filter

        out["Filter"] = capo_securityhub.types.string_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> SoftwareStringFilter:
    out: SoftwareStringFilter = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        import capo_securityhub.types.software_string_field

        out["field_name"] = (
            capo_securityhub.types.software_string_field.deserialize_json(
                data["FieldName"]
            )
        )
    if data.get("Filter") is not None:
        import capo_securityhub.types.string_filter

        out["filter"] = capo_securityhub.types.string_filter.deserialize_json(
            data["Filter"]
        )
    return out
