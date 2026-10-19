"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.arn
    import capo_customer_profiles.types.tag_map


class CreateRecommenderFilterResponse(TypedDict, closed=True):
    recommender_filter_arn: "capo_customer_profiles.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recommender filter.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderFilterResponse) -> dict:
    out: dict = {}
    out["RecommenderFilterArn"] = value["recommender_filter_arn"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecommenderFilterResponse:
    out: CreateRecommenderFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderFilterArn") is not None:
        out["recommender_filter_arn"] = data["RecommenderFilterArn"]
    else:
        out["recommender_filter_arn"] = ""
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
