"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListProfileTimesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.pagination_token
    import capo_codeguruprofiler.types.profile_times


class ListProfileTimesResponse(TypedDict, closed=True):
    profile_times: "capo_codeguruprofiler.types.profile_times.ProfileTimes"
    """<p>The list of start times of the available profiles for the aggregation period in the specified time range. </p>"""
    next_token: NotRequired[
        "capo_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value to include in a future <code>ListProfileTimes</code> request. When the results of a <code>ListProfileTimes</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileTimesResponse) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.profile_times

    out["profileTimes"] = capo_codeguruprofiler.types.profile_times.serialize_json(
        value["profile_times"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileTimesResponse:
    out: ListProfileTimesResponse = {}  # type: ignore[typeddict-item]
    if data.get("profileTimes") is not None:
        import capo_codeguruprofiler.types.profile_times

        out["profile_times"] = (
            capo_codeguruprofiler.types.profile_times.deserialize_json(
                data["profileTimes"]
            )
        )
    else:
        out["profile_times"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
