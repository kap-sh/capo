"""Generated from Smithy shape ``com.amazonaws.ec2#GetImageFindingsEntrySet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_finding

GetImageFindingsEntrySet: TypeAlias = list["capo_ec2.types.image_finding.ImageFinding"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetImageFindingsEntrySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.image_finding

        capo_ec2.types.image_finding.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> GetImageFindingsEntrySet:
    import capo_ec2.types.image_finding

    out: GetImageFindingsEntrySet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.image_finding.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> GetImageFindingsEntrySet:
    import capo_ec2.types.image_finding

    out: GetImageFindingsEntrySet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.image_finding.deserialize_ec2_query(child))
    return out
