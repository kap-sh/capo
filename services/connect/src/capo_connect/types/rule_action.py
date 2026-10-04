"""Generated from Smithy shape ``com.amazonaws.connect#RuleAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.action_type
    import capo_connect.types.assign_contact_category_action_definition
    import capo_connect.types.assign_sla_action_definition
    import capo_connect.types.create_case_action_definition
    import capo_connect.types.end_associated_tasks_action_definition
    import capo_connect.types.event_bridge_action_definition
    import capo_connect.types.extract_information_action_definition
    import capo_connect.types.send_in_app_notification_action_definition
    import capo_connect.types.send_notification_action_definition
    import capo_connect.types.submit_auto_evaluation_action_definition
    import capo_connect.types.task_action_definition
    import capo_connect.types.update_case_action_definition


class RuleAction(TypedDict, closed=True):
    action_type: "capo_connect.types.action_type.ActionType"
    """<p>The type of action that creates a rule.</p>"""
    task_action: NotRequired[
        "capo_connect.types.task_action_definition.TaskActionDefinition"
    ]
    """<p>Information about the task action. This field is required if <code>TriggerEventSource</code> is one of the following values: <code>OnZendeskTicketCreate</code> | <code>OnZendeskTicketStatusUpdate</code> | <code>OnSalesforceCaseCreate</code> </p>"""
    event_bridge_action: NotRequired[
        "capo_connect.types.event_bridge_action_definition.EventBridgeActionDefinition"
    ]
    """<p>Information about the EventBridge action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnRealTimeCallAnalysisAvailable</code> | <code>OnRealTimeChatAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code> | <code>OnContactEvaluationSubmit</code> | <code>OnMetricDataUpdate</code> </p>"""
    assign_contact_category_action: NotRequired[
        "capo_connect.types.assign_contact_category_action_definition.AssignContactCategoryActionDefinition"
    ]
    """<p>Information about the contact category action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnRealTimeCallAnalysisAvailable</code> | <code>OnRealTimeChatAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code> | <code>OnZendeskTicketCreate</code> | <code>OnZendeskTicketStatusUpdate</code> | <code>OnSalesforceCaseCreate</code> </p>"""
    send_notification_action: NotRequired[
        "capo_connect.types.send_notification_action_definition.SendNotificationActionDefinition"
    ]
    """<p>Information about the send notification action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnRealTimeCallAnalysisAvailable</code> | <code>OnRealTimeChatAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code> | <code>OnContactEvaluationSubmit</code> | <code>OnMetricDataUpdate</code> </p>"""
    create_case_action: NotRequired[
        "capo_connect.types.create_case_action_definition.CreateCaseActionDefinition"
    ]
    """<p>Information about the create case action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code>.</p>"""
    update_case_action: NotRequired[
        "capo_connect.types.update_case_action_definition.UpdateCaseActionDefinition"
    ]
    """<p>Information about the update case action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnCaseCreate</code> | <code>OnCaseUpdate</code>.</p>"""
    assign_sla_action: NotRequired[
        "capo_connect.types.assign_sla_action_definition.AssignSlaActionDefinition"
    ]
    """<p>Information about the assign SLA action.</p>"""
    end_associated_tasks_action: NotRequired[
        "capo_connect.types.end_associated_tasks_action_definition.EndAssociatedTasksActionDefinition"
    ]
    """<p>Information about the end associated tasks action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnCaseUpdate</code>.</p>"""
    submit_auto_evaluation_action: NotRequired[
        "capo_connect.types.submit_auto_evaluation_action_definition.SubmitAutoEvaluationActionDefinition"
    ]
    """<p>Information about the submit automated evaluation action.</p>"""
    extract_information_action: NotRequired[
        "capo_connect.types.extract_information_action_definition.ExtractInformationActionDefinition"
    ]
    """<p>Information about the extract information action.</p>"""
    send_in_app_notification_action: NotRequired[
        "capo_connect.types.send_in_app_notification_action_definition.SendInAppNotificationActionDefinition"
    ]
    """<p>Information about the send in-app notification action.</p> <p>Supported only for <code>TriggerEventSource</code> values: <code>OnPostCallAnalysisAvailable</code> | <code>OnRealTimeCallAnalysisAvailable</code> | <code>OnRealTimeChatAnalysisAvailable</code> | <code>OnPostChatAnalysisAvailable</code> | <code>OnAfterCallWorkAvailable</code> | <code>OnAfterChatWorkAvailable</code> | <code>OnEmailAnalysisAvailable</code> | <code>OnContactEvaluationSubmit</code> | <code>OnCaseCreate</code> | <code>OnCaseUpdate</code> | <code>OnSlaBreach</code> | <code>OnSchedulePublish</code> | <code>OnScheduleUpdate</code> | <code>OnScheduleTimeOffRequestActivity</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleAction) -> dict:
    out: dict = {}
    import capo_connect.types.action_type

    out["ActionType"] = capo_connect.types.action_type.serialize_json(
        value["action_type"]
    )
    if "task_action" in value:
        import capo_connect.types.task_action_definition

        out["TaskAction"] = capo_connect.types.task_action_definition.serialize_json(
            value["task_action"]
        )
    if "event_bridge_action" in value:
        import capo_connect.types.event_bridge_action_definition

        out["EventBridgeAction"] = (
            capo_connect.types.event_bridge_action_definition.serialize_json(
                value["event_bridge_action"]
            )
        )
    if "assign_contact_category_action" in value:
        import capo_connect.types.assign_contact_category_action_definition

        out["AssignContactCategoryAction"] = (
            capo_connect.types.assign_contact_category_action_definition.serialize_json(
                value["assign_contact_category_action"]
            )
        )
    if "send_notification_action" in value:
        import capo_connect.types.send_notification_action_definition

        out["SendNotificationAction"] = (
            capo_connect.types.send_notification_action_definition.serialize_json(
                value["send_notification_action"]
            )
        )
    if "create_case_action" in value:
        import capo_connect.types.create_case_action_definition

        out["CreateCaseAction"] = (
            capo_connect.types.create_case_action_definition.serialize_json(
                value["create_case_action"]
            )
        )
    if "update_case_action" in value:
        import capo_connect.types.update_case_action_definition

        out["UpdateCaseAction"] = (
            capo_connect.types.update_case_action_definition.serialize_json(
                value["update_case_action"]
            )
        )
    if "assign_sla_action" in value:
        import capo_connect.types.assign_sla_action_definition

        out["AssignSlaAction"] = (
            capo_connect.types.assign_sla_action_definition.serialize_json(
                value["assign_sla_action"]
            )
        )
    if "end_associated_tasks_action" in value:
        import capo_connect.types.end_associated_tasks_action_definition

        out["EndAssociatedTasksAction"] = (
            capo_connect.types.end_associated_tasks_action_definition.serialize_json(
                value["end_associated_tasks_action"]
            )
        )
    if "submit_auto_evaluation_action" in value:
        import capo_connect.types.submit_auto_evaluation_action_definition

        out["SubmitAutoEvaluationAction"] = (
            capo_connect.types.submit_auto_evaluation_action_definition.serialize_json(
                value["submit_auto_evaluation_action"]
            )
        )
    if "extract_information_action" in value:
        import capo_connect.types.extract_information_action_definition

        out["ExtractInformationAction"] = (
            capo_connect.types.extract_information_action_definition.serialize_json(
                value["extract_information_action"]
            )
        )
    if "send_in_app_notification_action" in value:
        import capo_connect.types.send_in_app_notification_action_definition

        out["SendInAppNotificationAction"] = (
            capo_connect.types.send_in_app_notification_action_definition.serialize_json(
                value["send_in_app_notification_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleAction:
    out: RuleAction = {}  # type: ignore[typeddict-item]
    if data.get("ActionType") is not None:
        import capo_connect.types.action_type

        out["action_type"] = capo_connect.types.action_type.deserialize_json(
            data["ActionType"]
        )
    else:
        raise DeserializationError("RuleAction.action_type required")
    if data.get("TaskAction") is not None:
        import capo_connect.types.task_action_definition

        out["task_action"] = capo_connect.types.task_action_definition.deserialize_json(
            data["TaskAction"]
        )
    if data.get("EventBridgeAction") is not None:
        import capo_connect.types.event_bridge_action_definition

        out["event_bridge_action"] = (
            capo_connect.types.event_bridge_action_definition.deserialize_json(
                data["EventBridgeAction"]
            )
        )
    if data.get("AssignContactCategoryAction") is not None:
        import capo_connect.types.assign_contact_category_action_definition

        out["assign_contact_category_action"] = (
            capo_connect.types.assign_contact_category_action_definition.deserialize_json(
                data["AssignContactCategoryAction"]
            )
        )
    if data.get("SendNotificationAction") is not None:
        import capo_connect.types.send_notification_action_definition

        out["send_notification_action"] = (
            capo_connect.types.send_notification_action_definition.deserialize_json(
                data["SendNotificationAction"]
            )
        )
    if data.get("CreateCaseAction") is not None:
        import capo_connect.types.create_case_action_definition

        out["create_case_action"] = (
            capo_connect.types.create_case_action_definition.deserialize_json(
                data["CreateCaseAction"]
            )
        )
    if data.get("UpdateCaseAction") is not None:
        import capo_connect.types.update_case_action_definition

        out["update_case_action"] = (
            capo_connect.types.update_case_action_definition.deserialize_json(
                data["UpdateCaseAction"]
            )
        )
    if data.get("AssignSlaAction") is not None:
        import capo_connect.types.assign_sla_action_definition

        out["assign_sla_action"] = (
            capo_connect.types.assign_sla_action_definition.deserialize_json(
                data["AssignSlaAction"]
            )
        )
    if data.get("EndAssociatedTasksAction") is not None:
        import capo_connect.types.end_associated_tasks_action_definition

        out["end_associated_tasks_action"] = (
            capo_connect.types.end_associated_tasks_action_definition.deserialize_json(
                data["EndAssociatedTasksAction"]
            )
        )
    if data.get("SubmitAutoEvaluationAction") is not None:
        import capo_connect.types.submit_auto_evaluation_action_definition

        out["submit_auto_evaluation_action"] = (
            capo_connect.types.submit_auto_evaluation_action_definition.deserialize_json(
                data["SubmitAutoEvaluationAction"]
            )
        )
    if data.get("ExtractInformationAction") is not None:
        import capo_connect.types.extract_information_action_definition

        out["extract_information_action"] = (
            capo_connect.types.extract_information_action_definition.deserialize_json(
                data["ExtractInformationAction"]
            )
        )
    if data.get("SendInAppNotificationAction") is not None:
        import capo_connect.types.send_in_app_notification_action_definition

        out["send_in_app_notification_action"] = (
            capo_connect.types.send_in_app_notification_action_definition.deserialize_json(
                data["SendInAppNotificationAction"]
            )
        )
    return out
