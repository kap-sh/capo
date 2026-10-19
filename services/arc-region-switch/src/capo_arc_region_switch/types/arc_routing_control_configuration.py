"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ArcRoutingControlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.region_and_routing_controls


class ArcRoutingControlConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    region_and_routing_controls: "capo_arc_region_switch.types.region_and_routing_controls.RegionAndRoutingControls"
    """<p>The Region and ARC routing controls for the configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArcRoutingControlConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    import capo_arc_region_switch.types.region_and_routing_controls

    out["regionAndRoutingControls"] = (
        capo_arc_region_switch.types.region_and_routing_controls.serialize_aws_json_1_0(
            value["region_and_routing_controls"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ArcRoutingControlConfiguration:
    out: ArcRoutingControlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("regionAndRoutingControls") is not None:
        import capo_arc_region_switch.types.region_and_routing_controls

        out["region_and_routing_controls"] = (
            capo_arc_region_switch.types.region_and_routing_controls.deserialize_aws_json_1_0(
                data["regionAndRoutingControls"]
            )
        )
    else:
        out["region_and_routing_controls"] = {}
    return out
