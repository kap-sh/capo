"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelOptionsSpecification``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ike_versions_request_list
    import capo_ec2.types.integer
    import capo_ec2.types.phase1_dh_group_numbers_request_list
    import capo_ec2.types.phase1_encryption_algorithms_request_list
    import capo_ec2.types.phase1_integrity_algorithms_request_list
    import capo_ec2.types.phase2_dh_group_numbers_request_list
    import capo_ec2.types.phase2_encryption_algorithms_request_list
    import capo_ec2.types.phase2_integrity_algorithms_request_list
    import capo_ec2.types.pre_shared_key
    import capo_ec2.types.string
    import capo_ec2.types.vpn_tunnel_log_options_specification


class VpnTunnelOptionsSpecification(TypedDict, closed=True):
    tunnel_inside_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The range of inside IPv4 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same virtual private gateway. </p> <p>Constraints: A size /30 CIDR block from the <code>169.254.0.0/16</code> range. The following CIDR blocks are reserved and cannot be used:</p> <ul> <li> <p> <code>169.254.0.0/30</code> </p> </li> <li> <p> <code>169.254.1.0/30</code> </p> </li> <li> <p> <code>169.254.2.0/30</code> </p> </li> <li> <p> <code>169.254.3.0/30</code> </p> </li> <li> <p> <code>169.254.4.0/30</code> </p> </li> <li> <p> <code>169.254.5.0/30</code> </p> </li> <li> <p> <code>169.254.169.252/30</code> </p> </li> </ul>"""
    tunnel_inside_ipv6_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The range of inside IPv6 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same transit gateway.</p> <p>Constraints: A size /126 CIDR block from the local <code>fd00::/8</code> range.</p>"""
    pre_shared_key: NotRequired["capo_ec2.types.pre_shared_key.preSharedKey"]
    """<p>The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway.</p> <p>Constraints: Allowed characters are alphanumeric characters, periods (.), and underscores (_). Must be between 8 and 64 characters in length and cannot start with zero (0).</p>"""
    phase1_lifetime_seconds: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The lifetime for phase 1 of the IKE negotiation, in seconds.</p> <p>Constraints: A value between 900 and 28,800.</p> <p>Default: <code>28800</code> </p>"""
    phase2_lifetime_seconds: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The lifetime for phase 2 of the IKE negotiation, in seconds.</p> <p>Constraints: A value between 900 and 3,600. The value must be less than the value for <code>Phase1LifetimeSeconds</code>.</p> <p>Default: <code>3600</code> </p>"""
    rekey_margin_time_seconds: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The margin time, in seconds, before the phase 2 lifetime expires, during which the Amazon Web Services side of the VPN connection performs an IKE rekey. The exact time of the rekey is randomly selected based on the value for <code>RekeyFuzzPercentage</code>.</p> <p>Constraints: A value between 60 and half of <code>Phase2LifetimeSeconds</code>.</p> <p>Default: <code>270</code> </p>"""
    rekey_fuzz_percentage: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The percentage of the rekey window (determined by <code>RekeyMarginTimeSeconds</code>) during which the rekey time is randomly selected.</p> <p>Constraints: A value between 0 and 100.</p> <p>Default: <code>100</code> </p>"""
    replay_window_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of packets in an IKE replay window.</p> <p>Constraints: A value between 64 and 2048.</p> <p>Default: <code>1024</code> </p>"""
    dpd_timeout_seconds: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of seconds after which a DPD timeout occurs.</p> <p>Constraints: A value greater than or equal to 30.</p> <p>Default: <code>30</code> </p>"""
    dpd_timeout_action: NotRequired["capo_ec2.types.string.String"]
    """<p>The action to take after DPD timeout occurs. Specify <code>restart</code> to restart the IKE initiation. Specify <code>clear</code> to end the IKE session.</p> <p>Valid Values: <code>clear</code> | <code>none</code> | <code>restart</code> </p> <p>Default: <code>clear</code> </p>"""
    phase1_encryption_algorithms: NotRequired[
        "capo_ec2.types.phase1_encryption_algorithms_request_list.Phase1EncryptionAlgorithmsRequestList"
    ]
    """<p>One or more encryption algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.</p> <p>Valid values: <code>AES128</code> | <code>AES256</code> | <code>AES128-GCM-16</code> | <code>AES256-GCM-16</code> </p>"""
    phase2_encryption_algorithms: NotRequired[
        "capo_ec2.types.phase2_encryption_algorithms_request_list.Phase2EncryptionAlgorithmsRequestList"
    ]
    """<p>One or more encryption algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.</p> <p>Valid values: <code>AES128</code> | <code>AES256</code> | <code>AES128-GCM-16</code> | <code>AES256-GCM-16</code> </p>"""
    phase1_integrity_algorithms: NotRequired[
        "capo_ec2.types.phase1_integrity_algorithms_request_list.Phase1IntegrityAlgorithmsRequestList"
    ]
    """<p>One or more integrity algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.</p> <p>Valid values: <code>SHA1</code> | <code>SHA2-256</code> | <code>SHA2-384</code> | <code>SHA2-512</code> </p>"""
    phase2_integrity_algorithms: NotRequired[
        "capo_ec2.types.phase2_integrity_algorithms_request_list.Phase2IntegrityAlgorithmsRequestList"
    ]
    """<p>One or more integrity algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.</p> <p>Valid values: <code>SHA1</code> | <code>SHA2-256</code> | <code>SHA2-384</code> | <code>SHA2-512</code> </p>"""
    phase1_dh_group_numbers: NotRequired[
        "capo_ec2.types.phase1_dh_group_numbers_request_list.Phase1DHGroupNumbersRequestList"
    ]
    """<p>One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 1 IKE negotiations.</p> <p>Valid values: <code>2</code> | <code>14</code> | <code>15</code> | <code>16</code> | <code>17</code> | <code>18</code> | <code>19</code> | <code>20</code> | <code>21</code> | <code>22</code> | <code>23</code> | <code>24</code> </p>"""
    phase2_dh_group_numbers: NotRequired[
        "capo_ec2.types.phase2_dh_group_numbers_request_list.Phase2DHGroupNumbersRequestList"
    ]
    """<p>One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 2 IKE negotiations.</p> <p>Valid values: <code>2</code> | <code>5</code> | <code>14</code> | <code>15</code> | <code>16</code> | <code>17</code> | <code>18</code> | <code>19</code> | <code>20</code> | <code>21</code> | <code>22</code> | <code>23</code> | <code>24</code> </p>"""
    ike_versions: NotRequired[
        "capo_ec2.types.ike_versions_request_list.IKEVersionsRequestList"
    ]
    """<p>The IKE versions that are permitted for the VPN tunnel.</p> <p>Valid values: <code>ikev1</code> | <code>ikev2</code> </p>"""
    startup_action: NotRequired["capo_ec2.types.string.String"]
    """<p>The action to take when the establishing the tunnel for the VPN connection. By default, your customer gateway device must initiate the IKE negotiation and bring up the tunnel. Specify <code>start</code> for Amazon Web Services to initiate the IKE negotiation.</p> <p>Valid Values: <code>add</code> | <code>start</code> </p> <p>Default: <code>add</code> </p>"""
    log_options: NotRequired[
        "capo_ec2.types.vpn_tunnel_log_options_specification.VpnTunnelLogOptionsSpecification"
    ]
    """<p>Options for logging VPN tunnel activity.</p>"""
    enable_tunnel_lifecycle_control: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Turn on or off tunnel endpoint lifecycle control feature.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnTunnelOptionsSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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
            (f"{key_prefix}DPDTimeoutSeconds", str(value["dpd_timeout_seconds"]))
        )
    if "dpd_timeout_action" in value:
        pairs.append(
            (f"{key_prefix}DPDTimeoutAction", str(value["dpd_timeout_action"]))
        )
    if "phase1_encryption_algorithms" in value:
        import capo_ec2.types.phase1_encryption_algorithms_request_list

        capo_ec2.types.phase1_encryption_algorithms_request_list.serialize_ec2_query(
            value["phase1_encryption_algorithms"],
            pairs,
            f"{key_prefix}Phase1EncryptionAlgorithm",
        )
    if "phase2_encryption_algorithms" in value:
        import capo_ec2.types.phase2_encryption_algorithms_request_list

        capo_ec2.types.phase2_encryption_algorithms_request_list.serialize_ec2_query(
            value["phase2_encryption_algorithms"],
            pairs,
            f"{key_prefix}Phase2EncryptionAlgorithm",
        )
    if "phase1_integrity_algorithms" in value:
        import capo_ec2.types.phase1_integrity_algorithms_request_list

        capo_ec2.types.phase1_integrity_algorithms_request_list.serialize_ec2_query(
            value["phase1_integrity_algorithms"],
            pairs,
            f"{key_prefix}Phase1IntegrityAlgorithm",
        )
    if "phase2_integrity_algorithms" in value:
        import capo_ec2.types.phase2_integrity_algorithms_request_list

        capo_ec2.types.phase2_integrity_algorithms_request_list.serialize_ec2_query(
            value["phase2_integrity_algorithms"],
            pairs,
            f"{key_prefix}Phase2IntegrityAlgorithm",
        )
    if "phase1_dh_group_numbers" in value:
        import capo_ec2.types.phase1_dh_group_numbers_request_list

        capo_ec2.types.phase1_dh_group_numbers_request_list.serialize_ec2_query(
            value["phase1_dh_group_numbers"], pairs, f"{key_prefix}Phase1DHGroupNumber"
        )
    if "phase2_dh_group_numbers" in value:
        import capo_ec2.types.phase2_dh_group_numbers_request_list

        capo_ec2.types.phase2_dh_group_numbers_request_list.serialize_ec2_query(
            value["phase2_dh_group_numbers"], pairs, f"{key_prefix}Phase2DHGroupNumber"
        )
    if "ike_versions" in value:
        import capo_ec2.types.ike_versions_request_list

        capo_ec2.types.ike_versions_request_list.serialize_ec2_query(
            value["ike_versions"], pairs, f"{key_prefix}IKEVersion"
        )
    if "startup_action" in value:
        pairs.append((f"{key_prefix}StartupAction", str(value["startup_action"])))
    if "log_options" in value:
        import capo_ec2.types.vpn_tunnel_log_options_specification

        capo_ec2.types.vpn_tunnel_log_options_specification.serialize_ec2_query(
            value["log_options"], pairs, f"{key_prefix}LogOptions"
        )
    if "enable_tunnel_lifecycle_control" in value:
        pairs.append(
            (
                f"{key_prefix}EnableTunnelLifecycleControl",
                "true" if value["enable_tunnel_lifecycle_control"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> VpnTunnelOptionsSpecification:
    out: VpnTunnelOptionsSpecification = {}  # type: ignore[typeddict-item]
    child_tunnel_inside_cidr = el.find("TunnelInsideCidr")
    if child_tunnel_inside_cidr is not None:
        out["tunnel_inside_cidr"] = str(child_tunnel_inside_cidr.text or "")
    child_tunnel_inside_ipv6_cidr = el.find("TunnelInsideIpv6Cidr")
    if child_tunnel_inside_ipv6_cidr is not None:
        out["tunnel_inside_ipv6_cidr"] = str(child_tunnel_inside_ipv6_cidr.text or "")
    child_pre_shared_key = el.find("PreSharedKey")
    if child_pre_shared_key is not None:
        out["pre_shared_key"] = str(child_pre_shared_key.text or "")
    child_phase1_lifetime_seconds = el.find("Phase1LifetimeSeconds")
    if child_phase1_lifetime_seconds is not None:
        out["phase1_lifetime_seconds"] = int(child_phase1_lifetime_seconds.text or "")
    child_phase2_lifetime_seconds = el.find("Phase2LifetimeSeconds")
    if child_phase2_lifetime_seconds is not None:
        out["phase2_lifetime_seconds"] = int(child_phase2_lifetime_seconds.text or "")
    child_rekey_margin_time_seconds = el.find("RekeyMarginTimeSeconds")
    if child_rekey_margin_time_seconds is not None:
        out["rekey_margin_time_seconds"] = int(
            child_rekey_margin_time_seconds.text or ""
        )
    child_rekey_fuzz_percentage = el.find("RekeyFuzzPercentage")
    if child_rekey_fuzz_percentage is not None:
        out["rekey_fuzz_percentage"] = int(child_rekey_fuzz_percentage.text or "")
    child_replay_window_size = el.find("ReplayWindowSize")
    if child_replay_window_size is not None:
        out["replay_window_size"] = int(child_replay_window_size.text or "")
    child_dpd_timeout_seconds = el.find("DPDTimeoutSeconds")
    if child_dpd_timeout_seconds is not None:
        out["dpd_timeout_seconds"] = int(child_dpd_timeout_seconds.text or "")
    child_dpd_timeout_action = el.find("DPDTimeoutAction")
    if child_dpd_timeout_action is not None:
        out["dpd_timeout_action"] = str(child_dpd_timeout_action.text or "")
    child_phase1_encryption_algorithms = el.find("Phase1EncryptionAlgorithm")
    if child_phase1_encryption_algorithms is not None:
        import capo_ec2.types.phase1_encryption_algorithms_request_list

        out["phase1_encryption_algorithms"] = (
            capo_ec2.types.phase1_encryption_algorithms_request_list.deserialize_ec2_query(
                child_phase1_encryption_algorithms
            )
        )
    child_phase2_encryption_algorithms = el.find("Phase2EncryptionAlgorithm")
    if child_phase2_encryption_algorithms is not None:
        import capo_ec2.types.phase2_encryption_algorithms_request_list

        out["phase2_encryption_algorithms"] = (
            capo_ec2.types.phase2_encryption_algorithms_request_list.deserialize_ec2_query(
                child_phase2_encryption_algorithms
            )
        )
    child_phase1_integrity_algorithms = el.find("Phase1IntegrityAlgorithm")
    if child_phase1_integrity_algorithms is not None:
        import capo_ec2.types.phase1_integrity_algorithms_request_list

        out["phase1_integrity_algorithms"] = (
            capo_ec2.types.phase1_integrity_algorithms_request_list.deserialize_ec2_query(
                child_phase1_integrity_algorithms
            )
        )
    child_phase2_integrity_algorithms = el.find("Phase2IntegrityAlgorithm")
    if child_phase2_integrity_algorithms is not None:
        import capo_ec2.types.phase2_integrity_algorithms_request_list

        out["phase2_integrity_algorithms"] = (
            capo_ec2.types.phase2_integrity_algorithms_request_list.deserialize_ec2_query(
                child_phase2_integrity_algorithms
            )
        )
    child_phase1_dh_group_numbers = el.find("Phase1DHGroupNumber")
    if child_phase1_dh_group_numbers is not None:
        import capo_ec2.types.phase1_dh_group_numbers_request_list

        out["phase1_dh_group_numbers"] = (
            capo_ec2.types.phase1_dh_group_numbers_request_list.deserialize_ec2_query(
                child_phase1_dh_group_numbers
            )
        )
    child_phase2_dh_group_numbers = el.find("Phase2DHGroupNumber")
    if child_phase2_dh_group_numbers is not None:
        import capo_ec2.types.phase2_dh_group_numbers_request_list

        out["phase2_dh_group_numbers"] = (
            capo_ec2.types.phase2_dh_group_numbers_request_list.deserialize_ec2_query(
                child_phase2_dh_group_numbers
            )
        )
    child_ike_versions = el.find("IKEVersion")
    if child_ike_versions is not None:
        import capo_ec2.types.ike_versions_request_list

        out["ike_versions"] = (
            capo_ec2.types.ike_versions_request_list.deserialize_ec2_query(
                child_ike_versions
            )
        )
    child_startup_action = el.find("StartupAction")
    if child_startup_action is not None:
        out["startup_action"] = str(child_startup_action.text or "")
    child_log_options = el.find("LogOptions")
    if child_log_options is not None:
        import capo_ec2.types.vpn_tunnel_log_options_specification

        out["log_options"] = (
            capo_ec2.types.vpn_tunnel_log_options_specification.deserialize_ec2_query(
                child_log_options
            )
        )
    child_enable_tunnel_lifecycle_control = el.find("EnableTunnelLifecycleControl")
    if child_enable_tunnel_lifecycle_control is not None:
        out["enable_tunnel_lifecycle_control"] = (
            child_enable_tunnel_lifecycle_control.text or ""
        ).lower() == "true"
    return out


def redact_sensitive(value: VpnTunnelOptionsSpecification) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pre_shared_key" in value:
        out["pre_shared_key"] = "*** Sensitive Data Redacted ***"
    return out
