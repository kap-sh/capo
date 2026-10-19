"""Generated from Smithy shape ``com.amazonaws.m2#ListEnvironmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.environment_summary_list
    import capo_m2.types.next_token


class ListEnvironmentsResponse(TypedDict, closed=True):
    environments: "capo_m2.types.environment_summary_list.EnvironmentSummaryList"
    """<p>Returns a list of summary details for all the runtime environments in your account. </p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>A pagination token that's returned when the response doesn't contain all the runtime environments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsResponse) -> dict:
    out: dict = {}
    import capo_m2.types.environment_summary_list

    out["environments"] = capo_m2.types.environment_summary_list.serialize_json(
        value["environments"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsResponse:
    out: ListEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("environments") is not None:
        import capo_m2.types.environment_summary_list

        out["environments"] = capo_m2.types.environment_summary_list.deserialize_json(
            data["environments"]
        )
    else:
        out["environments"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
