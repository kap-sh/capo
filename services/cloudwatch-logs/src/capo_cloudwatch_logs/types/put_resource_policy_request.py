"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.expected_revision_id
    import capo_cloudwatch_logs.types.policy_document
    import capo_cloudwatch_logs.types.policy_name


class PutResourcePolicyRequest(TypedDict, closed=True):
    policy_name: NotRequired["capo_cloudwatch_logs.types.policy_name.PolicyName"]
    """<p>Name of the new policy. This parameter is required.</p>"""
    policy_document: NotRequired[
        "capo_cloudwatch_logs.types.policy_document.PolicyDocument"
    ]
    """<p>Details of the new policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. This parameter is required.</p> <p>The following example creates a resource policy enabling the Route 53 service to put DNS query logs in to the specified log group. Replace <code>"logArn"</code> with the ARN of your CloudWatch Logs resource, such as a log group or log stream.</p> <p>CloudWatch Logs also supports <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn">aws:SourceArn</a> and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount">aws:SourceAccount</a> condition context keys.</p> <p>In the example resource policy, you would replace the value of <code>SourceArn</code> with the resource making the call from Route 53 to CloudWatch Logs. You would also replace the value of <code>SourceAccount</code> with the Amazon Web Services account ID making that call.</p> <p></p> <p> <code>{ "Version": "2012-10-17", "Statement": [ { "Sid": "Route53LogsToCloudWatchLogs", "Effect": "Allow", "Principal": { "Service": [ "route53.amazonaws.com" ] }, "Action": "logs:PutLogEvents", "Resource": "logArn", "Condition": { "ArnLike": { "aws:SourceArn": "myRoute53ResourceArn" }, "StringEquals": { "aws:SourceAccount": "myAwsAccountId" } } } ] }</code> </p>"""
    resource_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the CloudWatch Logs resource to which the resource policy needs to be added or attached. Currently only supports LogGroup ARN.</p>"""
    expected_revision_id: NotRequired[
        "capo_cloudwatch_logs.types.expected_revision_id.ExpectedRevisionId"
    ]
    """<p>The expected revision ID of the resource policy. Required when <code>resourceArn</code> is provided to prevent concurrent modifications. Use <code>null</code> when creating a resource policy for the first time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "expected_revision_id" in value:
        out["expectedRevisionId"] = value["expected_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("expectedRevisionId") is not None:
        out["expected_revision_id"] = data["expectedRevisionId"]
    return out
