"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectors``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.anomaly_detector

AnomalyDetectors: TypeAlias = list[
    "capo_cloudwatch.types.anomaly_detector.AnomalyDetector"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AnomalyDetectors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.anomaly_detector

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.anomaly_detector.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AnomalyDetectors:
    import capo_cloudwatch.types.anomaly_detector

    out: AnomalyDetectors = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.anomaly_detector.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AnomalyDetectors, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.anomaly_detector

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.anomaly_detector.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AnomalyDetectors:
    import capo_cloudwatch.types.anomaly_detector

    out: AnomalyDetectors = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.anomaly_detector.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetectors) -> list:
    import capo_cloudwatch.types.anomaly_detector

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.anomaly_detector.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AnomalyDetectors:
    import capo_cloudwatch.types.anomaly_detector

    out: AnomalyDetectors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.anomaly_detector.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnomalyDetectors) -> list:
    import capo_cloudwatch.types.anomaly_detector

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.anomaly_detector.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AnomalyDetectors:
    import capo_cloudwatch.types.anomaly_detector

    out: AnomalyDetectors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.anomaly_detector.deserialize_cbor(item))
    return out
