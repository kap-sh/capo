"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DecoderManifestValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import ServiceError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.invalid_network_interfaces
    import capo_iotfleetwise.types.invalid_signal_decoders
    import capo_iotfleetwise.types.string


class DecoderManifestValidationException_(TypedDict, closed=True):
    invalid_signals: NotRequired[
        "capo_iotfleetwise.types.invalid_signal_decoders.InvalidSignalDecoders"
    ]
    """<p>The request couldn't be completed because of invalid signals in the request.</p>"""
    invalid_network_interfaces: NotRequired[
        "capo_iotfleetwise.types.invalid_network_interfaces.InvalidNetworkInterfaces"
    ]
    """<p>The request couldn't be completed because of invalid network interfaces in the request.</p>"""
    message: NotRequired["capo_iotfleetwise.types.string.string"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecoderManifestValidationException_) -> dict:
    out: dict = {}
    if "invalid_signals" in value:
        import capo_iotfleetwise.types.invalid_signal_decoders

        out["invalidSignals"] = (
            capo_iotfleetwise.types.invalid_signal_decoders.serialize_aws_json_1_0(
                value["invalid_signals"]
            )
        )
    if "invalid_network_interfaces" in value:
        import capo_iotfleetwise.types.invalid_network_interfaces

        out["invalidNetworkInterfaces"] = (
            capo_iotfleetwise.types.invalid_network_interfaces.serialize_aws_json_1_0(
                value["invalid_network_interfaces"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DecoderManifestValidationException_:
    out: DecoderManifestValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("invalidSignals") is not None:
        import capo_iotfleetwise.types.invalid_signal_decoders

        out["invalid_signals"] = (
            capo_iotfleetwise.types.invalid_signal_decoders.deserialize_aws_json_1_0(
                data["invalidSignals"]
            )
        )
    if data.get("invalidNetworkInterfaces") is not None:
        import capo_iotfleetwise.types.invalid_network_interfaces

        out["invalid_network_interfaces"] = (
            capo_iotfleetwise.types.invalid_network_interfaces.deserialize_aws_json_1_0(
                data["invalidNetworkInterfaces"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DecoderManifestValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#DecoderManifestValidationException``."""

    code: str | None = "DecoderManifestValidationException"

    def __init__(
        self,
        data: DecoderManifestValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DecoderManifestValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DecoderManifestValidationException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
