"""Generated from Smithy shape ``com.amazonaws.glue#StartJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.execution_class
    import capo_glue.types.generic_map
    import capo_glue.types.id_string
    import capo_glue.types.integer_value
    import capo_glue.types.name_string
    import capo_glue.types.notification_property
    import capo_glue.types.nullable_boolean
    import capo_glue.types.nullable_double
    import capo_glue.types.nullable_integer
    import capo_glue.types.orchestration_policy_json_string
    import capo_glue.types.timeout
    import capo_glue.types.worker_type


class StartJobRunRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the job definition to use.</p>"""
    job_run_queuing_enabled: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether job run queuing is enabled for the job run.</p> <p>A value of true means job run queuing is enabled for the job run. If false or not populated, the job run will not be considered for queueing.</p>"""
    job_run_id: NotRequired["capo_glue.types.id_string.IdString"]
    """<p>The ID of a previous <code>JobRun</code> to retry.</p>"""
    arguments: NotRequired["capo_glue.types.generic_map.GenericMap"]
    """<p>The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.</p> <p>You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.</p> <p>Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Secrets Manager or other secret management mechanism if you intend to keep them within the Job. </p> <p>For information about how to specify and consume your own Job arguments, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html">Calling Glue APIs in Python</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Spark jobs, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html">Special Parameters Used by Glue</a> topic in the developer guide.</p> <p>For information about the arguments you can provide to this field when configuring Ray jobs, see <a href="https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html">Using job parameters in Ray jobs</a> in the developer guide.</p>"""
    allocated_capacity: "capo_glue.types.integer_value.IntegerValue"
    """<p>This field is deprecated. Use <code>MaxCapacity</code> instead.</p> <p>The number of Glue data processing units (DPUs) to allocate to this JobRun. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href="https://aws.amazon.com/glue/pricing/">Glue pricing page</a>.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The <code>JobRun</code> timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. This value overrides the timeout value set in the parent job. </p> <p>Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.</p> <p>When the value is left blank, the timeout is defaulted to 2,880 minutes for Glue version 4.0 and earlier, or 480 minutes for Glue version 5.0 and later.</p> <p>Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.</p> <p>For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.</p>"""
    max_capacity: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the <a href="https://aws.amazon.com/glue/pricing/"> Glue pricing page</a>.</p> <p>For Glue version 2.0+ jobs, you cannot specify a <code>Maximum capacity</code>. Instead, you should specify a <code>Worker type</code> and the <code>Number of workers</code>.</p> <p>Do not set <code>MaxCapacity</code> if using <code>WorkerType</code> and <code>NumberOfWorkers</code>.</p> <p>The value that can be allocated for <code>MaxCapacity</code> depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:</p> <ul> <li> <p>When you specify a Python shell job (<code>JobCommand.Name</code>="pythonshell"), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.</p> </li> <li> <p>When you specify an Apache Spark ETL job (<code>JobCommand.Name</code>="glueetl") or Apache Spark streaming ETL job (<code>JobCommand.Name</code>="gluestreaming"), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.</p> </li> </ul>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the <code>SecurityConfiguration</code> structure to be used with this job run.</p>"""
    notification_property: NotRequired[
        "capo_glue.types.notification_property.NotificationProperty"
    ]
    """<p>Specifies configuration properties of a job run notification.</p>"""
    worker_type: NotRequired["capo_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.</p> <ul> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.4X</code> worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).</p> </li> <li> <p>For the <code>G.8X</code> worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the <code>G.4X</code> worker type.</p> </li> <li> <p>For the <code>G.025X</code> worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for Glue version 3.0 or later streaming jobs.</p> </li> <li> <p>For the <code>Z.2X</code> worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.</p> </li> </ul>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of workers of a defined <code>workerType</code> that are allocated when a job runs.</p>"""
    execution_class: NotRequired["capo_glue.types.execution_class.ExecutionClass"]
    """<p>Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.</p> <p>The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary. </p> <p>Only jobs with Glue version 3.0 and above and command type <code>glueetl</code> will be allowed to set <code>ExecutionClass</code> to <code>FLEX</code>. The flexible execution class is available for Spark jobs.</p>"""
    execution_role_session_policy: NotRequired[
        "capo_glue.types.orchestration_policy_json_string.OrchestrationPolicyJsonString"
    ]
    """<p>This inline session policy to the StartJobRun API allows you to dynamically restrict the permissions of the specified execution role for the scope of the job, without requiring the creation of additional IAM roles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartJobRunRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    if "job_run_queuing_enabled" in value:
        out["JobRunQueuingEnabled"] = value["job_run_queuing_enabled"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "arguments" in value:
        import capo_glue.types.generic_map

        out["Arguments"] = capo_glue.types.generic_map.serialize_aws_json_1_1(
            value["arguments"]
        )
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
    if "notification_property" in value:
        import capo_glue.types.notification_property

        out["NotificationProperty"] = (
            capo_glue.types.notification_property.serialize_aws_json_1_1(
                value["notification_property"]
            )
        )
    if "worker_type" in value:
        import capo_glue.types.worker_type

        out["WorkerType"] = capo_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "execution_class" in value:
        import capo_glue.types.execution_class

        out["ExecutionClass"] = capo_glue.types.execution_class.serialize_aws_json_1_1(
            value["execution_class"]
        )
    if "execution_role_session_policy" in value:
        out["ExecutionRoleSessionPolicy"] = value["execution_role_session_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartJobRunRequest:
    out: StartJobRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("StartJobRunRequest.job_name required")
    if data.get("JobRunQueuingEnabled") is not None:
        out["job_run_queuing_enabled"] = data["JobRunQueuingEnabled"]
    if data.get("JobRunId") is not None:
        out["job_run_id"] = data["JobRunId"]
    if data.get("Arguments") is not None:
        import capo_glue.types.generic_map

        out["arguments"] = capo_glue.types.generic_map.deserialize_aws_json_1_1(
            data["Arguments"]
        )
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
    if data.get("NotificationProperty") is not None:
        import capo_glue.types.notification_property

        out["notification_property"] = (
            capo_glue.types.notification_property.deserialize_aws_json_1_1(
                data["NotificationProperty"]
            )
        )
    if data.get("WorkerType") is not None:
        import capo_glue.types.worker_type

        out["worker_type"] = capo_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("ExecutionClass") is not None:
        import capo_glue.types.execution_class

        out["execution_class"] = (
            capo_glue.types.execution_class.deserialize_aws_json_1_1(
                data["ExecutionClass"]
            )
        )
    if data.get("ExecutionRoleSessionPolicy") is not None:
        out["execution_role_session_policy"] = data["ExecutionRoleSessionPolicy"]
    return out
