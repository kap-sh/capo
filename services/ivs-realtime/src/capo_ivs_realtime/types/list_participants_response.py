"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListParticipantsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.pagination_token
    import capo_ivs_realtime.types.participant_list


class ListParticipantsResponse(TypedDict, closed=True):
    participants: "capo_ivs_realtime.types.participant_list.ParticipantList"
    """<p>List of the matching participants (summary information only).</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>If there are more participants than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListParticipantsResponse) -> dict:
    out: dict = {}
    import capo_ivs_realtime.types.participant_list

    out["participants"] = capo_ivs_realtime.types.participant_list.serialize_json(
        value["participants"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListParticipantsResponse:
    out: ListParticipantsResponse = {}  # type: ignore[typeddict-item]
    if data.get("participants") is not None:
        import capo_ivs_realtime.types.participant_list

        out["participants"] = capo_ivs_realtime.types.participant_list.deserialize_json(
            data["participants"]
        )
    else:
        out["participants"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
