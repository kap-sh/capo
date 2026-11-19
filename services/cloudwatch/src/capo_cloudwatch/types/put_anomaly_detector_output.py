"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutAnomalyDetectorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.anomaly_detector_id


class PutAnomalyDetectorOutput(TypedDict, closed=True):
    anomaly_detector_id: NotRequired[
        "capo_cloudwatch.types.anomaly_detector_id.AnomalyDetectorId"
    ]
    """<p>The unique identifier of the anomaly detector that you created or updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutAnomalyDetectorOutput) -> dict:
    out: dict = {}
    if "anomaly_detector_id" in value:
        out["AnomalyDetectorId"] = value["anomaly_detector_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutAnomalyDetectorOutput:
    out: PutAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyDetectorId") is not None:
        out["anomaly_detector_id"] = data["AnomalyDetectorId"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutAnomalyDetectorOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "anomaly_detector_id" in value:
        pairs.append(
            (f"{key_prefix}AnomalyDetectorId", str(value["anomaly_detector_id"]))
        )


def deserialize_query(el: Element) -> PutAnomalyDetectorOutput:
    out: PutAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    child_anomaly_detector_id = el.find("AnomalyDetectorId")
    if child_anomaly_detector_id is not None:
        out["anomaly_detector_id"] = str(child_anomaly_detector_id.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutAnomalyDetectorOutput) -> dict:
    out: dict = {}
    if "anomaly_detector_id" in value:
        out["AnomalyDetectorId"] = value["anomaly_detector_id"]
    return out


def deserialize_cbor(data: dict) -> PutAnomalyDetectorOutput:
    out: PutAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyDetectorId") is not None:
        out["anomaly_detector_id"] = data["AnomalyDetectorId"]
    return out
