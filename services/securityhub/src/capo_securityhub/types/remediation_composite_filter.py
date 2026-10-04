"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationCompositeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.remediation_string_filter_list


class RemediationCompositeFilter(TypedDict, closed=True):
    string_filters: NotRequired[
        "capo_securityhub.types.remediation_string_filter_list.RemediationStringFilterList"
    ]
    """<p>Enables filtering based on string field values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationCompositeFilter) -> dict:
    out: dict = {}
    if "string_filters" in value:
        import capo_securityhub.types.remediation_string_filter_list

        out["StringFilters"] = (
            capo_securityhub.types.remediation_string_filter_list.serialize_json(
                value["string_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemediationCompositeFilter:
    out: RemediationCompositeFilter = {}  # type: ignore[typeddict-item]
    if data.get("StringFilters") is not None:
        import capo_securityhub.types.remediation_string_filter_list

        out["string_filters"] = (
            capo_securityhub.types.remediation_string_filter_list.deserialize_json(
                data["StringFilters"]
            )
        )
    return out
