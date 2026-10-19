"""Generated from Smithy shape ``com.amazonaws.translate#InputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_translate.types.content_type
    import capo_translate.types.s3_uri


class InputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_translate.types.s3_uri.S3Uri"
    """<p>The URI of the AWS S3 folder that contains the input files. Amazon Translate translates all the files in the folder and all its sub-folders. The folder must be in the same Region as the API endpoint you are calling.</p>"""
    content_type: "capo_translate.types.content_type.ContentType"
    """<p>Describes the format of the data that you submit to Amazon Translate as input. You can specify one of the following multipurpose internet mail extension (MIME) types:</p> <ul> <li> <p> <code>text/html</code>: The input data consists of one or more HTML files. Amazon Translate translates only the text that resides in the <code>html</code> element in each file.</p> </li> <li> <p> <code>text/plain</code>: The input data consists of one or more unformatted text files. Amazon Translate translates every character in this type of input.</p> </li> <li> <p> <code>application/vnd.openxmlformats-officedocument.wordprocessingml.document</code>: The input data consists of one or more Word documents (.docx).</p> </li> <li> <p> <code>application/vnd.openxmlformats-officedocument.presentationml.presentation</code>: The input data consists of one or more PowerPoint Presentation files (.pptx).</p> </li> <li> <p> <code>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</code>: The input data consists of one or more Excel Workbook files (.xlsx).</p> </li> <li> <p> <code>application/x-xliff+xml</code>: The input data consists of one or more XML Localization Interchange File Format (XLIFF) files (.xlf). Amazon Translate supports only XLIFF version 1.2.</p> </li> </ul> <important> <p>If you structure your input data as HTML, ensure that you set this parameter to <code>text/html</code>. By doing so, you cut costs by limiting the translation to the contents of the <code>html</code> element in each file. Otherwise, if you set this parameter to <code>text/plain</code>, your costs will cover the translation of every character.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    out["ContentType"] = value["content_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        out["content_type"] = ""
    return out
