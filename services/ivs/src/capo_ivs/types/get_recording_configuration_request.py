"""Generated from Smithy shape ``com.amazonaws.ivs#GetRecordingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.recording_configuration_arn


class GetRecordingConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.recording_configuration_arn.RecordingConfigurationArn"
    """<p>ARN of the recording configuration to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecordingConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetRecordingConfigurationRequest:
    out: GetRecordingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
