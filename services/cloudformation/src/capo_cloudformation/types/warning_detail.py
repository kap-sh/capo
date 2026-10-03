"""Generated from Smithy shape ``com.amazonaws.cloudformation#WarningDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.warning_properties
    import capo_cloudformation.types.warning_type


class WarningDetail(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.warning_type.WarningType"]
    """<p>The type of this warning. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC-write-only-properties.html">Resolve write-only properties</a> in the <i>CloudFormation User Guide</i>.</p> <ul> <li> <p> <code>MUTUALLY_EXCLUSIVE_PROPERTIES</code> - The resource requires mutually-exclusive write-only properties. The IaC generator selects one set of mutually exclusive properties and converts the included properties into parameters. The parameter names have a suffix <code>OneOf</code> and the parameter descriptions indicate that the corresponding property can be replaced with other exclusive properties.</p> </li> <li> <p> <code>UNSUPPORTED_PROPERTIES</code> - Unsupported properties are present in the resource. One example of unsupported properties would be a required write-only property that is an array, because a parameter cannot be an array. Another example is an optional write-only property.</p> </li> <li> <p> <code>MUTUALLY_EXCLUSIVE_TYPES</code> - One or more required write-only properties are found in the resource, and the type of that property can be any of several types.</p> </li> </ul> <note> <p>Currently the resource and property reference documentation does not indicate if a property uses a type of <code>oneOf</code> or <code>anyOf</code>. You need to look at the resource provider schema.</p> </note>"""
    properties: NotRequired[
        "capo_cloudformation.types.warning_properties.WarningProperties"
    ]
    """<p>The properties of the resource that are impacted by this warning.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: WarningDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_cloudformation.types.warning_type

        capo_cloudformation.types.warning_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "properties" in value:
        import capo_cloudformation.types.warning_properties

        capo_cloudformation.types.warning_properties.serialize_query(
            value["properties"], pairs, f"{key_prefix}Properties"
        )


def deserialize_query(el: Element) -> WarningDetail:
    out: WarningDetail = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.warning_type

        out["type"] = capo_cloudformation.types.warning_type.deserialize_query(
            child_type
        )
    child_properties = el.find("Properties")
    if child_properties is not None:
        import capo_cloudformation.types.warning_properties

        out["properties"] = (
            capo_cloudformation.types.warning_properties.deserialize_query(
                child_properties
            )
        )
    return out
