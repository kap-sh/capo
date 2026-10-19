"""Generated from Smithy shape ``com.amazonaws.transcribe#DescribeLanguageModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.model_name


class DescribeLanguageModelRequest(TypedDict, closed=True):
    model_name: "capo_transcribe.types.model_name.ModelName"
    """<p>The name of the custom language model you want information about. Model names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLanguageModelRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLanguageModelRequest:
    out: DescribeLanguageModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        out["model_name"] = ""
    return out
