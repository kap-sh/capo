"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateFindingsReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.destination
    import capo_inspector2.types.filter_criteria
    import capo_inspector2.types.report_format


class CreateFindingsReportRequest(TypedDict, closed=True):
    filter_criteria: NotRequired["capo_inspector2.types.filter_criteria.FilterCriteria"]
    """<p>The filter criteria to apply to the results of the finding report.</p>"""
    report_format: "capo_inspector2.types.report_format.ReportFormat"
    """<p>The format to generate the report in.</p>"""
    s3_destination: "capo_inspector2.types.destination.Destination"
    """<p>The Amazon S3 export destination for the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFindingsReportRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import capo_inspector2.types.filter_criteria

        out["filterCriteria"] = capo_inspector2.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    out["reportFormat"] = value["report_format"]
    import capo_inspector2.types.destination

    out["s3Destination"] = capo_inspector2.types.destination.serialize_json(
        value["s3_destination"]
    )
    return out


def deserialize_json(data: dict) -> CreateFindingsReportRequest:
    out: CreateFindingsReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterCriteria") is not None:
        import capo_inspector2.types.filter_criteria

        out["filter_criteria"] = capo_inspector2.types.filter_criteria.deserialize_json(
            data["filterCriteria"]
        )
    if data.get("reportFormat") is not None:
        out["report_format"] = data["reportFormat"]
    else:
        out["report_format"] = ""
    if data.get("s3Destination") is not None:
        import capo_inspector2.types.destination

        out["s3_destination"] = capo_inspector2.types.destination.deserialize_json(
            data["s3Destination"]
        )
    else:
        raise DeserializationError(
            "CreateFindingsReportRequest.s3_destination required"
        )
    return out
