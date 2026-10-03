"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutIndexPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_identifier
    import capo_cloudwatch_logs.types.policy_document


class PutIndexPolicyRequest(TypedDict, closed=True):
    log_group_identifier: (
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    """<p>Specify either the log group name or log group ARN to apply this field index policy to. If you specify an ARN, use the format arn:aws:logs:<i>region</i>:<i>account-id</i>:log-group:<i>log_group_name</i> Don't include an * at the end.</p>"""
    policy_document: "capo_cloudwatch_logs.types.policy_document.PolicyDocument"
    """<p>The index policy document, in JSON format. The following is an example of an index policy document that creates indexes with different types.</p> <p> <code>"policyDocument": "{"Fields": [ "TransactionId" ], "FieldsV2": {"RequestId": {"type": "FIELD_INDEX"}, "APIName": {"type": "FACET"}, "StatusCode": {"type": "FACET"}}}"</code> </p> <p>You can use <code>FieldsV2</code> to specify the type for each field. Supported types are <code>FIELD_INDEX</code> and <code>FACET</code>. Field names within <code>Fields</code> and <code>FieldsV2</code> must be mutually exclusive.</p> <p>The policy document must include at least one field index. For more information about the fields that can be included and other restrictions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Syntax.html">Field index syntax and quotas</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutIndexPolicyRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    out["policyDocument"] = value["policy_document"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutIndexPolicyRequest:
    out: PutIndexPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        raise DeserializationError(
            "PutIndexPolicyRequest.log_group_identifier required"
        )
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError("PutIndexPolicyRequest.policy_document required")
    return out
