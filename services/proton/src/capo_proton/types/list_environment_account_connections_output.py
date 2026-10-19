"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentAccountConnectionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.environment_account_connection_summary_list
    import capo_proton.types.next_token


class ListEnvironmentAccountConnectionsOutput(TypedDict, closed=True):
    environment_account_connections: "capo_proton.types.environment_account_connection_summary_list.EnvironmentAccountConnectionSummaryList"
    """<p>An array of environment account connections with details that's returned by Proton. </p>"""
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next environment account connection in the array of environment account connections, after the current requested list of environment account connections.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentAccountConnectionsOutput) -> dict:
    out: dict = {}
    import capo_proton.types.environment_account_connection_summary_list

    out["environmentAccountConnections"] = (
        capo_proton.types.environment_account_connection_summary_list.serialize_aws_json_1_0(
            value["environment_account_connections"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentAccountConnectionsOutput:
    out: ListEnvironmentAccountConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("environmentAccountConnections") is not None:
        import capo_proton.types.environment_account_connection_summary_list

        out["environment_account_connections"] = (
            capo_proton.types.environment_account_connection_summary_list.deserialize_aws_json_1_0(
                data["environmentAccountConnections"]
            )
        )
    else:
        out["environment_account_connections"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
