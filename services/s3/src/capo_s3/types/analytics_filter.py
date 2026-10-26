"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError, SerializationError
from capo_s3.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3.types.analytics_and_operator
    import capo_s3.types.prefix
    import capo_s3.types.tag


class _AnalyticsFilter_Prefix(TypedDict, closed=True):
    Prefix: "capo_s3.types.prefix.Prefix"


class _AnalyticsFilter_Tag(TypedDict, closed=True):
    Tag: "capo_s3.types.tag.Tag"


class _AnalyticsFilter_And(TypedDict, closed=True):
    And: "capo_s3.types.analytics_and_operator.AnalyticsAndOperator"


AnalyticsFilter: TypeAlias = (
    _AnalyticsFilter_Prefix
    | _AnalyticsFilter_Tag
    | _AnalyticsFilter_And
    | UnknownUnionMember
)


# --- restXml ser/de ---
def serialize_xml(value: AnalyticsFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "$unknown" in value:
        raise SerializationError(
            f"AnalyticsFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Prefix" in value:
        SubElement(el, "Prefix").text = str(value["Prefix"])
    elif "Tag" in value:
        import capo_s3.types.tag

        capo_s3.types.tag.serialize_xml(value["Tag"], el, "Tag")
    elif "And" in value:
        import capo_s3.types.analytics_and_operator

        capo_s3.types.analytics_and_operator.serialize_xml(value["And"], el, "And")
    else:
        raise SerializationError("AnalyticsFilter: no variant present")


def deserialize_xml(el: Element) -> AnalyticsFilter:
    for child in el:
        if child.tag == "Prefix":
            return {"Prefix": str(child.text or "")}
        elif child.tag == "Tag":
            import capo_s3.types.tag

            return {"Tag": capo_s3.types.tag.deserialize_xml(child)}
        elif child.tag == "And":
            import capo_s3.types.analytics_and_operator

            return {"And": capo_s3.types.analytics_and_operator.deserialize_xml(child)}
        else:
            return {"$unknown": {"name": child.tag}}
    raise DeserializationError("AnalyticsFilter: no recognized variant element")
