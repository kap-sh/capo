"""Generated from Smithy shape ``com.amazonaws.braket#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import capo_braket.types.algorithm_specification
    import capo_braket.types.associations
    import capo_braket.types.device_config
    import capo_braket.types.hyper_parameters
    import capo_braket.types.input_config_list
    import capo_braket.types.instance_config
    import capo_braket.types.job_checkpoint_config
    import capo_braket.types.job_output_data_config
    import capo_braket.types.job_stopping_condition
    import capo_braket.types.role_arn
    import capo_braket.types.string64
    import capo_braket.types.tags_map


class CreateJobRequest(TypedDict, closed=True):
    client_token: "capo_braket.types.string64.String64"
    """<p>The client token associated with this request that guarantees that the request is idempotent.</p>"""
    algorithm_specification: (
        "capo_braket.types.algorithm_specification.AlgorithmSpecification"
    )
    """<p>Definition of the Amazon Braket job to be created. Specifies the container image the job uses and information about the Python scripts used for entry and training.</p>"""
    input_data_config: NotRequired[
        "capo_braket.types.input_config_list.InputConfigList"
    ]
    """<p>A list of parameters that specify the name and type of input data and where it is located.</p>"""
    output_data_config: "capo_braket.types.job_output_data_config.JobOutputDataConfig"
    """<p>The path to the S3 location where you want to store hybrid job artifacts and the encryption key used to store them.</p>"""
    checkpoint_config: NotRequired[
        "capo_braket.types.job_checkpoint_config.JobCheckpointConfig"
    ]
    """<p>Information about the output locations for hybrid job checkpoint data.</p>"""
    job_name: "str"
    """<p>The name of the Amazon Braket hybrid job.</p>"""
    role_arn: "capo_braket.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and hybrid job details to the users' s3 buckets.</p>"""
    stopping_condition: NotRequired[
        "capo_braket.types.job_stopping_condition.JobStoppingCondition"
    ]
    """<p> The user-defined criteria that specifies when a hybrid job stops running.</p>"""
    instance_config: "capo_braket.types.instance_config.InstanceConfig"
    """<p>Configuration of the resource instances to use while running the hybrid job on Amazon Braket.</p>"""
    hyper_parameters: NotRequired["capo_braket.types.hyper_parameters.HyperParameters"]
    """<p>Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the training job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of the hyperparameter.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request hyperparameter variable or plain text fields.</p> </important>"""
    device_config: "capo_braket.types.device_config.DeviceConfig"
    """<p>The quantum processing unit (QPU) or simulator used to create an Amazon Braket hybrid job.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>Tags to be added to the hybrid job you're creating.</p>"""
    associations: NotRequired["capo_braket.types.associations.Associations"]
    """<p>The list of Amazon Braket resources associated with the hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    import capo_braket.types.algorithm_specification

    out["algorithmSpecification"] = (
        capo_braket.types.algorithm_specification.serialize_json(
            value["algorithm_specification"]
        )
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
    if "checkpoint_config" in value:
        import capo_braket.types.job_checkpoint_config

        out["checkpointConfig"] = (
            capo_braket.types.job_checkpoint_config.serialize_json(
                value["checkpoint_config"]
            )
        )
    out["jobName"] = value["job_name"]
    out["roleArn"] = value["role_arn"]
    if "stopping_condition" in value:
        import capo_braket.types.job_stopping_condition

        out["stoppingCondition"] = (
            capo_braket.types.job_stopping_condition.serialize_json(
                value["stopping_condition"]
            )
        )
    import capo_braket.types.instance_config

    out["instanceConfig"] = capo_braket.types.instance_config.serialize_json(
        value["instance_config"]
    )
    if "hyper_parameters" in value:
        import capo_braket.types.hyper_parameters

        out["hyperParameters"] = capo_braket.types.hyper_parameters.serialize_json(
            value["hyper_parameters"]
        )
    import capo_braket.types.device_config

    out["deviceConfig"] = capo_braket.types.device_config.serialize_json(
        value["device_config"]
    )
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    if "associations" in value:
        import capo_braket.types.associations

        out["associations"] = capo_braket.types.associations.serialize_json(
            value["associations"]
        )
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("algorithmSpecification") is not None:
        import capo_braket.types.algorithm_specification

        out["algorithm_specification"] = (
            capo_braket.types.algorithm_specification.deserialize_json(
                data["algorithmSpecification"]
            )
        )
    else:
        raise DeserializationError("CreateJobRequest.algorithm_specification required")
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
        raise DeserializationError("CreateJobRequest.output_data_config required")
    if data.get("checkpointConfig") is not None:
        import capo_braket.types.job_checkpoint_config

        out["checkpoint_config"] = (
            capo_braket.types.job_checkpoint_config.deserialize_json(
                data["checkpointConfig"]
            )
        )
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("stoppingCondition") is not None:
        import capo_braket.types.job_stopping_condition

        out["stopping_condition"] = (
            capo_braket.types.job_stopping_condition.deserialize_json(
                data["stoppingCondition"]
            )
        )
    if data.get("instanceConfig") is not None:
        import capo_braket.types.instance_config

        out["instance_config"] = capo_braket.types.instance_config.deserialize_json(
            data["instanceConfig"]
        )
    else:
        raise DeserializationError("CreateJobRequest.instance_config required")
    if data.get("hyperParameters") is not None:
        import capo_braket.types.hyper_parameters

        out["hyper_parameters"] = capo_braket.types.hyper_parameters.deserialize_json(
            data["hyperParameters"]
        )
    if data.get("deviceConfig") is not None:
        import capo_braket.types.device_config

        out["device_config"] = capo_braket.types.device_config.deserialize_json(
            data["deviceConfig"]
        )
    else:
        raise DeserializationError("CreateJobRequest.device_config required")
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    if data.get("associations") is not None:
        import capo_braket.types.associations

        out["associations"] = capo_braket.types.associations.deserialize_json(
            data["associations"]
        )
    return out
