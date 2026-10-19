"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.assessment_rules_package_arn_list
    import capo_inspector.types.assessment_run_duration
    import capo_inspector.types.assessment_run_finding_counts
    import capo_inspector.types.assessment_run_name
    import capo_inspector.types.assessment_run_notification_list
    import capo_inspector.types.assessment_run_state
    import capo_inspector.types.assessment_run_state_change_list
    import capo_inspector.types.bool
    import capo_inspector.types.timestamp
    import capo_inspector.types.user_attribute_list


class AssessmentRun(TypedDict, closed=True):
    arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run.</p>"""
    name: "capo_inspector.types.assessment_run_name.AssessmentRunName"
    """<p>The auto-generated name for the assessment run.</p>"""
    assessment_template_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template that is associated with the assessment run.</p>"""
    state: "capo_inspector.types.assessment_run_state.AssessmentRunState"
    """<p>The state of the assessment run.</p>"""
    duration_in_seconds: (
        "capo_inspector.types.assessment_run_duration.AssessmentRunDuration"
    )
    """<p>The duration of the assessment run.</p>"""
    rules_package_arns: "capo_inspector.types.assessment_rules_package_arn_list.AssessmentRulesPackageArnList"
    """<p>The rules packages selected for the assessment run.</p>"""
    user_attributes_for_findings: (
        "capo_inspector.types.user_attribute_list.UserAttributeList"
    )
    """<p>The user-defined attributes that are assigned to every generated finding.</p>"""
    created_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The time when <a>StartAssessmentRun</a> was called.</p>"""
    started_at: NotRequired["capo_inspector.types.timestamp.Timestamp"]
    """<p>The time when <a>StartAssessmentRun</a> was called.</p>"""
    completed_at: NotRequired["capo_inspector.types.timestamp.Timestamp"]
    """<p>The assessment run completion time that corresponds to the rules packages evaluation completion time or failure.</p>"""
    state_changed_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The last time when the assessment run's state changed.</p>"""
    data_collected: "capo_inspector.types.bool.Bool"
    """<p>A Boolean value (true or false) that specifies whether the process of collecting data from the agents is completed.</p>"""
    state_changes: "capo_inspector.types.assessment_run_state_change_list.AssessmentRunStateChangeList"
    """<p>A list of the assessment run state changes.</p>"""
    notifications: "capo_inspector.types.assessment_run_notification_list.AssessmentRunNotificationList"
    """<p>A list of notifications for the event subscriptions. A notification about a particular generated finding is added to this list only once.</p>"""
    finding_counts: (
        "capo_inspector.types.assessment_run_finding_counts.AssessmentRunFindingCounts"
    )
    """<p>Provides a total count of generated findings per severity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRun) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["assessmentTemplateArn"] = value["assessment_template_arn"]
    import capo_inspector.types.assessment_run_state

    out["state"] = capo_inspector.types.assessment_run_state.serialize_aws_json_1_1(
        value["state"]
    )
    out["durationInSeconds"] = value["duration_in_seconds"]
    import capo_inspector.types.assessment_rules_package_arn_list

    out["rulesPackageArns"] = (
        capo_inspector.types.assessment_rules_package_arn_list.serialize_aws_json_1_1(
            value["rules_package_arns"]
        )
    )
    import capo_inspector.types.user_attribute_list

    out["userAttributesForFindings"] = (
        capo_inspector.types.user_attribute_list.serialize_aws_json_1_1(
            value["user_attributes_for_findings"]
        )
    )
    import capo_inspector.types.timestamp

    out["createdAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    if "started_at" in value:
        import capo_inspector.types.timestamp

        out["startedAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "completed_at" in value:
        import capo_inspector.types.timestamp

        out["completedAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
            value["completed_at"]
        )
    import capo_inspector.types.timestamp

    out["stateChangedAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["state_changed_at"]
    )
    out["dataCollected"] = value["data_collected"]
    import capo_inspector.types.assessment_run_state_change_list

    out["stateChanges"] = (
        capo_inspector.types.assessment_run_state_change_list.serialize_aws_json_1_1(
            value["state_changes"]
        )
    )
    import capo_inspector.types.assessment_run_notification_list

    out["notifications"] = (
        capo_inspector.types.assessment_run_notification_list.serialize_aws_json_1_1(
            value["notifications"]
        )
    )
    import capo_inspector.types.assessment_run_finding_counts

    out["findingCounts"] = (
        capo_inspector.types.assessment_run_finding_counts.serialize_aws_json_1_1(
            value["finding_counts"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRun:
    out: AssessmentRun = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("assessmentTemplateArn") is not None:
        out["assessment_template_arn"] = data["assessmentTemplateArn"]
    else:
        out["assessment_template_arn"] = ""
    if data.get("state") is not None:
        import capo_inspector.types.assessment_run_state

        out["state"] = (
            capo_inspector.types.assessment_run_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_inspector.types.assessment_run_state.AssessmentRunState", ""
        )
    if data.get("durationInSeconds") is not None:
        out["duration_in_seconds"] = data["durationInSeconds"]
    else:
        out["duration_in_seconds"] = 0
    if data.get("rulesPackageArns") is not None:
        import capo_inspector.types.assessment_rules_package_arn_list

        out["rules_package_arns"] = (
            capo_inspector.types.assessment_rules_package_arn_list.deserialize_aws_json_1_1(
                data["rulesPackageArns"]
            )
        )
    else:
        out["rules_package_arns"] = []
    if data.get("userAttributesForFindings") is not None:
        import capo_inspector.types.user_attribute_list

        out["user_attributes_for_findings"] = (
            capo_inspector.types.user_attribute_list.deserialize_aws_json_1_1(
                data["userAttributesForFindings"]
            )
        )
    else:
        out["user_attributes_for_findings"] = []
    if data.get("createdAt") is not None:
        import capo_inspector.types.timestamp

        out["created_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("startedAt") is not None:
        import capo_inspector.types.timestamp

        out["started_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if data.get("completedAt") is not None:
        import capo_inspector.types.timestamp

        out["completed_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["completedAt"]
        )
    if data.get("stateChangedAt") is not None:
        import capo_inspector.types.timestamp

        out["state_changed_at"] = (
            capo_inspector.types.timestamp.deserialize_aws_json_1_1(
                data["stateChangedAt"]
            )
        )
    else:
        import datetime

        out["state_changed_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("dataCollected") is not None:
        out["data_collected"] = data["dataCollected"]
    else:
        out["data_collected"] = False
    if data.get("stateChanges") is not None:
        import capo_inspector.types.assessment_run_state_change_list

        out["state_changes"] = (
            capo_inspector.types.assessment_run_state_change_list.deserialize_aws_json_1_1(
                data["stateChanges"]
            )
        )
    else:
        out["state_changes"] = []
    if data.get("notifications") is not None:
        import capo_inspector.types.assessment_run_notification_list

        out["notifications"] = (
            capo_inspector.types.assessment_run_notification_list.deserialize_aws_json_1_1(
                data["notifications"]
            )
        )
    else:
        out["notifications"] = []
    if data.get("findingCounts") is not None:
        import capo_inspector.types.assessment_run_finding_counts

        out["finding_counts"] = (
            capo_inspector.types.assessment_run_finding_counts.deserialize_aws_json_1_1(
                data["findingCounts"]
            )
        )
    else:
        out["finding_counts"] = {}
    return out
