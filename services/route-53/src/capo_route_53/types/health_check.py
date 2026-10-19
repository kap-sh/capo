"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.cloud_watch_alarm_configuration
    import capo_route_53.types.health_check_config
    import capo_route_53.types.health_check_id
    import capo_route_53.types.health_check_nonce
    import capo_route_53.types.health_check_version
    import capo_route_53.types.linked_service


class HealthCheck(TypedDict, closed=True):
    id: "capo_route_53.types.health_check_id.HealthCheckId"
    """<p>The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long. </p>"""
    caller_reference: "capo_route_53.types.health_check_nonce.HealthCheckNonce"
    """<p>A unique string that you specified when you created the health check.</p>"""
    linked_service: NotRequired["capo_route_53.types.linked_service.LinkedService"]
    """<p>If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can't edit or delete it using Amazon Route 53. </p>"""
    health_check_config: "capo_route_53.types.health_check_config.HealthCheckConfig"
    """<p>A complex type that contains detailed information about one health check.</p>"""
    health_check_version: "capo_route_53.types.health_check_version.HealthCheckVersion"
    """<p>The version of the health check. You can optionally pass this value in a call to <code>UpdateHealthCheck</code> to prevent overwriting another change to the health check.</p>"""
    cloud_watch_alarm_configuration: NotRequired[
        "capo_route_53.types.cloud_watch_alarm_configuration.CloudWatchAlarmConfiguration"
    ]
    """<p>A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HealthCheck, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    if "linked_service" in value:
        import capo_route_53.types.linked_service

        capo_route_53.types.linked_service.serialize_xml(
            value["linked_service"], el, "LinkedService"
        )
    import capo_route_53.types.health_check_config

    capo_route_53.types.health_check_config.serialize_xml(
        value["health_check_config"], el, "HealthCheckConfig"
    )
    SubElement(el, "HealthCheckVersion").text = str(value["health_check_version"])
    if "cloud_watch_alarm_configuration" in value:
        import capo_route_53.types.cloud_watch_alarm_configuration

        capo_route_53.types.cloud_watch_alarm_configuration.serialize_xml(
            value["cloud_watch_alarm_configuration"], el, "CloudWatchAlarmConfiguration"
        )


def deserialize_xml(el: Element) -> HealthCheck:
    out: HealthCheck = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        out["caller_reference"] = ""
    child_linked_service = el.find("LinkedService")
    if child_linked_service is not None:
        import capo_route_53.types.linked_service

        out["linked_service"] = capo_route_53.types.linked_service.deserialize_xml(
            child_linked_service
        )
    child_health_check_config = el.find("HealthCheckConfig")
    if child_health_check_config is not None:
        import capo_route_53.types.health_check_config

        out["health_check_config"] = (
            capo_route_53.types.health_check_config.deserialize_xml(
                child_health_check_config
            )
        )
    else:
        raise DeserializationError("HealthCheck.health_check_config required")
    child_health_check_version = el.find("HealthCheckVersion")
    if child_health_check_version is not None:
        out["health_check_version"] = int(child_health_check_version.text or "")
    else:
        out["health_check_version"] = 0
    child_cloud_watch_alarm_configuration = el.find("CloudWatchAlarmConfiguration")
    if child_cloud_watch_alarm_configuration is not None:
        import capo_route_53.types.cloud_watch_alarm_configuration

        out["cloud_watch_alarm_configuration"] = (
            capo_route_53.types.cloud_watch_alarm_configuration.deserialize_xml(
                child_cloud_watch_alarm_configuration
            )
        )
    return out
