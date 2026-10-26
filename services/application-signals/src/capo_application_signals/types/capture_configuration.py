"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CaptureConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError, SerializationError
from capo_application_signals.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_application_signals.types.code_capture_configuration


class _CaptureConfiguration_CodeCapture(TypedDict, closed=True):
    CodeCapture: "capo_application_signals.types.code_capture_configuration.CodeCaptureConfiguration"


CaptureConfiguration: TypeAlias = _CaptureConfiguration_CodeCapture | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: CaptureConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CaptureConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "CodeCapture" in value:
        import capo_application_signals.types.code_capture_configuration

        return {
            "CodeCapture": capo_application_signals.types.code_capture_configuration.serialize_json(
                value["CodeCapture"]
            )
        }
    else:
        raise SerializationError("CaptureConfiguration: no variant present")


def deserialize_json(data: dict) -> CaptureConfiguration:
    if data.get("CodeCapture") is not None:
        import capo_application_signals.types.code_capture_configuration

        return {
            "CodeCapture": capo_application_signals.types.code_capture_configuration.deserialize_json(
                data["CodeCapture"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CaptureConfiguration: no recognized variant key")
