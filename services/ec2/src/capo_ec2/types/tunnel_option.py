"""Generated from Smithy shape ``com.amazonaws.ec2#TunnelOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ike_versions_list
    import capo_ec2.types.integer
    import capo_ec2.types.phase1_dh_group_numbers_list
    import capo_ec2.types.phase1_encryption_algorithms_list
    import capo_ec2.types.phase1_integrity_algorithms_list
    import capo_ec2.types.phase2_dh_group_numbers_list
    import capo_ec2.types.phase2_encryption_algorithms_list
    import capo_ec2.types.phase2_integrity_algorithms_list
    import capo_ec2.types.pre_shared_key
    import capo_ec2.types.string
    import capo_ec2.types.vpn_tunnel_log_options


class TunnelOption(TypedDict, closed=True):
    outside_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel.</p>"""
    tunnel_inside_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The range of inside IPv4 addresses for the tunnel.</p>"""
    tunnel_inside_ipv6_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The range of inside IPv6 addresses for the tunnel.</p>"""
    pre_shared_key: NotRequired["capo_ec2.types.pre_shared_key.preSharedKey"]
    """<p>The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and the customer gateway.</p>"""
    phase1_lifetime_seconds: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The lifetime for phase 1 of the IKE negotiation, in seconds.</p>"""
    phase2_lifetime_seconds: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The lifetime for phase 2 of the IKE negotiation, in seconds.</p>"""
    rekey_margin_time_seconds: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The margin time, in seconds, before the phase 2 lifetime expires, during which the Amazon Web Services side of the VPN connection performs an IKE rekey.</p>"""
    rekey_fuzz_percentage: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The percentage of the rekey window determined by <code>RekeyMarginTimeSeconds</code> during which the rekey time is randomly selected.</p>"""
    replay_window_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of packets in an IKE replay window.</p>"""
    dpd_timeout_seconds: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of seconds after which a DPD timeout occurs.</p>"""
    dpd_timeout_action: NotRequired["capo_ec2.types.string.String"]
    """<p>The action to take after a DPD timeout occurs.</p>"""
    phase1_encryption_algorithms: NotRequired[
        "capo_ec2.types.phase1_encryption_algorithms_list.Phase1EncryptionAlgorithmsList"
    ]
    """<p>The permitted encryption algorithms for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase2_encryption_algorithms: NotRequired[
        "capo_ec2.types.phase2_encryption_algorithms_list.Phase2EncryptionAlgorithmsList"
    ]
    """<p>The permitted encryption algorithms for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    phase1_integrity_algorithms: NotRequired[
        "capo_ec2.types.phase1_integrity_algorithms_list.Phase1IntegrityAlgorithmsList"
    ]
    """<p>The permitted integrity algorithms for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase2_integrity_algorithms: NotRequired[
        "capo_ec2.types.phase2_integrity_algorithms_list.Phase2IntegrityAlgorithmsList"
    ]
    """<p>The permitted integrity algorithms for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    phase1_dh_group_numbers: NotRequired[
        "capo_ec2.types.phase1_dh_group_numbers_list.Phase1DHGroupNumbersList"
    ]
    """<p>The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase2_dh_group_numbers: NotRequired[
        "capo_ec2.types.phase2_dh_group_numbers_list.Phase2DHGroupNumbersList"
    ]
    """<p>The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    ike_versions: NotRequired["capo_ec2.types.ike_versions_list.IKEVersionsList"]
    """<p>The IKE versions that are permitted for the VPN tunnel.</p>"""
    startup_action: NotRequired["capo_ec2.types.string.String"]
    """<p>The action to take when the establishing the VPN tunnels for a VPN connection.</p>"""
    log_options: NotRequired[
        "capo_ec2.types.vpn_tunnel_log_options.VpnTunnelLogOptions"
    ]
    """<p>Options for logging VPN tunnel activity.</p>"""
    enable_tunnel_lifecycle_control: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Status of tunnel endpoint lifecycle control feature.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TunnelOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "outside_ip_address" in value:
        pairs.append(
            (f"{key_prefix}OutsideIpAddress", str(value["outside_ip_address"]))
        )
    if "tunnel_inside_cidr" in value:
        pairs.append(
            (f"{key_prefix}TunnelInsideCidr", str(value["tunnel_inside_cidr"]))
        )
    if "tunnel_inside_ipv6_cidr" in value:
        pairs.append(
            (f"{key_prefix}TunnelInsideIpv6Cidr", str(value["tunnel_inside_ipv6_cidr"]))
        )
    if "pre_shared_key" in value:
        pairs.append((f"{key_prefix}PreSharedKey", str(value["pre_shared_key"])))
    if "phase1_lifetime_seconds" in value:
        pairs.append(
            (
                f"{key_prefix}Phase1LifetimeSeconds",
                str(value["phase1_lifetime_seconds"]),
            )
        )
    if "phase2_lifetime_seconds" in value:
        pairs.append(
            (
                f"{key_prefix}Phase2LifetimeSeconds",
                str(value["phase2_lifetime_seconds"]),
            )
        )
    if "rekey_margin_time_seconds" in value:
        pairs.append(
            (
                f"{key_prefix}RekeyMarginTimeSeconds",
                str(value["rekey_margin_time_seconds"]),
            )
        )
    if "rekey_fuzz_percentage" in value:
        pairs.append(
            (f"{key_prefix}RekeyFuzzPercentage", str(value["rekey_fuzz_percentage"]))
        )
    if "replay_window_size" in value:
        pairs.append(
            (f"{key_prefix}ReplayWindowSize", str(value["replay_window_size"]))
        )
    if "dpd_timeout_seconds" in value:
        pairs.append(
            (f"{key_prefix}DpdTimeoutSeconds", str(value["dpd_timeout_seconds"]))
        )
    if "dpd_timeout_action" in value:
        pairs.append(
            (f"{key_prefix}DpdTimeoutAction", str(value["dpd_timeout_action"]))
        )
    if "phase1_encryption_algorithms" in value:
        import capo_ec2.types.phase1_encryption_algorithms_list

        capo_ec2.types.phase1_encryption_algorithms_list.serialize_ec2_query(
            value["phase1_encryption_algorithms"],
            pairs,
            f"{key_prefix}Phase1EncryptionAlgorithmSet",
        )
    if "phase2_encryption_algorithms" in value:
        import capo_ec2.types.phase2_encryption_algorithms_list

        capo_ec2.types.phase2_encryption_algorithms_list.serialize_ec2_query(
            value["phase2_encryption_algorithms"],
            pairs,
            f"{key_prefix}Phase2EncryptionAlgorithmSet",
        )
    if "phase1_integrity_algorithms" in value:
        import capo_ec2.types.phase1_integrity_algorithms_list

        capo_ec2.types.phase1_integrity_algorithms_list.serialize_ec2_query(
            value["phase1_integrity_algorithms"],
            pairs,
            f"{key_prefix}Phase1IntegrityAlgorithmSet",
        )
    if "phase2_integrity_algorithms" in value:
        import capo_ec2.types.phase2_integrity_algorithms_list

        capo_ec2.types.phase2_integrity_algorithms_list.serialize_ec2_query(
            value["phase2_integrity_algorithms"],
            pairs,
            f"{key_prefix}Phase2IntegrityAlgorithmSet",
        )
    if "phase1_dh_group_numbers" in value:
        import capo_ec2.types.phase1_dh_group_numbers_list

        capo_ec2.types.phase1_dh_group_numbers_list.serialize_ec2_query(
            value["phase1_dh_group_numbers"],
            pairs,
            f"{key_prefix}Phase1DHGroupNumberSet",
        )
    if "phase2_dh_group_numbers" in value:
        import capo_ec2.types.phase2_dh_group_numbers_list

        capo_ec2.types.phase2_dh_group_numbers_list.serialize_ec2_query(
            value["phase2_dh_group_numbers"],
            pairs,
            f"{key_prefix}Phase2DHGroupNumberSet",
        )
    if "ike_versions" in value:
        import capo_ec2.types.ike_versions_list

        capo_ec2.types.ike_versions_list.serialize_ec2_query(
            value["ike_versions"], pairs, f"{key_prefix}IkeVersionSet"
        )
    if "startup_action" in value:
        pairs.append((f"{key_prefix}StartupAction", str(value["startup_action"])))
    if "log_options" in value:
        import capo_ec2.types.vpn_tunnel_log_options

        capo_ec2.types.vpn_tunnel_log_options.serialize_ec2_query(
            value["log_options"], pairs, f"{key_prefix}LogOptions"
        )
    if "enable_tunnel_lifecycle_control" in value:
        pairs.append(
            (
                f"{key_prefix}EnableTunnelLifecycleControl",
                "true" if value["enable_tunnel_lifecycle_control"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> TunnelOption:
    out: TunnelOption = {}  # type: ignore[typeddict-item]
    child_outside_ip_address = el.find("outsideIpAddress")
    if child_outside_ip_address is not None:
        out["outside_ip_address"] = str(child_outside_ip_address.text or "")
    child_tunnel_inside_cidr = el.find("tunnelInsideCidr")
    if child_tunnel_inside_cidr is not None:
        out["tunnel_inside_cidr"] = str(child_tunnel_inside_cidr.text or "")
    child_tunnel_inside_ipv6_cidr = el.find("tunnelInsideIpv6Cidr")
    if child_tunnel_inside_ipv6_cidr is not None:
        out["tunnel_inside_ipv6_cidr"] = str(child_tunnel_inside_ipv6_cidr.text or "")
    child_pre_shared_key = el.find("preSharedKey")
    if child_pre_shared_key is not None:
        out["pre_shared_key"] = str(child_pre_shared_key.text or "")
    child_phase1_lifetime_seconds = el.find("phase1LifetimeSeconds")
    if child_phase1_lifetime_seconds is not None:
        out["phase1_lifetime_seconds"] = int(child_phase1_lifetime_seconds.text or "")
    child_phase2_lifetime_seconds = el.find("phase2LifetimeSeconds")
    if child_phase2_lifetime_seconds is not None:
        out["phase2_lifetime_seconds"] = int(child_phase2_lifetime_seconds.text or "")
    child_rekey_margin_time_seconds = el.find("rekeyMarginTimeSeconds")
    if child_rekey_margin_time_seconds is not None:
        out["rekey_margin_time_seconds"] = int(
            child_rekey_margin_time_seconds.text or ""
        )
    child_rekey_fuzz_percentage = el.find("rekeyFuzzPercentage")
    if child_rekey_fuzz_percentage is not None:
        out["rekey_fuzz_percentage"] = int(child_rekey_fuzz_percentage.text or "")
    child_replay_window_size = el.find("replayWindowSize")
    if child_replay_window_size is not None:
        out["replay_window_size"] = int(child_replay_window_size.text or "")
    child_dpd_timeout_seconds = el.find("dpdTimeoutSeconds")
    if child_dpd_timeout_seconds is not None:
        out["dpd_timeout_seconds"] = int(child_dpd_timeout_seconds.text or "")
    child_dpd_timeout_action = el.find("dpdTimeoutAction")
    if child_dpd_timeout_action is not None:
        out["dpd_timeout_action"] = str(child_dpd_timeout_action.text or "")
    child_phase1_encryption_algorithms = el.find("phase1EncryptionAlgorithmSet")
    if child_phase1_encryption_algorithms is not None:
        import capo_ec2.types.phase1_encryption_algorithms_list

        out["phase1_encryption_algorithms"] = (
            capo_ec2.types.phase1_encryption_algorithms_list.deserialize_ec2_query(
                child_phase1_encryption_algorithms
            )
        )
    child_phase2_encryption_algorithms = el.find("phase2EncryptionAlgorithmSet")
    if child_phase2_encryption_algorithms is not None:
        import capo_ec2.types.phase2_encryption_algorithms_list

        out["phase2_encryption_algorithms"] = (
            capo_ec2.types.phase2_encryption_algorithms_list.deserialize_ec2_query(
                child_phase2_encryption_algorithms
            )
        )
    child_phase1_integrity_algorithms = el.find("phase1IntegrityAlgorithmSet")
    if child_phase1_integrity_algorithms is not None:
        import capo_ec2.types.phase1_integrity_algorithms_list

        out["phase1_integrity_algorithms"] = (
            capo_ec2.types.phase1_integrity_algorithms_list.deserialize_ec2_query(
                child_phase1_integrity_algorithms
            )
        )
    child_phase2_integrity_algorithms = el.find("phase2IntegrityAlgorithmSet")
    if child_phase2_integrity_algorithms is not None:
        import capo_ec2.types.phase2_integrity_algorithms_list

        out["phase2_integrity_algorithms"] = (
            capo_ec2.types.phase2_integrity_algorithms_list.deserialize_ec2_query(
                child_phase2_integrity_algorithms
            )
        )
    child_phase1_dh_group_numbers = el.find("phase1DHGroupNumberSet")
    if child_phase1_dh_group_numbers is not None:
        import capo_ec2.types.phase1_dh_group_numbers_list

        out["phase1_dh_group_numbers"] = (
            capo_ec2.types.phase1_dh_group_numbers_list.deserialize_ec2_query(
                child_phase1_dh_group_numbers
            )
        )
    child_phase2_dh_group_numbers = el.find("phase2DHGroupNumberSet")
    if child_phase2_dh_group_numbers is not None:
        import capo_ec2.types.phase2_dh_group_numbers_list

        out["phase2_dh_group_numbers"] = (
            capo_ec2.types.phase2_dh_group_numbers_list.deserialize_ec2_query(
                child_phase2_dh_group_numbers
            )
        )
    child_ike_versions = el.find("ikeVersionSet")
    if child_ike_versions is not None:
        import capo_ec2.types.ike_versions_list

        out["ike_versions"] = capo_ec2.types.ike_versions_list.deserialize_ec2_query(
            child_ike_versions
        )
    child_startup_action = el.find("startupAction")
    if child_startup_action is not None:
        out["startup_action"] = str(child_startup_action.text or "")
    child_log_options = el.find("logOptions")
    if child_log_options is not None:
        import capo_ec2.types.vpn_tunnel_log_options

        out["log_options"] = (
            capo_ec2.types.vpn_tunnel_log_options.deserialize_ec2_query(
                child_log_options
            )
        )
    child_enable_tunnel_lifecycle_control = el.find("enableTunnelLifecycleControl")
    if child_enable_tunnel_lifecycle_control is not None:
        out["enable_tunnel_lifecycle_control"] = (
            child_enable_tunnel_lifecycle_control.text or ""
        ).lower() == "true"
    return out


def redact_sensitive(value: TunnelOption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pre_shared_key" in value:
        out["pre_shared_key"] = "*** Sensitive Data Redacted ***"
    return out
