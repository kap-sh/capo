"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#GetReportDefinitionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_applicationcostprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.format
    import capo_applicationcostprofiler.types.report_description
    import capo_applicationcostprofiler.types.report_frequency
    import capo_applicationcostprofiler.types.report_id
    import capo_applicationcostprofiler.types.s3_location
    import capo_applicationcostprofiler.types.timestamp


class GetReportDefinitionResult(TypedDict, closed=True):
    report_id: "capo_applicationcostprofiler.types.report_id.ReportId"
    """<p>ID of the report retrieved.</p>"""
    report_description: (
        "capo_applicationcostprofiler.types.report_description.ReportDescription"
    )
    """<p>Description of the report.</p>"""
    report_frequency: (
        "capo_applicationcostprofiler.types.report_frequency.ReportFrequency"
    )
    """<p>Cadence used to generate the report.</p>"""
    format: "capo_applicationcostprofiler.types.format.Format"
    """<p>Format of the generated report.</p>"""
    destination_s3_location: "capo_applicationcostprofiler.types.s3_location.S3Location"
    """<p>Amazon Simple Storage Service (Amazon S3) location where the report is uploaded.</p>"""
    created_at: "capo_applicationcostprofiler.types.timestamp.Timestamp"
    """<p>Timestamp (milliseconds) when this report definition was created.</p>"""
    last_updated: "capo_applicationcostprofiler.types.timestamp.Timestamp"
    """<p>Timestamp (milliseconds) when this report definition was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReportDefinitionResult) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    out["reportDescription"] = value["report_description"]
    import capo_applicationcostprofiler.types.report_frequency

    out["reportFrequency"] = (
        capo_applicationcostprofiler.types.report_frequency.serialize_json(
            value["report_frequency"]
        )
    )
    import capo_applicationcostprofiler.types.format

    out["format"] = capo_applicationcostprofiler.types.format.serialize_json(
        value["format"]
    )
    import capo_applicationcostprofiler.types.s3_location

    out["destinationS3Location"] = (
        capo_applicationcostprofiler.types.s3_location.serialize_json(
            value["destination_s3_location"]
        )
    )
    import capo_applicationcostprofiler.types.timestamp

    out["createdAt"] = capo_applicationcostprofiler.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_applicationcostprofiler.types.timestamp

    out["lastUpdated"] = capo_applicationcostprofiler.types.timestamp.serialize_json(
        value["last_updated"]
    )
    return out


def deserialize_json(data: dict) -> GetReportDefinitionResult:
    out: GetReportDefinitionResult = {}  # type: ignore[typeddict-item]
    if data.get("reportId") is not None:
        out["report_id"] = data["reportId"]
    else:
        out["report_id"] = ""
    if data.get("reportDescription") is not None:
        out["report_description"] = data["reportDescription"]
    else:
        out["report_description"] = ""
    if data.get("reportFrequency") is not None:
        import capo_applicationcostprofiler.types.report_frequency

        out["report_frequency"] = (
            capo_applicationcostprofiler.types.report_frequency.deserialize_json(
                data["reportFrequency"]
            )
        )
    else:
        import typing

        out["report_frequency"] = typing.cast(
            "capo_applicationcostprofiler.types.report_frequency.ReportFrequency", ""
        )
    if data.get("format") is not None:
        import capo_applicationcostprofiler.types.format

        out["format"] = capo_applicationcostprofiler.types.format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_applicationcostprofiler.types.format.Format", ""
        )
    if data.get("destinationS3Location") is not None:
        import capo_applicationcostprofiler.types.s3_location

        out["destination_s3_location"] = (
            capo_applicationcostprofiler.types.s3_location.deserialize_json(
                data["destinationS3Location"]
            )
        )
    else:
        raise DeserializationError(
            "GetReportDefinitionResult.destination_s3_location required"
        )
    if data.get("createdAt") is not None:
        import capo_applicationcostprofiler.types.timestamp

        out["created_at"] = (
            capo_applicationcostprofiler.types.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdated") is not None:
        import capo_applicationcostprofiler.types.timestamp

        out["last_updated"] = (
            capo_applicationcostprofiler.types.timestamp.deserialize_json(
                data["lastUpdated"]
            )
        )
    else:
        import datetime

        out["last_updated"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
