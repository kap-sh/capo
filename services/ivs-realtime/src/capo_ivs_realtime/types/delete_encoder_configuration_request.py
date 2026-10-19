"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DeleteEncoderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.encoder_configuration_arn


class DeleteEncoderConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
    """<p>ARN of the EncoderConfiguration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEncoderConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteEncoderConfigurationRequest:
    out: DeleteEncoderConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
