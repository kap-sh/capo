"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShardEventStream``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_kinesis._iter import AnyIterator
from capo_kinesis._protocol.eventstream import Message
from capo_kinesis.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_kinesis.errors.internal_failure_exception
    import capo_kinesis.errors.kms_access_denied_exception
    import capo_kinesis.errors.kms_disabled_exception
    import capo_kinesis.errors.kms_invalid_state_exception
    import capo_kinesis.errors.kms_not_found_exception
    import capo_kinesis.errors.kms_opt_in_required
    import capo_kinesis.errors.kms_throttling_exception
    import capo_kinesis.errors.resource_in_use_exception
    import capo_kinesis.errors.resource_not_found_exception
    import capo_kinesis.types.subscribe_to_shard_event


class _SubscribeToShardEventStream_SubscribeToShardEvent(TypedDict, closed=True):
    SubscribeToShardEvent: (
        "capo_kinesis.types.subscribe_to_shard_event.SubscribeToShardEvent"
    )


class _SubscribeToShardEventStream_ResourceNotFoundException(TypedDict, closed=True):
    ResourceNotFoundException: (
        "capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException_"
    )


class _SubscribeToShardEventStream_ResourceInUseException(TypedDict, closed=True):
    ResourceInUseException: (
        "capo_kinesis.errors.resource_in_use_exception.ResourceInUseException_"
    )


class _SubscribeToShardEventStream_KMSDisabledException(TypedDict, closed=True):
    KMSDisabledException: (
        "capo_kinesis.errors.kms_disabled_exception.KMSDisabledException_"
    )


class _SubscribeToShardEventStream_KMSInvalidStateException(TypedDict, closed=True):
    KMSInvalidStateException: (
        "capo_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException_"
    )


class _SubscribeToShardEventStream_KMSAccessDeniedException(TypedDict, closed=True):
    KMSAccessDeniedException: (
        "capo_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException_"
    )


class _SubscribeToShardEventStream_KMSNotFoundException(TypedDict, closed=True):
    KMSNotFoundException: (
        "capo_kinesis.errors.kms_not_found_exception.KMSNotFoundException_"
    )


class _SubscribeToShardEventStream_KMSOptInRequired(TypedDict, closed=True):
    KMSOptInRequired: "capo_kinesis.errors.kms_opt_in_required.KMSOptInRequired_"


class _SubscribeToShardEventStream_KMSThrottlingException(TypedDict, closed=True):
    KMSThrottlingException: (
        "capo_kinesis.errors.kms_throttling_exception.KMSThrottlingException_"
    )


class _SubscribeToShardEventStream_InternalFailureException(TypedDict, closed=True):
    InternalFailureException: (
        "capo_kinesis.errors.internal_failure_exception.InternalFailureException_"
    )


_SubscribeToShardEventStream: TypeAlias = (
    _SubscribeToShardEventStream_SubscribeToShardEvent
    | _SubscribeToShardEventStream_ResourceNotFoundException
    | _SubscribeToShardEventStream_ResourceInUseException
    | _SubscribeToShardEventStream_KMSDisabledException
    | _SubscribeToShardEventStream_KMSInvalidStateException
    | _SubscribeToShardEventStream_KMSAccessDeniedException
    | _SubscribeToShardEventStream_KMSNotFoundException
    | _SubscribeToShardEventStream_KMSOptInRequired
    | _SubscribeToShardEventStream_KMSThrottlingException
    | _SubscribeToShardEventStream_InternalFailureException
)
SubscribeToShardEventStream: TypeAlias = AnyIterator[_SubscribeToShardEventStream]


def serialize_event_aws_json_1_1(value: _SubscribeToShardEventStream) -> bytes:
    match value:
        case {"SubscribeToShardEvent": payload}:
            import capo_kinesis.types.subscribe_to_shard_event

            return capo_kinesis.types.subscribe_to_shard_event.serialize_event_aws_json_1_1(
                payload
            )
        case {"ResourceNotFoundException": payload}:
            import capo_kinesis.errors.resource_not_found_exception

            return capo_kinesis.errors.resource_not_found_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"ResourceInUseException": payload}:
            import capo_kinesis.errors.resource_in_use_exception

            return capo_kinesis.errors.resource_in_use_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSDisabledException": payload}:
            import capo_kinesis.errors.kms_disabled_exception

            return (
                capo_kinesis.errors.kms_disabled_exception.serialize_event_aws_json_1_1(
                    payload
                )
            )
        case {"KMSInvalidStateException": payload}:
            import capo_kinesis.errors.kms_invalid_state_exception

            return capo_kinesis.errors.kms_invalid_state_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSAccessDeniedException": payload}:
            import capo_kinesis.errors.kms_access_denied_exception

            return capo_kinesis.errors.kms_access_denied_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSNotFoundException": payload}:
            import capo_kinesis.errors.kms_not_found_exception

            return capo_kinesis.errors.kms_not_found_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSOptInRequired": payload}:
            import capo_kinesis.errors.kms_opt_in_required

            return capo_kinesis.errors.kms_opt_in_required.serialize_event_aws_json_1_1(
                payload
            )
        case {"KMSThrottlingException": payload}:
            import capo_kinesis.errors.kms_throttling_exception

            return capo_kinesis.errors.kms_throttling_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"InternalFailureException": payload}:
            import capo_kinesis.errors.internal_failure_exception

            return capo_kinesis.errors.internal_failure_exception.serialize_event_aws_json_1_1(
                payload
            )
        case _:
            raise ValueError(
                f"SubscribeToShardEventStream: unrecognized variant {value!r}"
            )


def deserialize_event_aws_json_1_1(
    message: Message, *, response: zapros.Response
) -> _SubscribeToShardEventStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "ResourceNotFoundException":
                import capo_kinesis.errors.resource_not_found_exception

                data = capo_kinesis.errors.resource_not_found_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException(
                    data, message=data.get("message"), response=response
                )
            case "ResourceInUseException":
                import capo_kinesis.errors.resource_in_use_exception

                data = capo_kinesis.errors.resource_in_use_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.resource_in_use_exception.ResourceInUseException(
                    data, message=data.get("message"), response=response
                )
            case "KMSDisabledException":
                import capo_kinesis.errors.kms_disabled_exception

                data = capo_kinesis.errors.kms_disabled_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.kms_disabled_exception.KMSDisabledException(
                    data, message=data.get("message"), response=response
                )
            case "KMSInvalidStateException":
                import capo_kinesis.errors.kms_invalid_state_exception

                data = capo_kinesis.errors.kms_invalid_state_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException(
                    data, message=data.get("message"), response=response
                )
            case "KMSAccessDeniedException":
                import capo_kinesis.errors.kms_access_denied_exception

                data = capo_kinesis.errors.kms_access_denied_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException(
                    data, message=data.get("message"), response=response
                )
            case "KMSNotFoundException":
                import capo_kinesis.errors.kms_not_found_exception

                data = capo_kinesis.errors.kms_not_found_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.kms_not_found_exception.KMSNotFoundException(
                    data, message=data.get("message"), response=response
                )
            case "KMSOptInRequired":
                import capo_kinesis.errors.kms_opt_in_required

                data = capo_kinesis.errors.kms_opt_in_required.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.kms_opt_in_required.KMSOptInRequired(
                    data, message=data.get("message"), response=response
                )
            case "KMSThrottlingException":
                import capo_kinesis.errors.kms_throttling_exception

                data = capo_kinesis.errors.kms_throttling_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.kms_throttling_exception.KMSThrottlingException(
                    data, message=data.get("message"), response=response
                )
            case "InternalFailureException":
                import capo_kinesis.errors.internal_failure_exception

                data = capo_kinesis.errors.internal_failure_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_kinesis.errors.internal_failure_exception.InternalFailureException(
                    data, message=data.get("message"), response=response
                )
        raise UnknownServiceError(
            code=str(exception_type), message=None, response=response
        )
    if message_type == "error":
        error_code = headers.get(":error-code")
        error_message = headers.get(":error-message")
        raise UnknownServiceError(
            code=None if error_code is None else str(error_code),
            message=None if error_message is None else str(error_message),
            response=response,
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "SubscribeToShardEvent":
            import capo_kinesis.types.subscribe_to_shard_event

            return {
                "SubscribeToShardEvent": capo_kinesis.types.subscribe_to_shard_event.deserialize_event_aws_json_1_1(
                    message
                )
            }
        case _:
            raise ValueError(
                f"SubscribeToShardEventStream: unrecognized event-type {event_type!r}"
            )
