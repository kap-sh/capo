"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ResourceMetricSelectionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.resource_metric_selection

ResourceMetricSelectionList: TypeAlias = list[
    "capo_cloudwatch.types.resource_metric_selection.ResourceMetricSelection"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceMetricSelectionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.resource_metric_selection

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.resource_metric_selection.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ResourceMetricSelectionList:
    import capo_cloudwatch.types.resource_metric_selection

    out: ResourceMetricSelectionList = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.resource_metric_selection.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ResourceMetricSelectionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.resource_metric_selection

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.resource_metric_selection.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ResourceMetricSelectionList:
    import capo_cloudwatch.types.resource_metric_selection

    out: ResourceMetricSelectionList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.resource_metric_selection.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceMetricSelectionList) -> list:
    import capo_cloudwatch.types.resource_metric_selection

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.resource_metric_selection.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceMetricSelectionList:
    import capo_cloudwatch.types.resource_metric_selection

    out: ResourceMetricSelectionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.resource_metric_selection.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceMetricSelectionList) -> list:
    import capo_cloudwatch.types.resource_metric_selection

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.resource_metric_selection.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ResourceMetricSelectionList:
    import capo_cloudwatch.types.resource_metric_selection

    out: ResourceMetricSelectionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.resource_metric_selection.deserialize_cbor(item)
        )
    return out
