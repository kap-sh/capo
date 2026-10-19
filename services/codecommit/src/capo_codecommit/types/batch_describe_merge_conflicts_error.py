"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchDescribeMergeConflictsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.exception_name
    import capo_codecommit.types.message
    import capo_codecommit.types.path


class BatchDescribeMergeConflictsError(TypedDict, closed=True):
    file_path: "capo_codecommit.types.path.Path"
    """<p>The path to the file.</p>"""
    exception_name: "capo_codecommit.types.exception_name.ExceptionName"
    """<p>The name of the exception.</p>"""
    message: "capo_codecommit.types.message.Message"
    """<p>The message provided by the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeMergeConflictsError) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    out["exceptionName"] = value["exception_name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeMergeConflictsError:
    out: BatchDescribeMergeConflictsError = {}  # type: ignore[typeddict-item]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    if data.get("exceptionName") is not None:
        out["exception_name"] = data["exceptionName"]
    else:
        out["exception_name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
