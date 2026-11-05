"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareGroupByRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.software_filters
    import capo_securityhub.types.software_group_by_field


class SoftwareGroupByRule(TypedDict, closed=True):
    group_by_field: NotRequired[
        "capo_securityhub.types.software_group_by_field.SoftwareGroupByField"
    ]
    """<p>Specifies the attribute that software statistics should be grouped by.</p>"""
    filters: NotRequired["capo_securityhub.types.software_filters.SoftwareFilters"]
    """<p>The criteria used to select the software packages included in the statistics. You can nest composite filters up to three levels deep.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareGroupByRule) -> dict:
    out: dict = {}
    if "group_by_field" in value:
        import capo_securityhub.types.software_group_by_field

        out["GroupByField"] = (
            capo_securityhub.types.software_group_by_field.serialize_json(
                value["group_by_field"]
            )
        )
    if "filters" in value:
        import capo_securityhub.types.software_filters

        out["Filters"] = capo_securityhub.types.software_filters.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> SoftwareGroupByRule:
    out: SoftwareGroupByRule = {}  # type: ignore[typeddict-item]
    if data.get("GroupByField") is not None:
        import capo_securityhub.types.software_group_by_field

        out["group_by_field"] = (
            capo_securityhub.types.software_group_by_field.deserialize_json(
                data["GroupByField"]
            )
        )
    if data.get("Filters") is not None:
        import capo_securityhub.types.software_filters

        out["filters"] = capo_securityhub.types.software_filters.deserialize_json(
            data["Filters"]
        )
    return out
