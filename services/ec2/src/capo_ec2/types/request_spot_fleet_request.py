"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotFleetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.spot_fleet_request_config_data


class RequestSpotFleetRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_config: NotRequired[
        "capo_ec2.types.spot_fleet_request_config_data.SpotFleetRequestConfigData"
    ]
    """<p>The configuration for the Spot Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestSpotFleetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "spot_fleet_request_config" in value:
        import capo_ec2.types.spot_fleet_request_config_data

        capo_ec2.types.spot_fleet_request_config_data.serialize_ec2_query(
            value["spot_fleet_request_config"],
            pairs,
            f"{key_prefix}SpotFleetRequestConfig",
        )


def deserialize_ec2_query(el: Element) -> RequestSpotFleetRequest:
    out: RequestSpotFleetRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_spot_fleet_request_config = el.find("spotFleetRequestConfig")
    if child_spot_fleet_request_config is not None:
        import capo_ec2.types.spot_fleet_request_config_data

        out["spot_fleet_request_config"] = (
            capo_ec2.types.spot_fleet_request_config_data.deserialize_ec2_query(
                child_spot_fleet_request_config
            )
        )
    return out


def redact_sensitive(value: RequestSpotFleetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "spot_fleet_request_config" in value:
        import capo_ec2.types.spot_fleet_request_config_data

        out["spot_fleet_request_config"] = (
            capo_ec2.types.spot_fleet_request_config_data.redact_sensitive(
                value["spot_fleet_request_config"]
            )
        )
    return out
