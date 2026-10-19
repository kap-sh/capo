"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ImportDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.name_or_arn
    import capo_lookoutequipment.types.tag_list


class ImportDatasetRequest(TypedDict, closed=True):
    source_dataset_arn: "capo_lookoutequipment.types.dataset_arn.DatasetArn"
    """<p>The Amazon Resource Name (ARN) of the dataset to import.</p>"""
    dataset_name: NotRequired["capo_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the machine learning dataset to be created. If the dataset already exists, Amazon Lookout for Equipment overwrites the existing dataset. If you don't specify this field, it is filled with the name of the source dataset.</p>"""
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""
    server_side_kms_key_id: NotRequired[
        "capo_lookoutequipment.types.name_or_arn.NameOrArn"
    ]
    """<p>Provides the identifier of the KMS key key used to encrypt model data by Amazon Lookout for Equipment. </p>"""
    tags: NotRequired["capo_lookoutequipment.types.tag_list.TagList"]
    """<p>Any tags associated with the dataset to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportDatasetRequest) -> dict:
    out: dict = {}
    out["SourceDatasetArn"] = value["source_dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    out["ClientToken"] = value["client_token"]
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    if "tags" in value:
        import capo_lookoutequipment.types.tag_list

        out["Tags"] = capo_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportDatasetRequest:
    out: ImportDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceDatasetArn") is not None:
        out["source_dataset_arn"] = data["SourceDatasetArn"]
    else:
        out["source_dataset_arn"] = ""
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("ServerSideKmsKeyId") is not None:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if data.get("Tags") is not None:
        import capo_lookoutequipment.types.tag_list

        out["tags"] = capo_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
