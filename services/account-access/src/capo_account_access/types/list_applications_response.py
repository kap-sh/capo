"""Generated from Smithy shape ``com.amazonaws.accountaccess#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.application_list


class ListApplicationsResponse(TypedDict, closed=True):
    applications: "capo_account_access.types.application_list.ApplicationList"
    """<p>The list of applications.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token to use in a subsequent request to retrieve the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import capo_account_access.types.application_list

    out["applications"] = capo_account_access.types.application_list.serialize_json(
        value["applications"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("applications") is not None:
        import capo_account_access.types.application_list

        out["applications"] = (
            capo_account_access.types.application_list.deserialize_json(
                data["applications"]
            )
        )
    else:
        raise DeserializationError("ListApplicationsResponse.applications required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
