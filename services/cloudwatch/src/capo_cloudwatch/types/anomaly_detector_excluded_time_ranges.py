"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorExcludedTimeRanges``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.range

AnomalyDetectorExcludedTimeRanges: TypeAlias = list["capo_cloudwatch.types.range.Range"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AnomalyDetectorExcludedTimeRanges, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.range

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.range.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> AnomalyDetectorExcludedTimeRanges:
    import capo_cloudwatch.types.range

    out: AnomalyDetectorExcludedTimeRanges = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.range.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AnomalyDetectorExcludedTimeRanges, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.range

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.range.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(
    parent: Element, tag: str
) -> AnomalyDetectorExcludedTimeRanges:
    import capo_cloudwatch.types.range

    out: AnomalyDetectorExcludedTimeRanges = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.range.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetectorExcludedTimeRanges) -> list:
    import capo_cloudwatch.types.range

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.range.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AnomalyDetectorExcludedTimeRanges:
    import capo_cloudwatch.types.range

    out: AnomalyDetectorExcludedTimeRanges = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.range.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnomalyDetectorExcludedTimeRanges) -> list:
    import capo_cloudwatch.types.range

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.range.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AnomalyDetectorExcludedTimeRanges:
    import capo_cloudwatch.types.range

    out: AnomalyDetectorExcludedTimeRanges = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.range.deserialize_cbor(item))
    return out
