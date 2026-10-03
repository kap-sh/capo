"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableSseDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsDynamoDbTableSseDescription(TypedDict, closed=True):
    inaccessible_encryption_date_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>If the key is inaccessible, the date and time when DynamoDB detected that the key was inaccessible.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the server-side encryption.</p>"""
    sse_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of server-side encryption.</p>"""
    kms_master_key_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the KMS key that is used for the KMS encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableSseDescription) -> dict:
    out: dict = {}
    if "inaccessible_encryption_date_time" in value:
        out["InaccessibleEncryptionDateTime"] = value[
            "inaccessible_encryption_date_time"
        ]
    if "status" in value:
        out["Status"] = value["status"]
    if "sse_type" in value:
        out["SseType"] = value["sse_type"]
    if "kms_master_key_arn" in value:
        out["KmsMasterKeyArn"] = value["kms_master_key_arn"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableSseDescription:
    out: AwsDynamoDbTableSseDescription = {}  # type: ignore[typeddict-item]
    if data.get("InaccessibleEncryptionDateTime") is not None:
        out["inaccessible_encryption_date_time"] = data[
            "InaccessibleEncryptionDateTime"
        ]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("SseType") is not None:
        out["sse_type"] = data["SseType"]
    if data.get("KmsMasterKeyArn") is not None:
        out["kms_master_key_arn"] = data["KmsMasterKeyArn"]
    return out
