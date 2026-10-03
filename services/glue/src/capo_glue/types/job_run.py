"""Generated from Smithy shape ``com.amazonaws.glue#JobRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.attempt_count
    import capo_glue.types.error_string
    import capo_glue.types.execution_class
    import capo_glue.types.execution_time
    import capo_glue.types.generic_map
    import capo_glue.types.generic_string
    import capo_glue.types.glue_version_string
    import capo_glue.types.id_string
    import capo_glue.types.integer_value
    import capo_glue.types.job_mode
    import capo_glue.types.job_run_state
    import capo_glue.types.maintenance_window
    import capo_glue.types.name_string
    import capo_glue.types.notification_property
    import capo_glue.types.nullable_boolean
    import capo_glue.types.nullable_double
    import capo_glue.types.nullable_integer
    import capo_glue.types.orchestration_message_string
    import capo_glue.types.orchestration_policy_json_string
    import capo_glue.types.predecessor_list
    import capo_glue.types.timeout
    import capo_glue.types.timestamp_value
    import capo_glue.types.worker_type


class JobRun(TypedDict, closed=True):
    id: NotRequired["capo_glue.types.id_string.IdString"]
    """<p>The ID of this job run.</p>"""
    attempt: "capo_glue.types.attempt_count.AttemptCount"
    """<p>The number of the attempt to run this job.</p>"""
    previous_run_id: NotRequired["capo_glue.types.id_string.IdString"]
    """<p>The ID of the previous run of this job. For example, the <code>JobRunId</code> specified in the <code>StartJobRun</code> action.</p>"""
    trigger_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the trigger that started this job run.</p>"""
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the job definition being used in this run.</p>"""
    job_mode: NotRequired["capo_glue.types.job_mode.JobMode"]
    """<p>A mode that describes how a job was created. Valid values are:</p> <ul> <li> <p> <code>SCRIPT</code> - The job was created using the Glue Studio script editor.</p> </li> <li> <p> <code>VISUAL</code> - The job was created using the Glue Studio visual editor.</p> </li> <li> <p> <code>NOTEBOOK</code> - The job was created using an interactive sessions notebook.</p> </li> </ul> <p>When the <code>JobMode</code> field is missing or null, <code>SCRIPT</code> is assigned as the default value.</p>"""
    job_run_queuing_enabled: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether job run queuing is enabled for the job run.</p> <p>A value of true means job run queuing is enabled for the job run. If false or not populated, the job run will not be considered for queueing.</p>"""
    started_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time at which this job run was started.</p>"""
    last_modified_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The last time that this job run was modified.</p>"""
    completed_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time that this job run completed.</p>"""
    job_run_state: NotRequired["capo_glue.types.job_run_state.JobRunState"]
    """<p>The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see <a href="https://docs.aws.amazon.com/glue/latest/dg/job-run-statuses.html">Glue Job Run Statuses</a>.</p>"""
    arguments: NotRequired["capo_glue.types.generic_map.GenericMap"]
    """<p>The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.</p> <p>You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.</p> <p>Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Secrets Manager or other secret management mechanism if you intend to keep them within the Job. </p> <p>For information about how to specify and consume your own Job arguments, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling Glue APIs in Python</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Spark jobs, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html">Special Parameters Used by Glue</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Ray jobs, see <a href="https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html">Using job parameters in Ray jobs</a> in the developer guide.</p>"""
    error_message: NotRequired["capo_glue.types.error_string.ErrorString"]
    """<p>An error message associated with this job run.</p>"""
    predecessor_runs: NotRequired["capo_glue.types.predecessor_list.PredecessorList"]
    """<p>A list of predecessors to this job run.</p>"""
    allocated_capacity: "capo_glue.types.integer_value.IntegerValue"
    """<p>This field is deprecated. Use <code>MaxCapacity</code> instead.</p> <p>The number of Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href="https://aws.amazon.com/glue/pricing/">Glue pricing page</a>.</p>"""
    execution_time: "capo_glue.types.execution_time.ExecutionTime"
    """<p>The amount of time (in seconds) that the job run consumed resources.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The <code>JobRun</code> timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. This value overrides the timeout value set in the parent job.</p> <p>Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.</p> <p>When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.</p> <p>Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.</p> <p>For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.</p>"""
    max_capacity: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href="https://aws.amazon.com/glue/pricing/"> Glue pricing page</a>.</p> <p>For Glue version 2.0+ jobs, you cannot specify a <code>Maximum capacity</code>. Instead, you should specify a <code>Worker type</code> and the <code>Number of workers</code>.</p> <p>Do not set <code>MaxCapacity</code> if using <code>WorkerType</code> and <code>NumberOfWorkers</code>.</p> <p>The value that can be allocated for <code>MaxCapacity</code> depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:</p> <ul> <li> <p>When you specify a Python shell job (<code>JobCommand.Name</code>="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.</p> </li> <li> <p>When you specify an Apache Spark ETL job (<code>JobCommand.Name</code>="glueetl") or Apache Spark streaming ETL job (<code>JobCommand.Name</code>="gluestreaming"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.</p> </li> </ul>"""
    worker_type: NotRequired["capo_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.</p> <ul> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.4X</code> worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).</p> </li> <li> <p>For the <code>G.8X</code> worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the <code>G.4X</code> worker type.</p> </li> <li> <p>For the <code>G.025X</code> worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for Glue version 3.0 or later streaming jobs.</p> </li> <li> <p>For the <code>Z.2X</code> worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.</p> </li> </ul>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of workers of a defined <code>workerType</code> that are allocated when a job runs.</p>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the <code>SecurityConfiguration</code> structure to be used with this job run.</p>"""
    log_group_name: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using KMS. This name can be <code>/aws-glue/jobs/</code>, in which case the default encryption is <code>NONE</code>. If you add a role name and <code>SecurityConfiguration</code> name (in other words, <code>/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/</code>), then that security configuration is used to encrypt the log group.</p>"""
    notification_property: NotRequired[
        "capo_glue.types.notification_property.NotificationProperty"
    ]
    """<p>Specifies configuration properties of a job run notification.</p>"""
    glue_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<p>In Spark jobs, <code>GlueVersion</code> determines the versions of Apache Spark and Python that Glue available in a job. The Python version indicates the version supported for jobs of type Spark. </p> <p>Ray jobs should set <code>GlueVersion</code> to <code>4.0</code> or greater. However, the versions of Ray, Python and additional libraries available in your Ray job are determined by the <code>Runtime</code> parameter of the Job command.</p> <p>For more information about the available Glue versions and corresponding Spark and Python versions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Glue version</a> in the developer guide.</p> <p>Jobs that are created without specifying a Glue version default to Glue 5.1.</p>"""
    dpu_seconds: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>This field can be set for either job runs with execution class <code>FLEX</code> or when Auto Scaling is enabled, and represents the total time each executor ran during the lifecycle of a job run in seconds, multiplied by a DPU factor (1 for <code>G.1X</code>, 2 for <code>G.2X</code>, or 0.25 for <code>G.025X</code> workers). This value may be different than the <code>executionEngineRuntime</code> * <code>MaxCapacity</code> as in the case of Auto Scaling jobs, as the number of executors running at a given time may be less than the <code>MaxCapacity</code>. Therefore, it is possible that the value of <code>DPUSeconds</code> is less than <code>executionEngineRuntime</code> * <code>MaxCapacity</code>.</p>"""
    execution_class: NotRequired["capo_glue.types.execution_class.ExecutionClass"]
    """<p>Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.</p> <p>The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary. </p> <p>Only jobs with Glue version 3.0 and above and command type <code>glueetl</code> will be allowed to set <code>ExecutionClass</code> to <code>FLEX</code>. The flexible execution class is available for Spark jobs.</p>"""
    maintenance_window: NotRequired[
        "capo_glue.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>This field specifies a day of the week and hour for a maintenance window for streaming jobs. Glue periodically performs maintenance activities. During these maintenance windows, Glue will need to restart your streaming jobs.</p> <p>Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.</p>"""
    profile_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of an Glue usage profile associated with the job run.</p>"""
    state_detail: NotRequired[
        "capo_glue.types.orchestration_message_string.OrchestrationMessageString"
    ]
    """<p>This field holds details that pertain to the state of a job run. The field is nullable.</p> <p>For example, when a job run is in a WAITING state as a result of job run queuing, the field has the reason why the job run is in that state.</p>"""
    execution_role_session_policy: NotRequired[
        "capo_glue.types.orchestration_policy_json_string.OrchestrationPolicyJsonString"
    ]
    """<p>This inline session policy to the StartJobRun API allows you to dynamically restrict the permissions of the specified execution role for the scope of the job, without requiring the creation of additional IAM roles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobRun) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    out["Attempt"] = value.get("attempt", 0)
    if "previous_run_id" in value:
        out["PreviousRunId"] = value["previous_run_id"]
    if "trigger_name" in value:
        out["TriggerName"] = value["trigger_name"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_mode" in value:
        import capo_glue.types.job_mode

        out["JobMode"] = capo_glue.types.job_mode.serialize_aws_json_1_1(
            value["job_mode"]
        )
    if "job_run_queuing_enabled" in value:
        out["JobRunQueuingEnabled"] = value["job_run_queuing_enabled"]
    if "started_on" in value:
        import capo_glue.types.timestamp_value

        out["StartedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "last_modified_on" in value:
        import capo_glue.types.timestamp_value

        out["LastModifiedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["last_modified_on"]
        )
    if "completed_on" in value:
        import capo_glue.types.timestamp_value

        out["CompletedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "job_run_state" in value:
        import capo_glue.types.job_run_state

        out["JobRunState"] = capo_glue.types.job_run_state.serialize_aws_json_1_1(
            value["job_run_state"]
        )
    if "arguments" in value:
        import capo_glue.types.generic_map

        out["Arguments"] = capo_glue.types.generic_map.serialize_aws_json_1_1(
            value["arguments"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "predecessor_runs" in value:
        import capo_glue.types.predecessor_list

        out["PredecessorRuns"] = (
            capo_glue.types.predecessor_list.serialize_aws_json_1_1(
                value["predecessor_runs"]
            )
        )
    out["AllocatedCapacity"] = value.get("allocated_capacity", 0)
    out["ExecutionTime"] = value.get("execution_time", 0)
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
    if "worker_type" in value:
        import capo_glue.types.worker_type

        out["WorkerType"] = capo_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "notification_property" in value:
        import capo_glue.types.notification_property

        out["NotificationProperty"] = (
            capo_glue.types.notification_property.serialize_aws_json_1_1(
                value["notification_property"]
            )
        )
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "dpu_seconds" in value:
        out["DPUSeconds"] = (
            "NaN"
            if value["dpu_seconds"] != value["dpu_seconds"]
            else "Infinity"
            if value["dpu_seconds"] == float("inf")
            else "-Infinity"
            if value["dpu_seconds"] == float("-inf")
            else value["dpu_seconds"]
        )
    if "execution_class" in value:
        import capo_glue.types.execution_class

        out["ExecutionClass"] = capo_glue.types.execution_class.serialize_aws_json_1_1(
            value["execution_class"]
        )
    if "maintenance_window" in value:
        out["MaintenanceWindow"] = value["maintenance_window"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "state_detail" in value:
        out["StateDetail"] = value["state_detail"]
    if "execution_role_session_policy" in value:
        out["ExecutionRoleSessionPolicy"] = value["execution_role_session_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobRun:
    out: JobRun = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Attempt") is not None:
        out["attempt"] = data["Attempt"]
    else:
        out["attempt"] = 0
    if data.get("PreviousRunId") is not None:
        out["previous_run_id"] = data["PreviousRunId"]
    if data.get("TriggerName") is not None:
        out["trigger_name"] = data["TriggerName"]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobMode") is not None:
        import capo_glue.types.job_mode

        out["job_mode"] = capo_glue.types.job_mode.deserialize_aws_json_1_1(
            data["JobMode"]
        )
    if data.get("JobRunQueuingEnabled") is not None:
        out["job_run_queuing_enabled"] = data["JobRunQueuingEnabled"]
    if data.get("StartedOn") is not None:
        import capo_glue.types.timestamp_value

        out["started_on"] = capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if data.get("LastModifiedOn") is not None:
        import capo_glue.types.timestamp_value

        out["last_modified_on"] = (
            capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["LastModifiedOn"]
            )
        )
    if data.get("CompletedOn") is not None:
        import capo_glue.types.timestamp_value

        out["completed_on"] = capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if data.get("JobRunState") is not None:
        import capo_glue.types.job_run_state

        out["job_run_state"] = capo_glue.types.job_run_state.deserialize_aws_json_1_1(
            data["JobRunState"]
        )
    if data.get("Arguments") is not None:
        import capo_glue.types.generic_map

        out["arguments"] = capo_glue.types.generic_map.deserialize_aws_json_1_1(
            data["Arguments"]
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("PredecessorRuns") is not None:
        import capo_glue.types.predecessor_list

        out["predecessor_runs"] = (
            capo_glue.types.predecessor_list.deserialize_aws_json_1_1(
                data["PredecessorRuns"]
            )
        )
    if data.get("AllocatedCapacity") is not None:
        out["allocated_capacity"] = data["AllocatedCapacity"]
    else:
        out["allocated_capacity"] = 0
    if data.get("ExecutionTime") is not None:
        out["execution_time"] = data["ExecutionTime"]
    else:
        out["execution_time"] = 0
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = float(data["MaxCapacity"])
    if data.get("WorkerType") is not None:
        import capo_glue.types.worker_type

        out["worker_type"] = capo_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    if data.get("LogGroupName") is not None:
        out["log_group_name"] = data["LogGroupName"]
    if data.get("NotificationProperty") is not None:
        import capo_glue.types.notification_property

        out["notification_property"] = (
            capo_glue.types.notification_property.deserialize_aws_json_1_1(
                data["NotificationProperty"]
            )
        )
    if data.get("GlueVersion") is not None:
        out["glue_version"] = data["GlueVersion"]
    if data.get("DPUSeconds") is not None:
        out["dpu_seconds"] = float(data["DPUSeconds"])
    if data.get("ExecutionClass") is not None:
        import capo_glue.types.execution_class

        out["execution_class"] = (
            capo_glue.types.execution_class.deserialize_aws_json_1_1(
                data["ExecutionClass"]
            )
        )
    if data.get("MaintenanceWindow") is not None:
        out["maintenance_window"] = data["MaintenanceWindow"]
    if data.get("ProfileName") is not None:
        out["profile_name"] = data["ProfileName"]
    if data.get("StateDetail") is not None:
        out["state_detail"] = data["StateDetail"]
    if data.get("ExecutionRoleSessionPolicy") is not None:
        out["execution_role_session_policy"] = data["ExecutionRoleSessionPolicy"]
    return out
