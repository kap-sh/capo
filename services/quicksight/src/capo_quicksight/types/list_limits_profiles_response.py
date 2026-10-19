"""Generated from Smithy shape ``com.amazonaws.quicksight#ListLimitsProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limits_profile_list


class ListLimitsProfilesResponse(TypedDict, closed=True):
    profiles: "capo_quicksight.types.limits_profile_list.LimitsProfileList"
    """<p>A list of limits profiles.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLimitsProfilesResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.limits_profile_list

    out["profiles"] = capo_quicksight.types.limits_profile_list.serialize_json(
        value["profiles"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLimitsProfilesResponse:
    out: ListLimitsProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("profiles") is not None:
        import capo_quicksight.types.limits_profile_list

        out["profiles"] = capo_quicksight.types.limits_profile_list.deserialize_json(
            data["profiles"]
        )
    else:
        out["profiles"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
