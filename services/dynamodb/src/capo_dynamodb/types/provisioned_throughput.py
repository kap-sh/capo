"""Generated from Smithy shape ``com.amazonaws.dynamodb#ProvisionedThroughput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.positive_long_object


class ProvisionedThroughput(TypedDict, closed=True):
    read_capacity_units: "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>If read/write capacity mode is <code>PAY_PER_REQUEST</code> the value is set to 0.</p>"""
    write_capacity_units: "capo_dynamodb.types.positive_long_object.PositiveLongObject"
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html">Specifying Read and Write Requirements</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>If read/write capacity mode is <code>PAY_PER_REQUEST</code> the value is set to 0.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionedThroughput) -> dict:
    out: dict = {}
    out["ReadCapacityUnits"] = value["read_capacity_units"]
    out["WriteCapacityUnits"] = value["write_capacity_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProvisionedThroughput:
    out: ProvisionedThroughput = {}  # type: ignore[typeddict-item]
    if data.get("ReadCapacityUnits") is not None:
        out["read_capacity_units"] = data["ReadCapacityUnits"]
    else:
        raise DeserializationError("ProvisionedThroughput.read_capacity_units required")
    if data.get("WriteCapacityUnits") is not None:
        out["write_capacity_units"] = data["WriteCapacityUnits"]
    else:
        raise DeserializationError(
            "ProvisionedThroughput.write_capacity_units required"
        )
    return out
