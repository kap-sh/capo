"""Generated from Smithy shape ``com.amazonaws.guardduty#PortProbeAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean
    import capo_guardduty.types.port_probe_details


class PortProbeAction(TypedDict, closed=True):
    blocked: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates whether EC2 blocked the port probe to the instance, such as with an ACL.</p>"""
    port_probe_details: NotRequired[
        "capo_guardduty.types.port_probe_details.PortProbeDetails"
    ]
    """<p>A list of objects related to port probe details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortProbeAction) -> dict:
    out: dict = {}
    if "blocked" in value:
        out["blocked"] = value["blocked"]
    if "port_probe_details" in value:
        import capo_guardduty.types.port_probe_details

        out["portProbeDetails"] = (
            capo_guardduty.types.port_probe_details.serialize_json(
                value["port_probe_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> PortProbeAction:
    out: PortProbeAction = {}  # type: ignore[typeddict-item]
    if data.get("blocked") is not None:
        out["blocked"] = data["blocked"]
    if data.get("portProbeDetails") is not None:
        import capo_guardduty.types.port_probe_details

        out["port_probe_details"] = (
            capo_guardduty.types.port_probe_details.deserialize_json(
                data["portProbeDetails"]
            )
        )
    return out


def redact_sensitive(value: PortProbeAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "port_probe_details" in value:
        import capo_guardduty.types.port_probe_details

        out["port_probe_details"] = (
            capo_guardduty.types.port_probe_details.redact_sensitive(
                value["port_probe_details"]
            )
        )
    return out
