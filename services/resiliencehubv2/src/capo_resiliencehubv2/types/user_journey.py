"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UserJourney``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_label
    import capo_resiliencehubv2.types.user_journey_id


class UserJourney(TypedDict, closed=True):
    user_journey_id: "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
    """<p>The unique identifier of the user journey.</p>"""
    name: "capo_resiliencehubv2.types.entity_label.EntityLabel"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the user journey was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the user journey was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserJourney) -> dict:
    out: dict = {}
    out["userJourneyId"] = value["user_journey_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UserJourney:
    out: UserJourney = {}  # type: ignore[typeddict-item]
    if data.get("userJourneyId") is not None:
        out["user_journey_id"] = data["userJourneyId"]
    else:
        out["user_journey_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
