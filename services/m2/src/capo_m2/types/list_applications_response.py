"""Generated from Smithy shape ``com.amazonaws.m2#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.application_summary_list
    import capo_m2.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    applications: "capo_m2.types.application_summary_list.ApplicationSummaryList"
    """<p>Returns a list of summary details for all the applications in a runtime environment.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>A pagination token that's returned when the response doesn't contain all applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import capo_m2.types.application_summary_list

    out["applications"] = capo_m2.types.application_summary_list.serialize_json(
        value["applications"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("applications") is not None:
        import capo_m2.types.application_summary_list

        out["applications"] = capo_m2.types.application_summary_list.deserialize_json(
            data["applications"]
        )
    else:
        out["applications"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
