"""Generated from Smithy shape ``com.amazonaws.s3#FilterRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.filter_rule_name
    import capo_s3.types.filter_rule_value


class FilterRule(TypedDict, closed=True):
    name: NotRequired["capo_s3.types.filter_rule_name.FilterRuleName"]
    """<p>The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html">Configuring Event Notifications</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    value: NotRequired["capo_s3.types.filter_rule_value.FilterRuleValue"]
    """<p>The value that the filter searches for in object key names.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FilterRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        import capo_s3.types.filter_rule_name

        capo_s3.types.filter_rule_name.serialize_xml(value["name"], el, "Name")
    if "value" in value:
        SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> FilterRule:
    out: FilterRule = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        import capo_s3.types.filter_rule_name

        out["name"] = capo_s3.types.filter_rule_name.deserialize_xml(child_name)
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
