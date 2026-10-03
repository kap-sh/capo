"""Generated from Smithy shape ``com.amazonaws.ssm#StartAutomationExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.automation_parameter_key
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.automation_targets
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_version
    import capo_ssm.types.execution_mode
    import capo_ssm.types.idempotency_token
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.tag_list
    import capo_ssm.types.target_locations
    import capo_ssm.types.target_locations_url
    import capo_ssm.types.target_maps


class StartAutomationExecutionRequest(TypedDict, closed=True):
    document_name: "capo_ssm.types.document_arn.DocumentARN"
    """<p>The name of the SSM document to run. This can be a public document or a custom document. To run a shared document belonging to another account, specify the document ARN. For more information about how to use shared documents, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html">Sharing SSM documents</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the Automation runbook to use for this execution.</p>"""
    parameters: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>A key-value map of execution parameters, which match the declared parameters in the Automation runbook.</p>"""
    client_token: NotRequired["capo_ssm.types.idempotency_token.IdempotencyToken"]
    """<p>User-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can't be reused.</p>"""
    mode: NotRequired["capo_ssm.types.execution_mode.ExecutionMode"]
    """<p>The execution mode of the automation. Valid modes include the following: Auto and Interactive. The default mode is Auto.</p>"""
    target_parameter_name: NotRequired[
        "capo_ssm.types.automation_parameter_key.AutomationParameterKey"
    ]
    """<p>The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify targets.</p>"""
    targets: NotRequired["capo_ssm.types.automation_targets.AutomationTargets"]
    """<p>A key-value mapping to target resources. Required if you specify TargetParameterName.</p> <p>If both this parameter and the <code>TargetLocation:Targets</code> parameter are supplied, <code>TargetLocation:Targets</code> takes precedence.</p>"""
    target_maps: NotRequired["capo_ssm.types.target_maps.TargetMaps"]
    """<p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The maximum number of targets allowed to run this task in parallel. You can specify a number, such as 10, or a percentage, such as 10%. The default value is <code>10</code>.</p> <p>If both this parameter and the <code>TargetLocation:TargetsMaxConcurrency</code> are supplied, <code>TargetLocation:TargetsMaxConcurrency</code> takes precedence.</p>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The number of errors that are allowed before the system stops running the automation on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops running the automation when the fourth error is received. If you specify 0, then the system stops running the automation on additional targets after the first error result is returned. If you run an automation on 50 resources and set max-errors to 10%, then the system stops running the automation on additional targets when the sixth error is received.</p> <p>Executions that are already running an automation when max-errors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set max-concurrency to 1 so the executions proceed one at a time.</p> <p>If this parameter and the <code>TargetLocation:TargetsMaxErrors</code> parameter are both supplied, <code>TargetLocation:TargetsMaxErrors</code> takes precedence.</p>"""
    target_locations: NotRequired["capo_ssm.types.target_locations.TargetLocations"]
    """<p>A location is a combination of Amazon Web Services Regions and/or Amazon Web Services accounts where you want to run the automation. Use this operation to start an automation in multiple Amazon Web Services Regions and multiple Amazon Web Services accounts. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation-multiple-accounts-and-regions.html">Running automations in multiple Amazon Web Services Regions and accounts</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>Optional metadata that you assign to a resource. You can specify a maximum of five tags for an automation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an automation to identify an environment or operating system. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=environment,Value=test</code> </p> </li> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> </ul> <note> <p>The <code>Array Members</code> maximum value is reported as 1000. This number includes capacity reserved for internal operations. When calling the <code>StartAutomationExecution</code> action, you can specify a maximum of 5 tags. You can, however, use the <a>AddTagsToResource</a> action to add up to a total of 50 tags to an existing automation configuration.</p> </note>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The CloudWatch alarm you want to apply to your automation.</p>"""
    target_locations_url: NotRequired[
        "capo_ssm.types.target_locations_url.TargetLocationsURL"
    ]
    """<p>Specify a publicly accessible URL for a file that contains the <code>TargetLocations</code> body. Currently, only files in presigned Amazon S3 buckets are supported. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAutomationExecutionRequest) -> dict:
    out: dict = {}
    out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "parameters" in value:
        import capo_ssm.types.automation_parameter_map

        out["Parameters"] = (
            capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "mode" in value:
        import capo_ssm.types.execution_mode

        out["Mode"] = capo_ssm.types.execution_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    if "target_parameter_name" in value:
        out["TargetParameterName"] = value["target_parameter_name"]
    if "targets" in value:
        import capo_ssm.types.automation_targets

        out["Targets"] = capo_ssm.types.automation_targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "target_maps" in value:
        import capo_ssm.types.target_maps

        out["TargetMaps"] = capo_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "target_locations" in value:
        import capo_ssm.types.target_locations

        out["TargetLocations"] = capo_ssm.types.target_locations.serialize_aws_json_1_1(
            value["target_locations"]
        )
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "target_locations_url" in value:
        out["TargetLocationsURL"] = value["target_locations_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAutomationExecutionRequest:
    out: StartAutomationExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    else:
        raise DeserializationError(
            "StartAutomationExecutionRequest.document_name required"
        )
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Parameters") is not None:
        import capo_ssm.types.automation_parameter_map

        out["parameters"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Mode") is not None:
        import capo_ssm.types.execution_mode

        out["mode"] = capo_ssm.types.execution_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    if data.get("TargetParameterName") is not None:
        out["target_parameter_name"] = data["TargetParameterName"]
    if data.get("Targets") is not None:
        import capo_ssm.types.automation_targets

        out["targets"] = capo_ssm.types.automation_targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("TargetMaps") is not None:
        import capo_ssm.types.target_maps

        out["target_maps"] = capo_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("MaxErrors") is not None:
        out["max_errors"] = data["MaxErrors"]
    if data.get("TargetLocations") is not None:
        import capo_ssm.types.target_locations

        out["target_locations"] = (
            capo_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("AlarmConfiguration") is not None:
        import capo_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if data.get("TargetLocationsURL") is not None:
        out["target_locations_url"] = data["TargetLocationsURL"]
    return out
