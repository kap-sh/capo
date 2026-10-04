"""Generated from Smithy shape ``com.amazonaws.endusermessaging#NotifyCodeConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.notify_code_configuration

NotifyCodeConfigurationList: TypeAlias = list[
    "capo_endusermessaging.types.notify_code_configuration.NotifyCodeConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotifyCodeConfigurationList) -> list:
    import capo_endusermessaging.types.notify_code_configuration

    out: list = []
    for item in value:
        out.append(
            capo_endusermessaging.types.notify_code_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NotifyCodeConfigurationList:
    import capo_endusermessaging.types.notify_code_configuration

    out: NotifyCodeConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_endusermessaging.types.notify_code_configuration.deserialize_json(item)
        )
    return out
