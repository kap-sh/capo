"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.application_list
    import capo_iotsitewise.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>Next Page Token</p>"""
    applications: "capo_iotsitewise.types.application_list.ApplicationList"
    """<p>List of applications</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_iotsitewise.types.application_list

    out["applications"] = capo_iotsitewise.types.application_list.serialize_json(
        value["applications"]
    )
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("applications") is not None:
        import capo_iotsitewise.types.application_list

        out["applications"] = capo_iotsitewise.types.application_list.deserialize_json(
            data["applications"]
        )
    else:
        out["applications"] = []
    return out
