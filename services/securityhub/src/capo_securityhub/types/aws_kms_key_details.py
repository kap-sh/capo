"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsKmsKeyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.double
    import capo_securityhub.types.non_empty_string


class AwsKmsKeyDetails(TypedDict, closed=True):
    aws_account_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The twelve-digit account ID of the Amazon Web Services account that owns the KMS key.</p>"""
    creation_date: NotRequired["capo_securityhub.types.double.Double"]
    """<p>Indicates when the KMS key was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The globally unique identifier for the KMS key.</p>"""
    key_manager: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The manager of the KMS key. KMS keys in your Amazon Web Services account are either customer managed or Amazon Web Services managed.</p>"""
    key_state: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The state of the KMS key. Valid values are as follows:</p> <ul> <li> <p> <code>Disabled</code> </p> </li> <li> <p> <code>Enabled</code> </p> </li> <li> <p> <code>PendingDeletion</code> </p> </li> <li> <p> <code>PendingImport</code> </p> </li> <li> <p> <code>Unavailable</code> </p> </li> </ul>"""
    origin: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source of the KMS key material.</p> <p>When this value is <code>AWS_KMS</code>, KMS created the key material.</p> <p>When this value is <code>EXTERNAL</code>, the key material was imported from your existing key management infrastructure or the KMS key lacks key material.</p> <p>When this value is <code>AWS_CLOUDHSM</code>, the key material was created in the CloudHSM cluster associated with a custom key store.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the KMS key.</p>"""
    key_rotation_status: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the key has key rotation enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsKmsKeyDetails) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["AWSAccountId"] = value["aws_account_id"]
    if "creation_date" in value:
        out["CreationDate"] = (
            "NaN"
            if value["creation_date"] != value["creation_date"]
            else "Infinity"
            if value["creation_date"] == float("inf")
            else "-Infinity"
            if value["creation_date"] == float("-inf")
            else value["creation_date"]
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_manager" in value:
        out["KeyManager"] = value["key_manager"]
    if "key_state" in value:
        out["KeyState"] = value["key_state"]
    if "origin" in value:
        out["Origin"] = value["origin"]
    if "description" in value:
        out["Description"] = value["description"]
    if "key_rotation_status" in value:
        out["KeyRotationStatus"] = value["key_rotation_status"]
    return out


def deserialize_json(data: dict) -> AwsKmsKeyDetails:
    out: AwsKmsKeyDetails = {}  # type: ignore[typeddict-item]
    if data.get("AWSAccountId") is not None:
        out["aws_account_id"] = data["AWSAccountId"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = float(data["CreationDate"])
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("KeyManager") is not None:
        out["key_manager"] = data["KeyManager"]
    if data.get("KeyState") is not None:
        out["key_state"] = data["KeyState"]
    if data.get("Origin") is not None:
        out["origin"] = data["Origin"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KeyRotationStatus") is not None:
        out["key_rotation_status"] = data["KeyRotationStatus"]
    return out
