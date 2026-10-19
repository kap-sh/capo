"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateRecommenderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class UpdateRecommenderResponse(TypedDict, closed=True):
    recommender_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommenderResponse) -> dict:
    out: dict = {}
    out["RecommenderName"] = value["recommender_name"]
    return out


def deserialize_json(data: dict) -> UpdateRecommenderResponse:
    out: UpdateRecommenderResponse = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderName") is not None:
        out["recommender_name"] = data["RecommenderName"]
    else:
        out["recommender_name"] = ""
    return out
