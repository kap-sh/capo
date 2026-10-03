"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableBillingModeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsDynamoDbTableBillingModeSummary(TypedDict, closed=True):
    billing_mode: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The method used to charge for read and write throughput and to manage capacity.</p>"""
    last_update_to_pay_per_request_date_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>If the billing mode is <code>PAY_PER_REQUEST</code>, indicates when the billing mode was set to that value.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableBillingModeSummary) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        out["BillingMode"] = value["billing_mode"]
    if "last_update_to_pay_per_request_date_time" in value:
        out["LastUpdateToPayPerRequestDateTime"] = value[
            "last_update_to_pay_per_request_date_time"
        ]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableBillingModeSummary:
    out: AwsDynamoDbTableBillingModeSummary = {}  # type: ignore[typeddict-item]
    if data.get("BillingMode") is not None:
        out["billing_mode"] = data["BillingMode"]
    if data.get("LastUpdateToPayPerRequestDateTime") is not None:
        out["last_update_to_pay_per_request_date_time"] = data[
            "LastUpdateToPayPerRequestDateTime"
        ]
    return out
