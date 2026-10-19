"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteUserJourneyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.user_journey_id


class DeleteUserJourneyRequest(TypedDict, closed=True):
    system_arn: "capo_resiliencehubv2.types.arn.Arn"
    user_journey_id: "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
    """<p>The identifier of the user journey to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserJourneyRequest) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    out["userJourneyId"] = value["user_journey_id"]
    return out


def deserialize_json(data: dict) -> DeleteUserJourneyRequest:
    out: DeleteUserJourneyRequest = {}  # type: ignore[typeddict-item]
    if data.get("systemArn") is not None:
        out["system_arn"] = data["systemArn"]
    else:
        out["system_arn"] = ""
    if data.get("userJourneyId") is not None:
        out["user_journey_id"] = data["userJourneyId"]
    else:
        out["user_journey_id"] = ""
    return out
