"""Generated from Smithy shape ``com.amazonaws.comprehend#InputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.document_reader_config
    import capo_comprehend.types.input_format
    import capo_comprehend.types.s3_uri


class InputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p>The Amazon S3 URI for the input data. The URI must be in same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. </p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p>"""
    input_format: NotRequired["capo_comprehend.types.input_format.InputFormat"]
    """<p>Specifies how the text in an input file should be processed:</p> <ul> <li> <p> <code>ONE_DOC_PER_FILE</code> - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.</p> </li> <li> <p> <code>ONE_DOC_PER_LINE</code> - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.</p> </li> </ul>"""
    document_reader_config: NotRequired[
        "capo_comprehend.types.document_reader_config.DocumentReaderConfig"
    ]
    """<p>Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "input_format" in value:
        import capo_comprehend.types.input_format

        out["InputFormat"] = capo_comprehend.types.input_format.serialize_aws_json_1_1(
            value["input_format"]
        )
    if "document_reader_config" in value:
        import capo_comprehend.types.document_reader_config

        out["DocumentReaderConfig"] = (
            capo_comprehend.types.document_reader_config.serialize_aws_json_1_1(
                value["document_reader_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
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
    if data.get("DocumentReaderConfig") is not None:
        import capo_comprehend.types.document_reader_config

        out["document_reader_config"] = (
            capo_comprehend.types.document_reader_config.deserialize_aws_json_1_1(
                data["DocumentReaderConfig"]
            )
        )
    return out
