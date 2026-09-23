"""Generated from Smithy shape ``com.amazonaws.s3#SelectObjectContentEventStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3._iter import AnyIterator
from capo_s3._protocol.eventstream import Message
from capo_s3.errors import UnknownServiceError

if TYPE_CHECKING:
    import capo_s3.types.continuation_event
    import capo_s3.types.end_event
    import capo_s3.types.progress_event
    import capo_s3.types.records_event
    import capo_s3.types.stats_event


class _SelectObjectContentEventStream_Records(TypedDict, closed=True):
    Records: "capo_s3.types.records_event.RecordsEvent"


class _SelectObjectContentEventStream_Stats(TypedDict, closed=True):
    Stats: "capo_s3.types.stats_event.StatsEvent"


class _SelectObjectContentEventStream_Progress(TypedDict, closed=True):
    Progress: "capo_s3.types.progress_event.ProgressEvent"


class _SelectObjectContentEventStream_Cont(TypedDict, closed=True):
    Cont: "capo_s3.types.continuation_event.ContinuationEvent"


class _SelectObjectContentEventStream_End(TypedDict, closed=True):
    End: "capo_s3.types.end_event.EndEvent"


_SelectObjectContentEventStream: TypeAlias = (
    _SelectObjectContentEventStream_Records
    | _SelectObjectContentEventStream_Stats
    | _SelectObjectContentEventStream_Progress
    | _SelectObjectContentEventStream_Cont
    | _SelectObjectContentEventStream_End
)
SelectObjectContentEventStream: TypeAlias = AnyIterator[_SelectObjectContentEventStream]


def serialize_event_xml(value: _SelectObjectContentEventStream) -> bytes:
    match value:
        case {"Records": payload}:
            import capo_s3.types.records_event

            return capo_s3.types.records_event.serialize_event_xml(payload)
        case {"Stats": payload}:
            import capo_s3.types.stats_event

            return capo_s3.types.stats_event.serialize_event_xml(payload)
        case {"Progress": payload}:
            import capo_s3.types.progress_event

            return capo_s3.types.progress_event.serialize_event_xml(payload)
        case {"Cont": payload}:
            import capo_s3.types.continuation_event

            return capo_s3.types.continuation_event.serialize_event_xml(payload)
        case {"End": payload}:
            import capo_s3.types.end_event

            return capo_s3.types.end_event.serialize_event_xml(payload)
        case _:
            raise ValueError(
                f"SelectObjectContentEventStream: unrecognized variant {value!r}"
            )


def deserialize_event_xml(message: Message) -> _SelectObjectContentEventStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        raise UnknownServiceError(
            code=str(exception_type), message=None, response=message
        )
    if message_type == "error":
        error_code = headers.get(":error-code")
        error_message = headers.get(":error-message")
        raise UnknownServiceError(
            code=None if error_code is None else str(error_code),
            message=None if error_message is None else str(error_message),
            response=message,
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "Records":
            import capo_s3.types.records_event

            return {
                "Records": capo_s3.types.records_event.deserialize_event_xml(message)
            }
        case "Stats":
            import capo_s3.types.stats_event

            return {"Stats": capo_s3.types.stats_event.deserialize_event_xml(message)}
        case "Progress":
            import capo_s3.types.progress_event

            return {
                "Progress": capo_s3.types.progress_event.deserialize_event_xml(message)
            }
        case "Cont":
            import capo_s3.types.continuation_event

            return {
                "Cont": capo_s3.types.continuation_event.deserialize_event_xml(message)
            }
        case "End":
            import capo_s3.types.end_event

            return {"End": capo_s3.types.end_event.deserialize_event_xml(message)}
        case _:
            raise ValueError(
                f"SelectObjectContentEventStream: unrecognized event-type {event_type!r}"
            )
