"""Generated from Smithy shape ``com.amazonaws.endusermessaging#GetNotifyCodeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.notify_code_configuration_id_or_arn


class GetNotifyCodeConfigurationInput(TypedDict, closed=True):
    notify_code_configuration_id: "capo_endusermessaging.types.notify_code_configuration_id_or_arn.NotifyCodeConfigurationIdOrArn"
    """<p>The unique identifier of the notify code configuration. You can specify either the bare ID or the full Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotifyCodeConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotifyCodeConfigurationInput:
    out: GetNotifyCodeConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
