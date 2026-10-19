"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentAccountConnectionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.environment_account_connection_requester_account_type
    import capo_proton.types.environment_account_connection_status_list
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.resource_name


class ListEnvironmentAccountConnectionsInput(TypedDict, closed=True):
    requested_by: "capo_proton.types.environment_account_connection_requester_account_type.EnvironmentAccountConnectionRequesterAccountType"
    """<p>The type of account making the <code>ListEnvironmentAccountConnections</code> request.</p>"""
    environment_name: NotRequired["capo_proton.types.resource_name.ResourceName"]
    """<p>The environment name that's associated with each listed environment account connection.</p>"""
    statuses: NotRequired[
        "capo_proton.types.environment_account_connection_status_list.EnvironmentAccountConnectionStatusList"
    ]
    """<p>The status details for each listed environment account connection.</p>"""
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next environment account connection in the array of environment account connections, after the list of environment account connections that was previously requested.</p>"""
    max_results: NotRequired["capo_proton.types.max_page_results.MaxPageResults"]
    """<p>The maximum number of environment account connections to list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentAccountConnectionsInput) -> dict:
    out: dict = {}
    out["requestedBy"] = value["requested_by"]
    if "environment_name" in value:
        out["environmentName"] = value["environment_name"]
    if "statuses" in value:
        import capo_proton.types.environment_account_connection_status_list

        out["statuses"] = (
            capo_proton.types.environment_account_connection_status_list.serialize_aws_json_1_0(
                value["statuses"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentAccountConnectionsInput:
    out: ListEnvironmentAccountConnectionsInput = {}  # type: ignore[typeddict-item]
    if data.get("requestedBy") is not None:
        out["requested_by"] = data["requestedBy"]
    else:
        out["requested_by"] = ""
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    if data.get("statuses") is not None:
        import capo_proton.types.environment_account_connection_status_list

        out["statuses"] = (
            capo_proton.types.environment_account_connection_status_list.deserialize_aws_json_1_0(
                data["statuses"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
