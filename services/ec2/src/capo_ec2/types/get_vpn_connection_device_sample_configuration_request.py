"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceSampleConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.vpn_connection_device_type_id
    import capo_ec2.types.vpn_connection_id


class GetVpnConnectionDeviceSampleConfigurationRequest(TypedDict, closed=True):
    vpn_connection_id: NotRequired["capo_ec2.types.vpn_connection_id.VpnConnectionId"]
    """<p>The <code>VpnConnectionId</code> specifies the Site-to-Site VPN connection used for the sample configuration.</p>"""
    vpn_connection_device_type_id: NotRequired[
        "capo_ec2.types.vpn_connection_device_type_id.VpnConnectionDeviceTypeId"
    ]
    """<p>Device identifier provided by the <code>GetVpnConnectionDeviceTypes</code> API.</p>"""
    internet_key_exchange_version: NotRequired["capo_ec2.types.string.String"]
    """<p>The IKE version to be used in the sample configuration file for your customer gateway device. You can specify one of the following versions: <code>ikev1</code> or <code>ikev2</code>.</p>"""
    sample_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of sample configuration to generate. Valid values are "compatibility" (includes IKEv1) or "recommended" (throws UnsupportedOperationException for IKEv1).</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVpnConnectionDeviceSampleConfigurationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_connection_id" in value:
        pairs.append((f"{key_prefix}VpnConnectionId", str(value["vpn_connection_id"])))
    if "vpn_connection_device_type_id" in value:
        pairs.append(
            (
                f"{key_prefix}VpnConnectionDeviceTypeId",
                str(value["vpn_connection_device_type_id"]),
            )
        )
    if "internet_key_exchange_version" in value:
        pairs.append(
            (
                f"{key_prefix}InternetKeyExchangeVersion",
                str(value["internet_key_exchange_version"]),
            )
        )
    if "sample_type" in value:
        pairs.append((f"{key_prefix}SampleType", str(value["sample_type"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> GetVpnConnectionDeviceSampleConfigurationRequest:
    out: GetVpnConnectionDeviceSampleConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_vpn_connection_id = el.find("VpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    child_vpn_connection_device_type_id = el.find("VpnConnectionDeviceTypeId")
    if child_vpn_connection_device_type_id is not None:
        out["vpn_connection_device_type_id"] = str(
            child_vpn_connection_device_type_id.text or ""
        )
    child_internet_key_exchange_version = el.find("InternetKeyExchangeVersion")
    if child_internet_key_exchange_version is not None:
        out["internet_key_exchange_version"] = str(
            child_internet_key_exchange_version.text or ""
        )
    child_sample_type = el.find("SampleType")
    if child_sample_type is not None:
        out["sample_type"] = str(child_sample_type.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
