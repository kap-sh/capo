"""Generated from Smithy shape ``com.amazonaws.appmesh#OutlierDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.duration
    import capo_app_mesh.types.outlier_detection_max_ejection_percent
    import capo_app_mesh.types.outlier_detection_max_server_errors


class OutlierDetection(TypedDict, closed=True):
    max_server_errors: "capo_app_mesh.types.outlier_detection_max_server_errors.OutlierDetectionMaxServerErrors"
    """<p>Number of consecutive <code>5xx</code> errors required for ejection. </p>"""
    interval: "capo_app_mesh.types.duration.Duration"
    """<p>The time interval between ejection sweep analysis.</p>"""
    base_ejection_duration: "capo_app_mesh.types.duration.Duration"
    """<p>The base amount of time for which a host is ejected.</p>"""
    max_ejection_percent: "capo_app_mesh.types.outlier_detection_max_ejection_percent.OutlierDetectionMaxEjectionPercent"
    """<p>Maximum percentage of hosts in load balancing pool for upstream service that can be ejected. Will eject at least one host regardless of the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutlierDetection) -> dict:
    out: dict = {}
    out["maxServerErrors"] = value["max_server_errors"]
    import capo_app_mesh.types.duration

    out["interval"] = capo_app_mesh.types.duration.serialize_json(value["interval"])
    import capo_app_mesh.types.duration

    out["baseEjectionDuration"] = capo_app_mesh.types.duration.serialize_json(
        value["base_ejection_duration"]
    )
    out["maxEjectionPercent"] = value["max_ejection_percent"]
    return out


def deserialize_json(data: dict) -> OutlierDetection:
    out: OutlierDetection = {}  # type: ignore[typeddict-item]
    if data.get("maxServerErrors") is not None:
        out["max_server_errors"] = data["maxServerErrors"]
    else:
        out["max_server_errors"] = 0
    if data.get("interval") is not None:
        import capo_app_mesh.types.duration

        out["interval"] = capo_app_mesh.types.duration.deserialize_json(
            data["interval"]
        )
    else:
        raise DeserializationError("OutlierDetection.interval required")
    if data.get("baseEjectionDuration") is not None:
        import capo_app_mesh.types.duration

        out["base_ejection_duration"] = capo_app_mesh.types.duration.deserialize_json(
            data["baseEjectionDuration"]
        )
    else:
        raise DeserializationError("OutlierDetection.base_ejection_duration required")
    if data.get("maxEjectionPercent") is not None:
        out["max_ejection_percent"] = data["maxEjectionPercent"]
    else:
        out["max_ejection_percent"] = 0
    return out
