"""Generated from Smithy shape ``com.amazonaws.rekognition#StopStreamProcessorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.stream_processor_name


class StopStreamProcessorRequest(TypedDict, closed=True):
    name: "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    """<p>The name of a stream processor created by <a>CreateStreamProcessor</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopStreamProcessorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopStreamProcessorRequest:
    out: StopStreamProcessorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
