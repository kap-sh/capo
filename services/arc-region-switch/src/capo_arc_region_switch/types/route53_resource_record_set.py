"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Route53ResourceRecordSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.route53_resource_record_set_identifier


class Route53ResourceRecordSet(TypedDict, closed=True):
    record_set_identifier: NotRequired[
        "capo_arc_region_switch.types.route53_resource_record_set_identifier.Route53ResourceRecordSetIdentifier"
    ]
    """<p>The Amazon Route 53 record set identifier.</p>"""
    region: NotRequired["capo_arc_region_switch.types.region.Region"]
    """<p>The Amazon Route 53 record set Region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53ResourceRecordSet) -> dict:
    out: dict = {}
    if "record_set_identifier" in value:
        out["recordSetIdentifier"] = value["record_set_identifier"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Route53ResourceRecordSet:
    out: Route53ResourceRecordSet = {}  # type: ignore[typeddict-item]
    if data.get("recordSetIdentifier") is not None:
        out["record_set_identifier"] = data["recordSetIdentifier"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Route53ResourceRecordSet) -> dict:
    out: dict = {}
    if "record_set_identifier" in value:
        out["recordSetIdentifier"] = value["record_set_identifier"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_cbor(data: dict) -> Route53ResourceRecordSet:
    out: Route53ResourceRecordSet = {}  # type: ignore[typeddict-item]
    if data.get("recordSetIdentifier") is not None:
        out["record_set_identifier"] = data["recordSetIdentifier"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out
