"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GlobalAuroraUngraceful``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.global_aurora_ungraceful_behavior


class GlobalAuroraUngraceful(TypedDict, closed=True):
    ungraceful: NotRequired[
        "capo_arc_region_switch.types.global_aurora_ungraceful_behavior.GlobalAuroraUngracefulBehavior"
    ]
    """<p>The ungraceful behavior. The only valid value is <code>failover</code>, which calls <code>FailoverGlobalCluster</code> with <code>AllowDataLoss</code> set to <code>true</code> and might cause data loss.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalAuroraUngraceful) -> dict:
    out: dict = {}
    if "ungraceful" in value:
        import capo_arc_region_switch.types.global_aurora_ungraceful_behavior

        out["ungraceful"] = (
            capo_arc_region_switch.types.global_aurora_ungraceful_behavior.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalAuroraUngraceful:
    out: GlobalAuroraUngraceful = {}  # type: ignore[typeddict-item]
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.global_aurora_ungraceful_behavior

        out["ungraceful"] = (
            capo_arc_region_switch.types.global_aurora_ungraceful_behavior.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    return out
