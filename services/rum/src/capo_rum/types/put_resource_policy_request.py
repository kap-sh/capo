"""Generated from Smithy shape ``com.amazonaws.rum#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_name
    import capo_rum.types.policy_revision_id


class PutResourcePolicyRequest(TypedDict, closed=True):
    name: "capo_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the app monitor that you want to apply this resource-based policy to. To find the names of your app monitors, you can use the <a href="https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListAppMonitors.html">ListAppMonitors</a> operation.</p>"""
    policy_document: "str"
    """<p>The JSON to use as the resource policy. The document can be up to 4 KB in size. For more information about the contents and syntax for this policy, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html">Using resource-based policies with CloudWatch RUM</a>.</p>"""
    policy_revision_id: NotRequired[
        "capo_rum.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A string value that you can use to conditionally update your policy. You can provide the revision ID of your existing policy to make mutating requests against that policy.</p> <p>When you assign a policy revision ID, then later requests about that policy will be rejected with an <code>InvalidPolicyRevisionIdException</code> error if they don't provide the correct current revision ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyDocument"] = value["policy_document"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyDocument") is not None:
        out["policy_document"] = data["PolicyDocument"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy_document required")
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
