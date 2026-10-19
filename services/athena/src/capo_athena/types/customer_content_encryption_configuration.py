"""Generated from Smithy shape ``com.amazonaws.athena#CustomerContentEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.kms_key


class CustomerContentEncryptionConfiguration(TypedDict, closed=True):
    kms_key: "capo_athena.types.kms_key.KmsKey"
    """<p>The customer managed KMS key that is used to encrypt the user's data stores in Athena.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerContentEncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerContentEncryptionConfiguration:
    out: CustomerContentEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    else:
        out["kms_key"] = ""
    return out
