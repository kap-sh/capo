"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceSampleConfigurationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_connection_device_sample_configuration


class GetVpnConnectionDeviceSampleConfigurationResult(TypedDict, closed=True):
    vpn_connection_device_sample_configuration: NotRequired[
        "capo_ec2.types.vpn_connection_device_sample_configuration.VpnConnectionDeviceSampleConfiguration"
    ]
    """<p>Sample configuration file for the specified customer gateway device.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVpnConnectionDeviceSampleConfigurationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_connection_device_sample_configuration" in value:
        pairs.append(
            (
                f"{key_prefix}VpnConnectionDeviceSampleConfiguration",
                str(value["vpn_connection_device_sample_configuration"]),
            )
        )


def deserialize_ec2_query(
    el: Element,
) -> GetVpnConnectionDeviceSampleConfigurationResult:
    out: GetVpnConnectionDeviceSampleConfigurationResult = {}  # type: ignore[typeddict-item]
    child_vpn_connection_device_sample_configuration = el.find(
        "vpnConnectionDeviceSampleConfiguration"
    )
    if child_vpn_connection_device_sample_configuration is not None:
        out["vpn_connection_device_sample_configuration"] = str(
            child_vpn_connection_device_sample_configuration.text or ""
        )
    return out


def redact_sensitive(
    value: GetVpnConnectionDeviceSampleConfigurationResult,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vpn_connection_device_sample_configuration" in value:
        out["vpn_connection_device_sample_configuration"] = (
            "*** Sensitive Data Redacted ***"
        )
    return out
