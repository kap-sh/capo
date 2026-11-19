"""Generated from Smithy shape ``com.amazonaws.ec2#MetricCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.metric_category

MetricCategoryList: TypeAlias = list["capo_ec2.types.metric_category.MetricCategory"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricCategoryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.metric_category

        capo_ec2.types.metric_category.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> MetricCategoryList:
    import capo_ec2.types.metric_category

    out: MetricCategoryList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.metric_category.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> MetricCategoryList:
    import capo_ec2.types.metric_category

    out: MetricCategoryList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.metric_category.deserialize_ec2_query(child))
    return out
