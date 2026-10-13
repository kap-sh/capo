"""Generated from Smithy shape ``com.amazonaws.cloudfront#StringSchemaConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.parameter_value
    import capo_cloudfront.types.sensitive_string_type


class StringSchemaConfig(TypedDict, closed=True):
    comment: NotRequired[
        "capo_cloudfront.types.sensitive_string_type.sensitiveStringType"
    ]
    """<p>A comment to describe the parameter.</p>"""
    default_value: NotRequired["capo_cloudfront.types.parameter_value.ParameterValue"]
    """<p>The default value of the parameter.</p>"""
    required: "capo_cloudfront.types.boolean.boolean"
    """<p>Whether the defined parameter is required.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StringSchemaConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    if "default_value" in value:
        SubElement(el, "DefaultValue").text = str(value["default_value"])
    SubElement(el, "Required").text = "true" if value["required"] else "false"


def deserialize_xml(el: Element) -> StringSchemaConfig:
    out: StringSchemaConfig = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_required = el.find("Required")
    if child_required is not None:
        out["required"] = (child_required.text or "").lower() == "true"
    else:
        raise DeserializationError("StringSchemaConfig.required required")
    return out


def redact_sensitive(value: StringSchemaConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comment" in value:
        out["comment"] = "*** Sensitive Data Redacted ***"
    return out
