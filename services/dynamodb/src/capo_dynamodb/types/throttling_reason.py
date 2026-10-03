"""Generated from Smithy shape ``com.amazonaws.dynamodb#ThrottlingReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.reason
    import capo_dynamodb.types.resource


class ThrottlingReason(TypedDict, closed=True):
    reason: NotRequired["capo_dynamodb.types.reason.Reason"]
    """<p>The reason for throttling. The throttling reason follows a specific format: <code>ResourceType+OperationType+LimitType</code>:</p> <ul> <li> <p>Resource Type (What is being throttled): Table or Index</p> </li> <li> <p>Operation Type (What kind of operation): Read or Write</p> </li> <li> <p>Limit Type (Why the throttling occurred):</p> <ul> <li> <p> <code>ProvisionedThroughputExceeded</code>: The request rate is exceeding the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html">provisioned throughput capacity</a> (read or write capacity units) configured for a table or a global secondary index (GSI) in provisioned capacity mode.</p> </li> <li> <p> <code>AccountLimitExceeded</code>: The request rate has caused a table or global secondary index (GSI) in on-demand mode to exceed the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#default-limits-throughput">per-table account-level service quotas</a> for read/write throughput in the current Amazon Web Services Region. </p> </li> <li> <p> <code>KeyRangeThroughputExceeded</code>: The request rate directed at a specific partition key value has exceeded the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html">internal partition-level throughput limits</a>, indicating uneven access patterns across the table's or GSI's key space.</p> </li> <li> <p> <code>MaxOnDemandThroughputExceeded</code>: The request rate has exceeded the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode-max-throughput.html">configured maximum throughput limits</a> set for a table or index in on-demand capacity mode.</p> </li> </ul> </li> </ul> <p>Examples of complete throttling reasons:</p> <ul> <li> <p>TableReadProvisionedThroughputExceeded</p> </li> <li> <p>IndexWriteAccountLimitExceeded</p> </li> </ul> <p>This helps identify exactly what resource is being throttled, what type of operation caused it, and why the throttling occurred.</p>"""
    resource: NotRequired["capo_dynamodb.types.resource.Resource"]
    """<p>The Amazon Resource Name (ARN) of the DynamoDB table or index that experienced the throttling event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingReason) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "resource" in value:
        out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingReason:
    out: ThrottlingReason = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    return out
