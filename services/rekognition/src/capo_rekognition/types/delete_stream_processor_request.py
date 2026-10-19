"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteStreamProcessorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.stream_processor_name


class DeleteStreamProcessorRequest(TypedDict, closed=True):
    name: "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    """<p>The name of the stream processor you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStreamProcessorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStreamProcessorRequest:
    out: DeleteStreamProcessorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
