"""Generated from Smithy shape ``com.amazonaws.glue#Session``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connections_list
    import capo_glue.types.description_string
    import capo_glue.types.double_value
    import capo_glue.types.glue_version_string
    import capo_glue.types.idle_timeout
    import capo_glue.types.name_string
    import capo_glue.types.nullable_double
    import capo_glue.types.nullable_integer
    import capo_glue.types.orchestration_arguments_map
    import capo_glue.types.orchestration_role_arn
    import capo_glue.types.session_command
    import capo_glue.types.session_status
    import capo_glue.types.session_type
    import capo_glue.types.timestamp_value
    import capo_glue.types.worker_type


class Session(TypedDict, closed=True):
    id: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The ID of the session.</p>"""
    created_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The time and date when the session was created.</p>"""
    status: NotRequired["capo_glue.types.session_status.SessionStatus"]
    """<p>The session status. </p>"""
    error_message: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The error message displayed during the session.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The description of the session.</p>"""
    role: NotRequired["capo_glue.types.orchestration_role_arn.OrchestrationRoleArn"]
    """<p>The name or Amazon Resource Name (ARN) of the IAM role associated with the Session.</p>"""
    command: NotRequired["capo_glue.types.session_command.SessionCommand"]
    """<p>The command object.See SessionCommand.</p>"""
    default_arguments: NotRequired[
        "capo_glue.types.orchestration_arguments_map.OrchestrationArgumentsMap"
    ]
    """<p>A map array of key-value pairs. Max is 75 pairs. </p>"""
    connections: NotRequired["capo_glue.types.connections_list.ConnectionsList"]
    """<p>The number of connections used for the session.</p>"""
    progress: "capo_glue.types.double_value.DoubleValue"
    """<p>The code execution progress of the session.</p>"""
    max_capacity: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The number of Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory. </p>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the SecurityConfiguration structure to be used with the session.</p>"""
    glue_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<p>The Glue version determines the versions of Apache Spark and Python that Glue supports. The GlueVersion must be greater than 2.0.</p>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of workers of a defined <code>WorkerType</code> to use for the session.</p>"""
    worker_type: NotRequired["capo_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated when a session runs. Accepts a value of <code>G.1X</code>, <code>G.2X</code>, <code>G.4X</code>, <code>G.8X</code>, <code>G.12X</code>, <code>G.16X</code>, <code>R.1X</code>, <code>R.2X</code>, <code>R.4X</code>, or <code>R.8X</code> for Spark sessions. Accepts the value <code>Z.2X</code> for Ray sessions.</p> <p>The <code>G.12X</code>, <code>G.16X</code>, and <code>R.1X</code> through <code>R.8X</code> worker types are available only for Glue version 4.0 or later Spark ETL jobs in select Amazon Web Services Regions. For the supported Regions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Configuring job properties for Spark jobs</a> in the developer guide.</p>"""
    completed_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time that this session is completed.</p>"""
    execution_time: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The total time the session ran for.</p>"""
    dpu_seconds: NotRequired["capo_glue.types.nullable_double.NullableDouble"]
    """<p>The DPUs consumed by the session (formula: ExecutionTime * MaxCapacity).</p>"""
    idle_timeout: NotRequired["capo_glue.types.idle_timeout.IdleTimeout"]
    """<p>The number of minutes when idle before the session times out.</p>"""
    profile_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of an Glue usage profile associated with the session.</p>"""
    session_type: NotRequired["capo_glue.types.session_type.SessionType"]
    """<p>The type of the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "created_on" in value:
        import capo_glue.types.timestamp_value

        out["CreatedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "status" in value:
        import capo_glue.types.session_status

        out["Status"] = capo_glue.types.session_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role" in value:
        out["Role"] = value["role"]
    if "command" in value:
        import capo_glue.types.session_command

        out["Command"] = capo_glue.types.session_command.serialize_aws_json_1_1(
            value["command"]
        )
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
    out["Progress"] = (
        "NaN"
        if value.get("progress", 0) != value.get("progress", 0)
        else "Infinity"
        if value.get("progress", 0) == float("inf")
        else "-Infinity"
        if value.get("progress", 0) == float("-inf")
        else value.get("progress", 0)
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
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "worker_type" in value:
        import capo_glue.types.worker_type

        out["WorkerType"] = capo_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "completed_on" in value:
        import capo_glue.types.timestamp_value

        out["CompletedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "execution_time" in value:
        out["ExecutionTime"] = (
            "NaN"
            if value["execution_time"] != value["execution_time"]
            else "Infinity"
            if value["execution_time"] == float("inf")
            else "-Infinity"
            if value["execution_time"] == float("-inf")
            else value["execution_time"]
        )
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
    if "idle_timeout" in value:
        out["IdleTimeout"] = value["idle_timeout"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "session_type" in value:
        import capo_glue.types.session_type

        out["SessionType"] = capo_glue.types.session_type.serialize_aws_json_1_1(
            value["session_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("CreatedOn") is not None:
        import capo_glue.types.timestamp_value

        out["created_on"] = capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["CreatedOn"]
        )
    if data.get("Status") is not None:
        import capo_glue.types.session_status

        out["status"] = capo_glue.types.session_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    if data.get("Command") is not None:
        import capo_glue.types.session_command

        out["command"] = capo_glue.types.session_command.deserialize_aws_json_1_1(
            data["Command"]
        )
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
    if data.get("Progress") is not None:
        out["progress"] = float(data["Progress"])
    else:
        out["progress"] = 0
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = float(data["MaxCapacity"])
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    if data.get("GlueVersion") is not None:
        out["glue_version"] = data["GlueVersion"]
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("WorkerType") is not None:
        import capo_glue.types.worker_type

        out["worker_type"] = capo_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if data.get("CompletedOn") is not None:
        import capo_glue.types.timestamp_value

        out["completed_on"] = capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if data.get("ExecutionTime") is not None:
        out["execution_time"] = float(data["ExecutionTime"])
    if data.get("DPUSeconds") is not None:
        out["dpu_seconds"] = float(data["DPUSeconds"])
    if data.get("IdleTimeout") is not None:
        out["idle_timeout"] = data["IdleTimeout"]
    if data.get("ProfileName") is not None:
        out["profile_name"] = data["ProfileName"]
    if data.get("SessionType") is not None:
        import capo_glue.types.session_type

        out["session_type"] = capo_glue.types.session_type.deserialize_aws_json_1_1(
            data["SessionType"]
        )
    return out
