"""Generated from Smithy shape ``com.amazonaws.proton#ListDeploymentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.deployment_summary_list
    import capo_proton.types.next_token


class ListDeploymentsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next deployment in the array of deployment, after the current requested list of deployment.</p>"""
    deployments: "capo_proton.types.deployment_summary_list.DeploymentSummaryList"
    """<p>An array of deployment with summary data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDeploymentsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.deployment_summary_list

    out["deployments"] = (
        capo_proton.types.deployment_summary_list.serialize_aws_json_1_0(
            value["deployments"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDeploymentsOutput:
    out: ListDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("deployments") is not None:
        import capo_proton.types.deployment_summary_list

        out["deployments"] = (
            capo_proton.types.deployment_summary_list.deserialize_aws_json_1_0(
                data["deployments"]
            )
        )
    else:
        out["deployments"] = []
    return out
