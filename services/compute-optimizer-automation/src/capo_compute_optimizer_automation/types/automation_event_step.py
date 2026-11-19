"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEventStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.estimated_monthly_savings
    import capo_compute_optimizer_automation.types.event_id
    import capo_compute_optimizer_automation.types.resource_id
    import capo_compute_optimizer_automation.types.step_id
    import capo_compute_optimizer_automation.types.step_status
    import capo_compute_optimizer_automation.types.step_type


class AutomationEventStep(TypedDict, closed=True):
    event_id: NotRequired["capo_compute_optimizer_automation.types.event_id.EventId"]
    """<p> The ID of the automation event this step belongs to. </p>"""
    step_id: NotRequired["capo_compute_optimizer_automation.types.step_id.StepId"]
    """<p> The unique identifier for this step. </p>"""
    step_type: NotRequired["capo_compute_optimizer_automation.types.step_type.StepType"]
    """<p> The type of step. </p>"""
    step_status: NotRequired[
        "capo_compute_optimizer_automation.types.step_status.StepStatus"
    ]
    """<p> The current status of the step. </p>"""
    resource_id: NotRequired[
        "capo_compute_optimizer_automation.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the resource being acted upon in this step.</p>"""
    start_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when this automation event step started execution.</p>"""
    completed_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when this automation event step completed execution.</p>"""
    estimated_monthly_savings: NotRequired[
        "capo_compute_optimizer_automation.types.estimated_monthly_savings.EstimatedMonthlySavings"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEventStep) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "step_type" in value:
        import capo_compute_optimizer_automation.types.step_type

        out["stepType"] = (
            capo_compute_optimizer_automation.types.step_type.serialize_aws_json_1_0(
                value["step_type"]
            )
        )
    if "step_status" in value:
        import capo_compute_optimizer_automation.types.step_status

        out["stepStatus"] = (
            capo_compute_optimizer_automation.types.step_status.serialize_aws_json_1_0(
                value["step_status"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "start_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["startTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start_timestamp"]
            )
        )
    if "completed_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["completedTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completed_timestamp"]
            )
        )
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_aws_json_1_0(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutomationEventStep:
    out: AutomationEventStep = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    if data.get("stepType") is not None:
        import capo_compute_optimizer_automation.types.step_type

        out["step_type"] = (
            capo_compute_optimizer_automation.types.step_type.deserialize_aws_json_1_0(
                data["stepType"]
            )
        )
    if data.get("stepStatus") is not None:
        import capo_compute_optimizer_automation.types.step_status

        out["step_status"] = (
            capo_compute_optimizer_automation.types.step_status.deserialize_aws_json_1_0(
                data["stepStatus"]
            )
        )
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("startTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["start_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTimestamp"]
            )
        )
    if data.get("completedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["completed_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["completedTimestamp"]
            )
        )
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_aws_json_1_0(
                data["estimatedMonthlySavings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutomationEventStep) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "step_type" in value:
        import capo_compute_optimizer_automation.types.step_type

        out["stepType"] = (
            capo_compute_optimizer_automation.types.step_type.serialize_cbor(
                value["step_type"]
            )
        )
    if "step_status" in value:
        import capo_compute_optimizer_automation.types.step_status

        out["stepStatus"] = (
            capo_compute_optimizer_automation.types.step_status.serialize_cbor(
                value["step_status"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "start_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["startTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["start_timestamp"]
            )
        )
    if "completed_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["completedTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["completed_timestamp"]
            )
        )
    if "estimated_monthly_savings" in value:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimatedMonthlySavings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.serialize_cbor(
                value["estimated_monthly_savings"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AutomationEventStep:
    out: AutomationEventStep = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    if data.get("stepType") is not None:
        import capo_compute_optimizer_automation.types.step_type

        out["step_type"] = (
            capo_compute_optimizer_automation.types.step_type.deserialize_cbor(
                data["stepType"]
            )
        )
    if data.get("stepStatus") is not None:
        import capo_compute_optimizer_automation.types.step_status

        out["step_status"] = (
            capo_compute_optimizer_automation.types.step_status.deserialize_cbor(
                data["stepStatus"]
            )
        )
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("startTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["start_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["startTimestamp"]
            )
        )
    if data.get("completedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["completed_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["completedTimestamp"]
            )
        )
    if data.get("estimatedMonthlySavings") is not None:
        import capo_compute_optimizer_automation.types.estimated_monthly_savings

        out["estimated_monthly_savings"] = (
            capo_compute_optimizer_automation.types.estimated_monthly_savings.deserialize_cbor(
                data["estimatedMonthlySavings"]
            )
        )
    return out
