"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ServerCertificateScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.addresses
    import capo_network_firewall.types.decryption_action
    import capo_network_firewall.types.domain_match
    import capo_network_firewall.types.port_ranges
    import capo_network_firewall.types.protocol_numbers
    import capo_network_firewall.types.tls_inspection_scope_deployment_mode


class ServerCertificateScope(TypedDict, closed=True):
    sources: NotRequired["capo_network_firewall.types.addresses.Addresses"]
    """<p>The source IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any source address.</p>"""
    destinations: NotRequired["capo_network_firewall.types.addresses.Addresses"]
    """<p>The destination IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any destination address.</p>"""
    source_ports: NotRequired["capo_network_firewall.types.port_ranges.PortRanges"]
    """<p>The source ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any source port.</p> <p>You can specify individual ports, for example <code>1994</code>, and you can specify port ranges, such as <code>1990:1994</code>.</p>"""
    destination_ports: NotRequired["capo_network_firewall.types.port_ranges.PortRanges"]
    """<p>The destination ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any destination port.</p> <p>You can specify individual ports, for example <code>1994</code>, and you can specify port ranges, such as <code>1990:1994</code>.</p>"""
    protocols: NotRequired[
        "capo_network_firewall.types.protocol_numbers.ProtocolNumbers"
    ]
    """<p>The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.</p> <p>Network Firewall currently supports only TCP.</p>"""
    domain_match: NotRequired["capo_network_firewall.types.domain_match.DomainMatch"]
    """<p>The domains that this scope matches, based on the host name in the client's HTTP CONNECT request. Domain matching applies only to proxy mode firewalls. If you specify <code>DomainMatch</code>, you must set <code>DeploymentMode</code> to <code>EXPLICIT_PROXY_ONLY</code>. If you don't specify <code>DomainMatch</code>, the scope matches traffic by its source, destination, ports, and protocols only.</p>"""
    decryption_action: NotRequired[
        "capo_network_firewall.types.decryption_action.DecryptionAction"
    ]
    """<p>Whether the firewall decrypts traffic that matches this scope. You can choose from the following values:</p> <ul> <li> <p> <code>DECRYPT</code> - The firewall decrypts the traffic for inspection.</p> </li> <li> <p> <code>BYPASS</code> - The firewall doesn't decrypt the traffic.</p> </li> </ul>"""
    deployment_mode: NotRequired[
        "capo_network_firewall.types.tls_inspection_scope_deployment_mode.TLSInspectionScopeDeploymentMode"
    ]
    """<p>The type of firewall that this scope applies to. If you don't specify a value, the scope applies to both types, the same as <code>ALL</code>. You can choose from the following values:</p> <ul> <li> <p> <code>ALL</code> - The scope applies to both transparent firewalls and proxy mode firewalls.</p> </li> <li> <p> <code>TRANSPARENT_FIREWALL_ONLY</code> - The scope applies only to transparent firewalls.</p> </li> <li> <p> <code>EXPLICIT_PROXY_ONLY</code> - The scope applies only to proxy mode firewalls. A scope that specifies <code>DomainMatch</code> must use this value.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServerCertificateScope) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_network_firewall.types.addresses

        out["Sources"] = capo_network_firewall.types.addresses.serialize_aws_json_1_0(
            value["sources"]
        )
    if "destinations" in value:
        import capo_network_firewall.types.addresses

        out["Destinations"] = (
            capo_network_firewall.types.addresses.serialize_aws_json_1_0(
                value["destinations"]
            )
        )
    if "source_ports" in value:
        import capo_network_firewall.types.port_ranges

        out["SourcePorts"] = (
            capo_network_firewall.types.port_ranges.serialize_aws_json_1_0(
                value["source_ports"]
            )
        )
    if "destination_ports" in value:
        import capo_network_firewall.types.port_ranges

        out["DestinationPorts"] = (
            capo_network_firewall.types.port_ranges.serialize_aws_json_1_0(
                value["destination_ports"]
            )
        )
    if "protocols" in value:
        import capo_network_firewall.types.protocol_numbers

        out["Protocols"] = (
            capo_network_firewall.types.protocol_numbers.serialize_aws_json_1_0(
                value["protocols"]
            )
        )
    if "domain_match" in value:
        import capo_network_firewall.types.domain_match

        out["DomainMatch"] = (
            capo_network_firewall.types.domain_match.serialize_aws_json_1_0(
                value["domain_match"]
            )
        )
    if "decryption_action" in value:
        import capo_network_firewall.types.decryption_action

        out["DecryptionAction"] = (
            capo_network_firewall.types.decryption_action.serialize_aws_json_1_0(
                value["decryption_action"]
            )
        )
    if "deployment_mode" in value:
        import capo_network_firewall.types.tls_inspection_scope_deployment_mode

        out["DeploymentMode"] = (
            capo_network_firewall.types.tls_inspection_scope_deployment_mode.serialize_aws_json_1_0(
                value["deployment_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServerCertificateScope:
    out: ServerCertificateScope = {}  # type: ignore[typeddict-item]
    if data.get("Sources") is not None:
        import capo_network_firewall.types.addresses

        out["sources"] = capo_network_firewall.types.addresses.deserialize_aws_json_1_0(
            data["Sources"]
        )
    if data.get("Destinations") is not None:
        import capo_network_firewall.types.addresses

        out["destinations"] = (
            capo_network_firewall.types.addresses.deserialize_aws_json_1_0(
                data["Destinations"]
            )
        )
    if data.get("SourcePorts") is not None:
        import capo_network_firewall.types.port_ranges

        out["source_ports"] = (
            capo_network_firewall.types.port_ranges.deserialize_aws_json_1_0(
                data["SourcePorts"]
            )
        )
    if data.get("DestinationPorts") is not None:
        import capo_network_firewall.types.port_ranges

        out["destination_ports"] = (
            capo_network_firewall.types.port_ranges.deserialize_aws_json_1_0(
                data["DestinationPorts"]
            )
        )
    if data.get("Protocols") is not None:
        import capo_network_firewall.types.protocol_numbers

        out["protocols"] = (
            capo_network_firewall.types.protocol_numbers.deserialize_aws_json_1_0(
                data["Protocols"]
            )
        )
    if data.get("DomainMatch") is not None:
        import capo_network_firewall.types.domain_match

        out["domain_match"] = (
            capo_network_firewall.types.domain_match.deserialize_aws_json_1_0(
                data["DomainMatch"]
            )
        )
    if data.get("DecryptionAction") is not None:
        import capo_network_firewall.types.decryption_action

        out["decryption_action"] = (
            capo_network_firewall.types.decryption_action.deserialize_aws_json_1_0(
                data["DecryptionAction"]
            )
        )
    if data.get("DeploymentMode") is not None:
        import capo_network_firewall.types.tls_inspection_scope_deployment_mode

        out["deployment_mode"] = (
            capo_network_firewall.types.tls_inspection_scope_deployment_mode.deserialize_aws_json_1_0(
                data["DeploymentMode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServerCertificateScope) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_network_firewall.types.addresses

        out["Sources"] = capo_network_firewall.types.addresses.serialize_cbor(
            value["sources"]
        )
    if "destinations" in value:
        import capo_network_firewall.types.addresses

        out["Destinations"] = capo_network_firewall.types.addresses.serialize_cbor(
            value["destinations"]
        )
    if "source_ports" in value:
        import capo_network_firewall.types.port_ranges

        out["SourcePorts"] = capo_network_firewall.types.port_ranges.serialize_cbor(
            value["source_ports"]
        )
    if "destination_ports" in value:
        import capo_network_firewall.types.port_ranges

        out["DestinationPorts"] = (
            capo_network_firewall.types.port_ranges.serialize_cbor(
                value["destination_ports"]
            )
        )
    if "protocols" in value:
        import capo_network_firewall.types.protocol_numbers

        out["Protocols"] = capo_network_firewall.types.protocol_numbers.serialize_cbor(
            value["protocols"]
        )
    if "domain_match" in value:
        import capo_network_firewall.types.domain_match

        out["DomainMatch"] = capo_network_firewall.types.domain_match.serialize_cbor(
            value["domain_match"]
        )
    if "decryption_action" in value:
        import capo_network_firewall.types.decryption_action

        out["DecryptionAction"] = (
            capo_network_firewall.types.decryption_action.serialize_cbor(
                value["decryption_action"]
            )
        )
    if "deployment_mode" in value:
        import capo_network_firewall.types.tls_inspection_scope_deployment_mode

        out["DeploymentMode"] = (
            capo_network_firewall.types.tls_inspection_scope_deployment_mode.serialize_cbor(
                value["deployment_mode"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ServerCertificateScope:
    out: ServerCertificateScope = {}  # type: ignore[typeddict-item]
    if data.get("Sources") is not None:
        import capo_network_firewall.types.addresses

        out["sources"] = capo_network_firewall.types.addresses.deserialize_cbor(
            data["Sources"]
        )
    if data.get("Destinations") is not None:
        import capo_network_firewall.types.addresses

        out["destinations"] = capo_network_firewall.types.addresses.deserialize_cbor(
            data["Destinations"]
        )
    if data.get("SourcePorts") is not None:
        import capo_network_firewall.types.port_ranges

        out["source_ports"] = capo_network_firewall.types.port_ranges.deserialize_cbor(
            data["SourcePorts"]
        )
    if data.get("DestinationPorts") is not None:
        import capo_network_firewall.types.port_ranges

        out["destination_ports"] = (
            capo_network_firewall.types.port_ranges.deserialize_cbor(
                data["DestinationPorts"]
            )
        )
    if data.get("Protocols") is not None:
        import capo_network_firewall.types.protocol_numbers

        out["protocols"] = (
            capo_network_firewall.types.protocol_numbers.deserialize_cbor(
                data["Protocols"]
            )
        )
    if data.get("DomainMatch") is not None:
        import capo_network_firewall.types.domain_match

        out["domain_match"] = capo_network_firewall.types.domain_match.deserialize_cbor(
            data["DomainMatch"]
        )
    if data.get("DecryptionAction") is not None:
        import capo_network_firewall.types.decryption_action

        out["decryption_action"] = (
            capo_network_firewall.types.decryption_action.deserialize_cbor(
                data["DecryptionAction"]
            )
        )
    if data.get("DeploymentMode") is not None:
        import capo_network_firewall.types.tls_inspection_scope_deployment_mode

        out["deployment_mode"] = (
            capo_network_firewall.types.tls_inspection_scope_deployment_mode.deserialize_cbor(
                data["DeploymentMode"]
            )
        )
    return out
