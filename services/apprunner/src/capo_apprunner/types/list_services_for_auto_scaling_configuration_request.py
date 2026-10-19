"""Generated from Smithy shape ``com.amazonaws.apprunner#ListServicesForAutoScalingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.max_results
    import capo_apprunner.types.next_token


class ListServicesForAutoScalingConfigurationRequest(TypedDict, closed=True):
    auto_scaling_configuration_arn: (
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to list the services for.</p> <p>The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is used.</p>"""
    max_results: NotRequired["capo_apprunner.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>"""
    next_token: NotRequired["capo_apprunner.types.next_token.NextToken"]
    """<p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListServicesForAutoScalingConfigurationRequest,
) -> dict:
    out: dict = {}
    out["AutoScalingConfigurationArn"] = value["auto_scaling_configuration_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListServicesForAutoScalingConfigurationRequest:
    out: ListServicesForAutoScalingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoScalingConfigurationArn") is not None:
        out["auto_scaling_configuration_arn"] = data["AutoScalingConfigurationArn"]
    else:
        out["auto_scaling_configuration_arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
