"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesDataPointSummaryFormOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.data_point_identifier
    import capo_datazone.types.form_type_identifier
    import capo_datazone.types.revision
    import capo_datazone.types.time_series_form_name


class TimeSeriesDataPointSummaryFormOutput(TypedDict, closed=True):
    form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series data points summary form.</p>"""
    type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The type ID of the time series data points summary form.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The type revision of the time series data points summary form.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of the time series data points summary form.</p>"""
    content_summary: NotRequired["str"]
    """<p>The content of the summary of the time series data points form.</p>"""
    id: NotRequired["capo_datazone.types.data_point_identifier.DataPointIdentifier"]
    """<p>The ID of the time series data points summary form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesDataPointSummaryFormOutput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    import capo_datazone.types._prelude.timestamp

    out["timestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "content_summary" in value:
        out["contentSummary"] = value["content_summary"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> TimeSeriesDataPointSummaryFormOutput:
    out: TimeSeriesDataPointSummaryFormOutput = {}  # type: ignore[typeddict-item]
    if data.get("formName") is not None:
        out["form_name"] = data["formName"]
    else:
        out["form_name"] = ""
    if data.get("typeIdentifier") is not None:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        out["type_identifier"] = ""
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    if data.get("timestamp") is not None:
        import capo_datazone.types._prelude.timestamp

        out["timestamp"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("contentSummary") is not None:
        out["content_summary"] = data["contentSummary"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out
