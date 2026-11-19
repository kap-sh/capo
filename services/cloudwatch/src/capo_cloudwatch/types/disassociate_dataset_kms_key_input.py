"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DisassociateDatasetKmsKeyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dataset_identifier


class DisassociateDatasetKmsKeyInput(TypedDict, closed=True):
    dataset_identifier: NotRequired[
        "capo_cloudwatch.types.dataset_identifier.DatasetIdentifier"
    ]
    """<p>Specifies the identifier of the dataset from which to remove the KMS key association. For the <code>default</code> dataset, you can specify either <code>default</code> or the full dataset Amazon Resource Name (ARN) in the format <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:dataset/default</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateDatasetKmsKeyInput) -> dict:
    out: dict = {}
    if "dataset_identifier" in value:
        out["DatasetIdentifier"] = value["dataset_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateDatasetKmsKeyInput:
    out: DisassociateDatasetKmsKeyInput = {}  # type: ignore[typeddict-item]
    if data.get("DatasetIdentifier") is not None:
        out["dataset_identifier"] = data["DatasetIdentifier"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DisassociateDatasetKmsKeyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dataset_identifier" in value:
        pairs.append(
            (f"{key_prefix}DatasetIdentifier", str(value["dataset_identifier"]))
        )


def deserialize_query(el: Element) -> DisassociateDatasetKmsKeyInput:
    out: DisassociateDatasetKmsKeyInput = {}  # type: ignore[typeddict-item]
    child_dataset_identifier = el.find("DatasetIdentifier")
    if child_dataset_identifier is not None:
        out["dataset_identifier"] = str(child_dataset_identifier.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateDatasetKmsKeyInput) -> dict:
    out: dict = {}
    if "dataset_identifier" in value:
        out["DatasetIdentifier"] = value["dataset_identifier"]
    return out


def deserialize_cbor(data: dict) -> DisassociateDatasetKmsKeyInput:
    out: DisassociateDatasetKmsKeyInput = {}  # type: ignore[typeddict-item]
    if data.get("DatasetIdentifier") is not None:
        out["dataset_identifier"] = data["DatasetIdentifier"]
    return out
