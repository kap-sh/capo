"""Generated from Smithy shape ``com.amazonaws.athena#StartSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.boxed_boolean
    import capo_athena.types.description_string
    import capo_athena.types.engine_configuration
    import capo_athena.types.idempotency_token
    import capo_athena.types.monitoring_configuration
    import capo_athena.types.name_string
    import capo_athena.types.role_arn
    import capo_athena.types.session_idle_timeout_in_minutes
    import capo_athena.types.tag_list
    import capo_athena.types.work_group_name


class StartSessionRequest(TypedDict, closed=True):
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>The session description.</p>"""
    work_group: "capo_athena.types.work_group_name.WorkGroupName"
    """<p>The workgroup to which the session belongs.</p>"""
    engine_configuration: "capo_athena.types.engine_configuration.EngineConfiguration"
    """<p>Contains engine data processing unit (DPU) configuration settings and parameter mappings.</p>"""
    execution_role: NotRequired["capo_athena.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role used to access user resources for Spark sessions and Identity Center enabled workgroups. This property applies only to Spark enabled workgroups and Identity Center enabled workgroups.</p>"""
    monitoring_configuration: NotRequired[
        "capo_athena.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>Contains the configuration settings for managed log persistence, delivering logs to Amazon S3 buckets, Amazon CloudWatch log groups etc.</p>"""
    notebook_version: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>The notebook version. This value is supplied automatically for notebook sessions in the Athena console and is not required for programmatic session access. The only valid notebook version is <code>Athena notebook version 1</code>. If you specify a value for <code>NotebookVersion</code>, you must also specify a value for <code>NotebookId</code>. See <a>EngineConfiguration$AdditionalConfigs</a>.</p>"""
    session_idle_timeout_in_minutes: NotRequired[
        "capo_athena.types.session_idle_timeout_in_minutes.SessionIdleTimeoutInMinutes"
    ]
    """<p>The idle timeout in minutes for the session.</p>"""
    client_request_token: NotRequired[
        "capo_athena.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the session is idempotent (executes only once). If another <code>StartSessionRequest</code> is received, the same response is returned and another session is not created. If a parameter has changed, an error is returned.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""
    tags: NotRequired["capo_athena.types.tag_list.TagList"]
    """<p>A list of comma separated tags to add to the session that is created.</p>"""
    copy_work_group_tags: NotRequired["capo_athena.types.boxed_boolean.BoxedBoolean"]
    """<p>Copies the tags from the Workgroup to the Session when.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSessionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["WorkGroup"] = value["work_group"]
    import capo_athena.types.engine_configuration

    out["EngineConfiguration"] = (
        capo_athena.types.engine_configuration.serialize_aws_json_1_1(
            value["engine_configuration"]
        )
    )
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
    if "monitoring_configuration" in value:
        import capo_athena.types.monitoring_configuration

        out["MonitoringConfiguration"] = (
            capo_athena.types.monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "notebook_version" in value:
        out["NotebookVersion"] = value["notebook_version"]
    if "session_idle_timeout_in_minutes" in value:
        out["SessionIdleTimeoutInMinutes"] = value["session_idle_timeout_in_minutes"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_athena.types.tag_list

        out["Tags"] = capo_athena.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "copy_work_group_tags" in value:
        out["CopyWorkGroupTags"] = value["copy_work_group_tags"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSessionRequest:
    out: StartSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("WorkGroup") is not None:
        out["work_group"] = data["WorkGroup"]
    else:
        out["work_group"] = ""
    if data.get("EngineConfiguration") is not None:
        import capo_athena.types.engine_configuration

        out["engine_configuration"] = (
            capo_athena.types.engine_configuration.deserialize_aws_json_1_1(
                data["EngineConfiguration"]
            )
        )
    else:
        raise DeserializationError("StartSessionRequest.engine_configuration required")
    if data.get("ExecutionRole") is not None:
        out["execution_role"] = data["ExecutionRole"]
    if data.get("MonitoringConfiguration") is not None:
        import capo_athena.types.monitoring_configuration

        out["monitoring_configuration"] = (
            capo_athena.types.monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if data.get("NotebookVersion") is not None:
        out["notebook_version"] = data["NotebookVersion"]
    if data.get("SessionIdleTimeoutInMinutes") is not None:
        out["session_idle_timeout_in_minutes"] = data["SessionIdleTimeoutInMinutes"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_athena.types.tag_list

        out["tags"] = capo_athena.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("CopyWorkGroupTags") is not None:
        out["copy_work_group_tags"] = data["CopyWorkGroupTags"]
    return out
