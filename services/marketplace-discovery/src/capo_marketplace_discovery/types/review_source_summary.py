"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ReviewSourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.non_negative_count
    import capo_marketplace_discovery.types.review_source_id
    import capo_marketplace_discovery.types.url


class ReviewSourceSummary(TypedDict, closed=True):
    source_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The name of the review source, such as AWS Marketplace.</p>"""
    source_id: "capo_marketplace_discovery.types.review_source_id.ReviewSourceId"
    """<p>The machine-readable identifier of the review source.</p>"""
    source_url: NotRequired["capo_marketplace_discovery.types.url.URL"]
    """<p>The URL where the reviews can be accessed at the source.</p>"""
    average_rating: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The average rating across all reviews from this source.</p>"""
    total_reviews: (
        "capo_marketplace_discovery.types.non_negative_count.NonNegativeCount"
    )
    """<p>The total number of reviews available from this source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReviewSourceSummary) -> dict:
    out: dict = {}
    out["sourceName"] = value["source_name"]
    import capo_marketplace_discovery.types.review_source_id

    out["sourceId"] = capo_marketplace_discovery.types.review_source_id.serialize_json(
        value["source_id"]
    )
    if "source_url" in value:
        out["sourceUrl"] = value["source_url"]
    out["averageRating"] = value["average_rating"]
    out["totalReviews"] = value["total_reviews"]
    return out


def deserialize_json(data: dict) -> ReviewSourceSummary:
    out: ReviewSourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    else:
        out["source_name"] = ""
    if data.get("sourceId") is not None:
        import capo_marketplace_discovery.types.review_source_id

        out["source_id"] = (
            capo_marketplace_discovery.types.review_source_id.deserialize_json(
                data["sourceId"]
            )
        )
    else:
        import typing

        out["source_id"] = typing.cast(
            "capo_marketplace_discovery.types.review_source_id.ReviewSourceId", ""
        )
    if data.get("sourceUrl") is not None:
        out["source_url"] = data["sourceUrl"]
    if data.get("averageRating") is not None:
        out["average_rating"] = data["averageRating"]
    else:
        out["average_rating"] = ""
    if data.get("totalReviews") is not None:
        out["total_reviews"] = data["totalReviews"]
    else:
        out["total_reviews"] = 0
    return out
