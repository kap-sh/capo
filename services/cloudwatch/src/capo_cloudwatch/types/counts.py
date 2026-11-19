"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Counts``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.datapoint_value

Counts: TypeAlias = list["capo_cloudwatch.types.datapoint_value.DatapointValue"]


# --- awsQuery ser/de ---
def serialize_query(value: Counts, pairs: list[tuple[str, str]], prefix: str) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append(
            (
                f"{prefix}.member.{n}",
                (
                    "NaN"
                    if item != item
                    else "Infinity"
                    if item == float("inf")
                    else "-Infinity"
                    if item == float("-inf")
                    else str(item)
                ),
            )
        )


def deserialize_query(el: Element) -> Counts:
    out: Counts = []
    for child in el.findall("member"):
        out.append(float(child.text or ""))
    return out


def serialize_query_flat(
    value: Counts, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append(
            (
                f"{prefix}.{n}",
                (
                    "NaN"
                    if item != item
                    else "Infinity"
                    if item == float("inf")
                    else "-Infinity"
                    if item == float("-inf")
                    else str(item)
                ),
            )
        )


def deserialize_query_flat(parent: Element, tag: str) -> Counts:
    out: Counts = []
    for child in parent.findall(tag):
        out.append(float(child.text or ""))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Counts) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_aws_json_1_0(data: list) -> Counts:
    return [float(item) for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Counts) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Counts:
    return [float(item) for item in data if item is not None]
