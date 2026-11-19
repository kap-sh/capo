"""Generated from Smithy shape ``com.amazonaws.ec2#ActiveVpnTunnelStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.active_additional_key_exchanges_list
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.vpn_tunnel_provisioning_status


class ActiveVpnTunnelStatus(TypedDict, closed=True):
    phase1_encryption_algorithm: NotRequired["capo_ec2.types.string.String"]
    """<p>The encryption algorithm negotiated in Phase 1 IKE negotiations.</p>"""
    phase2_encryption_algorithm: NotRequired["capo_ec2.types.string.String"]
    """<p>The encryption algorithm negotiated in Phase 2 IKE negotiations.</p>"""
    phase1_integrity_algorithm: NotRequired["capo_ec2.types.string.String"]
    """<p>The integrity algorithm negotiated in Phase 1 IKE negotiations.</p>"""
    phase2_integrity_algorithm: NotRequired["capo_ec2.types.string.String"]
    """<p>The integrity algorithm negotiated in Phase 2 IKE negotiations.</p>"""
    phase1_dh_group: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The Diffie-Hellman group number being used in Phase 1 IKE negotiations.</p>"""
    phase2_dh_group: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The Diffie-Hellman group number being used in Phase 2 IKE negotiations.</p>"""
    ike_version: NotRequired["capo_ec2.types.string.String"]
    """<p>The version of the Internet Key Exchange (IKE) protocol being used.</p>"""
    provisioning_status: NotRequired[
        "capo_ec2.types.vpn_tunnel_provisioning_status.VpnTunnelProvisioningStatus"
    ]
    """<p>The current provisioning status of the VPN tunnel.</p>"""
    provisioning_status_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the current provisioning status.</p>"""
    phase1_additional_key_exchanges: NotRequired[
        "capo_ec2.types.active_additional_key_exchanges_list.ActiveAdditionalKeyExchangesList"
    ]
    """<p>The additional key exchanges negotiated in Phase 1 IKE negotiations.</p>"""
    phase2_additional_key_exchanges: NotRequired[
        "capo_ec2.types.active_additional_key_exchanges_list.ActiveAdditionalKeyExchangesList"
    ]
    """<p>The additional key exchanges negotiated in Phase 2 IKE negotiations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ActiveVpnTunnelStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "phase1_encryption_algorithm" in value:
        pairs.append(
            (
                f"{key_prefix}Phase1EncryptionAlgorithm",
                str(value["phase1_encryption_algorithm"]),
            )
        )
    if "phase2_encryption_algorithm" in value:
        pairs.append(
            (
                f"{key_prefix}Phase2EncryptionAlgorithm",
                str(value["phase2_encryption_algorithm"]),
            )
        )
    if "phase1_integrity_algorithm" in value:
        pairs.append(
            (
                f"{key_prefix}Phase1IntegrityAlgorithm",
                str(value["phase1_integrity_algorithm"]),
            )
        )
    if "phase2_integrity_algorithm" in value:
        pairs.append(
            (
                f"{key_prefix}Phase2IntegrityAlgorithm",
                str(value["phase2_integrity_algorithm"]),
            )
        )
    if "phase1_dh_group" in value:
        pairs.append((f"{key_prefix}Phase1DHGroup", str(value["phase1_dh_group"])))
    if "phase2_dh_group" in value:
        pairs.append((f"{key_prefix}Phase2DHGroup", str(value["phase2_dh_group"])))
    if "ike_version" in value:
        pairs.append((f"{key_prefix}IkeVersion", str(value["ike_version"])))
    if "provisioning_status" in value:
        import capo_ec2.types.vpn_tunnel_provisioning_status

        capo_ec2.types.vpn_tunnel_provisioning_status.serialize_ec2_query(
            value["provisioning_status"], pairs, f"{key_prefix}ProvisioningStatus"
        )
    if "provisioning_status_reason" in value:
        pairs.append(
            (
                f"{key_prefix}ProvisioningStatusReason",
                str(value["provisioning_status_reason"]),
            )
        )
    if "phase1_additional_key_exchanges" in value:
        import capo_ec2.types.active_additional_key_exchanges_list

        capo_ec2.types.active_additional_key_exchanges_list.serialize_ec2_query(
            value["phase1_additional_key_exchanges"],
            pairs,
            f"{key_prefix}Phase1AdditionalKeyExchangeSet",
        )
    if "phase2_additional_key_exchanges" in value:
        import capo_ec2.types.active_additional_key_exchanges_list

        capo_ec2.types.active_additional_key_exchanges_list.serialize_ec2_query(
            value["phase2_additional_key_exchanges"],
            pairs,
            f"{key_prefix}Phase2AdditionalKeyExchangeSet",
        )


def deserialize_ec2_query(el: Element) -> ActiveVpnTunnelStatus:
    out: ActiveVpnTunnelStatus = {}  # type: ignore[typeddict-item]
    child_phase1_encryption_algorithm = el.find("phase1EncryptionAlgorithm")
    if child_phase1_encryption_algorithm is not None:
        out["phase1_encryption_algorithm"] = str(
            child_phase1_encryption_algorithm.text or ""
        )
    child_phase2_encryption_algorithm = el.find("phase2EncryptionAlgorithm")
    if child_phase2_encryption_algorithm is not None:
        out["phase2_encryption_algorithm"] = str(
            child_phase2_encryption_algorithm.text or ""
        )
    child_phase1_integrity_algorithm = el.find("phase1IntegrityAlgorithm")
    if child_phase1_integrity_algorithm is not None:
        out["phase1_integrity_algorithm"] = str(
            child_phase1_integrity_algorithm.text or ""
        )
    child_phase2_integrity_algorithm = el.find("phase2IntegrityAlgorithm")
    if child_phase2_integrity_algorithm is not None:
        out["phase2_integrity_algorithm"] = str(
            child_phase2_integrity_algorithm.text or ""
        )
    child_phase1_dh_group = el.find("phase1DHGroup")
    if child_phase1_dh_group is not None:
        out["phase1_dh_group"] = int(child_phase1_dh_group.text or "")
    child_phase2_dh_group = el.find("phase2DHGroup")
    if child_phase2_dh_group is not None:
        out["phase2_dh_group"] = int(child_phase2_dh_group.text or "")
    child_ike_version = el.find("ikeVersion")
    if child_ike_version is not None:
        out["ike_version"] = str(child_ike_version.text or "")
    child_provisioning_status = el.find("provisioningStatus")
    if child_provisioning_status is not None:
        import capo_ec2.types.vpn_tunnel_provisioning_status

        out["provisioning_status"] = (
            capo_ec2.types.vpn_tunnel_provisioning_status.deserialize_ec2_query(
                child_provisioning_status
            )
        )
    child_provisioning_status_reason = el.find("provisioningStatusReason")
    if child_provisioning_status_reason is not None:
        out["provisioning_status_reason"] = str(
            child_provisioning_status_reason.text or ""
        )
    child_phase1_additional_key_exchanges = el.find("phase1AdditionalKeyExchangeSet")
    if child_phase1_additional_key_exchanges is not None:
        import capo_ec2.types.active_additional_key_exchanges_list

        out["phase1_additional_key_exchanges"] = (
            capo_ec2.types.active_additional_key_exchanges_list.deserialize_ec2_query(
                child_phase1_additional_key_exchanges
            )
        )
    child_phase2_additional_key_exchanges = el.find("phase2AdditionalKeyExchangeSet")
    if child_phase2_additional_key_exchanges is not None:
        import capo_ec2.types.active_additional_key_exchanges_list

        out["phase2_additional_key_exchanges"] = (
            capo_ec2.types.active_additional_key_exchanges_list.deserialize_ec2_query(
                child_phase2_additional_key_exchanges
            )
        )
    return out
