"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateTLSInspectionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.tls_inspection_configuration
    import capo_network_firewall.types.update_token


class UpdateTLSInspectionConfigurationRequest(TypedDict, closed=True):
    tls_inspection_configuration_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p>"""
    tls_inspection_configuration_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p>"""
    tls_inspection_configuration: "capo_network_firewall.types.tls_inspection_configuration.TLSInspectionConfiguration"
    """<p>The object that defines a TLS inspection configuration. This, along with <a>TLSInspectionConfigurationResponse</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p> <p>Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.</p> <p>To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html">Inspecting SSL/TLS traffic with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the TLS inspection configuration. </p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your TLS inspection configuration.</p>"""
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the TLS inspection configuration. The token marks the state of the TLS inspection configuration resource at the time of the request. </p> <p>To make changes to the TLS inspection configuration, you provide the token in your request. Network Firewall uses the token to ensure that the TLS inspection configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the TLS inspection configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateTLSInspectionConfigurationRequest) -> dict:
    out: dict = {}
    if "tls_inspection_configuration_arn" in value:
        out["TLSInspectionConfigurationArn"] = value["tls_inspection_configuration_arn"]
    if "tls_inspection_configuration_name" in value:
        out["TLSInspectionConfigurationName"] = value[
            "tls_inspection_configuration_name"
        ]
    import capo_network_firewall.types.tls_inspection_configuration

    out["TLSInspectionConfiguration"] = (
        capo_network_firewall.types.tls_inspection_configuration.serialize_aws_json_1_0(
            value["tls_inspection_configuration"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "encryption_configuration" in value:
        import capo_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateTLSInspectionConfigurationRequest:
    out: UpdateTLSInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("TLSInspectionConfigurationArn") is not None:
        out["tls_inspection_configuration_arn"] = data["TLSInspectionConfigurationArn"]
    if data.get("TLSInspectionConfigurationName") is not None:
        out["tls_inspection_configuration_name"] = data[
            "TLSInspectionConfigurationName"
        ]
    if data.get("TLSInspectionConfiguration") is not None:
        import capo_network_firewall.types.tls_inspection_configuration

        out["tls_inspection_configuration"] = (
            capo_network_firewall.types.tls_inspection_configuration.deserialize_aws_json_1_0(
                data["TLSInspectionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTLSInspectionConfigurationRequest.tls_inspection_configuration required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        raise DeserializationError(
            "UpdateTLSInspectionConfigurationRequest.update_token required"
        )
    return out
