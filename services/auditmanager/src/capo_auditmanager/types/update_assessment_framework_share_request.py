"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.share_request_action
    import capo_auditmanager.types.share_request_type
    import capo_auditmanager.types.uuid


class UpdateAssessmentFrameworkShareRequest(TypedDict, closed=True):
    request_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the share request. </p>"""
    request_type: "capo_auditmanager.types.share_request_type.ShareRequestType"
    """<p>Specifies whether the share request is a sent request or a received request.</p>"""
    action: "capo_auditmanager.types.share_request_action.ShareRequestAction"
    """<p>Specifies the update action for the share request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkShareRequest) -> dict:
    out: dict = {}
    import capo_auditmanager.types.share_request_type

    out["requestType"] = capo_auditmanager.types.share_request_type.serialize_json(
        value["request_type"]
    )
    import capo_auditmanager.types.share_request_action

    out["action"] = capo_auditmanager.types.share_request_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentFrameworkShareRequest:
    out: UpdateAssessmentFrameworkShareRequest = {}  # type: ignore[typeddict-item]
    if data.get("requestType") is not None:
        import capo_auditmanager.types.share_request_type

        out["request_type"] = (
            capo_auditmanager.types.share_request_type.deserialize_json(
                data["requestType"]
            )
        )
    else:
        import typing

        out["request_type"] = typing.cast(
            "capo_auditmanager.types.share_request_type.ShareRequestType", ""
        )
    if data.get("action") is not None:
        import capo_auditmanager.types.share_request_action

        out["action"] = capo_auditmanager.types.share_request_action.deserialize_json(
            data["action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_auditmanager.types.share_request_action.ShareRequestAction", ""
        )
    return out
