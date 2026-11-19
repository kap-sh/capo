"""Generated from Smithy shape ``com.amazonaws.qconnect#ProfileRecommendation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.profile_catalog_item
    import capo_qconnect.types.profile_recommendation_score


class ProfileRecommendation(TypedDict, closed=True):
    score: "capo_qconnect.types.profile_recommendation_score.ProfileRecommendationScore"
    """<p>The relevance score of the recommendation.</p>"""
    catalog_item: NotRequired[
        "capo_qconnect.types.profile_catalog_item.ProfileCatalogItem"
    ]
    """<p>The catalog item that is associated with the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileRecommendation) -> dict:
    out: dict = {}
    out["score"] = (
        "NaN"
        if value.get("score", 0) != value.get("score", 0)
        else "Infinity"
        if value.get("score", 0) == float("inf")
        else "-Infinity"
        if value.get("score", 0) == float("-inf")
        else value.get("score", 0)
    )
    if "catalog_item" in value:
        import capo_qconnect.types.profile_catalog_item

        out["catalogItem"] = capo_qconnect.types.profile_catalog_item.serialize_json(
            value["catalog_item"]
        )
    return out


def deserialize_json(data: dict) -> ProfileRecommendation:
    out: ProfileRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    else:
        out["score"] = 0
    if data.get("catalogItem") is not None:
        import capo_qconnect.types.profile_catalog_item

        out["catalog_item"] = capo_qconnect.types.profile_catalog_item.deserialize_json(
            data["catalogItem"]
        )
    return out


def redact_sensitive(value: ProfileRecommendation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "score" in value:
        out["score"] = "*** Sensitive Data Redacted ***"
    if "catalog_item" in value:
        import capo_qconnect.types.profile_catalog_item

        out["catalog_item"] = capo_qconnect.types.profile_catalog_item.redact_sensitive(
            value["catalog_item"]
        )
    return out
