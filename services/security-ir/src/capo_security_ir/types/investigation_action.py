"""Generated from Smithy shape ``com.amazonaws.securityir#InvestigationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.action_type
    import capo_security_ir.types.execution_status
    import capo_security_ir.types.investigation_content
    import capo_security_ir.types.investigation_feedback
    import capo_security_ir.types.investigation_id
    import capo_security_ir.types.investigation_title


class InvestigationAction(TypedDict, closed=True):
    investigation_id: "capo_security_ir.types.investigation_id.InvestigationId"
    """<p>The unique identifier for this investigation action. This ID is used to track and reference the specific investigation throughout its lifecycle.</p>"""
    action_type: "capo_security_ir.types.action_type.ActionType"
    """<p>The type of investigation action being performed. This categorizes the investigation method or approach used in the case.</p>"""
    title: "capo_security_ir.types.investigation_title.InvestigationTitle"
    """<p>Human-readable summary of the investigation focus. This provides a brief description of what the investigation is examining or analyzing.</p>"""
    content: "capo_security_ir.types.investigation_content.InvestigationContent"
    """<p>Detailed investigation results in rich markdown format. This field contains the comprehensive findings, analysis, and conclusions from the investigation.</p>"""
    status: "capo_security_ir.types.execution_status.ExecutionStatus"
    """<p>The current execution status of the investigation. This indicates whether the investigation is pending, in progress, completed, or failed.</p>"""
    last_updated: "datetime.datetime"
    """<p>ISO 8601 timestamp of the most recent status update. This indicates when the investigation was last modified or when its status last changed.</p>"""
    feedback: NotRequired[
        "capo_security_ir.types.investigation_feedback.InvestigationFeedback"
    ]
    """<p>User feedback for this investigation result. This contains the user's assessment and comments about the quality and usefulness of the investigation findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationAction) -> dict:
    out: dict = {}
    out["investigationId"] = value["investigation_id"]
    import capo_security_ir.types.action_type

    out["actionType"] = capo_security_ir.types.action_type.serialize_json(
        value["action_type"]
    )
    out["title"] = value["title"]
    out["content"] = value["content"]
    import capo_security_ir.types.execution_status

    out["status"] = capo_security_ir.types.execution_status.serialize_json(
        value["status"]
    )
    import capo_security_ir.types._prelude.timestamp

    out["lastUpdated"] = capo_security_ir.types._prelude.timestamp.serialize_json(
        value["last_updated"]
    )
    if "feedback" in value:
        import capo_security_ir.types.investigation_feedback

        out["feedback"] = capo_security_ir.types.investigation_feedback.serialize_json(
            value["feedback"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationAction:
    out: InvestigationAction = {}  # type: ignore[typeddict-item]
    if data.get("investigationId") is not None:
        out["investigation_id"] = data["investigationId"]
    else:
        out["investigation_id"] = ""
    if data.get("actionType") is not None:
        import capo_security_ir.types.action_type

        out["action_type"] = capo_security_ir.types.action_type.deserialize_json(
            data["actionType"]
        )
    else:
        import typing

        out["action_type"] = typing.cast(
            "capo_security_ir.types.action_type.ActionType", ""
        )
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    if data.get("status") is not None:
        import capo_security_ir.types.execution_status

        out["status"] = capo_security_ir.types.execution_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_security_ir.types.execution_status.ExecutionStatus", ""
        )
    if data.get("lastUpdated") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["last_updated"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["lastUpdated"]
            )
        )
    else:
        import datetime

        out["last_updated"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("feedback") is not None:
        import capo_security_ir.types.investigation_feedback

        out["feedback"] = (
            capo_security_ir.types.investigation_feedback.deserialize_json(
                data["feedback"]
            )
        )
    return out
