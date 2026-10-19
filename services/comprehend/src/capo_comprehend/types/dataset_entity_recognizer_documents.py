"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetEntityRecognizerDocuments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.input_format
    import capo_comprehend.types.s3_uri


class DatasetEntityRecognizerDocuments(TypedDict, closed=True):
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p> Specifies the Amazon S3 location where the documents for the dataset are located. </p>"""
    input_format: NotRequired["capo_comprehend.types.input_format.InputFormat"]
    """<p> Specifies how the text in an input file should be processed. This is optional, and the default is ONE_DOC_PER_LINE. ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetEntityRecognizerDocuments) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "input_format" in value:
        import capo_comprehend.types.input_format

        out["InputFormat"] = capo_comprehend.types.input_format.serialize_aws_json_1_1(
            value["input_format"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetEntityRecognizerDocuments:
    out: DatasetEntityRecognizerDocuments = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("InputFormat") is not None:
        import capo_comprehend.types.input_format

        out["input_format"] = (
            capo_comprehend.types.input_format.deserialize_aws_json_1_1(
                data["InputFormat"]
            )
        )
    return out
