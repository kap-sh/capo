"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.anomaly_detector_status_code


class AnomalyDetectorStatus(TypedDict, closed=True):
    status_code: "capo_amp.types.anomaly_detector_status_code.AnomalyDetectorStatusCode"
    """<p>The status code of the anomaly detector.</p>"""
    status_reason: NotRequired["str"]
    """<p>A description of the current status of the anomaly detector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorStatus) -> dict:
    out: dict = {}
    import capo_amp.types.anomaly_detector_status_code

    out["statusCode"] = capo_amp.types.anomaly_detector_status_code.serialize_json(
        value["status_code"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> AnomalyDetectorStatus:
    out: AnomalyDetectorStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        import capo_amp.types.anomaly_detector_status_code

        out["status_code"] = (
            capo_amp.types.anomaly_detector_status_code.deserialize_json(
                data["statusCode"]
            )
        )
    else:
        import typing

        out["status_code"] = typing.cast(
            "capo_amp.types.anomaly_detector_status_code.AnomalyDetectorStatusCode", ""
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
