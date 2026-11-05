"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#CategoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.points_of_interest
    import capo_connect_contact_lens.types.rule_id


class CategoryDetails(TypedDict, closed=True):
    points_of_interest: NotRequired[
        "capo_connect_contact_lens.types.points_of_interest.PointsOfInterest"
    ]
    """<p>The section of audio where the category rule was detected.</p>"""
    rule_id: NotRequired["capo_connect_contact_lens.types.rule_id.RuleId"]
    """<p>The unique identifier of the rule that created the matched category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryDetails) -> dict:
    out: dict = {}
    if "points_of_interest" in value:
        import capo_connect_contact_lens.types.points_of_interest

        out["PointsOfInterest"] = (
            capo_connect_contact_lens.types.points_of_interest.serialize_json(
                value["points_of_interest"]
            )
        )
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> CategoryDetails:
    out: CategoryDetails = {}  # type: ignore[typeddict-item]
    if data.get("PointsOfInterest") is not None:
        import capo_connect_contact_lens.types.points_of_interest

        out["points_of_interest"] = (
            capo_connect_contact_lens.types.points_of_interest.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    return out
