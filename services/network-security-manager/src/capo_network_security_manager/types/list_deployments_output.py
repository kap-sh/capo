"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListDeploymentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_summary_list
    import capo_network_security_manager.types.next_token


class ListDeploymentsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""
    deployments: "capo_network_security_manager.types.deployment_summary_list.DeploymentSummaryList"
    """<p>The list of deployments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_network_security_manager.types.deployment_summary_list

    out["deployments"] = (
        capo_network_security_manager.types.deployment_summary_list.serialize_json(
            value["deployments"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListDeploymentsOutput:
    out: ListDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("deployments") is not None:
        import capo_network_security_manager.types.deployment_summary_list

        out["deployments"] = (
            capo_network_security_manager.types.deployment_summary_list.deserialize_json(
                data["deployments"]
            )
        )
    else:
        raise DeserializationError("ListDeploymentsOutput.deployments required")
    return out
