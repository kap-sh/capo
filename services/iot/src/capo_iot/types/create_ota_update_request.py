"""Generated from Smithy shape ``com.amazonaws.iot#CreateOTAUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.additional_parameter_map
    import capo_iot.types.aws_job_abort_config
    import capo_iot.types.aws_job_executions_rollout_config
    import capo_iot.types.aws_job_presigned_url_config
    import capo_iot.types.aws_job_timeout_config
    import capo_iot.types.ota_update_description
    import capo_iot.types.ota_update_files
    import capo_iot.types.ota_update_id
    import capo_iot.types.protocols
    import capo_iot.types.role_arn
    import capo_iot.types.tag_list
    import capo_iot.types.target_selection
    import capo_iot.types.targets


class CreateOTAUpdateRequest(TypedDict, closed=True):
    ota_update_id: "capo_iot.types.ota_update_id.OTAUpdateId"
    """<p>The ID of the OTA update to be created.</p>"""
    description: NotRequired[
        "capo_iot.types.ota_update_description.OTAUpdateDescription"
    ]
    """<p>The description of the OTA update.</p>"""
    targets: "capo_iot.types.targets.Targets"
    """<p>The devices targeted to receive OTA updates.</p>"""
    protocols: NotRequired["capo_iot.types.protocols.Protocols"]
    """<p>The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.</p>"""
    target_selection: NotRequired["capo_iot.types.target_selection.TargetSelection"]
    """<p>Specifies whether the update will continue to run (CONTINUOUS), or will be complete after all the things specified as targets have completed the update (SNAPSHOT). If continuous, the update may also be run on a thing when a change is detected in a target. For example, an update will run on a thing when the thing is added to a target group, even after the update was completed by all things originally in the group. Valid values: CONTINUOUS | SNAPSHOT.</p>"""
    aws_job_executions_rollout_config: NotRequired[
        "capo_iot.types.aws_job_executions_rollout_config.AwsJobExecutionsRolloutConfig"
    ]
    """<p>Configuration for the rollout of OTA updates.</p>"""
    aws_job_presigned_url_config: NotRequired[
        "capo_iot.types.aws_job_presigned_url_config.AwsJobPresignedUrlConfig"
    ]
    """<p>Configuration information for pre-signed URLs.</p>"""
    aws_job_abort_config: NotRequired[
        "capo_iot.types.aws_job_abort_config.AwsJobAbortConfig"
    ]
    """<p>The criteria that determine when and how a job abort takes place.</p>"""
    aws_job_timeout_config: NotRequired[
        "capo_iot.types.aws_job_timeout_config.AwsJobTimeoutConfig"
    ]
    """<p>Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to <code>IN_PROGRESS</code>. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to <code>TIMED_OUT</code>.</p>"""
    files: "capo_iot.types.ota_update_files.OTAUpdateFiles"
    """<p>The files to be streamed by the OTA update.</p>"""
    role_arn: "capo_iot.types.role_arn.RoleArn"
    """<p>The IAM role that grants Amazon Web Services IoT Core access to the Amazon S3, IoT jobs and Amazon Web Services Code Signing resources to create an OTA update job.</p>"""
    additional_parameters: NotRequired[
        "capo_iot.types.additional_parameter_map.AdditionalParameterMap"
    ]
    """<p>A list of additional OTA update parameters, which are name-value pairs. They won't be sent to devices as a part of the Job document.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOTAUpdateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_iot.types.targets

    out["targets"] = capo_iot.types.targets.serialize_json(value["targets"])
    if "protocols" in value:
        import capo_iot.types.protocols

        out["protocols"] = capo_iot.types.protocols.serialize_json(value["protocols"])
    if "target_selection" in value:
        import capo_iot.types.target_selection

        out["targetSelection"] = capo_iot.types.target_selection.serialize_json(
            value["target_selection"]
        )
    if "aws_job_executions_rollout_config" in value:
        import capo_iot.types.aws_job_executions_rollout_config

        out["awsJobExecutionsRolloutConfig"] = (
            capo_iot.types.aws_job_executions_rollout_config.serialize_json(
                value["aws_job_executions_rollout_config"]
            )
        )
    if "aws_job_presigned_url_config" in value:
        import capo_iot.types.aws_job_presigned_url_config

        out["awsJobPresignedUrlConfig"] = (
            capo_iot.types.aws_job_presigned_url_config.serialize_json(
                value["aws_job_presigned_url_config"]
            )
        )
    if "aws_job_abort_config" in value:
        import capo_iot.types.aws_job_abort_config

        out["awsJobAbortConfig"] = capo_iot.types.aws_job_abort_config.serialize_json(
            value["aws_job_abort_config"]
        )
    if "aws_job_timeout_config" in value:
        import capo_iot.types.aws_job_timeout_config

        out["awsJobTimeoutConfig"] = (
            capo_iot.types.aws_job_timeout_config.serialize_json(
                value["aws_job_timeout_config"]
            )
        )
    import capo_iot.types.ota_update_files

    out["files"] = capo_iot.types.ota_update_files.serialize_json(value["files"])
    out["roleArn"] = value["role_arn"]
    if "additional_parameters" in value:
        import capo_iot.types.additional_parameter_map

        out["additionalParameters"] = (
            capo_iot.types.additional_parameter_map.serialize_json(
                value["additional_parameters"]
            )
        )
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateOTAUpdateRequest:
    out: CreateOTAUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("targets") is not None:
        import capo_iot.types.targets

        out["targets"] = capo_iot.types.targets.deserialize_json(data["targets"])
    else:
        out["targets"] = []
    if data.get("protocols") is not None:
        import capo_iot.types.protocols

        out["protocols"] = capo_iot.types.protocols.deserialize_json(data["protocols"])
    if data.get("targetSelection") is not None:
        import capo_iot.types.target_selection

        out["target_selection"] = capo_iot.types.target_selection.deserialize_json(
            data["targetSelection"]
        )
    if data.get("awsJobExecutionsRolloutConfig") is not None:
        import capo_iot.types.aws_job_executions_rollout_config

        out["aws_job_executions_rollout_config"] = (
            capo_iot.types.aws_job_executions_rollout_config.deserialize_json(
                data["awsJobExecutionsRolloutConfig"]
            )
        )
    if data.get("awsJobPresignedUrlConfig") is not None:
        import capo_iot.types.aws_job_presigned_url_config

        out["aws_job_presigned_url_config"] = (
            capo_iot.types.aws_job_presigned_url_config.deserialize_json(
                data["awsJobPresignedUrlConfig"]
            )
        )
    if data.get("awsJobAbortConfig") is not None:
        import capo_iot.types.aws_job_abort_config

        out["aws_job_abort_config"] = (
            capo_iot.types.aws_job_abort_config.deserialize_json(
                data["awsJobAbortConfig"]
            )
        )
    if data.get("awsJobTimeoutConfig") is not None:
        import capo_iot.types.aws_job_timeout_config

        out["aws_job_timeout_config"] = (
            capo_iot.types.aws_job_timeout_config.deserialize_json(
                data["awsJobTimeoutConfig"]
            )
        )
    if data.get("files") is not None:
        import capo_iot.types.ota_update_files

        out["files"] = capo_iot.types.ota_update_files.deserialize_json(data["files"])
    else:
        out["files"] = []
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("additionalParameters") is not None:
        import capo_iot.types.additional_parameter_map

        out["additional_parameters"] = (
            capo_iot.types.additional_parameter_map.deserialize_json(
                data["additionalParameters"]
            )
        )
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out
