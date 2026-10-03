"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_group_failover_criteria
    import capo_cloudfront.types.origin_group_members
    import capo_cloudfront.types.origin_group_selection_criteria
    import capo_cloudfront.types.string


class OriginGroup(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The origin group's ID.</p>"""
    failover_criteria: "capo_cloudfront.types.origin_group_failover_criteria.OriginGroupFailoverCriteria"
    """<p>A complex type that contains information about the failover criteria for an origin group.</p>"""
    members: "capo_cloudfront.types.origin_group_members.OriginGroupMembers"
    """<p>A complex type that contains information about the origins in an origin group.</p>"""
    selection_criteria: NotRequired[
        "capo_cloudfront.types.origin_group_selection_criteria.OriginGroupSelectionCriteria"
    ]
    """<p>The selection criteria for the origin group. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html#concept_origin_groups.creating">Create an origin group</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginGroup, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.origin_group_failover_criteria

    capo_cloudfront.types.origin_group_failover_criteria.serialize_xml(
        value["failover_criteria"], el, "FailoverCriteria"
    )
    import capo_cloudfront.types.origin_group_members

    capo_cloudfront.types.origin_group_members.serialize_xml(
        value["members"], el, "Members"
    )
    if "selection_criteria" in value:
        import capo_cloudfront.types.origin_group_selection_criteria

        capo_cloudfront.types.origin_group_selection_criteria.serialize_xml(
            value["selection_criteria"], el, "SelectionCriteria"
        )


def deserialize_xml(el: Element) -> OriginGroup:
    out: OriginGroup = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("OriginGroup.id required")
    child_failover_criteria = el.find("FailoverCriteria")
    if child_failover_criteria is not None:
        import capo_cloudfront.types.origin_group_failover_criteria

        out["failover_criteria"] = (
            capo_cloudfront.types.origin_group_failover_criteria.deserialize_xml(
                child_failover_criteria
            )
        )
    else:
        raise DeserializationError("OriginGroup.failover_criteria required")
    child_members = el.find("Members")
    if child_members is not None:
        import capo_cloudfront.types.origin_group_members

        out["members"] = capo_cloudfront.types.origin_group_members.deserialize_xml(
            child_members
        )
    else:
        raise DeserializationError("OriginGroup.members required")
    child_selection_criteria = el.find("SelectionCriteria")
    if child_selection_criteria is not None:
        import capo_cloudfront.types.origin_group_selection_criteria

        out["selection_criteria"] = (
            capo_cloudfront.types.origin_group_selection_criteria.deserialize_xml(
                child_selection_criteria
            )
        )
    return out
