"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RdsUngraceful``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.rds_ungraceful_behavior


class RdsUngraceful(TypedDict, closed=True):
    ungraceful: NotRequired[
        "capo_arc_region_switch.types.rds_ungraceful_behavior.RdsUngracefulBehavior"
    ]
    """<p>The ungraceful behavior to perform if switching to ungraceful execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsUngraceful) -> dict:
    out: dict = {}
    if "ungraceful" in value:
        import capo_arc_region_switch.types.rds_ungraceful_behavior

        out["ungraceful"] = (
            capo_arc_region_switch.types.rds_ungraceful_behavior.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RdsUngraceful:
    out: RdsUngraceful = {}  # type: ignore[typeddict-item]
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.rds_ungraceful_behavior

        out["ungraceful"] = (
            capo_arc_region_switch.types.rds_ungraceful_behavior.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RdsUngraceful) -> dict:
    out: dict = {}
    if "ungraceful" in value:
        import capo_arc_region_switch.types.rds_ungraceful_behavior

        out["ungraceful"] = (
            capo_arc_region_switch.types.rds_ungraceful_behavior.serialize_cbor(
                value["ungraceful"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RdsUngraceful:
    out: RdsUngraceful = {}  # type: ignore[typeddict-item]
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.rds_ungraceful_behavior

        out["ungraceful"] = (
            capo_arc_region_switch.types.rds_ungraceful_behavior.deserialize_cbor(
                data["ungraceful"]
            )
        )
    return out
