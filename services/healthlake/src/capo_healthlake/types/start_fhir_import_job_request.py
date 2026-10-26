"""Generated from Smithy shape ``com.amazonaws.healthlake#StartFHIRImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.bounded_length_string
    import capo_healthlake.types.client_token_string
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.default_enabled_boolean
    import capo_healthlake.types.health_lake_boolean
    import capo_healthlake.types.iam_role_arn
    import capo_healthlake.types.input_data_config
    import capo_healthlake.types.job_name
    import capo_healthlake.types.output_data_config
    import capo_healthlake.types.validation_level


class StartFHIRImportJobRequest(TypedDict, closed=True):
    job_name: NotRequired["capo_healthlake.types.job_name.JobName"]
    """<p>The import job name.</p>"""
    input_data_config: "capo_healthlake.types.input_data_config.InputDataConfig"
    """<p>The input properties for the import job request.</p>"""
    job_output_data_config: "capo_healthlake.types.output_data_config.OutputDataConfig"
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    data_access_role_arn: "capo_healthlake.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) that grants access permission to HealthLake.</p>"""
    client_token: NotRequired[
        "capo_healthlake.types.client_token_string.ClientTokenString"
    ]
    """<p>The optional user-provided token used for ensuring API idempotency.</p>"""
    validation_level: NotRequired[
        "capo_healthlake.types.validation_level.ValidationLevel"
    ]
    """<p>The validation level of the import job.</p>"""
    profile_id: NotRequired[
        "capo_healthlake.types.bounded_length_string.BoundedLengthString"
    ]
    """<p>The data transformation profile identifier to use for the import job.</p>"""
    input_format: NotRequired[
        "capo_healthlake.types.bounded_length_string.BoundedLengthString"
    ]
    """<p>The input format of the data to be imported.</p>"""
    drift_detection_enabled: NotRequired[
        "capo_healthlake.types.health_lake_boolean.HealthLakeBoolean"
    ]
    """<p>Specifies whether to enable drift detection for the import job.</p>"""
    provenance_enabled: NotRequired[
        "capo_healthlake.types.default_enabled_boolean.DefaultEnabledBoolean"
    ]
    """<p>Specifies whether to enable provenance for the import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFHIRImportJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_healthlake.types.input_data_config

    out["InputDataConfig"] = (
        capo_healthlake.types.input_data_config.serialize_aws_json_1_0(
            value["input_data_config"]
        )
    )
    import capo_healthlake.types.output_data_config

    out["JobOutputDataConfig"] = (
        capo_healthlake.types.output_data_config.serialize_aws_json_1_0(
            value["job_output_data_config"]
        )
    )
    out["DatastoreId"] = value["datastore_id"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "validation_level" in value:
        import capo_healthlake.types.validation_level

        out["ValidationLevel"] = (
            capo_healthlake.types.validation_level.serialize_aws_json_1_0(
                value["validation_level"]
            )
        )
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "input_format" in value:
        out["InputFormat"] = value["input_format"]
    if "drift_detection_enabled" in value:
        out["DriftDetectionEnabled"] = value["drift_detection_enabled"]
    if "provenance_enabled" in value:
        out["ProvenanceEnabled"] = value["provenance_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFHIRImportJobRequest:
    out: StartFHIRImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("InputDataConfig") is not None:
        import capo_healthlake.types.input_data_config

        out["input_data_config"] = (
            capo_healthlake.types.input_data_config.deserialize_aws_json_1_0(
                data["InputDataConfig"]
            )
        )
    else:
        out["input_data_config"] = {"$unknown": {"name": ""}}
    if data.get("JobOutputDataConfig") is not None:
        import capo_healthlake.types.output_data_config

        out["job_output_data_config"] = (
            capo_healthlake.types.output_data_config.deserialize_aws_json_1_0(
                data["JobOutputDataConfig"]
            )
        )
    else:
        out["job_output_data_config"] = {"$unknown": {"name": ""}}
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        out["data_access_role_arn"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ValidationLevel") is not None:
        import capo_healthlake.types.validation_level

        out["validation_level"] = (
            capo_healthlake.types.validation_level.deserialize_aws_json_1_0(
                data["ValidationLevel"]
            )
        )
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    if data.get("InputFormat") is not None:
        out["input_format"] = data["InputFormat"]
    if data.get("DriftDetectionEnabled") is not None:
        out["drift_detection_enabled"] = data["DriftDetectionEnabled"]
    if data.get("ProvenanceEnabled") is not None:
        out["provenance_enabled"] = data["ProvenanceEnabled"]
    return out
