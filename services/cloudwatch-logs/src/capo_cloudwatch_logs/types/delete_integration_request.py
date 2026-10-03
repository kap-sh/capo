"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.force
    import capo_cloudwatch_logs.types.integration_name


class DeleteIntegrationRequest(TypedDict, closed=True):
    integration_name: "capo_cloudwatch_logs.types.integration_name.IntegrationName"
    """<p>The name of the integration to delete. To find the name of your integration, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html">ListIntegrations</a>.</p>"""
    force: "capo_cloudwatch_logs.types.force.Force"
    """<p>Specify <code>true</code> to force the deletion of the integration even if vended logs dashboards currently exist.</p> <p>The default is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationName"] = value["integration_name"]
    out["force"] = value.get("force", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIntegrationRequest:
    out: DeleteIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationName") is not None:
        out["integration_name"] = data["integrationName"]
    else:
        raise DeserializationError("DeleteIntegrationRequest.integration_name required")
    if data.get("force") is not None:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
