"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Route53HealthCheckList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.route53_health_check

Route53HealthCheckList: TypeAlias = list[
    "capo_arc_region_switch.types.route53_health_check.Route53HealthCheck"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53HealthCheckList) -> list:
    import capo_arc_region_switch.types.route53_health_check

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.route53_health_check.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Route53HealthCheckList:
    import capo_arc_region_switch.types.route53_health_check

    out: Route53HealthCheckList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.route53_health_check.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Route53HealthCheckList) -> list:
    import capo_arc_region_switch.types.route53_health_check

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.route53_health_check.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> Route53HealthCheckList:
    import capo_arc_region_switch.types.route53_health_check

    out: Route53HealthCheckList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.route53_health_check.deserialize_cbor(item)
        )
    return out
