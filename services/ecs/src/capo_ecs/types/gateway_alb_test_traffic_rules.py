"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayAlbTestTrafficRules``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_test_traffic_header


class GatewayAlbTestTrafficRules(TypedDict, closed=True):
    header: NotRequired[
        "capo_ecs.types.gateway_test_traffic_header.GatewayTestTrafficHeader"
    ]
    """<p>The header-based rule that identifies test traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayAlbTestTrafficRules) -> dict:
    out: dict = {}
    if "header" in value:
        import capo_ecs.types.gateway_test_traffic_header

        out["header"] = (
            capo_ecs.types.gateway_test_traffic_header.serialize_aws_json_1_1(
                value["header"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayAlbTestTrafficRules:
    out: GatewayAlbTestTrafficRules = {}  # type: ignore[typeddict-item]
    if data.get("header") is not None:
        import capo_ecs.types.gateway_test_traffic_header

        out["header"] = (
            capo_ecs.types.gateway_test_traffic_header.deserialize_aws_json_1_1(
                data["header"]
            )
        )
    return out
