"""Generated from Smithy shape ``com.amazonaws.emr#NotebookExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.date
    import capo_emr.types.environment_variables_map
    import capo_emr.types.execution_engine_config
    import capo_emr.types.notebook_execution_status
    import capo_emr.types.notebook_s3_location_for_output
    import capo_emr.types.output_notebook_format
    import capo_emr.types.output_notebook_s3_location_for_output
    import capo_emr.types.tag_list
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_max_len256


class NotebookExecution(TypedDict, closed=True):
    notebook_execution_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The unique identifier of a notebook execution.</p>"""
    editor_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The unique identifier of the Amazon EMR Notebook that is used for the notebook execution.</p>"""
    execution_engine: NotRequired[
        "capo_emr.types.execution_engine_config.ExecutionEngineConfig"
    ]
    """<p>The execution engine, such as an Amazon EMR cluster, used to run the Amazon EMR notebook and perform the notebook execution.</p>"""
    notebook_execution_name: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>A name for the notebook execution.</p>"""
    notebook_params: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>Input parameters in JSON format passed to the Amazon EMR Notebook at runtime for execution.</p>"""
    status: NotRequired[
        "capo_emr.types.notebook_execution_status.NotebookExecutionStatus"
    ]
    """<p>The status of the notebook execution.</p> <ul> <li> <p> <code>START_PENDING</code> indicates that the cluster has received the execution request but execution has not begun.</p> </li> <li> <p> <code>STARTING</code> indicates that the execution is starting on the cluster.</p> </li> <li> <p> <code>RUNNING</code> indicates that the execution is being processed by the cluster.</p> </li> <li> <p> <code>FINISHING</code> indicates that execution processing is in the final stages.</p> </li> <li> <p> <code>FINISHED</code> indicates that the execution has completed without error.</p> </li> <li> <p> <code>FAILING</code> indicates that the execution is failing and will not finish successfully.</p> </li> <li> <p> <code>FAILED</code> indicates that the execution failed.</p> </li> <li> <p> <code>STOP_PENDING</code> indicates that the cluster has received a <code>StopNotebookExecution</code> request and the stop is pending.</p> </li> <li> <p> <code>STOPPING</code> indicates that the cluster is in the process of stopping the execution as a result of a <code>StopNotebookExecution</code> request.</p> </li> <li> <p> <code>STOPPED</code> indicates that the execution stopped because of a <code>StopNotebookExecution</code> request.</p> </li> </ul>"""
    start_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The timestamp when notebook execution started.</p>"""
    end_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The timestamp when notebook execution ended.</p>"""
    arn: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The Amazon Resource Name (ARN) of the notebook execution.</p>"""
    output_notebook_uri: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The location of the notebook execution's output file in Amazon S3.</p>"""
    last_state_change_reason: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The reason for the latest status change of the notebook execution.</p>"""
    notebook_instance_security_group_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The unique identifier of the Amazon EC2 security group associated with the Amazon EMR Notebook instance. For more information see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html">Specifying Amazon EC2 Security Groups for Amazon EMR Notebooks</a> in the <i>Amazon EMR Management Guide</i>.</p>"""
    tags: NotRequired["capo_emr.types.tag_list.TagList"]
    """<p>A list of tags associated with a notebook execution. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters and an optional value string with a maximum of 256 characters.</p>"""
    notebook_s3_location: NotRequired[
        "capo_emr.types.notebook_s3_location_for_output.NotebookS3LocationForOutput"
    ]
    """<p>The Amazon S3 location that stores the notebook execution input.</p>"""
    output_notebook_s3_location: NotRequired[
        "capo_emr.types.output_notebook_s3_location_for_output.OutputNotebookS3LocationForOutput"
    ]
    """<p>The Amazon S3 location for the notebook execution output.</p>"""
    output_notebook_format: NotRequired[
        "capo_emr.types.output_notebook_format.OutputNotebookFormat"
    ]
    """<p>The output format for the notebook execution.</p>"""
    environment_variables: NotRequired[
        "capo_emr.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>The environment variables associated with the notebook execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookExecution) -> dict:
    out: dict = {}
    if "notebook_execution_id" in value:
        out["NotebookExecutionId"] = value["notebook_execution_id"]
    if "editor_id" in value:
        out["EditorId"] = value["editor_id"]
    if "execution_engine" in value:
        import capo_emr.types.execution_engine_config

        out["ExecutionEngine"] = (
            capo_emr.types.execution_engine_config.serialize_aws_json_1_1(
                value["execution_engine"]
            )
        )
    if "notebook_execution_name" in value:
        out["NotebookExecutionName"] = value["notebook_execution_name"]
    if "notebook_params" in value:
        out["NotebookParams"] = value["notebook_params"]
    if "status" in value:
        import capo_emr.types.notebook_execution_status

        out["Status"] = capo_emr.types.notebook_execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "start_time" in value:
        import capo_emr.types.date

        out["StartTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_emr.types.date

        out["EndTime"] = capo_emr.types.date.serialize_aws_json_1_1(value["end_time"])
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "output_notebook_uri" in value:
        out["OutputNotebookURI"] = value["output_notebook_uri"]
    if "last_state_change_reason" in value:
        out["LastStateChangeReason"] = value["last_state_change_reason"]
    if "notebook_instance_security_group_id" in value:
        out["NotebookInstanceSecurityGroupId"] = value[
            "notebook_instance_security_group_id"
        ]
    if "tags" in value:
        import capo_emr.types.tag_list

        out["Tags"] = capo_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "notebook_s3_location" in value:
        import capo_emr.types.notebook_s3_location_for_output

        out["NotebookS3Location"] = (
            capo_emr.types.notebook_s3_location_for_output.serialize_aws_json_1_1(
                value["notebook_s3_location"]
            )
        )
    if "output_notebook_s3_location" in value:
        import capo_emr.types.output_notebook_s3_location_for_output

        out["OutputNotebookS3Location"] = (
            capo_emr.types.output_notebook_s3_location_for_output.serialize_aws_json_1_1(
                value["output_notebook_s3_location"]
            )
        )
    if "output_notebook_format" in value:
        import capo_emr.types.output_notebook_format

        out["OutputNotebookFormat"] = (
            capo_emr.types.output_notebook_format.serialize_aws_json_1_1(
                value["output_notebook_format"]
            )
        )
    if "environment_variables" in value:
        import capo_emr.types.environment_variables_map

        out["EnvironmentVariables"] = (
            capo_emr.types.environment_variables_map.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookExecution:
    out: NotebookExecution = {}  # type: ignore[typeddict-item]
    if data.get("NotebookExecutionId") is not None:
        out["notebook_execution_id"] = data["NotebookExecutionId"]
    if data.get("EditorId") is not None:
        out["editor_id"] = data["EditorId"]
    if data.get("ExecutionEngine") is not None:
        import capo_emr.types.execution_engine_config

        out["execution_engine"] = (
            capo_emr.types.execution_engine_config.deserialize_aws_json_1_1(
                data["ExecutionEngine"]
            )
        )
    if data.get("NotebookExecutionName") is not None:
        out["notebook_execution_name"] = data["NotebookExecutionName"]
    if data.get("NotebookParams") is not None:
        out["notebook_params"] = data["NotebookParams"]
    if data.get("Status") is not None:
        import capo_emr.types.notebook_execution_status

        out["status"] = (
            capo_emr.types.notebook_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_emr.types.date

        out["start_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_emr.types.date

        out["end_time"] = capo_emr.types.date.deserialize_aws_json_1_1(data["EndTime"])
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("OutputNotebookURI") is not None:
        out["output_notebook_uri"] = data["OutputNotebookURI"]
    if data.get("LastStateChangeReason") is not None:
        out["last_state_change_reason"] = data["LastStateChangeReason"]
    if data.get("NotebookInstanceSecurityGroupId") is not None:
        out["notebook_instance_security_group_id"] = data[
            "NotebookInstanceSecurityGroupId"
        ]
    if data.get("Tags") is not None:
        import capo_emr.types.tag_list

        out["tags"] = capo_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("NotebookS3Location") is not None:
        import capo_emr.types.notebook_s3_location_for_output

        out["notebook_s3_location"] = (
            capo_emr.types.notebook_s3_location_for_output.deserialize_aws_json_1_1(
                data["NotebookS3Location"]
            )
        )
    if data.get("OutputNotebookS3Location") is not None:
        import capo_emr.types.output_notebook_s3_location_for_output

        out["output_notebook_s3_location"] = (
            capo_emr.types.output_notebook_s3_location_for_output.deserialize_aws_json_1_1(
                data["OutputNotebookS3Location"]
            )
        )
    if data.get("OutputNotebookFormat") is not None:
        import capo_emr.types.output_notebook_format

        out["output_notebook_format"] = (
            capo_emr.types.output_notebook_format.deserialize_aws_json_1_1(
                data["OutputNotebookFormat"]
            )
        )
    if data.get("EnvironmentVariables") is not None:
        import capo_emr.types.environment_variables_map

        out["environment_variables"] = (
            capo_emr.types.environment_variables_map.deserialize_aws_json_1_1(
                data["EnvironmentVariables"]
            )
        )
    return out
