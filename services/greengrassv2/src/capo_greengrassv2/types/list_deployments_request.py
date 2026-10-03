"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.default_max_results
    import capo_greengrassv2.types.deployment_history_filter
    import capo_greengrassv2.types.next_token_string
    import capo_greengrassv2.types.target_arn
    import capo_greengrassv2.types.thing_group_arn


class ListDeploymentsRequest(TypedDict, closed=True):
    target_arn: NotRequired["capo_greengrassv2.types.target_arn.TargetARN"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the target IoT thing or thing group.</p>"""
    history_filter: NotRequired[
        "capo_greengrassv2.types.deployment_history_filter.DeploymentHistoryFilter"
    ]
    """<p>The filter for the list of deployments. Choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all deployments.</p> </li> <li> <p> <code>LATEST_ONLY</code> – The list includes only the latest revision of each deployment.</p> </li> </ul> <p>Default: <code>LATEST_ONLY</code> </p>"""
    parent_target_arn: NotRequired[
        "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
    ]
    """<p>The parent deployment's target <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> within a subdeployment.</p>"""
    max_results: NotRequired[
        "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
    ]
    """<p>The maximum number of results to be returned per paginated request.</p> <p>Default: <code>50</code> </p>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDeploymentsRequest:
    out: ListDeploymentsRequest = {}  # type: ignore[typeddict-item]
    return out
