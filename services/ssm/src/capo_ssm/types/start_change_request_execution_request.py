"""Generated from Smithy shape ``com.amazonaws.ssm#StartChangeRequestExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.boolean
    import capo_ssm.types.change_details_value
    import capo_ssm.types.change_request_name
    import capo_ssm.types.date_time
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_version
    import capo_ssm.types.idempotency_token
    import capo_ssm.types.runbooks
    import capo_ssm.types.tag_list


class StartChangeRequestExecutionRequest(TypedDict, closed=True):
    scheduled_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time specified in the change request to run the Automation runbooks.</p> <note> <p>The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.</p> </note>"""
    document_name: "capo_ssm.types.document_arn.DocumentARN"
    """<p>The name of the change template document to run during the runbook workflow.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the change template document to run during the runbook workflow.</p>"""
    parameters: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>A key-value map of parameters that match the declared parameters in the change template document.</p>"""
    change_request_name: NotRequired[
        "capo_ssm.types.change_request_name.ChangeRequestName"
    ]
    """<p>The name of the change request associated with the runbook workflow to be run.</p>"""
    client_token: NotRequired["capo_ssm.types.idempotency_token.IdempotencyToken"]
    """<p>The user-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can't be reused.</p>"""
    auto_approve: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Indicates whether the change request can be approved automatically without the need for manual approvals.</p> <p>If <code>AutoApprovable</code> is enabled in a change template, then setting <code>AutoApprove</code> to <code>true</code> in <code>StartChangeRequestExecution</code> creates a change request that bypasses approver review.</p> <note> <p>Change Calendar restrictions are not bypassed in this scenario. If the state of an associated calendar is <code>CLOSED</code>, change freeze approvers must still grant permission for this change request to run. If they don't, the change won't be processed until the calendar state is again <code>OPEN</code>. </p> </note>"""
    runbooks: "capo_ssm.types.runbooks.Runbooks"
    """<p>Information about the Automation runbooks that are run during the runbook workflow.</p> <note> <p>The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.</p> </note>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>Optional metadata that you assign to a resource. You can specify a maximum of five tags for a change request. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a change request to identify an environment or target Amazon Web Services Region. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> <li> <p> <code>Key=Region,Value=us-east-2</code> </p> </li> </ul> <note> <p>The <code>Array Members</code> maximum value is reported as 1000. This number includes capacity reserved for internal operations. When calling the <code>StartChangeRequestExecution</code> action, you can specify a maximum of 5 tags. You can, however, use the <a>AddTagsToResource</a> action to add up to a total of 50 tags to an existing change request configuration.</p> </note>"""
    scheduled_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time that the requester expects the runbook workflow related to the change request to complete. The time is an estimate only that the requester provides for reviewers.</p>"""
    change_details: NotRequired[
        "capo_ssm.types.change_details_value.ChangeDetailsValue"
    ]
    """<p>User-provided details about the change. If no details are provided, content specified in the <b>Template information</b> section of the associated change template is added.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartChangeRequestExecutionRequest) -> dict:
    out: dict = {}
    if "scheduled_time" in value:
        import capo_ssm.types.date_time

        out["ScheduledTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["scheduled_time"]
        )
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
    if "change_request_name" in value:
        out["ChangeRequestName"] = value["change_request_name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "auto_approve" in value:
        out["AutoApprove"] = value["auto_approve"]
    import capo_ssm.types.runbooks

    out["Runbooks"] = capo_ssm.types.runbooks.serialize_aws_json_1_1(value["runbooks"])
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "scheduled_end_time" in value:
        import capo_ssm.types.date_time

        out["ScheduledEndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["scheduled_end_time"]
        )
    if "change_details" in value:
        out["ChangeDetails"] = value["change_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartChangeRequestExecutionRequest:
    out: StartChangeRequestExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScheduledTime") is not None:
        import capo_ssm.types.date_time

        out["scheduled_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ScheduledTime"]
        )
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    else:
        out["document_name"] = ""
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("Parameters") is not None:
        import capo_ssm.types.automation_parameter_map

        out["parameters"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("ChangeRequestName") is not None:
        out["change_request_name"] = data["ChangeRequestName"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("AutoApprove") is not None:
        out["auto_approve"] = data["AutoApprove"]
    if data.get("Runbooks") is not None:
        import capo_ssm.types.runbooks

        out["runbooks"] = capo_ssm.types.runbooks.deserialize_aws_json_1_1(
            data["Runbooks"]
        )
    else:
        out["runbooks"] = []
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("ScheduledEndTime") is not None:
        import capo_ssm.types.date_time

        out["scheduled_end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ScheduledEndTime"]
        )
    if data.get("ChangeDetails") is not None:
        out["change_details"] = data["ChangeDetails"]
    return out
