"""Generated from Smithy shape ``com.amazonaws.sfn#HistoryEventList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.history_event

HistoryEventList: TypeAlias = list["capo_sfn.types.history_event.HistoryEvent"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HistoryEventList) -> list:
    import capo_sfn.types.history_event

    out: list = []
    for item in value:
        out.append(capo_sfn.types.history_event.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> HistoryEventList:
    import capo_sfn.types.history_event

    out: HistoryEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sfn.types.history_event.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: HistoryEventList) -> list[Any]:
    import capo_sfn.types.history_event

    return [capo_sfn.types.history_event.redact_sensitive(item) for item in value]
