"""Generated from Smithy shape ``com.amazonaws.route53#AccountLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.account_limit_type
    import capo_route_53.types.limit_value


class AccountLimit(TypedDict, closed=True):
    type: "capo_route_53.types.account_limit_type.AccountLimitType"
    """<p>The limit that you requested. Valid values include the following:</p> <ul> <li> <p> <b>MAX_HEALTH_CHECKS_BY_OWNER</b>: The maximum number of health checks that you can create using the current account.</p> </li> <li> <p> <b>MAX_HOSTED_ZONES_BY_OWNER</b>: The maximum number of hosted zones that you can create using the current account.</p> </li> <li> <p> <b>MAX_REUSABLE_DELEGATION_SETS_BY_OWNER</b>: The maximum number of reusable delegation sets that you can create using the current account.</p> </li> <li> <p> <b>MAX_TRAFFIC_POLICIES_BY_OWNER</b>: The maximum number of traffic policies that you can create using the current account.</p> </li> <li> <p> <b>MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER</b>: The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)</p> </li> </ul>"""
    value: "capo_route_53.types.limit_value.LimitValue"
    """<p>The current value for the limit that is specified by <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_AccountLimit.html#Route53-Type-AccountLimit-Type">Type</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AccountLimit, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.account_limit_type

    capo_route_53.types.account_limit_type.serialize_xml(value["type"], el, "Type")
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> AccountLimit:
    out: AccountLimit = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_route_53.types.account_limit_type

        out["type"] = capo_route_53.types.account_limit_type.deserialize_xml(child_type)
    else:
        raise DeserializationError("AccountLimit.type required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = int(child_value.text or "")
    else:
        raise DeserializationError("AccountLimit.value required")
    return out
