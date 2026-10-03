"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDestinationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.access_policy
    import capo_cloudwatch_logs.types.destination_name
    import capo_cloudwatch_logs.types.force_update


class PutDestinationPolicyRequest(TypedDict, closed=True):
    destination_name: "capo_cloudwatch_logs.types.destination_name.DestinationName"
    """<p>A name for an existing destination.</p>"""
    access_policy: "capo_cloudwatch_logs.types.access_policy.AccessPolicy"
    """<p>An IAM policy document that authorizes cross-account users to deliver their log events to the associated destination. This can be up to 5120 bytes.</p>"""
    force_update: NotRequired["capo_cloudwatch_logs.types.force_update.ForceUpdate"]
    """<p>Specify true if you are updating an existing destination policy to grant permission to an organization ID instead of granting permission to individual Amazon Web Services accounts. Before you update a destination policy this way, you must first update the subscription filters in the accounts that send logs to this destination. If you do not, the subscription filters might stop working. By specifying <code>true</code> for <code>forceUpdate</code>, you are affirming that you have already updated the subscription filters. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-Update.html"> Updating an existing cross-account subscription</a> </p> <p>If you omit this parameter, the default of <code>false</code> is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDestinationPolicyRequest) -> dict:
    out: dict = {}
    out["destinationName"] = value["destination_name"]
    out["accessPolicy"] = value["access_policy"]
    if "force_update" in value:
        out["forceUpdate"] = value["force_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDestinationPolicyRequest:
    out: PutDestinationPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("destinationName") is not None:
        out["destination_name"] = data["destinationName"]
    else:
        raise DeserializationError(
            "PutDestinationPolicyRequest.destination_name required"
        )
    if data.get("accessPolicy") is not None:
        out["access_policy"] = data["accessPolicy"]
    else:
        raise DeserializationError("PutDestinationPolicyRequest.access_policy required")
    if data.get("forceUpdate") is not None:
        out["force_update"] = data["forceUpdate"]
    return out
