"""Generated from Smithy shape ``com.amazonaws.auditmanager#ValidateAssessmentReportIntegrityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.s3_url


class ValidateAssessmentReportIntegrityRequest(TypedDict, closed=True):
    s3_relative_path: "capo_auditmanager.types.s3_url.S3Url"
    """<p> The relative path of the Amazon S3 bucket that the assessment report is stored in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateAssessmentReportIntegrityRequest) -> dict:
    out: dict = {}
    out["s3RelativePath"] = value["s3_relative_path"]
    return out


def deserialize_json(data: dict) -> ValidateAssessmentReportIntegrityRequest:
    out: ValidateAssessmentReportIntegrityRequest = {}  # type: ignore[typeddict-item]
    if data.get("s3RelativePath") is not None:
        out["s3_relative_path"] = data["s3RelativePath"]
    else:
        out["s3_relative_path"] = ""
    return out
