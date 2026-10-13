"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ListEnvironmentsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.environment_list
    import capo_workspaces_thin_client.types.pagination_token


class ListEnvironmentsResponse(TypedDict, closed=True):
    environments: NotRequired[
        "capo_workspaces_thin_client.types.environment_list.EnvironmentList"
    ]
    """<p>Describes environments.</p>"""
    next_token: NotRequired[
        "capo_workspaces_thin_client.types.pagination_token.PaginationToken"
    ]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsResponse) -> dict:
    out: dict = {}
    if "environments" in value:
        import capo_workspaces_thin_client.types.environment_list

        out["environments"] = (
            capo_workspaces_thin_client.types.environment_list.serialize_json(
                value["environments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsResponse:
    out: ListEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("environments") is not None:
        import capo_workspaces_thin_client.types.environment_list

        out["environments"] = (
            capo_workspaces_thin_client.types.environment_list.deserialize_json(
                data["environments"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListEnvironmentsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environments" in value:
        import capo_workspaces_thin_client.types.environment_list

        out["environments"] = (
            capo_workspaces_thin_client.types.environment_list.redact_sensitive(
                value["environments"]
            )
        )
    return out
