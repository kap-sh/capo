"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ProcessorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.processor

ProcessorList: TypeAlias = list["capo_chime_sdk_messaging.types.processor.Processor"]


# --- restJson1 ser/de ---
def serialize_json(value: ProcessorList) -> list:
    import capo_chime_sdk_messaging.types.processor

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_messaging.types.processor.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProcessorList:
    import capo_chime_sdk_messaging.types.processor

    out: ProcessorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime_sdk_messaging.types.processor.deserialize_json(item))
    return out


def redact_sensitive(value: ProcessorList) -> list[Any]:
    import capo_chime_sdk_messaging.types.processor

    return [
        capo_chime_sdk_messaging.types.processor.redact_sensitive(item)
        for item in value
    ]
