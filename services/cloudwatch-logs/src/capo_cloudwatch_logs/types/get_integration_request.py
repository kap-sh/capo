"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.integration_name


class GetIntegrationRequest(TypedDict, closed=True):
    integration_name: "capo_cloudwatch_logs.types.integration_name.IntegrationName"
    """<p>The name of the integration that you want to find information about. To find the name of your integration, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html">ListIntegrations</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationName"] = value["integration_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIntegrationRequest:
    out: GetIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationName") is not None:
        out["integration_name"] = data["integrationName"]
    else:
        raise DeserializationError("GetIntegrationRequest.integration_name required")
    return out
