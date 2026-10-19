"""Generated from Smithy shape ``com.amazonaws.route53#CreateHealthCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.health_check_config
    import capo_route_53.types.health_check_nonce


class CreateHealthCheckRequest(TypedDict, closed=True):
    caller_reference: "capo_route_53.types.health_check_nonce.HealthCheckNonce"
    """<p>A unique string that identifies the request and that allows you to retry a failed <code>CreateHealthCheck</code> request without the risk of creating two identical health checks:</p> <ul> <li> <p>If you send a <code>CreateHealthCheck</code> request with the same <code>CallerReference</code> and settings as a previous request, and if the health check doesn't exist, Amazon Route 53 creates the health check. If the health check does exist, Route 53 returns the health check configuration in the response. </p> </li> <li> <p>If you send a <code>CreateHealthCheck</code> request with the same <code>CallerReference</code> as a deleted health check, regardless of the settings, Route 53 returns a <code>HealthCheckAlreadyExists</code> error.</p> </li> <li> <p>If you send a <code>CreateHealthCheck</code> request with the same <code>CallerReference</code> as an existing health check but with different settings, Route 53 returns a <code>HealthCheckAlreadyExists</code> error.</p> </li> <li> <p>If you send a <code>CreateHealthCheck</code> request with a unique <code>CallerReference</code> but settings identical to an existing health check, Route 53 creates the health check.</p> </li> </ul> <p> Route 53 does not store the <code>CallerReference</code> for a deleted health check indefinitely. The <code>CallerReference</code> for a deleted health check will be deleted after a number of days.</p>"""
    health_check_config: "capo_route_53.types.health_check_config.HealthCheckConfig"
    """<p>A complex type that contains settings for a new health check.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateHealthCheckRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    import capo_route_53.types.health_check_config

    capo_route_53.types.health_check_config.serialize_xml(
        value["health_check_config"], el, "HealthCheckConfig"
    )


def deserialize_xml(el: Element) -> CreateHealthCheckRequest:
    out: CreateHealthCheckRequest = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        out["caller_reference"] = ""
    child_health_check_config = el.find("HealthCheckConfig")
    if child_health_check_config is not None:
        import capo_route_53.types.health_check_config

        out["health_check_config"] = (
            capo_route_53.types.health_check_config.deserialize_xml(
                child_health_check_config
            )
        )
    else:
        raise DeserializationError(
            "CreateHealthCheckRequest.health_check_config required"
        )
    return out
