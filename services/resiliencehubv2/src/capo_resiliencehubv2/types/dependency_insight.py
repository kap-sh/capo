"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyInsight``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.insights_category


class DependencyInsight(TypedDict, closed=True):
    category: "capo_resiliencehubv2.types.insights_category.InsightsCategory"
    """<p>The category of the insight. Valid values:</p> <ul> <li> <p>CROSS_REGION - The insight relates to dependencies used across multiple Regions.</p> </li> <li> <p>NEW_DEPENDENCY - The insight relates to a recently detected dependency.</p> </li> <li> <p>THIRD_PARTY - The insight relates to a third-party dependency.</p> </li> <li> <p>UNEVEN_USAGE - The insight relates to a dependency with uneven usage across the service.</p> </li> <li> <p>AWS_SERVICE - The insight relates to a dependency on an Amazon Web Services service.</p> </li> </ul>"""
    description: "str"
    """<p>A human-readable explanation of the insight, describing the dependency behavior or condition that was detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyInsight) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.insights_category

    out["category"] = capo_resiliencehubv2.types.insights_category.serialize_json(
        value["category"]
    )
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> DependencyInsight:
    out: DependencyInsight = {}  # type: ignore[typeddict-item]
    if data.get("category") is not None:
        import capo_resiliencehubv2.types.insights_category

        out["category"] = capo_resiliencehubv2.types.insights_category.deserialize_json(
            data["category"]
        )
    else:
        import typing

        out["category"] = typing.cast(
            "capo_resiliencehubv2.types.insights_category.InsightsCategory", ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
