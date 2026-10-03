"""Generated from Smithy shape ``com.amazonaws.rekognition#StartStreamProcessorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.stream_processing_start_selector
    import capo_rekognition.types.stream_processing_stop_selector
    import capo_rekognition.types.stream_processor_name


class StartStreamProcessorRequest(TypedDict, closed=True):
    name: "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    """<p>The name of the stream processor to start processing.</p>"""
    start_selector: NotRequired[
        "capo_rekognition.types.stream_processing_start_selector.StreamProcessingStartSelector"
    ]
    """<p> Specifies the starting point in the Kinesis stream to start processing. You can use the producer timestamp or the fragment number. If you use the producer timestamp, you must put the time in milliseconds. For more information about fragment numbers, see <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Fragment.html">Fragment</a>. </p> <p>This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.</p>"""
    stop_selector: NotRequired[
        "capo_rekognition.types.stream_processing_stop_selector.StreamProcessingStopSelector"
    ]
    """<p> Specifies when to stop processing the stream. You can specify a maximum amount of time to process the video. </p> <p>This is a required parameter for label detection stream processors and should not be used to start a face search stream processor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartStreamProcessorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "start_selector" in value:
        import capo_rekognition.types.stream_processing_start_selector

        out["StartSelector"] = (
            capo_rekognition.types.stream_processing_start_selector.serialize_aws_json_1_1(
                value["start_selector"]
            )
        )
    if "stop_selector" in value:
        import capo_rekognition.types.stream_processing_stop_selector

        out["StopSelector"] = (
            capo_rekognition.types.stream_processing_stop_selector.serialize_aws_json_1_1(
                value["stop_selector"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartStreamProcessorRequest:
    out: StartStreamProcessorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartStreamProcessorRequest.name required")
    if data.get("StartSelector") is not None:
        import capo_rekognition.types.stream_processing_start_selector

        out["start_selector"] = (
            capo_rekognition.types.stream_processing_start_selector.deserialize_aws_json_1_1(
                data["StartSelector"]
            )
        )
    if data.get("StopSelector") is not None:
        import capo_rekognition.types.stream_processing_stop_selector

        out["stop_selector"] = (
            capo_rekognition.types.stream_processing_stop_selector.deserialize_aws_json_1_1(
                data["StopSelector"]
            )
        )
    return out
