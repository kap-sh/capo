"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.recommendation_attribute_map


class Recommendation(TypedDict, closed=True):
    type: "str"
    """<p>The recommendation source type. Known values: <code>OpportunityQuality</code>, <code>SolutionRecommendation</code>, <code>SpecialistRecommendation</code>.</p>"""
    details: "str"
    """<p>Human-readable recommendation text from this source.</p>"""
    attributes: NotRequired[
        "capo_partnercentral_selling.types.recommendation_attribute_map.RecommendationAttributeMap"
    ]
    """<p>Source-specific metadata as key-value pairs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Recommendation) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    out["Details"] = value["details"]
    if "attributes" in value:
        import capo_partnercentral_selling.types.recommendation_attribute_map

        out["Attributes"] = (
            capo_partnercentral_selling.types.recommendation_attribute_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Details") is not None:
        out["details"] = data["Details"]
    else:
        out["details"] = ""
    if data.get("Attributes") is not None:
        import capo_partnercentral_selling.types.recommendation_attribute_map

        out["attributes"] = (
            capo_partnercentral_selling.types.recommendation_attribute_map.deserialize_aws_json_1_0(
                data["Attributes"]
            )
        )
    return out
