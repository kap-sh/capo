"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetEncoderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.encoder_configuration_arn


class GetEncoderConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
    """<p>ARN of the EncoderConfiguration resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEncoderConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetEncoderConfigurationRequest:
    out: GetEncoderConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
