"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteUserJourneyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.user_journey_id


class DeleteUserJourneyResponse(TypedDict, closed=True):
    user_journey_id: "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
    """<p>The identifier of the deleted user journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserJourneyResponse) -> dict:
    out: dict = {}
    out["userJourneyId"] = value["user_journey_id"]
    return out


def deserialize_json(data: dict) -> DeleteUserJourneyResponse:
    out: DeleteUserJourneyResponse = {}  # type: ignore[typeddict-item]
    if data.get("userJourneyId") is not None:
        out["user_journey_id"] = data["userJourneyId"]
    else:
        out["user_journey_id"] = ""
    return out
