"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTestTrafficHeaderRules``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.service_connect_test_traffic_header_match_rules
    import capo_ecs.types.string


class ServiceConnectTestTrafficHeaderRules(TypedDict, closed=True):
    name: "capo_ecs.types.string.String"
    """<p>The name of the HTTP header to examine for test traffic routing. Common examples include custom headers like <code>X-Test-Version</code> or <code>X-Canary-Request</code> that can be used to identify test traffic.</p>"""
    value: NotRequired[
        "capo_ecs.types.service_connect_test_traffic_header_match_rules.ServiceConnectTestTrafficHeaderMatchRules"
    ]
    """<p>The header value matching configuration that determines how the HTTP header value is evaluated for test traffic routing decisions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectTestTrafficHeaderRules) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "value" in value:
        import capo_ecs.types.service_connect_test_traffic_header_match_rules

        out["value"] = (
            capo_ecs.types.service_connect_test_traffic_header_match_rules.serialize_aws_json_1_1(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectTestTrafficHeaderRules:
    out: ServiceConnectTestTrafficHeaderRules = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        import capo_ecs.types.service_connect_test_traffic_header_match_rules

        out["value"] = (
            capo_ecs.types.service_connect_test_traffic_header_match_rules.deserialize_aws_json_1_1(
                data["value"]
            )
        )
    return out
