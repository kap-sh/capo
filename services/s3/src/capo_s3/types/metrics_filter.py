"""Generated from Smithy shape ``com.amazonaws.s3#MetricsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError, SerializationError
from capo_s3.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3.types.access_point_arn
    import capo_s3.types.metrics_and_operator
    import capo_s3.types.prefix
    import capo_s3.types.tag


class _MetricsFilter_Prefix(TypedDict, closed=True):
    Prefix: "capo_s3.types.prefix.Prefix"


class _MetricsFilter_Tag(TypedDict, closed=True):
    Tag: "capo_s3.types.tag.Tag"


class _MetricsFilter_AccessPointArn(TypedDict, closed=True):
    AccessPointArn: "capo_s3.types.access_point_arn.AccessPointArn"


class _MetricsFilter_And(TypedDict, closed=True):
    And: "capo_s3.types.metrics_and_operator.MetricsAndOperator"


MetricsFilter: TypeAlias = (
    _MetricsFilter_Prefix
    | _MetricsFilter_Tag
    | _MetricsFilter_AccessPointArn
    | _MetricsFilter_And
    | UnknownUnionMember
)


# --- restXml ser/de ---
def serialize_xml(value: MetricsFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "$unknown" in value:
        raise SerializationError(
            f"MetricsFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Prefix" in value:
        SubElement(el, "Prefix").text = str(value["Prefix"])
    elif "Tag" in value:
        import capo_s3.types.tag

        capo_s3.types.tag.serialize_xml(value["Tag"], el, "Tag")
    elif "AccessPointArn" in value:
        SubElement(el, "AccessPointArn").text = str(value["AccessPointArn"])
    elif "And" in value:
        import capo_s3.types.metrics_and_operator

        capo_s3.types.metrics_and_operator.serialize_xml(value["And"], el, "And")
    else:
        raise SerializationError("MetricsFilter: no variant present")


def deserialize_xml(el: Element) -> MetricsFilter:
    for child in el:
        if child.tag == "Prefix":
            return {"Prefix": str(child.text or "")}
        elif child.tag == "Tag":
            import capo_s3.types.tag

            return {"Tag": capo_s3.types.tag.deserialize_xml(child)}
        elif child.tag == "AccessPointArn":
            return {"AccessPointArn": str(child.text or "")}
        elif child.tag == "And":
            import capo_s3.types.metrics_and_operator

            return {"And": capo_s3.types.metrics_and_operator.deserialize_xml(child)}
        else:
            return {"$unknown": {"name": child.tag}}
    raise DeserializationError("MetricsFilter: no recognized variant element")
