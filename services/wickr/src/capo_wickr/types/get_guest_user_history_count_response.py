"""Generated from Smithy shape ``com.amazonaws.wickr#GetGuestUserHistoryCountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.guest_user_history_count_list


class GetGuestUserHistoryCountResponse(TypedDict, closed=True):
    history: "capo_wickr.types.guest_user_history_count_list.GuestUserHistoryCountList"
    """<p>A list of historical guest user counts, organized by month and billing period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGuestUserHistoryCountResponse) -> dict:
    out: dict = {}
    import capo_wickr.types.guest_user_history_count_list

    out["history"] = capo_wickr.types.guest_user_history_count_list.serialize_json(
        value["history"]
    )
    return out


def deserialize_json(data: dict) -> GetGuestUserHistoryCountResponse:
    out: GetGuestUserHistoryCountResponse = {}  # type: ignore[typeddict-item]
    if data.get("history") is not None:
        import capo_wickr.types.guest_user_history_count_list

        out["history"] = (
            capo_wickr.types.guest_user_history_count_list.deserialize_json(
                data["history"]
            )
        )
    else:
        out["history"] = []
    return out
