"""Generated from Smithy shape ``com.amazonaws.configservice#StopConfigurationRecorderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.recorder_name


class StopConfigurationRecorderRequest(TypedDict, closed=True):
    configuration_recorder_name: "capo_config_service.types.recorder_name.RecorderName"
    """<p>The name of the customer managed configuration recorder that you want to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopConfigurationRecorderRequest) -> dict:
    out: dict = {}
    out["ConfigurationRecorderName"] = value["configuration_recorder_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopConfigurationRecorderRequest:
    out: StopConfigurationRecorderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationRecorderName") is not None:
        out["configuration_recorder_name"] = data["ConfigurationRecorderName"]
    else:
        out["configuration_recorder_name"] = ""
    return out
