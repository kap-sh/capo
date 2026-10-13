"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTaskList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.conversion_task

DescribeConversionTaskList: TypeAlias = list[
    "capo_ec2.types.conversion_task.ConversionTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeConversionTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.conversion_task

        capo_ec2.types.conversion_task.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> DescribeConversionTaskList:
    import capo_ec2.types.conversion_task

    out: DescribeConversionTaskList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.conversion_task.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> DescribeConversionTaskList:
    import capo_ec2.types.conversion_task

    out: DescribeConversionTaskList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.conversion_task.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: DescribeConversionTaskList) -> list[Any]:
    import capo_ec2.types.conversion_task

    return [capo_ec2.types.conversion_task.redact_sensitive(item) for item in value]
