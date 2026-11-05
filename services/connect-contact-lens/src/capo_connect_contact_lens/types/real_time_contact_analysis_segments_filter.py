"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#RealTimeContactAnalysisSegmentsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.categories_attribute_filter


class RealTimeContactAnalysisSegmentsFilter(TypedDict, closed=True):
    categories_attribute_filter: NotRequired[
        "capo_connect_contact_lens.types.categories_attribute_filter.CategoriesAttributeFilter"
    ]
    """<p>A filter applied to category segments based on the tags of the rules that create the matched categories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentsFilter) -> dict:
    out: dict = {}
    if "categories_attribute_filter" in value:
        import capo_connect_contact_lens.types.categories_attribute_filter

        out["CategoriesAttributeFilter"] = (
            capo_connect_contact_lens.types.categories_attribute_filter.serialize_json(
                value["categories_attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentsFilter:
    out: RealTimeContactAnalysisSegmentsFilter = {}  # type: ignore[typeddict-item]
    if data.get("CategoriesAttributeFilter") is not None:
        import capo_connect_contact_lens.types.categories_attribute_filter

        out["categories_attribute_filter"] = (
            capo_connect_contact_lens.types.categories_attribute_filter.deserialize_json(
                data["CategoriesAttributeFilter"]
            )
        )
    return out
