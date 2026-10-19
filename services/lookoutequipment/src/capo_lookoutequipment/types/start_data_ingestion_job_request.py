"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StartDataIngestionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_identifier
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.ingestion_input_configuration


class StartDataIngestionJobRequest(TypedDict, closed=True):
    dataset_name: "capo_lookoutequipment.types.dataset_identifier.DatasetIdentifier"
    """<p>The name of the dataset being used by the data ingestion job. </p>"""
    ingestion_input_configuration: "capo_lookoutequipment.types.ingestion_input_configuration.IngestionInputConfiguration"
    """<p> Specifies information for the input data for the data ingestion job, including dataset S3 location. </p>"""
    role_arn: "capo_lookoutequipment.types.iam_role_arn.IamRoleArn"
    """<p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the data ingestion job. </p>"""
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDataIngestionJobRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    import capo_lookoutequipment.types.ingestion_input_configuration

    out["IngestionInputConfiguration"] = (
        capo_lookoutequipment.types.ingestion_input_configuration.serialize_aws_json_1_0(
            value["ingestion_input_configuration"]
        )
    )
    out["RoleArn"] = value["role_arn"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDataIngestionJobRequest:
    out: StartDataIngestionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        out["dataset_name"] = ""
    if data.get("IngestionInputConfiguration") is not None:
        import capo_lookoutequipment.types.ingestion_input_configuration

        out["ingestion_input_configuration"] = (
            capo_lookoutequipment.types.ingestion_input_configuration.deserialize_aws_json_1_0(
                data["IngestionInputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartDataIngestionJobRequest.ingestion_input_configuration required"
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out
