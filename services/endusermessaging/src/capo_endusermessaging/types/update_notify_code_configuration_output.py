"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateNotifyCodeConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.notify_code_configuration


class UpdateNotifyCodeConfigurationOutput(TypedDict, closed=True):
    notify_code_configuration: (
        "capo_endusermessaging.types.notify_code_configuration.NotifyCodeConfiguration"
    )
    """<p>The notify code configuration resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotifyCodeConfigurationOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.notify_code_configuration

    out["notifyCodeConfiguration"] = (
        capo_endusermessaging.types.notify_code_configuration.serialize_json(
            value["notify_code_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateNotifyCodeConfigurationOutput:
    out: UpdateNotifyCodeConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("notifyCodeConfiguration") is not None:
        import capo_endusermessaging.types.notify_code_configuration

        out["notify_code_configuration"] = (
            capo_endusermessaging.types.notify_code_configuration.deserialize_json(
                data["notifyCodeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNotifyCodeConfigurationOutput.notify_code_configuration required"
        )
    return out
