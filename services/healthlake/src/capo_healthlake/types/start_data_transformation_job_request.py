"""Generated from Smithy shape ``com.amazonaws.healthlake#StartDataTransformationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.client_token
    import capo_healthlake.types.data_transformation_iam_role_arn
    import capo_healthlake.types.data_transformation_job_name
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.transformation_input_data_config
    import capo_healthlake.types.transformation_output_data_config


class StartDataTransformationJobRequest(TypedDict, closed=True):
    input_data_config: "capo_healthlake.types.transformation_input_data_config.TransformationInputDataConfig"
    """<p>The Amazon S3 location and format of the source files to transform.</p>"""
    output_data_config: "capo_healthlake.types.transformation_output_data_config.TransformationOutputDataConfig"
    """<p>The Amazon S3 output location and Amazon Web Services Key Management Service (Amazon Web Services KMS) encryption configuration.</p>"""
    data_access_role_arn: "capo_healthlake.types.data_transformation_iam_role_arn.DataTransformationIamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) role that HealthLake assumes to read from and write to the specified Amazon S3 locations.</p>"""
    client_token: "capo_healthlake.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>"""
    job_name: NotRequired[
        "capo_healthlake.types.data_transformation_job_name.DataTransformationJobName"
    ]
    """<p>A descriptive name for the data transformation job.</p>"""
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the data transformation profile to use for conversion.</p>"""
    drift_detection_enabled: NotRequired["bool"]
    """<p>Specifies whether drift detection is enabled for this job. When enabled, HealthLake writes a drift report to the output Amazon S3 location alongside the converted files.</p>"""
    provenance_enabled: NotRequired["bool"]
    """<p>Specifies whether FHIR R4 Provenance resource generation is enabled for this transformation job. When provenance is enabled, the service also generates related DocumentReference and Device resources. If you don't specify a value, the default is <code>true</code>. To disable provenance output, set this parameter to <code>false</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDataTransformationJobRequest) -> dict:
    out: dict = {}
    import capo_healthlake.types.transformation_input_data_config

    out["InputDataConfig"] = (
        capo_healthlake.types.transformation_input_data_config.serialize_aws_json_1_0(
            value["input_data_config"]
        )
    )
    import capo_healthlake.types.transformation_output_data_config

    out["OutputDataConfig"] = (
        capo_healthlake.types.transformation_output_data_config.serialize_aws_json_1_0(
            value["output_data_config"]
        )
    )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    out["ClientToken"] = value["client_token"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    out["ProfileId"] = value["profile_id"]
    if "drift_detection_enabled" in value:
        out["DriftDetectionEnabled"] = value["drift_detection_enabled"]
    if "provenance_enabled" in value:
        out["ProvenanceEnabled"] = value["provenance_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDataTransformationJobRequest:
    out: StartDataTransformationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("InputDataConfig") is not None:
        import capo_healthlake.types.transformation_input_data_config

        out["input_data_config"] = (
            capo_healthlake.types.transformation_input_data_config.deserialize_aws_json_1_0(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartDataTransformationJobRequest.input_data_config required"
        )
    if data.get("OutputDataConfig") is not None:
        import capo_healthlake.types.transformation_output_data_config

        out["output_data_config"] = (
            capo_healthlake.types.transformation_output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartDataTransformationJobRequest.output_data_config required"
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        out["data_access_role_arn"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("DriftDetectionEnabled") is not None:
        out["drift_detection_enabled"] = data["DriftDetectionEnabled"]
    if data.get("ProvenanceEnabled") is not None:
        out["provenance_enabled"] = data["ProvenanceEnabled"]
    return out
