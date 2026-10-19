"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ImportModelVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_identifier
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.inference_data_import_strategy
    import capo_lookoutequipment.types.labels_input_configuration
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_version_arn
    import capo_lookoutequipment.types.name_or_arn
    import capo_lookoutequipment.types.tag_list


class ImportModelVersionRequest(TypedDict, closed=True):
    source_model_version_arn: (
        "capo_lookoutequipment.types.model_version_arn.ModelVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the model version to import.</p>"""
    model_name: NotRequired["capo_lookoutequipment.types.model_name.ModelName"]
    """<p>The name for the machine learning model to be created. If the model already exists, Amazon Lookout for Equipment creates a new version. If you do not specify this field, it is filled with the name of the source model.</p>"""
    dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier"
    """<p>The name of the dataset for the machine learning model being imported. </p>"""
    labels_input_configuration: NotRequired[
        "capo_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
    ]
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""
    role_arn: NotRequired["capo_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of a role with permission to access the data source being used to create the machine learning model. </p>"""
    server_side_kms_key_id: NotRequired[
        "capo_lookoutequipment.types.name_or_arn.NameOrArn"
    ]
    """<p>Provides the identifier of the KMS key key used to encrypt model data by Amazon Lookout for Equipment. </p>"""
    tags: NotRequired["capo_lookoutequipment.types.tag_list.TagList"]
    """<p>The tags associated with the machine learning model to be created. </p>"""
    inference_data_import_strategy: NotRequired[
        "capo_lookoutequipment.types.inference_data_import_strategy.InferenceDataImportStrategy"
    ]
    """<p>Indicates how to import the accumulated inference data when a model version is imported. The possible values are as follows:</p> <ul> <li> <p>NO_IMPORT – Don't import the data.</p> </li> <li> <p>ADD_WHEN_EMPTY – Only import the data from the source model if there is no existing data in the target model.</p> </li> <li> <p>OVERWRITE – Import the data from the source model and overwrite the existing data in the target model.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportModelVersionRequest) -> dict:
    out: dict = {}
    out["SourceModelVersionArn"] = value["source_model_version_arn"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    out["DatasetName"] = value["dataset_name"]
    if "labels_input_configuration" in value:
        import capo_lookoutequipment.types.labels_input_configuration

        out["LabelsInputConfiguration"] = (
            capo_lookoutequipment.types.labels_input_configuration.serialize_aws_json_1_0(
                value["labels_input_configuration"]
            )
        )
    out["ClientToken"] = value["client_token"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    if "tags" in value:
        import capo_lookoutequipment.types.tag_list

        out["Tags"] = capo_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "inference_data_import_strategy" in value:
        import capo_lookoutequipment.types.inference_data_import_strategy

        out["InferenceDataImportStrategy"] = (
            capo_lookoutequipment.types.inference_data_import_strategy.serialize_aws_json_1_0(
                value["inference_data_import_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportModelVersionRequest:
    out: ImportModelVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceModelVersionArn") is not None:
        out["source_model_version_arn"] = data["SourceModelVersionArn"]
    else:
        out["source_model_version_arn"] = ""
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        out["dataset_name"] = ""
    if data.get("LabelsInputConfiguration") is not None:
        import capo_lookoutequipment.types.labels_input_configuration

        out["labels_input_configuration"] = (
            capo_lookoutequipment.types.labels_input_configuration.deserialize_aws_json_1_0(
                data["LabelsInputConfiguration"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ServerSideKmsKeyId") is not None:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if data.get("Tags") is not None:
        import capo_lookoutequipment.types.tag_list

        out["tags"] = capo_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("InferenceDataImportStrategy") is not None:
        import capo_lookoutequipment.types.inference_data_import_strategy

        out["inference_data_import_strategy"] = (
            capo_lookoutequipment.types.inference_data_import_strategy.deserialize_aws_json_1_0(
                data["InferenceDataImportStrategy"]
            )
        )
    return out
