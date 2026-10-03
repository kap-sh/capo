"""Generated from Smithy shape ``com.amazonaws.glue#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.code_gen_configuration_nodes
    import capo_glue.types.connections_list
    import capo_glue.types.description_string
    import capo_glue.types.execution_class
    import capo_glue.types.execution_property
    import capo_glue.types.generic_map
    import capo_glue.types.glue_version_string
    import capo_glue.types.integer_value
    import capo_glue.types.job_command
    import capo_glue.types.job_mode
    import capo_glue.types.maintenance_window
    import capo_glue.types.max_retries
    import capo_glue.types.name_string
    import capo_glue.types.notification_property
    import capo_glue.types.nullable_boolean
    import capo_glue.types.nullable_double
    import capo_glue.types.nullable_integer
    import capo_glue.types.role_string
    import capo_glue.types.source_control_details
    import capo_glue.types.tags_map
    import capo_glue.types.timeout
    import capo_glue.types.uri_string
    import capo_glue.types.worker_type


class CreateJobRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name you assign to this job definition. It must be unique in your account.</p>"""
    job_mode: NotRequired["capo_glue.types.job_mode.JobMode"]
    """<p>A mode that describes how a job was created. Valid values are:</p> <ul> <li> <p> <code>SCRIPT</code> - The job was created using the Glue Studio script editor.</p> </li> <li> <p> <code>VISUAL</code> - The job was created using the Glue Studio visual editor.</p> </li> <li> <p> <code>NOTEBOOK</code> - The job was created using an interactive sessions notebook.</p> </li> </ul> <p>When the <code>JobMode</code> field is missing or null, <code>SCRIPT</code> is assigned as the default value.</p>"""
    job_run_queuing_enabled: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether job run queuing is enabled for the job runs for this job.</p> <p>A value of true means job run queuing is enabled for the job runs. If false or not populated, the job runs will not be considered for queueing.</p> <p>If this field does not match the value set in the job run, then the value from the job run field will be used.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>Description of the job being defined.</p>"""
    log_uri: NotRequired["capo_glue.types.uri_string.UriString"]
    """<p>This field is reserved for future use.</p>"""
    role: "capo_glue.types.role_string.RoleString"
    """<p>The name or Amazon Resource Name (ARN) of the IAM role associated with this job.</p>"""
    execution_property: NotRequired[
        "capo_glue.types.execution_property.ExecutionProperty"
    ]
    """<p>An <code>ExecutionProperty</code> specifying the maximum number of concurrent runs allowed for this job.</p>"""
    command: "capo_glue.types.job_command.JobCommand"
    """<p>The <code>JobCommand</code> that runs this job.</p>"""
    default_arguments: NotRequired["capo_glue.types.generic_map.GenericMap"]
    """<p>The default arguments for every run of this job, specified as name-value pairs.</p> <p>You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.</p> <p>Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Secrets Manager or other secret management mechanism if you intend to keep them within the Job. </p> <p>For information about how to specify and consume your own Job arguments, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling Glue APIs in Python</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Spark jobs, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html">Special Parameters Used by Glue</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Ray jobs, see <a href="https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html">Using job parameters in Ray jobs</a> in the developer guide.</p>"""
    non_overridable_arguments: NotRequired["capo_glue.types.generic_map.GenericMap"]
    """<p>Arguments for this job that are not overridden when providing job arguments in a job run, specified as name-value pairs.</p>"""
    connections: NotRequired["capo_glue.types.connections_list.ConnectionsList"]
    """<p>The connections used for this job.</p>"""
    max_retries: "capo_glue.types.max_retries.MaxRetries"
    """<p>The maximum number of times to retry this job if it fails.</p>"""
    allocated_capacity: "capo_glue.types.integer_value.IntegerValue"
    """<p>This parameter is deprecated. Use <code>MaxCapacity</code> instead.</p> <p>The number of Glue data processing units (DPUs) to allocate to this Job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href="https://aws.amazon.com/glue/pricing/">Glue pricing page</a>.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters <code>TIMEOUT</code> status.</p> <p>Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.</p> <p>When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.</p> <p>Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.</p> <p>For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.</p>"""
    max_capacity: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href="https://aws.amazon.com/glue/pricing/"> Glue pricing page</a>.</p> <p>For Glue version 2.0+ jobs, you cannot specify a <code>Maximum capacity</code>. Instead, you should specify a <code>Worker type</code> and the <code>Number of workers</code>.</p> <p>Do not set <code>MaxCapacity</code> if using <code>WorkerType</code> and <code>NumberOfWorkers</code>.</p> <p>The value that can be allocated for <code>MaxCapacity</code> depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:</p> <ul> <li> <p>When you specify a Python shell job (<code>JobCommand.Name</code>="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.</p> </li> <li> <p>When you specify an Apache Spark ETL job (<code>JobCommand.Name</code>="glueetl") or Apache Spark streaming ETL job (<code>JobCommand.Name</code>="gluestreaming"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.</p> </li> </ul>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the <code>SecurityConfiguration</code> structure to be used with this job.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The tags to use with this job. You may use tags to limit access to the job. For more information about tags in Glue, see <a href="https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html">Amazon Web Services Tags in Glue</a> in the developer guide.</p>"""
    notification_property: NotRequired[
        "capo_glue.types.notification_property.NotificationProperty"
    ]
    """<p>Specifies configuration properties of a job notification.</p>"""
    glue_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<p>In Spark jobs, <code>GlueVersion</code> determines the versions of Apache Spark and Python that Glue available in a job. The Python version indicates the version supported for jobs of type Spark. </p> <p>Ray jobs should set <code>GlueVersion</code> to <code>4.0</code> or greater. However, the versions of Ray, Python and additional libraries available in your Ray job are determined by the <code>Runtime</code> parameter of the Job command.</p> <p>For more information about the available Glue versions and corresponding Spark and Python versions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Glue version</a> in the developer guide.</p> <p>Jobs that are created without specifying a Glue version default to Glue 5.1.</p>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of workers of a defined <code>workerType</code> that are allocated when a job runs.</p>"""
    worker_type: NotRequired["capo_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.</p> <ul> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.4X</code> worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Spain), Europe (Stockholm), and South America (São Paulo).</p> </li> <li> <p>For the <code>G.8X</code> worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the <code>G.4X</code> worker type.</p> </li> <li> <p>For the <code>G.025X</code> worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for Glue version 3.0 or later streaming jobs.</p> </li> <li> <p>For the <code>Z.2X</code> worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.</p> </li> </ul>"""
    code_gen_configuration_nodes: NotRequired[
        "capo_glue.types.code_gen_configuration_nodes.CodeGenConfigurationNodes"
    ]
    """<p>The representation of a directed acyclic graph on which both the Glue Studio visual component and Glue Studio code generation is based.</p>"""
    execution_class: NotRequired["capo_glue.types.execution_class.ExecutionClass"]
    """<p>Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.</p> <p>The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary. </p> <p>Only jobs with Glue version 3.0 and above and command type <code>glueetl</code> will be allowed to set <code>ExecutionClass</code> to <code>FLEX</code>. The flexible execution class is available for Spark jobs.</p>"""
    source_control_details: NotRequired[
        "capo_glue.types.source_control_details.SourceControlDetails"
    ]
    """<p>The details for a source control configuration for a job, allowing synchronization of job artifacts to or from a remote repository.</p>"""
    maintenance_window: NotRequired[
        "capo_glue.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>This field specifies a day of the week and hour for a maintenance window for streaming jobs. Glue periodically performs maintenance activities. During these maintenance windows, Glue will need to restart your streaming jobs.</p> <p>Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateJobRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "job_mode" in value:
        import capo_glue.types.job_mode

        out["JobMode"] = capo_glue.types.job_mode.serialize_aws_json_1_1(
            value["job_mode"]
        )
    if "job_run_queuing_enabled" in value:
        out["JobRunQueuingEnabled"] = value["job_run_queuing_enabled"]
    if "description" in value:
        out["Description"] = value["description"]
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    out["Role"] = value["role"]
    if "execution_property" in value:
        import capo_glue.types.execution_property

        out["ExecutionProperty"] = (
            capo_glue.types.execution_property.serialize_aws_json_1_1(
                value["execution_property"]
            )
        )
    import capo_glue.types.job_command

    out["Command"] = capo_glue.types.job_command.serialize_aws_json_1_1(
        value["command"]
    )
    if "default_arguments" in value:
        import capo_glue.types.generic_map

        out["DefaultArguments"] = capo_glue.types.generic_map.serialize_aws_json_1_1(
            value["default_arguments"]
        )
    if "non_overridable_arguments" in value:
        import capo_glue.types.generic_map

        out["NonOverridableArguments"] = (
            capo_glue.types.generic_map.serialize_aws_json_1_1(
                value["non_overridable_arguments"]
            )
        )
    if "connections" in value:
        import capo_glue.types.connections_list

        out["Connections"] = capo_glue.types.connections_list.serialize_aws_json_1_1(
            value["connections"]
        )
    out["MaxRetries"] = value.get("max_retries", 0)
    out["AllocatedCapacity"] = value.get("allocated_capacity", 0)
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "max_capacity" in value:
        out["MaxCapacity"] = (
            "NaN"
            if value["max_capacity"] != value["max_capacity"]
            else "Infinity"
            if value["max_capacity"] == float("inf")
            else "-Infinity"
            if value["max_capacity"] == float("-inf")
            else value["max_capacity"]
        )
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "notification_property" in value:
        import capo_glue.types.notification_property

        out["NotificationProperty"] = (
            capo_glue.types.notification_property.serialize_aws_json_1_1(
                value["notification_property"]
            )
        )
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "worker_type" in value:
        import capo_glue.types.worker_type

        out["WorkerType"] = capo_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "code_gen_configuration_nodes" in value:
        import capo_glue.types.code_gen_configuration_nodes

        out["CodeGenConfigurationNodes"] = (
            capo_glue.types.code_gen_configuration_nodes.serialize_aws_json_1_1(
                value["code_gen_configuration_nodes"]
            )
        )
    if "execution_class" in value:
        import capo_glue.types.execution_class

        out["ExecutionClass"] = capo_glue.types.execution_class.serialize_aws_json_1_1(
            value["execution_class"]
        )
    if "source_control_details" in value:
        import capo_glue.types.source_control_details

        out["SourceControlDetails"] = (
            capo_glue.types.source_control_details.serialize_aws_json_1_1(
                value["source_control_details"]
            )
        )
    if "maintenance_window" in value:
        out["MaintenanceWindow"] = value["maintenance_window"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateJobRequest.name required")
    if data.get("JobMode") is not None:
        import capo_glue.types.job_mode

        out["job_mode"] = capo_glue.types.job_mode.deserialize_aws_json_1_1(
            data["JobMode"]
        )
    if data.get("JobRunQueuingEnabled") is not None:
        out["job_run_queuing_enabled"] = data["JobRunQueuingEnabled"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LogUri") is not None:
        out["log_uri"] = data["LogUri"]
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        raise DeserializationError("CreateJobRequest.role required")
    if data.get("ExecutionProperty") is not None:
        import capo_glue.types.execution_property

        out["execution_property"] = (
            capo_glue.types.execution_property.deserialize_aws_json_1_1(
                data["ExecutionProperty"]
            )
        )
    if data.get("Command") is not None:
        import capo_glue.types.job_command

        out["command"] = capo_glue.types.job_command.deserialize_aws_json_1_1(
            data["Command"]
        )
    else:
        raise DeserializationError("CreateJobRequest.command required")
    if data.get("DefaultArguments") is not None:
        import capo_glue.types.generic_map

        out["default_arguments"] = capo_glue.types.generic_map.deserialize_aws_json_1_1(
            data["DefaultArguments"]
        )
    if data.get("NonOverridableArguments") is not None:
        import capo_glue.types.generic_map

        out["non_overridable_arguments"] = (
            capo_glue.types.generic_map.deserialize_aws_json_1_1(
                data["NonOverridableArguments"]
            )
        )
    if data.get("Connections") is not None:
        import capo_glue.types.connections_list

        out["connections"] = capo_glue.types.connections_list.deserialize_aws_json_1_1(
            data["Connections"]
        )
    if data.get("MaxRetries") is not None:
        out["max_retries"] = data["MaxRetries"]
    else:
        out["max_retries"] = 0
    if data.get("AllocatedCapacity") is not None:
        out["allocated_capacity"] = data["AllocatedCapacity"]
    else:
        out["allocated_capacity"] = 0
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = float(data["MaxCapacity"])
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("NotificationProperty") is not None:
        import capo_glue.types.notification_property

        out["notification_property"] = (
            capo_glue.types.notification_property.deserialize_aws_json_1_1(
                data["NotificationProperty"]
            )
        )
    if data.get("GlueVersion") is not None:
        out["glue_version"] = data["GlueVersion"]
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("WorkerType") is not None:
        import capo_glue.types.worker_type

        out["worker_type"] = capo_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if data.get("CodeGenConfigurationNodes") is not None:
        import capo_glue.types.code_gen_configuration_nodes

        out["code_gen_configuration_nodes"] = (
            capo_glue.types.code_gen_configuration_nodes.deserialize_aws_json_1_1(
                data["CodeGenConfigurationNodes"]
            )
        )
    if data.get("ExecutionClass") is not None:
        import capo_glue.types.execution_class

        out["execution_class"] = (
            capo_glue.types.execution_class.deserialize_aws_json_1_1(
                data["ExecutionClass"]
            )
        )
    if data.get("SourceControlDetails") is not None:
        import capo_glue.types.source_control_details

        out["source_control_details"] = (
            capo_glue.types.source_control_details.deserialize_aws_json_1_1(
                data["SourceControlDetails"]
            )
        )
    if data.get("MaintenanceWindow") is not None:
        out["maintenance_window"] = data["MaintenanceWindow"]
    return out
