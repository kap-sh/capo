"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageTaskList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.import_image_task

ImportImageTaskList: TypeAlias = list[
    "capo_ec2.types.import_image_task.ImportImageTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportImageTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.import_image_task

        capo_ec2.types.import_image_task.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ImportImageTaskList:
    import capo_ec2.types.import_image_task

    out: ImportImageTaskList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.import_image_task.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ImportImageTaskList:
    import capo_ec2.types.import_image_task

    out: ImportImageTaskList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.import_image_task.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: ImportImageTaskList) -> list[Any]:
    import capo_ec2.types.import_image_task

    return [capo_ec2.types.import_image_task.redact_sensitive(item) for item in value]
