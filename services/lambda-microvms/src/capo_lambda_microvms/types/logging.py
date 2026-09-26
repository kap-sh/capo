"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#Logging``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.cloud_watch_logging
    import capo_lambda_microvms.types.logging_disabled


class _Logging_disabled(TypedDict, closed=True):
    disabled: "capo_lambda_microvms.types.logging_disabled.LoggingDisabled"


class _Logging_cloudWatch(TypedDict, closed=True):
    cloudWatch: "capo_lambda_microvms.types.cloud_watch_logging.CloudWatchLogging"


Logging: TypeAlias = _Logging_disabled | _Logging_cloudWatch


# --- restJson1 ser/de ---
def serialize_json(value: Logging) -> dict:
    if "disabled" in value:
        import capo_lambda_microvms.types.logging_disabled

        return {
            "disabled": capo_lambda_microvms.types.logging_disabled.serialize_json(
                value["disabled"]
            )
        }
    elif "cloudWatch" in value:
        import capo_lambda_microvms.types.cloud_watch_logging

        return {
            "cloudWatch": capo_lambda_microvms.types.cloud_watch_logging.serialize_json(
                value["cloudWatch"]
            )
        }
    else:
        raise SerializationError("Logging: no variant present")


def deserialize_json(data: dict) -> Logging:
    if data.get("disabled") is not None:
        import capo_lambda_microvms.types.logging_disabled

        return {
            "disabled": capo_lambda_microvms.types.logging_disabled.deserialize_json(
                data["disabled"]
            )
        }
    elif data.get("cloudWatch") is not None:
        import capo_lambda_microvms.types.cloud_watch_logging

        return {
            "cloudWatch": capo_lambda_microvms.types.cloud_watch_logging.deserialize_json(
                data["cloudWatch"]
            )
        }
    else:
        raise DeserializationError("Logging: no recognized variant key")
