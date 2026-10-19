"""Generated from Smithy shape ``com.amazonaws.freetier#ListAccountActivitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.activities
    import capo_freetier.types.next_page_token


class ListAccountActivitiesResponse(TypedDict, closed=True):
    activities: "capo_freetier.types.activities.Activities"
    """<p> A brief information about the activities. </p>"""
    next_token: NotRequired["capo_freetier.types.next_page_token.NextPageToken"]
    """<p> The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAccountActivitiesResponse) -> dict:
    out: dict = {}
    import capo_freetier.types.activities

    out["activities"] = capo_freetier.types.activities.serialize_aws_json_1_0(
        value["activities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAccountActivitiesResponse:
    out: ListAccountActivitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("activities") is not None:
        import capo_freetier.types.activities

        out["activities"] = capo_freetier.types.activities.deserialize_aws_json_1_0(
            data["activities"]
        )
    else:
        out["activities"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
