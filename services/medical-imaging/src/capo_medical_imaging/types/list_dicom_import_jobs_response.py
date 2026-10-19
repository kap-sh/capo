"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ListDICOMImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_import_job_summaries
    import capo_medical_imaging.types.next_token


class ListDICOMImportJobsResponse(TypedDict, closed=True):
    job_summaries: (
        "capo_medical_imaging.types.dicom_import_job_summaries.DICOMImportJobSummaries"
    )
    """<p>A list of job summaries.</p>"""
    next_token: NotRequired["capo_medical_imaging.types.next_token.NextToken"]
    """<p>The pagination token used to retrieve the list of import jobs on the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDICOMImportJobsResponse) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.dicom_import_job_summaries

    out["jobSummaries"] = (
        capo_medical_imaging.types.dicom_import_job_summaries.serialize_json(
            value["job_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDICOMImportJobsResponse:
    out: ListDICOMImportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobSummaries") is not None:
        import capo_medical_imaging.types.dicom_import_job_summaries

        out["job_summaries"] = (
            capo_medical_imaging.types.dicom_import_job_summaries.deserialize_json(
                data["jobSummaries"]
            )
        )
    else:
        out["job_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
