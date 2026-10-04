"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.remediation_composite_filter_list


class RemediationFilters(TypedDict, closed=True):
    composite_filters: NotRequired[
        "capo_securityhub.types.remediation_composite_filter_list.RemediationCompositeFilterList"
    ]
    """<p>A collection of complex filtering conditions that can be applied to remediation target data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationFilters) -> dict:
    out: dict = {}
    if "composite_filters" in value:
        import capo_securityhub.types.remediation_composite_filter_list

        out["CompositeFilters"] = (
            capo_securityhub.types.remediation_composite_filter_list.serialize_json(
                value["composite_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemediationFilters:
    out: RemediationFilters = {}  # type: ignore[typeddict-item]
    if data.get("CompositeFilters") is not None:
        import capo_securityhub.types.remediation_composite_filter_list

        out["composite_filters"] = (
            capo_securityhub.types.remediation_composite_filter_list.deserialize_json(
                data["CompositeFilters"]
            )
        )
    return out
