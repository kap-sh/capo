"""Generated from Smithy shape ``com.amazonaws.ec2#BundleTaskList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.bundle_task

BundleTaskList: TypeAlias = list["capo_ec2.types.bundle_task.BundleTask"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BundleTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.bundle_task

        capo_ec2.types.bundle_task.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> BundleTaskList:
    import capo_ec2.types.bundle_task

    out: BundleTaskList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.bundle_task.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> BundleTaskList:
    import capo_ec2.types.bundle_task

    out: BundleTaskList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.bundle_task.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: BundleTaskList) -> list[Any]:
    import capo_ec2.types.bundle_task

    return [capo_ec2.types.bundle_task.redact_sensitive(item) for item in value]
