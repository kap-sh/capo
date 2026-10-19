"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.auto_remediation_attempt_seconds
    import capo_config_service.types.auto_remediation_attempts
    import capo_config_service.types.boolean
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.execution_controls
    import capo_config_service.types.remediation_parameters
    import capo_config_service.types.remediation_target_type
    import capo_config_service.types.string
    import capo_config_service.types.string_with_char_limit256
    import capo_config_service.types.string_with_char_limit1024


class RemediationConfiguration(TypedDict, closed=True):
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule.</p>"""
    target_type: (
        "capo_config_service.types.remediation_target_type.RemediationTargetType"
    )
    """<p>The type of the target. Target executes remediation. For example, SSM document.</p>"""
    target_id: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>Target ID is the name of the SSM document.</p>"""
    target_version: NotRequired["capo_config_service.types.string.String"]
    """<p>Version of the target. For example, version of the SSM document.</p> <note> <p>If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.</p> </note>"""
    parameters: NotRequired[
        "capo_config_service.types.remediation_parameters.RemediationParameters"
    ]
    """<p>An object of the RemediationParameterValue.</p>"""
    resource_type: NotRequired["capo_config_service.types.string.String"]
    """<p>The type of a resource. </p>"""
    automatic: "capo_config_service.types.boolean.Boolean"
    """<p>The remediation is triggered automatically.</p>"""
    execution_controls: NotRequired[
        "capo_config_service.types.execution_controls.ExecutionControls"
    ]
    """<p>An ExecutionControls object.</p>"""
    maximum_automatic_attempts: NotRequired[
        "capo_config_service.types.auto_remediation_attempts.AutoRemediationAttempts"
    ]
    """<p>The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.</p> <p>For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.</p>"""
    retry_attempt_seconds: NotRequired[
        "capo_config_service.types.auto_remediation_attempt_seconds.AutoRemediationAttemptSeconds"
    ]
    """<p>Time window to determine whether or not to add a remediation exception to prevent infinite remediation attempts. If <code>MaximumAutomaticAttempts</code> remediation attempts have been made under <code>RetryAttemptSeconds</code>, a remediation exception will be added to the resource. If you do not select a number, the default is 60 seconds. </p> <p>For example, if you specify <code>RetryAttemptSeconds</code> as 50 seconds and <code>MaximumAutomaticAttempts</code> as 5, Config will run auto-remediations 5 times within 50 seconds before adding a remediation exception to the resource.</p>"""
    arn: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>Amazon Resource Name (ARN) of remediation configuration.</p>"""
    created_by_service: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>Name of the service that owns the service-linked rule, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationConfiguration) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    import capo_config_service.types.remediation_target_type

    out["TargetType"] = (
        capo_config_service.types.remediation_target_type.serialize_aws_json_1_1(
            value["target_type"]
        )
    )
    out["TargetId"] = value["target_id"]
    if "target_version" in value:
        out["TargetVersion"] = value["target_version"]
    if "parameters" in value:
        import capo_config_service.types.remediation_parameters

        out["Parameters"] = (
            capo_config_service.types.remediation_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["Automatic"] = value.get("automatic", False)
    if "execution_controls" in value:
        import capo_config_service.types.execution_controls

        out["ExecutionControls"] = (
            capo_config_service.types.execution_controls.serialize_aws_json_1_1(
                value["execution_controls"]
            )
        )
    if "maximum_automatic_attempts" in value:
        out["MaximumAutomaticAttempts"] = value["maximum_automatic_attempts"]
    if "retry_attempt_seconds" in value:
        out["RetryAttemptSeconds"] = value["retry_attempt_seconds"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_by_service" in value:
        out["CreatedByService"] = value["created_by_service"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationConfiguration:
    out: RemediationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ConfigRuleName") is not None:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        out["config_rule_name"] = ""
    if data.get("TargetType") is not None:
        import capo_config_service.types.remediation_target_type

        out["target_type"] = (
            capo_config_service.types.remediation_target_type.deserialize_aws_json_1_1(
                data["TargetType"]
            )
        )
    else:
        import typing

        out["target_type"] = typing.cast(
            "capo_config_service.types.remediation_target_type.RemediationTargetType",
            "",
        )
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    else:
        out["target_id"] = ""
    if data.get("TargetVersion") is not None:
        out["target_version"] = data["TargetVersion"]
    if data.get("Parameters") is not None:
        import capo_config_service.types.remediation_parameters

        out["parameters"] = (
            capo_config_service.types.remediation_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Automatic") is not None:
        out["automatic"] = data["Automatic"]
    else:
        out["automatic"] = False
    if data.get("ExecutionControls") is not None:
        import capo_config_service.types.execution_controls

        out["execution_controls"] = (
            capo_config_service.types.execution_controls.deserialize_aws_json_1_1(
                data["ExecutionControls"]
            )
        )
    if data.get("MaximumAutomaticAttempts") is not None:
        out["maximum_automatic_attempts"] = data["MaximumAutomaticAttempts"]
    if data.get("RetryAttemptSeconds") is not None:
        out["retry_attempt_seconds"] = data["RetryAttemptSeconds"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreatedByService") is not None:
        out["created_by_service"] = data["CreatedByService"]
    return out
