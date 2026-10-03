"""Generated from Smithy shape ``com.amazonaws.braket#GetJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_braket.types.algorithm_specification
    import capo_braket.types.associations
    import capo_braket.types.device_config
    import capo_braket.types.hybrid_job_queue_info
    import capo_braket.types.hyper_parameters
    import capo_braket.types.input_config_list
    import capo_braket.types.instance_config
    import capo_braket.types.job_arn
    import capo_braket.types.job_checkpoint_config
    import capo_braket.types.job_events
    import capo_braket.types.job_output_data_config
    import capo_braket.types.job_primary_status
    import capo_braket.types.job_stopping_condition
    import capo_braket.types.role_arn
    import capo_braket.types.string1024
    import capo_braket.types.tags_map


class GetJobResponse(TypedDict, closed=True):
    status: "capo_braket.types.job_primary_status.JobPrimaryStatus"
    """<p>The status of the Amazon Braket hybrid job.</p>"""
    job_arn: "capo_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket hybrid job.</p>"""
    role_arn: "capo_braket.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and other hybrid job details to the s3 buckets of a user.</p>"""
    failure_reason: NotRequired["capo_braket.types.string1024.String1024"]
    """<p>A description of the reason why an Amazon Braket hybrid job failed, if it failed.</p>"""
    job_name: "str"
    """<p>The name of the Amazon Braket hybrid job.</p>"""
    hyper_parameters: NotRequired["capo_braket.types.hyper_parameters.HyperParameters"]
    """<p>Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the traiing job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of th hyperparameter.</p>"""
    input_data_config: NotRequired[
        "capo_braket.types.input_config_list.InputConfigList"
    ]
    """<p>A list of parameters that specify the name and type of input data and where it is located.</p>"""
    output_data_config: "capo_braket.types.job_output_data_config.JobOutputDataConfig"
    """<p>The path to the S3 location where hybrid job artifacts are stored and the encryption key used to store them there.</p>"""
    stopping_condition: NotRequired[
        "capo_braket.types.job_stopping_condition.JobStoppingCondition"
    ]
    """<p>The user-defined criteria that specifies when to stop a running hybrid job.</p>"""
    checkpoint_config: NotRequired[
        "capo_braket.types.job_checkpoint_config.JobCheckpointConfig"
    ]
    """<p>Information about the output locations for hybrid job checkpoint data.</p>"""
    algorithm_specification: (
        "capo_braket.types.algorithm_specification.AlgorithmSpecification"
    )
    """<p>Definition of the Amazon Braket hybrid job created. Provides information about the container image used, and the Python scripts used for training.</p>"""
    instance_config: "capo_braket.types.instance_config.InstanceConfig"
    """<p>The resource instances to use while running the hybrid job on Amazon Braket.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the Amazon Braket hybrid job was created.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job was started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job ended.</p>"""
    billable_duration: NotRequired["int"]
    """<p>The billable time for which the Amazon Braket hybrid job used to complete.</p>"""
    device_config: NotRequired["capo_braket.types.device_config.DeviceConfig"]
    """<p>The primary device used by the Amazon Braket hybrid job.</p>"""
    events: NotRequired["capo_braket.types.job_events.JobEvents"]
    """<p>Details about the time and type of events occurred related to the Amazon Braket hybrid job.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>The tags associated with this hybrid job.</p>"""
    queue_info: NotRequired[
        "capo_braket.types.hybrid_job_queue_info.HybridJobQueueInfo"
    ]
    """<p>Queue information for the requested hybrid job. Only returned if <code>QueueInfo</code> is specified in the <code>additionalAttributeNames"</code> field in the <code>GetJob</code> API request.</p>"""
    associations: NotRequired["capo_braket.types.associations.Associations"]
    """<p>The list of Amazon Braket resources associated with the hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobResponse) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["jobArn"] = value["job_arn"]
    out["roleArn"] = value["role_arn"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    out["jobName"] = value["job_name"]
    if "hyper_parameters" in value:
        import capo_braket.types.hyper_parameters

        out["hyperParameters"] = capo_braket.types.hyper_parameters.serialize_json(
            value["hyper_parameters"]
        )
    if "input_data_config" in value:
        import capo_braket.types.input_config_list

        out["inputDataConfig"] = capo_braket.types.input_config_list.serialize_json(
            value["input_data_config"]
        )
    import capo_braket.types.job_output_data_config

    out["outputDataConfig"] = capo_braket.types.job_output_data_config.serialize_json(
        value["output_data_config"]
    )
    if "stopping_condition" in value:
        import capo_braket.types.job_stopping_condition

        out["stoppingCondition"] = (
            capo_braket.types.job_stopping_condition.serialize_json(
                value["stopping_condition"]
            )
        )
    if "checkpoint_config" in value:
        import capo_braket.types.job_checkpoint_config

        out["checkpointConfig"] = (
            capo_braket.types.job_checkpoint_config.serialize_json(
                value["checkpoint_config"]
            )
        )
    import capo_braket.types.algorithm_specification

    out["algorithmSpecification"] = (
        capo_braket.types.algorithm_specification.serialize_json(
            value["algorithm_specification"]
        )
    )
    import capo_braket.types.instance_config

    out["instanceConfig"] = capo_braket.types.instance_config.serialize_json(
        value["instance_config"]
    )
    import capo_braket._protocol.serialize

    out["createdAt"] = capo_braket._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "started_at" in value:
        import capo_braket._protocol.serialize

        out["startedAt"] = capo_braket._protocol.serialize.fmt_date_time(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_braket._protocol.serialize

        out["endedAt"] = capo_braket._protocol.serialize.fmt_date_time(
            value["ended_at"]
        )
    if "billable_duration" in value:
        out["billableDuration"] = value["billable_duration"]
    if "device_config" in value:
        import capo_braket.types.device_config

        out["deviceConfig"] = capo_braket.types.device_config.serialize_json(
            value["device_config"]
        )
    if "events" in value:
        import capo_braket.types.job_events

        out["events"] = capo_braket.types.job_events.serialize_json(value["events"])
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    if "queue_info" in value:
        import capo_braket.types.hybrid_job_queue_info

        out["queueInfo"] = capo_braket.types.hybrid_job_queue_info.serialize_json(
            value["queue_info"]
        )
    if "associations" in value:
        import capo_braket.types.associations

        out["associations"] = capo_braket.types.associations.serialize_json(
            value["associations"]
        )
    return out


def deserialize_json(data: dict) -> GetJobResponse:
    out: GetJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetJobResponse.status required")
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("GetJobResponse.job_arn required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetJobResponse.role_arn required")
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("GetJobResponse.job_name required")
    if data.get("hyperParameters") is not None:
        import capo_braket.types.hyper_parameters

        out["hyper_parameters"] = capo_braket.types.hyper_parameters.deserialize_json(
            data["hyperParameters"]
        )
    if data.get("inputDataConfig") is not None:
        import capo_braket.types.input_config_list

        out["input_data_config"] = capo_braket.types.input_config_list.deserialize_json(
            data["inputDataConfig"]
        )
    if data.get("outputDataConfig") is not None:
        import capo_braket.types.job_output_data_config

        out["output_data_config"] = (
            capo_braket.types.job_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError("GetJobResponse.output_data_config required")
    if data.get("stoppingCondition") is not None:
        import capo_braket.types.job_stopping_condition

        out["stopping_condition"] = (
            capo_braket.types.job_stopping_condition.deserialize_json(
                data["stoppingCondition"]
            )
        )
    if data.get("checkpointConfig") is not None:
        import capo_braket.types.job_checkpoint_config

        out["checkpoint_config"] = (
            capo_braket.types.job_checkpoint_config.deserialize_json(
                data["checkpointConfig"]
            )
        )
    if data.get("algorithmSpecification") is not None:
        import capo_braket.types.algorithm_specification

        out["algorithm_specification"] = (
            capo_braket.types.algorithm_specification.deserialize_json(
                data["algorithmSpecification"]
            )
        )
    else:
        raise DeserializationError("GetJobResponse.algorithm_specification required")
    if data.get("instanceConfig") is not None:
        import capo_braket.types.instance_config

        out["instance_config"] = capo_braket.types.instance_config.deserialize_json(
            data["instanceConfig"]
        )
    else:
        raise DeserializationError("GetJobResponse.instance_config required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("GetJobResponse.created_at required")
    if data.get("startedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["startedAt"].replace("Z", "+00:00")
        )
    if data.get("endedAt") is not None:
        import datetime

        out["ended_at"] = datetime.datetime.fromisoformat(
            data["endedAt"].replace("Z", "+00:00")
        )
    if data.get("billableDuration") is not None:
        out["billable_duration"] = data["billableDuration"]
    if data.get("deviceConfig") is not None:
        import capo_braket.types.device_config

        out["device_config"] = capo_braket.types.device_config.deserialize_json(
            data["deviceConfig"]
        )
    if data.get("events") is not None:
        import capo_braket.types.job_events

        out["events"] = capo_braket.types.job_events.deserialize_json(data["events"])
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    if data.get("queueInfo") is not None:
        import capo_braket.types.hybrid_job_queue_info

        out["queue_info"] = capo_braket.types.hybrid_job_queue_info.deserialize_json(
            data["queueInfo"]
        )
    if data.get("associations") is not None:
        import capo_braket.types.associations

        out["associations"] = capo_braket.types.associations.deserialize_json(
            data["associations"]
        )
    return out
