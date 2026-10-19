"""Generated from Smithy shape ``com.amazonaws.iot#StartDetectMitigationActionsTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.client_request_token
    import capo_iot.types.detect_mitigation_actions_task_target
    import capo_iot.types.detect_mitigation_actions_to_execute_list
    import capo_iot.types.mitigation_actions_task_id
    import capo_iot.types.nullable_boolean
    import capo_iot.types.violation_event_occurrence_range


class StartDetectMitigationActionsTaskRequest(TypedDict, closed=True):
    task_id: "capo_iot.types.mitigation_actions_task_id.MitigationActionsTaskId"
    """<p> The unique identifier of the task. </p>"""
    target: "capo_iot.types.detect_mitigation_actions_task_target.DetectMitigationActionsTaskTarget"
    """<p> Specifies the ML Detect findings to which the mitigation actions are applied. </p>"""
    actions: "capo_iot.types.detect_mitigation_actions_to_execute_list.DetectMitigationActionsToExecuteList"
    """<p> The actions to be performed when a device has unexpected behavior. </p>"""
    violation_event_occurrence_range: NotRequired[
        "capo_iot.types.violation_event_occurrence_range.ViolationEventOccurrenceRange"
    ]
    """<p> Specifies the time period of which violation events occurred between. </p>"""
    include_only_active_violations: NotRequired[
        "capo_iot.types.nullable_boolean.NullableBoolean"
    ]
    """<p> Specifies to list only active violations. </p>"""
    include_suppressed_alerts: NotRequired[
        "capo_iot.types.nullable_boolean.NullableBoolean"
    ]
    """<p> Specifies to include suppressed alerts. </p>"""
    client_request_token: "capo_iot.types.client_request_token.ClientRequestToken"
    """<p> Each mitigation action task must have a unique client request token. If you try to create a new task with the same token as a task that already exists, an exception occurs. If you omit this value, Amazon Web Services SDKs will automatically generate a unique client request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDetectMitigationActionsTaskRequest) -> dict:
    out: dict = {}
    import capo_iot.types.detect_mitigation_actions_task_target

    out["target"] = capo_iot.types.detect_mitigation_actions_task_target.serialize_json(
        value["target"]
    )
    import capo_iot.types.detect_mitigation_actions_to_execute_list

    out["actions"] = (
        capo_iot.types.detect_mitigation_actions_to_execute_list.serialize_json(
            value["actions"]
        )
    )
    if "violation_event_occurrence_range" in value:
        import capo_iot.types.violation_event_occurrence_range

        out["violationEventOccurrenceRange"] = (
            capo_iot.types.violation_event_occurrence_range.serialize_json(
                value["violation_event_occurrence_range"]
            )
        )
    if "include_only_active_violations" in value:
        out["includeOnlyActiveViolations"] = value["include_only_active_violations"]
    if "include_suppressed_alerts" in value:
        out["includeSuppressedAlerts"] = value["include_suppressed_alerts"]
    out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> StartDetectMitigationActionsTaskRequest:
    out: StartDetectMitigationActionsTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("target") is not None:
        import capo_iot.types.detect_mitigation_actions_task_target

        out["target"] = (
            capo_iot.types.detect_mitigation_actions_task_target.deserialize_json(
                data["target"]
            )
        )
    else:
        raise DeserializationError(
            "StartDetectMitigationActionsTaskRequest.target required"
        )
    if data.get("actions") is not None:
        import capo_iot.types.detect_mitigation_actions_to_execute_list

        out["actions"] = (
            capo_iot.types.detect_mitigation_actions_to_execute_list.deserialize_json(
                data["actions"]
            )
        )
    else:
        out["actions"] = []
    if data.get("violationEventOccurrenceRange") is not None:
        import capo_iot.types.violation_event_occurrence_range

        out["violation_event_occurrence_range"] = (
            capo_iot.types.violation_event_occurrence_range.deserialize_json(
                data["violationEventOccurrenceRange"]
            )
        )
    if data.get("includeOnlyActiveViolations") is not None:
        out["include_only_active_violations"] = data["includeOnlyActiveViolations"]
    if data.get("includeSuppressedAlerts") is not None:
        out["include_suppressed_alerts"] = data["includeSuppressedAlerts"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    else:
        out["client_request_token"] = ""
    return out
