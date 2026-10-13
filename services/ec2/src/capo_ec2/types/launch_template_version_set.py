"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateVersionSet``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_version

LaunchTemplateVersionSet: TypeAlias = list[
    "capo_ec2.types.launch_template_version.LaunchTemplateVersion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateVersionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_template_version

        capo_ec2.types.launch_template_version.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateVersionSet:
    import capo_ec2.types.launch_template_version

    out: LaunchTemplateVersionSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.launch_template_version.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LaunchTemplateVersionSet:
    import capo_ec2.types.launch_template_version

    out: LaunchTemplateVersionSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.launch_template_version.deserialize_ec2_query(child))
    return out


def redact_sensitive(value: LaunchTemplateVersionSet) -> list[Any]:
    import capo_ec2.types.launch_template_version

    return [
        capo_ec2.types.launch_template_version.redact_sensitive(item) for item in value
    ]
