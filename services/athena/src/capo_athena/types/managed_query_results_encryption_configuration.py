"""Generated from Smithy shape ``com.amazonaws.athena#ManagedQueryResultsEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.kms_key


class ManagedQueryResultsEncryptionConfiguration(TypedDict, closed=True):
    kms_key: "capo_athena.types.kms_key.KmsKey"
    """<p>The ARN of an KMS key for encrypting managed query results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedQueryResultsEncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedQueryResultsEncryptionConfiguration:
    out: ManagedQueryResultsEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    else:
        out["kms_key"] = ""
    return out
