"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DatapointValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.datapoint_value
    import capo_cloudwatch.types.extended_statistic

DatapointValueMap: TypeAlias = dict[
    "capo_cloudwatch.types.extended_statistic.ExtendedStatistic",
    "capo_cloudwatch.types.datapoint_value.DatapointValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: DatapointValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = (
            "NaN"
            if value != value
            else "Infinity"
            if value == float("inf")
            else "-Infinity"
            if value == float("-inf")
            else value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DatapointValueMap:
    out: DatapointValueMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: DatapointValueMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        pairs.append(
            (
                f"{prefix}.entry.{n}.value",
                (
                    "NaN"
                    if value != value
                    else "Infinity"
                    if value == float("inf")
                    else "-Infinity"
                    if value == float("-inf")
                    else str(value)
                ),
            )
        )


def deserialize_query(el: Element) -> DatapointValueMap:
    out: DatapointValueMap = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = float(str(value_element.text))
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: DatapointValueMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        pairs.append(
            (
                f"{prefix}.{n}.value",
                (
                    "NaN"
                    if value != value
                    else "Infinity"
                    if value == float("inf")
                    else "-Infinity"
                    if value == float("-inf")
                    else str(value)
                ),
            )
        )


def deserialize_query_flat(parent: Element, tag: str) -> DatapointValueMap:
    out: DatapointValueMap = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = float(str(value_element.text))
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: DatapointValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> DatapointValueMap:
    out: DatapointValueMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out
