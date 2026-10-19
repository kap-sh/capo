"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesDataPointFormInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.form_type_identifier
    import capo_datazone.types.revision
    import capo_datazone.types.time_series_form_name


class TimeSeriesDataPointFormInput(TypedDict, closed=True):
    form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series data points form.</p>"""
    type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The ID of the type of the time series data points form.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision type of the time series data points form.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of the time series data points form.</p>"""
    content: NotRequired["str"]
    """<p>The content of the time series data points form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesDataPointFormInput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    import capo_datazone.types._prelude.timestamp

    out["timestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> TimeSeriesDataPointFormInput:
    out: TimeSeriesDataPointFormInput = {}  # type: ignore[typeddict-item]
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
    if data.get("content") is not None:
        out["content"] = data["content"]
    return out
