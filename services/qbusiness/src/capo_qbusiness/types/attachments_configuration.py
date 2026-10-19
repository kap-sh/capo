"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.attachments_control_mode


class AttachmentsConfiguration(TypedDict, closed=True):
    attachments_control_mode: (
        "capo_qbusiness.types.attachments_control_mode.AttachmentsControlMode"
    )
    """<p>Status information about whether file upload functionality is activated or deactivated for your end user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentsConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.attachments_control_mode

    out["attachmentsControlMode"] = (
        capo_qbusiness.types.attachments_control_mode.serialize_json(
            value["attachments_control_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> AttachmentsConfiguration:
    out: AttachmentsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("attachmentsControlMode") is not None:
        import capo_qbusiness.types.attachments_control_mode

        out["attachments_control_mode"] = (
            capo_qbusiness.types.attachments_control_mode.deserialize_json(
                data["attachmentsControlMode"]
            )
        )
    else:
        import typing

        out["attachments_control_mode"] = typing.cast(
            "capo_qbusiness.types.attachments_control_mode.AttachmentsControlMode", ""
        )
    return out
