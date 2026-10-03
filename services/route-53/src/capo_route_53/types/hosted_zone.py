"""Generated from Smithy shape ``com.amazonaws.route53#HostedZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.hosted_zone_config
    import capo_route_53.types.hosted_zone_features
    import capo_route_53.types.hosted_zone_rr_set_count
    import capo_route_53.types.linked_service
    import capo_route_53.types.nonce
    import capo_route_53.types.resource_id


class HostedZone(TypedDict, closed=True):
    id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID that Amazon Route 53 assigned to the hosted zone when you created it.</p>"""
    name: "capo_route_53.types.dns_name.DNSName"
    """<p>The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.</p> <p>For information about how to specify characters other than <code>a-z</code>, <code>0-9</code>, and <code>-</code> (hyphen) and how to specify internationalized domain names, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html">CreateHostedZone</a>.</p>"""
    caller_reference: "capo_route_53.types.nonce.Nonce"
    """<p>The value that you specified for <code>CallerReference</code> when you created the hosted zone.</p>"""
    config: NotRequired["capo_route_53.types.hosted_zone_config.HostedZoneConfig"]
    """<p>A complex type that includes the <code>Comment</code> and <code>PrivateZone</code> elements. If you omitted the <code>HostedZoneConfig</code> and <code>Comment</code> elements from the request, the <code>Config</code> and <code>Comment</code> elements don't appear in the response.</p>"""
    resource_record_set_count: NotRequired[
        "capo_route_53.types.hosted_zone_rr_set_count.HostedZoneRRSetCount"
    ]
    """<p>The number of resource record sets in the hosted zone.</p>"""
    linked_service: NotRequired["capo_route_53.types.linked_service.LinkedService"]
    """<p>If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can't edit or delete it using Route 53. </p>"""
    features: NotRequired["capo_route_53.types.hosted_zone_features.HostedZoneFeatures"]
    """<p>The features configuration for the hosted zone, including accelerated recovery settings and status information.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZone, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    if "config" in value:
        import capo_route_53.types.hosted_zone_config

        capo_route_53.types.hosted_zone_config.serialize_xml(
            value["config"], el, "Config"
        )
    if "resource_record_set_count" in value:
        SubElement(el, "ResourceRecordSetCount").text = str(
            value["resource_record_set_count"]
        )
    if "linked_service" in value:
        import capo_route_53.types.linked_service

        capo_route_53.types.linked_service.serialize_xml(
            value["linked_service"], el, "LinkedService"
        )
    if "features" in value:
        import capo_route_53.types.hosted_zone_features

        capo_route_53.types.hosted_zone_features.serialize_xml(
            value["features"], el, "Features"
        )


def deserialize_xml(el: Element) -> HostedZone:
    out: HostedZone = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("HostedZone.id required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("HostedZone.name required")
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        raise DeserializationError("HostedZone.caller_reference required")
    child_config = el.find("Config")
    if child_config is not None:
        import capo_route_53.types.hosted_zone_config

        out["config"] = capo_route_53.types.hosted_zone_config.deserialize_xml(
            child_config
        )
    child_resource_record_set_count = el.find("ResourceRecordSetCount")
    if child_resource_record_set_count is not None:
        out["resource_record_set_count"] = int(
            child_resource_record_set_count.text or ""
        )
    child_linked_service = el.find("LinkedService")
    if child_linked_service is not None:
        import capo_route_53.types.linked_service

        out["linked_service"] = capo_route_53.types.linked_service.deserialize_xml(
            child_linked_service
        )
    child_features = el.find("Features")
    if child_features is not None:
        import capo_route_53.types.hosted_zone_features

        out["features"] = capo_route_53.types.hosted_zone_features.deserialize_xml(
            child_features
        )
    return out
