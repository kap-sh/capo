"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedSecurityPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.fips
    import capo_transfer.types.security_policy_name
    import capo_transfer.types.security_policy_options
    import capo_transfer.types.security_policy_protocols
    import capo_transfer.types.security_policy_resource_type


class DescribedSecurityPolicy(TypedDict, closed=True):
    fips: NotRequired["capo_transfer.types.fips.Fips"]
    """<p>Specifies whether this policy enables Federal Information Processing Standards (FIPS). This parameter applies to both server and connector security policies.</p>"""
    security_policy_name: "capo_transfer.types.security_policy_name.SecurityPolicyName"
    """<p>The text name of the specified security policy.</p>"""
    ssh_ciphers: NotRequired[
        "capo_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the enabled Secure Shell (SSH) cipher encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.</p>"""
    ssh_kexs: NotRequired[
        "capo_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the enabled SSH key exchange (KEX) encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.</p>"""
    ssh_macs: NotRequired[
        "capo_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the enabled SSH message authentication code (MAC) encryption algorithms in the security policy that is attached to the server or connector. This parameter applies to both server and connector security policies.</p>"""
    tls_ciphers: NotRequired[
        "capo_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the enabled Transport Layer Security (TLS) cipher encryption algorithms in the security policy that is attached to the server.</p> <note> <p>This parameter only applies to security policies for servers.</p> </note>"""
    ssh_host_key_algorithms: NotRequired[
        "capo_transfer.types.security_policy_options.SecurityPolicyOptions"
    ]
    """<p>Lists the host key algorithms for the security policy.</p> <note> <p>This parameter only applies to security policies for connectors.</p> </note>"""
    type: NotRequired[
        "capo_transfer.types.security_policy_resource_type.SecurityPolicyResourceType"
    ]
    """<p>The resource type to which the security policy applies, either server or connector.</p>"""
    protocols: NotRequired[
        "capo_transfer.types.security_policy_protocols.SecurityPolicyProtocols"
    ]
    """<p>Lists the file transfer protocols that the security policy applies to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedSecurityPolicy) -> dict:
    out: dict = {}
    if "fips" in value:
        out["Fips"] = value["fips"]
    out["SecurityPolicyName"] = value["security_policy_name"]
    if "ssh_ciphers" in value:
        import capo_transfer.types.security_policy_options

        out["SshCiphers"] = (
            capo_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["ssh_ciphers"]
            )
        )
    if "ssh_kexs" in value:
        import capo_transfer.types.security_policy_options

        out["SshKexs"] = (
            capo_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["ssh_kexs"]
            )
        )
    if "ssh_macs" in value:
        import capo_transfer.types.security_policy_options

        out["SshMacs"] = (
            capo_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["ssh_macs"]
            )
        )
    if "tls_ciphers" in value:
        import capo_transfer.types.security_policy_options

        out["TlsCiphers"] = (
            capo_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["tls_ciphers"]
            )
        )
    if "ssh_host_key_algorithms" in value:
        import capo_transfer.types.security_policy_options

        out["SshHostKeyAlgorithms"] = (
            capo_transfer.types.security_policy_options.serialize_aws_json_1_1(
                value["ssh_host_key_algorithms"]
            )
        )
    if "type" in value:
        import capo_transfer.types.security_policy_resource_type

        out["Type"] = (
            capo_transfer.types.security_policy_resource_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "protocols" in value:
        import capo_transfer.types.security_policy_protocols

        out["Protocols"] = (
            capo_transfer.types.security_policy_protocols.serialize_aws_json_1_1(
                value["protocols"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedSecurityPolicy:
    out: DescribedSecurityPolicy = {}  # type: ignore[typeddict-item]
    if data.get("Fips") is not None:
        out["fips"] = data["Fips"]
    if data.get("SecurityPolicyName") is not None:
        out["security_policy_name"] = data["SecurityPolicyName"]
    else:
        out["security_policy_name"] = ""
    if data.get("SshCiphers") is not None:
        import capo_transfer.types.security_policy_options

        out["ssh_ciphers"] = (
            capo_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["SshCiphers"]
            )
        )
    if data.get("SshKexs") is not None:
        import capo_transfer.types.security_policy_options

        out["ssh_kexs"] = (
            capo_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["SshKexs"]
            )
        )
    if data.get("SshMacs") is not None:
        import capo_transfer.types.security_policy_options

        out["ssh_macs"] = (
            capo_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["SshMacs"]
            )
        )
    if data.get("TlsCiphers") is not None:
        import capo_transfer.types.security_policy_options

        out["tls_ciphers"] = (
            capo_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["TlsCiphers"]
            )
        )
    if data.get("SshHostKeyAlgorithms") is not None:
        import capo_transfer.types.security_policy_options

        out["ssh_host_key_algorithms"] = (
            capo_transfer.types.security_policy_options.deserialize_aws_json_1_1(
                data["SshHostKeyAlgorithms"]
            )
        )
    if data.get("Type") is not None:
        import capo_transfer.types.security_policy_resource_type

        out["type"] = (
            capo_transfer.types.security_policy_resource_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Protocols") is not None:
        import capo_transfer.types.security_policy_protocols

        out["protocols"] = (
            capo_transfer.types.security_policy_protocols.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    return out
