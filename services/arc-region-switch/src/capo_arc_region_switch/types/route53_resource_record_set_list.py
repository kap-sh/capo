"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Route53ResourceRecordSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.route53_resource_record_set

Route53ResourceRecordSetList: TypeAlias = list[
    "capo_arc_region_switch.types.route53_resource_record_set.Route53ResourceRecordSet"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53ResourceRecordSetList) -> list:
    import capo_arc_region_switch.types.route53_resource_record_set

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.route53_resource_record_set.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Route53ResourceRecordSetList:
    import capo_arc_region_switch.types.route53_resource_record_set

    out: Route53ResourceRecordSetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.route53_resource_record_set.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Route53ResourceRecordSetList) -> list:
    import capo_arc_region_switch.types.route53_resource_record_set

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.route53_resource_record_set.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> Route53ResourceRecordSetList:
    import capo_arc_region_switch.types.route53_resource_record_set

    out: Route53ResourceRecordSetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.route53_resource_record_set.deserialize_cbor(
                item
            )
        )
    return out
