"""Generated from Smithy shape ``com.amazonaws.autoscaling#AttachTrafficSourcesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.skip_zonal_shift_validation
    import capo_auto_scaling.types.traffic_sources
    import capo_auto_scaling.types.xml_string_max_len255


class AttachTrafficSourcesType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    traffic_sources: NotRequired[
        "capo_auto_scaling.types.traffic_sources.TrafficSources"
    ]
    """<p>The unique identifiers of one or more traffic sources. You can specify up to 10 traffic sources.</p>"""
    skip_zonal_shift_validation: NotRequired[
        "capo_auto_scaling.types.skip_zonal_shift_validation.SkipZonalShiftValidation"
    ]
    """<p> If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify <code>true</code>. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html">Auto Scaling group zonal shift</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachTrafficSourcesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "traffic_sources" in value:
        import capo_auto_scaling.types.traffic_sources

        capo_auto_scaling.types.traffic_sources.serialize_query(
            value["traffic_sources"], pairs, f"{key_prefix}TrafficSources"
        )
    if "skip_zonal_shift_validation" in value:
        pairs.append(
            (
                f"{key_prefix}SkipZonalShiftValidation",
                "true" if value["skip_zonal_shift_validation"] else "false",
            )
        )


def deserialize_query(el: Element) -> AttachTrafficSourcesType:
    out: AttachTrafficSourcesType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_traffic_sources = el.find("TrafficSources")
    if child_traffic_sources is not None:
        import capo_auto_scaling.types.traffic_sources

        out["traffic_sources"] = (
            capo_auto_scaling.types.traffic_sources.deserialize_query(
                child_traffic_sources
            )
        )
    child_skip_zonal_shift_validation = el.find("SkipZonalShiftValidation")
    if child_skip_zonal_shift_validation is not None:
        out["skip_zonal_shift_validation"] = (
            child_skip_zonal_shift_validation.text or ""
        ).lower() == "true"
    return out
