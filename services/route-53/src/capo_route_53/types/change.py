"""Generated from Smithy shape ``com.amazonaws.route53#Change``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.change_action
    import capo_route_53.types.resource_record_set


class Change(TypedDict, closed=True):
    action: "capo_route_53.types.change_action.ChangeAction"
    """<p>The action to perform:</p> <ul> <li> <p> <code>CREATE</code>: Creates a resource record set that has the specified values.</p> </li> <li> <p> <code>DELETE</code>: Deletes a existing resource record set.</p> <important> <p>To delete the resource record set that is associated with a traffic policy instance, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicyInstance.html">DeleteTrafficPolicyInstance</a>. Amazon Route 53 will delete the resource record set automatically. If you delete the resource record set by using <code>ChangeResourceRecordSets</code>, Route 53 doesn't automatically delete the traffic policy instance, and you'll continue to be charged for it even though it's no longer in use. </p> </important> </li> <li> <p> <code>UPSERT</code>: If a resource record set doesn't already exist, Route 53 creates it. If a resource record set does exist, Route 53 updates it with the values in the request.</p> </li> </ul>"""
    resource_record_set: "capo_route_53.types.resource_record_set.ResourceRecordSet"
    """<p>Information about the resource record set to create, delete, or update.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Change, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.change_action

    capo_route_53.types.change_action.serialize_xml(value["action"], el, "Action")
    import capo_route_53.types.resource_record_set

    capo_route_53.types.resource_record_set.serialize_xml(
        value["resource_record_set"], el, "ResourceRecordSet"
    )


def deserialize_xml(el: Element) -> Change:
    out: Change = {}  # type: ignore[typeddict-item]
    child_action = el.find("Action")
    if child_action is not None:
        import capo_route_53.types.change_action

        out["action"] = capo_route_53.types.change_action.deserialize_xml(child_action)
    else:
        raise DeserializationError("Change.action required")
    child_resource_record_set = el.find("ResourceRecordSet")
    if child_resource_record_set is not None:
        import capo_route_53.types.resource_record_set

        out["resource_record_set"] = (
            capo_route_53.types.resource_record_set.deserialize_xml(
                child_resource_record_set
            )
        )
    else:
        raise DeserializationError("Change.resource_record_set required")
    return out
