"""Generated from Smithy shape ``com.amazonaws.s3#BucketLifecycleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.lifecycle_rules


class BucketLifecycleConfiguration(TypedDict, closed=True):
    rules: "capo_s3.types.lifecycle_rules.LifecycleRules"
    """<p>A lifecycle rule for individual objects in an Amazon S3 bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: BucketLifecycleConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.lifecycle_rules

    capo_s3.types.lifecycle_rules.serialize_xml_flat(value["rules"], el, "Rule")


def deserialize_xml(el: Element) -> BucketLifecycleConfiguration:
    out: BucketLifecycleConfiguration = {}  # type: ignore[typeddict-item]
    if el.find("Rule") is not None:
        import capo_s3.types.lifecycle_rules

        out["rules"] = capo_s3.types.lifecycle_rules.deserialize_xml_flat(el, "Rule")
    else:
        out["rules"] = []
    return out
