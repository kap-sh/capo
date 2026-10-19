"""Generated from Smithy shape ``com.amazonaws.apprunner#ListAutoScalingConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.auto_scaling_configuration_summary_list
    import capo_apprunner.types.next_token


class ListAutoScalingConfigurationsResponse(TypedDict, closed=True):
    auto_scaling_configuration_summary_list: "capo_apprunner.types.auto_scaling_configuration_summary_list.AutoScalingConfigurationSummaryList"
    """<p>A list of summary information records for auto scaling configurations. In a paginated request, the request returns up to <code>MaxResults</code> records for each call.</p>"""
    next_token: NotRequired["capo_apprunner.types.next_token.NextToken"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutoScalingConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.auto_scaling_configuration_summary_list

    out["AutoScalingConfigurationSummaryList"] = (
        capo_apprunner.types.auto_scaling_configuration_summary_list.serialize_aws_json_1_0(
            value["auto_scaling_configuration_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutoScalingConfigurationsResponse:
    out: ListAutoScalingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AutoScalingConfigurationSummaryList") is not None:
        import capo_apprunner.types.auto_scaling_configuration_summary_list

        out["auto_scaling_configuration_summary_list"] = (
            capo_apprunner.types.auto_scaling_configuration_summary_list.deserialize_aws_json_1_0(
                data["AutoScalingConfigurationSummaryList"]
            )
        )
    else:
        out["auto_scaling_configuration_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
