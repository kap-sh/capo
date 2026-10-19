"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLBCookieStickinessPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.cookie_expiration_period
    import capo_elastic_load_balancing.types.policy_name


class CreateLBCookieStickinessPolicyInput(TypedDict, closed=True):
    load_balancer_name: (
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    policy_name: "capo_elastic_load_balancing.types.policy_name.PolicyName"
    """<p>The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.</p>"""
    cookie_expiration_period: NotRequired[
        "capo_elastic_load_balancing.types.cookie_expiration_period.CookieExpirationPeriod"
    ]
    """<p>The time period, in seconds, after which the cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLBCookieStickinessPolicyInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"])))
    pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    if "cookie_expiration_period" in value:
        pairs.append(
            (
                f"{key_prefix}CookieExpirationPeriod",
                str(value["cookie_expiration_period"]),
            )
        )


def deserialize_query(el: Element) -> CreateLBCookieStickinessPolicyInput:
    out: CreateLBCookieStickinessPolicyInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        out["load_balancer_name"] = ""
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        out["policy_name"] = ""
    child_cookie_expiration_period = el.find("CookieExpirationPeriod")
    if child_cookie_expiration_period is not None:
        out["cookie_expiration_period"] = int(child_cookie_expiration_period.text or "")
    return out
