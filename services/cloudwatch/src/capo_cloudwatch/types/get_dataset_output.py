"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetDatasetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dataset_arn
    import capo_cloudwatch.types.dataset_id
    import capo_cloudwatch.types.kms_key_arn


class GetDatasetOutput(TypedDict, closed=True):
    dataset_id: NotRequired["capo_cloudwatch.types.dataset_id.DatasetId"]
    """<p>Returns the identifier of the dataset.</p>"""
    arn: NotRequired["capo_cloudwatch.types.dataset_arn.DatasetArn"]
    """<p>Returns the Amazon Resource Name (ARN) of the dataset, in the format <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:dataset/<i>dataset-id</i> </code>.</p>"""
    kms_key_arn: NotRequired["capo_cloudwatch.types.kms_key_arn.KmsKeyArn"]
    """<p>Returns the Amazon Resource Name (ARN) of the customer managed Amazon Web Services KMS key that is currently associated with the dataset, if any. If the dataset is not associated with a customer managed KMS key, this field is not included in the response and the dataset is encrypted at rest using an Amazon Web Services owned key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDatasetOutput) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["DatasetId"] = value["dataset_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDatasetOutput:
    out: GetDatasetOutput = {}  # type: ignore[typeddict-item]
    if data.get("DatasetId") is not None:
        out["dataset_id"] = data["DatasetId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDatasetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dataset_id" in value:
        pairs.append((f"{key_prefix}DatasetId", str(value["dataset_id"])))
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "kms_key_arn" in value:
        pairs.append((f"{key_prefix}KmsKeyArn", str(value["kms_key_arn"])))


def deserialize_query(el: Element) -> GetDatasetOutput:
    out: GetDatasetOutput = {}  # type: ignore[typeddict-item]
    child_dataset_id = el.find("DatasetId")
    if child_dataset_id is not None:
        out["dataset_id"] = str(child_dataset_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_kms_key_arn = el.find("KmsKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDatasetOutput) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["DatasetId"] = value["dataset_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_cbor(data: dict) -> GetDatasetOutput:
    out: GetDatasetOutput = {}  # type: ignore[typeddict-item]
    if data.get("DatasetId") is not None:
        out["dataset_id"] = data["DatasetId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
