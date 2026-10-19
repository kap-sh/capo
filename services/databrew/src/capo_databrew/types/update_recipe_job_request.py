"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateRecipeJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.data_catalog_output_list
    import capo_databrew.types.database_output_list
    import capo_databrew.types.encryption_key_arn
    import capo_databrew.types.encryption_mode
    import capo_databrew.types.job_name
    import capo_databrew.types.log_subscription
    import capo_databrew.types.max_capacity
    import capo_databrew.types.max_retries
    import capo_databrew.types.output_list
    import capo_databrew.types.timeout


class UpdateRecipeJobRequest(TypedDict, closed=True):
    encryption_key_arn: NotRequired[
        "capo_databrew.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.</p>"""
    encryption_mode: NotRequired["capo_databrew.types.encryption_mode.EncryptionMode"]
    """<p>The encryption mode for the job, which can be one of the following:</p> <ul> <li> <p> <code>SSE-KMS</code> - Server-side encryption with keys managed by KMS.</p> </li> <li> <p> <code>SSE-S3</code> - Server-side encryption with keys managed by Amazon S3.</p> </li> </ul>"""
    name: "capo_databrew.types.job_name.JobName"
    """<p>The name of the job to update.</p>"""
    log_subscription: NotRequired[
        "capo_databrew.types.log_subscription.LogSubscription"
    ]
    """<p>Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.</p>"""
    max_capacity: NotRequired["capo_databrew.types.max_capacity.MaxCapacity"]
    """<p>The maximum number of nodes that DataBrew can consume when the job processes data.</p>"""
    max_retries: NotRequired["capo_databrew.types.max_retries.MaxRetries"]
    """<p>The maximum number of times to retry the job after a job run fails.</p>"""
    outputs: NotRequired["capo_databrew.types.output_list.OutputList"]
    """<p>One or more artifacts that represent the output from running the job. </p>"""
    data_catalog_outputs: NotRequired[
        "capo_databrew.types.data_catalog_output_list.DataCatalogOutputList"
    ]
    """<p>One or more artifacts that represent the Glue Data Catalog output from running the job.</p>"""
    database_outputs: NotRequired[
        "capo_databrew.types.database_output_list.DatabaseOutputList"
    ]
    """<p>Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.</p>"""
    role_arn: "capo_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.</p>"""
    timeout: NotRequired["capo_databrew.types.timeout.Timeout"]
    """<p>The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of <code>TIMEOUT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecipeJobRequest) -> dict:
    out: dict = {}
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "encryption_mode" in value:
        import capo_databrew.types.encryption_mode

        out["EncryptionMode"] = capo_databrew.types.encryption_mode.serialize_json(
            value["encryption_mode"]
        )
    if "log_subscription" in value:
        import capo_databrew.types.log_subscription

        out["LogSubscription"] = capo_databrew.types.log_subscription.serialize_json(
            value["log_subscription"]
        )
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    if "max_retries" in value:
        out["MaxRetries"] = value["max_retries"]
    if "outputs" in value:
        import capo_databrew.types.output_list

        out["Outputs"] = capo_databrew.types.output_list.serialize_json(
            value["outputs"]
        )
    if "data_catalog_outputs" in value:
        import capo_databrew.types.data_catalog_output_list

        out["DataCatalogOutputs"] = (
            capo_databrew.types.data_catalog_output_list.serialize_json(
                value["data_catalog_outputs"]
            )
        )
    if "database_outputs" in value:
        import capo_databrew.types.database_output_list

        out["DatabaseOutputs"] = (
            capo_databrew.types.database_output_list.serialize_json(
                value["database_outputs"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    return out


def deserialize_json(data: dict) -> UpdateRecipeJobRequest:
    out: UpdateRecipeJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("EncryptionMode") is not None:
        import capo_databrew.types.encryption_mode

        out["encryption_mode"] = capo_databrew.types.encryption_mode.deserialize_json(
            data["EncryptionMode"]
        )
    if data.get("LogSubscription") is not None:
        import capo_databrew.types.log_subscription

        out["log_subscription"] = capo_databrew.types.log_subscription.deserialize_json(
            data["LogSubscription"]
        )
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = data["MaxCapacity"]
    if data.get("MaxRetries") is not None:
        out["max_retries"] = data["MaxRetries"]
    if data.get("Outputs") is not None:
        import capo_databrew.types.output_list

        out["outputs"] = capo_databrew.types.output_list.deserialize_json(
            data["Outputs"]
        )
    if data.get("DataCatalogOutputs") is not None:
        import capo_databrew.types.data_catalog_output_list

        out["data_catalog_outputs"] = (
            capo_databrew.types.data_catalog_output_list.deserialize_json(
                data["DataCatalogOutputs"]
            )
        )
    if data.get("DatabaseOutputs") is not None:
        import capo_databrew.types.database_output_list

        out["database_outputs"] = (
            capo_databrew.types.database_output_list.deserialize_json(
                data["DatabaseOutputs"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("UpdateRecipeJobRequest.role_arn required")
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    return out
