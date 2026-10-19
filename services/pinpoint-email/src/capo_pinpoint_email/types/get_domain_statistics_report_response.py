"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetDomainStatisticsReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.daily_volumes
    import capo_pinpoint_email.types.overall_volume


class GetDomainStatisticsReportResponse(TypedDict, closed=True):
    overall_volume: "capo_pinpoint_email.types.overall_volume.OverallVolume"
    """<p>An object that contains deliverability metrics for the domain that you specified. The data in this object is a summary of all of the data that was collected from the <code>StartDate</code> to the <code>EndDate</code>.</p>"""
    daily_volumes: "capo_pinpoint_email.types.daily_volumes.DailyVolumes"
    """<p>An object that contains deliverability metrics for the domain that you specified. This object contains data for each day, starting on the <code>StartDate</code> and ending on the <code>EndDate</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainStatisticsReportResponse) -> dict:
    out: dict = {}
    import capo_pinpoint_email.types.overall_volume

    out["OverallVolume"] = capo_pinpoint_email.types.overall_volume.serialize_json(
        value["overall_volume"]
    )
    import capo_pinpoint_email.types.daily_volumes

    out["DailyVolumes"] = capo_pinpoint_email.types.daily_volumes.serialize_json(
        value["daily_volumes"]
    )
    return out


def deserialize_json(data: dict) -> GetDomainStatisticsReportResponse:
    out: GetDomainStatisticsReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("OverallVolume") is not None:
        import capo_pinpoint_email.types.overall_volume

        out["overall_volume"] = (
            capo_pinpoint_email.types.overall_volume.deserialize_json(
                data["OverallVolume"]
            )
        )
    else:
        raise DeserializationError(
            "GetDomainStatisticsReportResponse.overall_volume required"
        )
    if data.get("DailyVolumes") is not None:
        import capo_pinpoint_email.types.daily_volumes

        out["daily_volumes"] = capo_pinpoint_email.types.daily_volumes.deserialize_json(
            data["DailyVolumes"]
        )
    else:
        out["daily_volumes"] = []
    return out
