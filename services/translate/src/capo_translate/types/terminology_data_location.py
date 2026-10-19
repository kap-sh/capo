"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyDataLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_translate.types.string


class TerminologyDataLocation(TypedDict, closed=True):
    repository_type: "capo_translate.types.string.String"
    """<p>The repository type for the custom terminology data.</p>"""
    location: "capo_translate.types.string.String"
    """<p>The Amazon S3 location of the most recent custom terminology input file that was successfully imported into Amazon Translate. The location is returned as a presigned URL that has a 30-minute expiration .</p> <important> <p>Amazon Translate doesn't scan all input files for the risk of CSV injection attacks. </p> <p>CSV injection occurs when a .csv or .tsv file is altered so that a record contains malicious code. The record begins with a special character, such as =, +, -, or @. When the file is opened in a spreadsheet program, the program might interpret the record as a formula and run the code within it.</p> <p>Before you download an input file from Amazon S3, ensure that you recognize the file and trust its creator.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminologyDataLocation) -> dict:
    out: dict = {}
    out["RepositoryType"] = value["repository_type"]
    out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminologyDataLocation:
    out: TerminologyDataLocation = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryType") is not None:
        out["repository_type"] = data["RepositoryType"]
    else:
        out["repository_type"] = ""
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    else:
        out["location"] = ""
    return out
