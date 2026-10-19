"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssociatedSystem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.user_journey_id_list


class AssociatedSystem(TypedDict, closed=True):
    system_arn: "capo_resiliencehubv2.types.arn.Arn"
    system_name: NotRequired["capo_resiliencehubv2.types.entity_name.EntityName"]
    user_journey_ids: NotRequired[
        "capo_resiliencehubv2.types.user_journey_id_list.UserJourneyIdList"
    ]
    """<p>The list of user journey identifiers that associate this system with the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedSystem) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    if "system_name" in value:
        out["systemName"] = value["system_name"]
    if "user_journey_ids" in value:
        import capo_resiliencehubv2.types.user_journey_id_list

        out["userJourneyIds"] = (
            capo_resiliencehubv2.types.user_journey_id_list.serialize_json(
                value["user_journey_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociatedSystem:
    out: AssociatedSystem = {}  # type: ignore[typeddict-item]
    if data.get("systemArn") is not None:
        out["system_arn"] = data["systemArn"]
    else:
        out["system_arn"] = ""
    if data.get("systemName") is not None:
        out["system_name"] = data["systemName"]
    if data.get("userJourneyIds") is not None:
        import capo_resiliencehubv2.types.user_journey_id_list

        out["user_journey_ids"] = (
            capo_resiliencehubv2.types.user_journey_id_list.deserialize_json(
                data["userJourneyIds"]
            )
        )
    return out
