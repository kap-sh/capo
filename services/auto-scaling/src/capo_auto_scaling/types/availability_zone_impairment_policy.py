"""Generated from Smithy shape ``com.amazonaws.autoscaling#AvailabilityZoneImpairmentPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.impaired_zone_health_check_behavior
    import capo_auto_scaling.types.zonal_shift_enabled


class AvailabilityZoneImpairmentPolicy(TypedDict, closed=True):
    zonal_shift_enabled: NotRequired[
        "capo_auto_scaling.types.zonal_shift_enabled.ZonalShiftEnabled"
    ]
    """<p> If <code>true</code>, enable zonal shift for your Auto Scaling group. </p>"""
    impaired_zone_health_check_behavior: NotRequired[
        "capo_auto_scaling.types.impaired_zone_health_check_behavior.ImpairedZoneHealthCheckBehavior"
    ]
    """<p> Specifies the health check behavior for the impaired Availability Zone in an active zonal shift. If you select <code>Replace unhealthy</code>, instances that appear unhealthy will be replaced in all Availability Zones. If you select <code>Ignore unhealthy</code>, instances will not be replaced in the Availability Zone with the active zonal shift. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html">Auto Scaling group zonal shift</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZoneImpairmentPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "zonal_shift_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}ZonalShiftEnabled",
                "true" if value["zonal_shift_enabled"] else "false",
            )
        )
    if "impaired_zone_health_check_behavior" in value:
        import capo_auto_scaling.types.impaired_zone_health_check_behavior

        capo_auto_scaling.types.impaired_zone_health_check_behavior.serialize_query(
            value["impaired_zone_health_check_behavior"],
            pairs,
            f"{key_prefix}ImpairedZoneHealthCheckBehavior",
        )


def deserialize_query(el: Element) -> AvailabilityZoneImpairmentPolicy:
    out: AvailabilityZoneImpairmentPolicy = {}  # type: ignore[typeddict-item]
    child_zonal_shift_enabled = el.find("ZonalShiftEnabled")
    if child_zonal_shift_enabled is not None:
        out["zonal_shift_enabled"] = (
            child_zonal_shift_enabled.text or ""
        ).lower() == "true"
    child_impaired_zone_health_check_behavior = el.find(
        "ImpairedZoneHealthCheckBehavior"
    )
    if child_impaired_zone_health_check_behavior is not None:
        import capo_auto_scaling.types.impaired_zone_health_check_behavior

        out["impaired_zone_health_check_behavior"] = (
            capo_auto_scaling.types.impaired_zone_health_check_behavior.deserialize_query(
                child_impaired_zone_health_check_behavior
            )
        )
    return out
