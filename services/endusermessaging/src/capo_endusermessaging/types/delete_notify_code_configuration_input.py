"""Generated from Smithy shape ``com.amazonaws.endusermessaging#DeleteNotifyCodeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.notify_code_configuration_id_or_arn


class DeleteNotifyCodeConfigurationInput(TypedDict, closed=True):
    notify_code_configuration_id: "capo_endusermessaging.types.notify_code_configuration_id_or_arn.NotifyCodeConfigurationIdOrArn"
    """<p>The unique identifier of the notify code configuration. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotifyCodeConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNotifyCodeConfigurationInput:
    out: DeleteNotifyCodeConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
