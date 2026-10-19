"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.dataset_schema
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.name_or_arn
    import capo_lookoutequipment.types.tag_list


class CreateDatasetRequest(TypedDict, closed=True):
    dataset_name: "capo_lookoutequipment.types.dataset_name.DatasetName"
    """<p>The name of the dataset being created. </p>"""
    dataset_schema: NotRequired[
        "capo_lookoutequipment.types.dataset_schema.DatasetSchema"
    ]
    """<p>A JSON description of the data that is in each time series dataset, including names, column names, and data types. </p>"""
    server_side_kms_key_id: NotRequired[
        "capo_lookoutequipment.types.name_or_arn.NameOrArn"
    ]
    """<p>Provides the identifier of the KMS key used to encrypt dataset data by Amazon Lookout for Equipment. </p>"""
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""
    tags: NotRequired["capo_lookoutequipment.types.tag_list.TagList"]
    """<p>Any tags associated with the ingested data described in the dataset. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    if "dataset_schema" in value:
        import capo_lookoutequipment.types.dataset_schema

        out["DatasetSchema"] = (
            capo_lookoutequipment.types.dataset_schema.serialize_aws_json_1_0(
                value["dataset_schema"]
            )
        )
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_lookoutequipment.types.tag_list

        out["Tags"] = capo_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        out["dataset_name"] = ""
    if data.get("DatasetSchema") is not None:
        import capo_lookoutequipment.types.dataset_schema

        out["dataset_schema"] = (
            capo_lookoutequipment.types.dataset_schema.deserialize_aws_json_1_0(
                data["DatasetSchema"]
            )
        )
    if data.get("ServerSideKmsKeyId") is not None:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Tags") is not None:
        import capo_lookoutequipment.types.tag_list

        out["tags"] = capo_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
