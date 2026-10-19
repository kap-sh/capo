"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.dataset_input_data_config
    import capo_comprehend.types.dataset_type
    import capo_comprehend.types.description
    import capo_comprehend.types.tag_list


class CreateDatasetRequest(TypedDict, closed=True):
    flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    """<p>The Amazon Resource Number (ARN) of the flywheel of the flywheel to receive the data.</p>"""
    dataset_name: "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
    """<p>Name of the dataset.</p>"""
    dataset_type: NotRequired["capo_comprehend.types.dataset_type.DatasetType"]
    """<p>The dataset type. You can specify that the data in a dataset is for training the model or for testing the model.</p>"""
    description: NotRequired["capo_comprehend.types.description.Description"]
    """<p>Description of the dataset.</p>"""
    input_data_config: (
        "capo_comprehend.types.dataset_input_data_config.DatasetInputDataConfig"
    )
    """<p>Information about the input data configuration. The type of input data varies based on the format of the input and whether the data is for a classifier model or an entity recognition model.</p>"""
    client_request_token: NotRequired[
        "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    tags: NotRequired["capo_comprehend.types.tag_list.TagList"]
    """<p>Tags for the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    out["DatasetName"] = value["dataset_name"]
    if "dataset_type" in value:
        import capo_comprehend.types.dataset_type

        out["DatasetType"] = capo_comprehend.types.dataset_type.serialize_aws_json_1_1(
            value["dataset_type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_comprehend.types.dataset_input_data_config

    out["InputDataConfig"] = (
        capo_comprehend.types.dataset_input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_comprehend.types.tag_list

        out["Tags"] = capo_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        out["flywheel_arn"] = ""
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        out["dataset_name"] = ""
    if data.get("DatasetType") is not None:
        import capo_comprehend.types.dataset_type

        out["dataset_type"] = (
            capo_comprehend.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("InputDataConfig") is not None:
        import capo_comprehend.types.dataset_input_data_config

        out["input_data_config"] = (
            capo_comprehend.types.dataset_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetRequest.input_data_config required")
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_comprehend.types.tag_list

        out["tags"] = capo_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
