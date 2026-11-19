"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAnomalyDetectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.anomaly_detectors
    import capo_cloudwatch.types.next_token


class DescribeAnomalyDetectorsOutput(TypedDict, closed=True):
    anomaly_detectors: NotRequired[
        "capo_cloudwatch.types.anomaly_detectors.AnomalyDetectors"
    ]
    """<p>The list of anomaly detection models returned by the operation.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAnomalyDetectorsOutput) -> dict:
    out: dict = {}
    if "anomaly_detectors" in value:
        import capo_cloudwatch.types.anomaly_detectors

        out["AnomalyDetectors"] = (
            capo_cloudwatch.types.anomaly_detectors.serialize_aws_json_1_0(
                value["anomaly_detectors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAnomalyDetectorsOutput:
    out: DescribeAnomalyDetectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyDetectors") is not None:
        import capo_cloudwatch.types.anomaly_detectors

        out["anomaly_detectors"] = (
            capo_cloudwatch.types.anomaly_detectors.deserialize_aws_json_1_0(
                data["AnomalyDetectors"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAnomalyDetectorsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "anomaly_detectors" in value:
        import capo_cloudwatch.types.anomaly_detectors

        capo_cloudwatch.types.anomaly_detectors.serialize_query(
            value["anomaly_detectors"], pairs, f"{key_prefix}AnomalyDetectors"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAnomalyDetectorsOutput:
    out: DescribeAnomalyDetectorsOutput = {}  # type: ignore[typeddict-item]
    child_anomaly_detectors = el.find("AnomalyDetectors")
    if child_anomaly_detectors is not None:
        import capo_cloudwatch.types.anomaly_detectors

        out["anomaly_detectors"] = (
            capo_cloudwatch.types.anomaly_detectors.deserialize_query(
                child_anomaly_detectors
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAnomalyDetectorsOutput) -> dict:
    out: dict = {}
    if "anomaly_detectors" in value:
        import capo_cloudwatch.types.anomaly_detectors

        out["AnomalyDetectors"] = (
            capo_cloudwatch.types.anomaly_detectors.serialize_cbor(
                value["anomaly_detectors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAnomalyDetectorsOutput:
    out: DescribeAnomalyDetectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("AnomalyDetectors") is not None:
        import capo_cloudwatch.types.anomaly_detectors

        out["anomaly_detectors"] = (
            capo_cloudwatch.types.anomaly_detectors.deserialize_cbor(
                data["AnomalyDetectors"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
