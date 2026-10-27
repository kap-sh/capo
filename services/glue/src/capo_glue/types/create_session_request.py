"""Generated from Smithy shape ``com.amazonaws.glue#CreateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.connections_list
    import capo_glue.types.description_string
    import capo_glue.types.glue_version_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_double
    import capo_glue.types.nullable_integer
    import capo_glue.types.orchestration_arguments_map
    import capo_glue.types.orchestration_name_string
    import capo_glue.types.orchestration_role_arn
    import capo_glue.types.session_command
    import capo_glue.types.session_type
    import capo_glue.types.tags_map
    import capo_glue.types.timeout
    import capo_glue.types.worker_type


class CreateSessionRequest(TypedDict, closed=True):
    id: "capo_glue.types.name_string.NameString"
    """<p>The ID of the session request. </p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The description of the session. </p>"""
    role: "capo_glue.types.orchestration_role_arn.OrchestrationRoleArn"
    """<p>The IAM Role ARN </p>"""
    command: "capo_glue.types.session_command.SessionCommand"
    """<p>The <code>SessionCommand</code> that runs the job. </p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p> The number of minutes before session times out. Default for Spark ETL jobs is 48 hours (2880 minutes). Consult the documentation for other job types. </p>"""
    idle_timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p> The number of minutes when idle before session times out. Default for Spark ETL jobs is value of Timeout. Consult the documentation for other job types. </p>"""
    default_arguments: NotRequired[
        "capo_glue.types.orchestration_arguments_map.OrchestrationArgumentsMap"
    ]
    """<p>A map array of key-value pairs. Max is 75 pairs. </p>"""
    connections: NotRequired["capo_glue.types.connections_list.ConnectionsList"]
    """<p>The number of connections to use for the session. </p>"""
    max_capacity: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The number of Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory. </p>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of workers of a defined <code>WorkerType</code> to use for the session. </p>"""
    worker_type: NotRequired["capo_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X, G.12X, G.16X, R.1X, R.2X, R.4X, or R.8X for Spark jobs. Accepts the value Z.2X for Ray notebooks.</p> <ul> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.</p> </li> <li> <p>For the <code>G.4X</code> worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p> </li> <li> <p>For the <code>G.8X</code> worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p> </li> <li> <p>For the <code>G.12X</code> worker type, each worker maps to 12 DPU (48 vCPUs, 192 GB of memory) with 768GB disk, and provides 1 executor per worker. We recommend this worker type for jobs with very large workloads. This worker type is available only for Glue version 4.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p> </li> <li> <p>For the <code>G.16X</code> worker type, each worker maps to 16 DPU (64 vCPUs, 256 GB of memory) with 1024GB disk, and provides 1 executor per worker. We recommend this worker type for jobs with very large workloads. This worker type is available only for Glue version 4.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p> </li> <li> <p>For the <code>R.1X</code> worker type, each worker maps to 1 M-DPU (4 vCPUs, 32 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for memory-intensive workloads. This worker type is available only for Glue version 4.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p> </li> <li> <p>For the <code>R.2X</code> worker type, each worker maps to 2 M-DPU (8 vCPUs, 64 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for memory-intensive workloads. This worker type is available only for Glue version 4.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p> </li> <li> <p>For the <code>R.4X</code> worker type, each worker maps to 4 M-DPU (16 vCPUs, 128 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for memory-intensive workloads. This worker type is available only for Glue version 4.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p> </li> <li> <p>For the <code>R.8X</code> worker type, each worker maps to 8 M-DPU (32 vCPUs, 256 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for memory-intensive workloads. This worker type is available only for Glue version 4.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p> </li> <li> <p>For the <code>Z.2X</code> worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.</p> </li> </ul>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the SecurityConfiguration structure to be used with the session </p>"""
    glue_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<p>The Glue version determines the versions of Apache Spark and Python that Glue supports. The GlueVersion must be greater than 2.0. </p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>The map of key value pairs (tags) belonging to the session.</p>"""
    request_origin: NotRequired[
        "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request. </p>"""
    session_type: NotRequired["capo_glue.types.session_type.SessionType"]
    """<p>The type of session to create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSessionRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Role"] = value["role"]
    import capo_glue.types.session_command

    out["Command"] = capo_glue.types.session_command.serialize_aws_json_1_1(
        value["command"]
    )
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "idle_timeout" in value:
        out["IdleTimeout"] = value["idle_timeout"]
    if "default_arguments" in value:
        import capo_glue.types.orchestration_arguments_map

        out["DefaultArguments"] = (
            capo_glue.types.orchestration_arguments_map.serialize_aws_json_1_1(
                value["default_arguments"]
            )
        )
    if "connections" in value:
        import capo_glue.types.connections_list

        out["Connections"] = capo_glue.types.connections_list.serialize_aws_json_1_1(
            value["connections"]
        )
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
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "worker_type" in value:
        import capo_glue.types.worker_type

        out["WorkerType"] = capo_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    if "session_type" in value:
        import capo_glue.types.session_type

        out["SessionType"] = capo_glue.types.session_type.serialize_aws_json_1_1(
            value["session_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSessionRequest:
    out: CreateSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        out["role"] = ""
    if data.get("Command") is not None:
        import capo_glue.types.session_command

        out["command"] = capo_glue.types.session_command.deserialize_aws_json_1_1(
            data["Command"]
        )
    else:
        raise DeserializationError("CreateSessionRequest.command required")
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("IdleTimeout") is not None:
        out["idle_timeout"] = data["IdleTimeout"]
    if data.get("DefaultArguments") is not None:
        import capo_glue.types.orchestration_arguments_map

        out["default_arguments"] = (
            capo_glue.types.orchestration_arguments_map.deserialize_aws_json_1_1(
                data["DefaultArguments"]
            )
        )
    if data.get("Connections") is not None:
        import capo_glue.types.connections_list

        out["connections"] = capo_glue.types.connections_list.deserialize_aws_json_1_1(
            data["Connections"]
        )
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = float(data["MaxCapacity"])
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("WorkerType") is not None:
        import capo_glue.types.worker_type

        out["worker_type"] = capo_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    if data.get("GlueVersion") is not None:
        out["glue_version"] = data["GlueVersion"]
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("RequestOrigin") is not None:
        out["request_origin"] = data["RequestOrigin"]
    if data.get("SessionType") is not None:
        import capo_glue.types.session_type

        out["session_type"] = capo_glue.types.session_type.deserialize_aws_json_1_1(
            data["SessionType"]
        )
    return out
