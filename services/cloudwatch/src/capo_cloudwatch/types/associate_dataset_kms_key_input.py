"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AssociateDatasetKmsKeyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dataset_identifier
    import capo_cloudwatch.types.kms_key_arn


class AssociateDatasetKmsKeyInput(TypedDict, closed=True):
    dataset_identifier: NotRequired[
        "capo_cloudwatch.types.dataset_identifier.DatasetIdentifier"
    ]
    """<p>Specifies the identifier of the dataset that you want to associate the KMS key with. For the <code>default</code> dataset, you can specify either <code>default</code> or the full dataset Amazon Resource Name (ARN) in the format <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:dataset/default</code>.</p>"""
    kms_key_arn: NotRequired["capo_cloudwatch.types.kms_key_arn.KmsKeyArn"]
    """<p>Specifies the Amazon Resource Name (ARN) of the customer managed KMS key to associate with the dataset. The key must be a symmetric encryption KMS key (<code>SYMMETRIC_DEFAULT</code>) in the same Amazon Web Services Region as the dataset.</p> <p>The ARN must be in the format <code>arn:aws:kms:<i>Region</i>:<i>account-id</i>:key/<i>key-id</i> </code>. Key IDs, aliases, and alias ARNs are not accepted.</p> <p>For more information about KMS key ARNs, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key ARN</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateDatasetKmsKeyInput) -> dict:
    out: dict = {}
    if "dataset_identifier" in value:
        out["DatasetIdentifier"] = value["dataset_identifier"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateDatasetKmsKeyInput:
    out: AssociateDatasetKmsKeyInput = {}  # type: ignore[typeddict-item]
    if data.get("DatasetIdentifier") is not None:
        out["dataset_identifier"] = data["DatasetIdentifier"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: AssociateDatasetKmsKeyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dataset_identifier" in value:
        pairs.append(
            (f"{key_prefix}DatasetIdentifier", str(value["dataset_identifier"]))
        )
    if "kms_key_arn" in value:
        pairs.append((f"{key_prefix}KmsKeyArn", str(value["kms_key_arn"])))


def deserialize_query(el: Element) -> AssociateDatasetKmsKeyInput:
    out: AssociateDatasetKmsKeyInput = {}  # type: ignore[typeddict-item]
    child_dataset_identifier = el.find("DatasetIdentifier")
    if child_dataset_identifier is not None:
        out["dataset_identifier"] = str(child_dataset_identifier.text or "")
    child_kms_key_arn = el.find("KmsKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    return out
