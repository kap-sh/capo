"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.any_length_string
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.comprehend_dataset_arn
    import capo_comprehend.types.dataset_status
    import capo_comprehend.types.dataset_type
    import capo_comprehend.types.description
    import capo_comprehend.types.number_of_documents
    import capo_comprehend.types.s3_uri
    import capo_comprehend.types.timestamp


class DatasetProperties(TypedDict, closed=True):
    dataset_arn: NotRequired[
        "capo_comprehend.types.comprehend_dataset_arn.ComprehendDatasetArn"
    ]
    """<p>The ARN of the dataset.</p>"""
    dataset_name: NotRequired[
        "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p>The name of the dataset.</p>"""
    dataset_type: NotRequired["capo_comprehend.types.dataset_type.DatasetType"]
    """<p>The dataset type (training data or test data).</p>"""
    dataset_s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>The S3 URI where the dataset is stored.</p>"""
    description: NotRequired["capo_comprehend.types.description.Description"]
    """<p>Description of the dataset.</p>"""
    status: NotRequired["capo_comprehend.types.dataset_status.DatasetStatus"]
    """<p>The dataset status. While the system creates the dataset, the status is <code>CREATING</code>. When the dataset is ready to use, the status changes to <code>COMPLETED</code>. </p>"""
    message: NotRequired["capo_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of the dataset.</p>"""
    number_of_documents: NotRequired[
        "capo_comprehend.types.number_of_documents.NumberOfDocuments"
    ]
    """<p>The number of documents in the dataset.</p>"""
    creation_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Creation time of the dataset.</p>"""
    end_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Time when the data from the dataset becomes available in the data lake.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetProperties) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_type" in value:
        import capo_comprehend.types.dataset_type

        out["DatasetType"] = capo_comprehend.types.dataset_type.serialize_aws_json_1_1(
            value["dataset_type"]
        )
    if "dataset_s3_uri" in value:
        out["DatasetS3Uri"] = value["dataset_s3_uri"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_comprehend.types.dataset_status

        out["Status"] = capo_comprehend.types.dataset_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "number_of_documents" in value:
        out["NumberOfDocuments"] = value["number_of_documents"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import capo_comprehend.types.timestamp

        out["EndTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetProperties:
    out: DatasetProperties = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("DatasetType") is not None:
        import capo_comprehend.types.dataset_type

        out["dataset_type"] = (
            capo_comprehend.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    if data.get("DatasetS3Uri") is not None:
        out["dataset_s3_uri"] = data["DatasetS3Uri"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_comprehend.types.dataset_status

        out["status"] = capo_comprehend.types.dataset_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("NumberOfDocuments") is not None:
        out["number_of_documents"] = data["NumberOfDocuments"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("EndTime") is not None:
        import capo_comprehend.types.timestamp

        out["end_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DatasetProperties) -> dict:
    out: dict = {}
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_type" in value:
        import capo_comprehend.types.dataset_type

        out["DatasetType"] = capo_comprehend.types.dataset_type.serialize_cbor(
            value["dataset_type"]
        )
    if "dataset_s3_uri" in value:
        out["DatasetS3Uri"] = value["dataset_s3_uri"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_comprehend.types.dataset_status

        out["Status"] = capo_comprehend.types.dataset_status.serialize_cbor(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "number_of_documents" in value:
        out["NumberOfDocuments"] = value["number_of_documents"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["creation_time"]
        )
    if "end_time" in value:
        import capo_comprehend.types.timestamp

        out["EndTime"] = capo_comprehend.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    return out


def deserialize_cbor(data: dict) -> DatasetProperties:
    out: DatasetProperties = {}  # type: ignore[typeddict-item]
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("DatasetType") is not None:
        import capo_comprehend.types.dataset_type

        out["dataset_type"] = capo_comprehend.types.dataset_type.deserialize_cbor(
            data["DatasetType"]
        )
    if data.get("DatasetS3Uri") is not None:
        out["dataset_s3_uri"] = data["DatasetS3Uri"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_comprehend.types.dataset_status

        out["status"] = capo_comprehend.types.dataset_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("NumberOfDocuments") is not None:
        out["number_of_documents"] = data["NumberOfDocuments"]
    if data.get("CreationTime") is not None:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["CreationTime"]
        )
    if data.get("EndTime") is not None:
        import capo_comprehend.types.timestamp

        out["end_time"] = capo_comprehend.types.timestamp.deserialize_cbor(
            data["EndTime"]
        )
    return out
