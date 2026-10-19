"""Generated from Smithy shape ``com.amazonaws.healthlake#TransformationJobProgressReport``."""

from typing_extensions import TypedDict


class TransformationJobProgressReport(TypedDict, closed=True):
    total_files_scanned: "int"
    """<p>The total number of source files scanned by the job.</p>"""
    total_files_converted: "int"
    """<p>The total number of source files successfully converted.</p>"""
    total_files_failed: "int"
    """<p>The total number of source files that failed conversion.</p>"""
    total_resources_generated: "int"
    """<p>The total number of FHIR R4 resources generated across all converted files.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformationJobProgressReport) -> dict:
    out: dict = {}
    out["TotalFilesScanned"] = value["total_files_scanned"]
    out["TotalFilesConverted"] = value["total_files_converted"]
    out["TotalFilesFailed"] = value["total_files_failed"]
    out["TotalResourcesGenerated"] = value["total_resources_generated"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TransformationJobProgressReport:
    out: TransformationJobProgressReport = {}  # type: ignore[typeddict-item]
    if data.get("TotalFilesScanned") is not None:
        out["total_files_scanned"] = data["TotalFilesScanned"]
    else:
        out["total_files_scanned"] = 0
    if data.get("TotalFilesConverted") is not None:
        out["total_files_converted"] = data["TotalFilesConverted"]
    else:
        out["total_files_converted"] = 0
    if data.get("TotalFilesFailed") is not None:
        out["total_files_failed"] = data["TotalFilesFailed"]
    else:
        out["total_files_failed"] = 0
    if data.get("TotalResourcesGenerated") is not None:
        out["total_resources_generated"] = data["TotalResourcesGenerated"]
    else:
        out["total_resources_generated"] = 0
    return out
