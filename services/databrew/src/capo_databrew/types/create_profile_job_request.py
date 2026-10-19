"""Generated from Smithy shape ``com.amazonaws.databrew#CreateProfileJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.dataset_name
    import capo_databrew.types.encryption_key_arn
    import capo_databrew.types.encryption_mode
    import capo_databrew.types.job_name
    import capo_databrew.types.job_sample
    import capo_databrew.types.log_subscription
    import capo_databrew.types.max_capacity
    import capo_databrew.types.max_retries
    import capo_databrew.types.profile_configuration
    import capo_databrew.types.s3_location
    import capo_databrew.types.tag_map
    import capo_databrew.types.timeout
    import capo_databrew.types.validation_configuration_list


class CreateProfileJobRequest(TypedDict, closed=True):
    dataset_name: "capo_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset that this job is to act upon.</p>"""
    encryption_key_arn: NotRequired[
        "capo_databrew.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.</p>"""
    encryption_mode: NotRequired["capo_databrew.types.encryption_mode.EncryptionMode"]
    """<p>The encryption mode for the job, which can be one of the following:</p> <ul> <li> <p> <code>SSE-KMS</code> - <code>SSE-KMS</code> - Server-side encryption with KMS-managed keys.</p> </li> <li> <p> <code>SSE-S3</code> - Server-side encryption with keys managed by Amazon S3.</p> </li> </ul>"""
    name: "capo_databrew.types.job_name.JobName"
    """<p>The name of the job to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    log_subscription: NotRequired[
        "capo_databrew.types.log_subscription.LogSubscription"
    ]
    """<p>Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.</p>"""
    max_capacity: NotRequired["capo_databrew.types.max_capacity.MaxCapacity"]
    """<p>The maximum number of nodes that DataBrew can use when the job processes data.</p>"""
    max_retries: NotRequired["capo_databrew.types.max_retries.MaxRetries"]
    """<p>The maximum number of times to retry the job after a job run fails.</p>"""
    output_location: "capo_databrew.types.s3_location.S3Location"
    configuration: NotRequired[
        "capo_databrew.types.profile_configuration.ProfileConfiguration"
    ]
    """<p>Configuration for profile jobs. Used to select columns, do evaluations, and override default parameters of evaluations. When configuration is null, the profile job will run with default settings.</p>"""
    validation_configurations: NotRequired[
        "capo_databrew.types.validation_configuration_list.ValidationConfigurationList"
    ]
    """<p>List of validation configurations that are applied to the profile job.</p>"""
    role_arn: "capo_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this job.</p>"""
    timeout: NotRequired["capo_databrew.types.timeout.Timeout"]
    """<p>The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of <code>TIMEOUT</code>.</p>"""
    job_sample: NotRequired["capo_databrew.types.job_sample.JobSample"]
    """<p>Sample configuration for profile jobs only. Determines the number of rows on which the profile job will be executed. If a JobSample value is not provided, the default value will be used. The default value is CUSTOM_ROWS for the mode parameter and 20000 for the size parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileJobRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "encryption_mode" in value:
        import capo_databrew.types.encryption_mode

        out["EncryptionMode"] = capo_databrew.types.encryption_mode.serialize_json(
            value["encryption_mode"]
        )
    out["Name"] = value["name"]
    if "log_subscription" in value:
        import capo_databrew.types.log_subscription

        out["LogSubscription"] = capo_databrew.types.log_subscription.serialize_json(
            value["log_subscription"]
        )
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    if "max_retries" in value:
        out["MaxRetries"] = value["max_retries"]
    import capo_databrew.types.s3_location

    out["OutputLocation"] = capo_databrew.types.s3_location.serialize_json(
        value["output_location"]
    )
    if "configuration" in value:
        import capo_databrew.types.profile_configuration

        out["Configuration"] = capo_databrew.types.profile_configuration.serialize_json(
            value["configuration"]
        )
    if "validation_configurations" in value:
        import capo_databrew.types.validation_configuration_list

        out["ValidationConfigurations"] = (
            capo_databrew.types.validation_configuration_list.serialize_json(
                value["validation_configurations"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "job_sample" in value:
        import capo_databrew.types.job_sample

        out["JobSample"] = capo_databrew.types.job_sample.serialize_json(
            value["job_sample"]
        )
    return out


def deserialize_json(data: dict) -> CreateProfileJobRequest:
    out: CreateProfileJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatasetName") is not None:
        out["dataset_name"] = data["DatasetName"]
    else:
        raise DeserializationError("CreateProfileJobRequest.dataset_name required")
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("EncryptionMode") is not None:
        import capo_databrew.types.encryption_mode

        out["encryption_mode"] = capo_databrew.types.encryption_mode.deserialize_json(
            data["EncryptionMode"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateProfileJobRequest.name required")
    if data.get("LogSubscription") is not None:
        import capo_databrew.types.log_subscription

        out["log_subscription"] = capo_databrew.types.log_subscription.deserialize_json(
            data["LogSubscription"]
        )
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = data["MaxCapacity"]
    if data.get("MaxRetries") is not None:
        out["max_retries"] = data["MaxRetries"]
    if data.get("OutputLocation") is not None:
        import capo_databrew.types.s3_location

        out["output_location"] = capo_databrew.types.s3_location.deserialize_json(
            data["OutputLocation"]
        )
    else:
        raise DeserializationError("CreateProfileJobRequest.output_location required")
    if data.get("Configuration") is not None:
        import capo_databrew.types.profile_configuration

        out["configuration"] = (
            capo_databrew.types.profile_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("ValidationConfigurations") is not None:
        import capo_databrew.types.validation_configuration_list

        out["validation_configurations"] = (
            capo_databrew.types.validation_configuration_list.deserialize_json(
                data["ValidationConfigurations"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateProfileJobRequest.role_arn required")
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("JobSample") is not None:
        import capo_databrew.types.job_sample

        out["job_sample"] = capo_databrew.types.job_sample.deserialize_json(
            data["JobSample"]
        )
    return out
