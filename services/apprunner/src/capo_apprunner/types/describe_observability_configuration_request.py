"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeObservabilityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn


class DescribeObservabilityConfigurationRequest(TypedDict, closed=True):
    observability_configuration_arn: (
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner observability configuration that you want a description for.</p> <p>The ARN can be a full observability configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is described.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeObservabilityConfigurationRequest) -> dict:
    out: dict = {}
    out["ObservabilityConfigurationArn"] = value["observability_configuration_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeObservabilityConfigurationRequest:
    out: DescribeObservabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ObservabilityConfigurationArn") is not None:
        out["observability_configuration_arn"] = data["ObservabilityConfigurationArn"]
    else:
        out["observability_configuration_arn"] = ""
    return out
