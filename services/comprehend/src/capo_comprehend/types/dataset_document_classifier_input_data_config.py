"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetDocumentClassifierInputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.label_delimiter
    import capo_comprehend.types.s3_uri


class DatasetDocumentClassifierInputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p>The Amazon S3 URI for the input data. The S3 bucket must be in the same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of input files.</p> <p>For example, if you use the URI <code>S3://bucketName/prefix</code>, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.</p> <p>This parameter is required if you set <code>DataFormat</code> to <code>COMPREHEND_CSV</code>.</p>"""
    label_delimiter: NotRequired["capo_comprehend.types.label_delimiter.LabelDelimiter"]
    """<p>Indicates the delimiter used to separate each label for training a multi-label classifier. The default delimiter between labels is a pipe (|). You can use a different character as a delimiter (if it's an allowed character) by specifying it under Delimiter for labels. If the training documents use a delimiter other than the default or the delimiter you specify, the labels on that line will be combined to make a single unique label, such as LABELLABELLABEL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetDocumentClassifierInputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "label_delimiter" in value:
        out["LabelDelimiter"] = value["label_delimiter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetDocumentClassifierInputDataConfig:
    out: DatasetDocumentClassifierInputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("LabelDelimiter") is not None:
        out["label_delimiter"] = data["LabelDelimiter"]
    return out
