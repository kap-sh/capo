"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_list
    import capo_emr_serverless.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    applications: "capo_emr_serverless.types.application_list.ApplicationList"
    """<p>The output lists the specified applications.</p>"""
    next_token: NotRequired["capo_emr_serverless.types.next_token.NextToken"]
    """<p>The output displays the token for the next set of application results. This is required for pagination and is available as a response of the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import capo_emr_serverless.types.application_list

    out["applications"] = capo_emr_serverless.types.application_list.serialize_json(
        value["applications"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("applications") is not None:
        import capo_emr_serverless.types.application_list

        out["applications"] = (
            capo_emr_serverless.types.application_list.deserialize_json(
                data["applications"]
            )
        )
    else:
        out["applications"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
