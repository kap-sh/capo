"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableProvisionedThroughput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsDynamoDbTableProvisionedThroughput(TypedDict, closed=True):
    last_decrease_date_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the provisioned throughput was last decreased.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    last_increase_date_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the provisioned throughput was last increased.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    number_of_decreases_today: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of times during the current UTC calendar day that the provisioned throughput was decreased.</p>"""
    read_capacity_units: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The maximum number of strongly consistent reads consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""
    write_capacity_units: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableProvisionedThroughput) -> dict:
    out: dict = {}
    if "last_decrease_date_time" in value:
        out["LastDecreaseDateTime"] = value["last_decrease_date_time"]
    if "last_increase_date_time" in value:
        out["LastIncreaseDateTime"] = value["last_increase_date_time"]
    if "number_of_decreases_today" in value:
        out["NumberOfDecreasesToday"] = value["number_of_decreases_today"]
    if "read_capacity_units" in value:
        out["ReadCapacityUnits"] = value["read_capacity_units"]
    if "write_capacity_units" in value:
        out["WriteCapacityUnits"] = value["write_capacity_units"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableProvisionedThroughput:
    out: AwsDynamoDbTableProvisionedThroughput = {}  # type: ignore[typeddict-item]
    if data.get("LastDecreaseDateTime") is not None:
        out["last_decrease_date_time"] = data["LastDecreaseDateTime"]
    if data.get("LastIncreaseDateTime") is not None:
        out["last_increase_date_time"] = data["LastIncreaseDateTime"]
    if data.get("NumberOfDecreasesToday") is not None:
        out["number_of_decreases_today"] = data["NumberOfDecreasesToday"]
    if data.get("ReadCapacityUnits") is not None:
        out["read_capacity_units"] = data["ReadCapacityUnits"]
    if data.get("WriteCapacityUnits") is not None:
        out["write_capacity_units"] = data["WriteCapacityUnits"]
    return out
