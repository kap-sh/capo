"""Generated from Smithy shape ``com.amazonaws.healthlake#StartFHIRExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.client_token_string
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.iam_role_arn
    import capo_healthlake.types.job_name
    import capo_healthlake.types.output_data_config


class StartFHIRExportJobRequest(TypedDict, closed=True):
    job_name: NotRequired["capo_healthlake.types.job_name.JobName"]
    """<p>The export job name.</p>"""
    output_data_config: "capo_healthlake.types.output_data_config.OutputDataConfig"
    """<p>The output data configuration supplied when the export job was started.</p>"""
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier from which files are being exported.</p>"""
    data_access_role_arn: "capo_healthlake.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) used during initiation of the export job.</p>"""
    client_token: NotRequired[
        "capo_healthlake.types.client_token_string.ClientTokenString"
    ]
    """<p>An optional user provided token used for ensuring API idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFHIRExportJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_healthlake.types.output_data_config

    out["OutputDataConfig"] = (
        capo_healthlake.types.output_data_config.serialize_aws_json_1_0(
            value["output_data_config"]
        )
    )
    out["DatastoreId"] = value["datastore_id"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFHIRExportJobRequest:
    out: StartFHIRExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("OutputDataConfig") is not None:
        import capo_healthlake.types.output_data_config

        out["output_data_config"] = (
            capo_healthlake.types.output_data_config.deserialize_aws_json_1_0(
                data["OutputDataConfig"]
            )
        )
    else:
        import capo_healthlake.types._unknown

        out["output_data_config"] = capo_healthlake.types._unknown.UnknownUnionMember(
            ""
        )
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
    return out
