"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#CreateConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_scep.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.certificate_authority_arn
    import capo_pca_connector_scep.types.client_token
    import capo_pca_connector_scep.types.mobile_device_management
    import capo_pca_connector_scep.types.tags
    import capo_pca_connector_scep.types.vpc_endpoint_id


class CreateConnectorRequest(TypedDict, closed=True):
    certificate_authority_arn: "capo_pca_connector_scep.types.certificate_authority_arn.CertificateAuthorityArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Private Certificate Authority certificate authority to use with this connector. Due to security vulnerabilities present in the SCEP protocol, we recommend using a private CA that's dedicated for use with the connector.</p> <p>To retrieve the private CAs associated with your account, you can call <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> using the Amazon Web Services Private CA API.</p>"""
    mobile_device_management: NotRequired[
        "capo_pca_connector_scep.types.mobile_device_management.MobileDeviceManagement"
    ]
    """<p>If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use. A general-purpose connector is designed to work with clients or endpoints that support the SCEP protocol, except Connector for SCEP for Microsoft Intune. With connectors for general-purpose use, you manage SCEP challenge passwords using Connector for SCEP. For information about considerations and limitations with using Connector for SCEP, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlc4scep-considerations-limitations.html">Considerations and Limitations</a>.</p> <p>If you provide an <code>IntuneConfiguration</code>, Connector for SCEP creates a connector for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune. For more information, see <a href="https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html">Using Connector for SCEP for Microsoft Intune</a>.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_pca_connector_scep.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>If you don't supply a value, by default Connector for SCEP creates a connector accessible over the public internet. If you provide a VPC endpoint ID, creates a connector accessible only through that specific VPC endpoint.</p>"""
    client_token: NotRequired["capo_pca_connector_scep.types.client_token.ClientToken"]
    """<p>Custom string that can be used to distinguish between calls to the <a href="https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>"""
    tags: NotRequired["capo_pca_connector_scep.types.tags.Tags"]
    """<p>The key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "mobile_device_management" in value:
        import capo_pca_connector_scep.types.mobile_device_management

        out["MobileDeviceManagement"] = (
            capo_pca_connector_scep.types.mobile_device_management.serialize_json(
                value["mobile_device_management"]
            )
        )
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_pca_connector_scep.types.tags

        out["Tags"] = capo_pca_connector_scep.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConnectorRequest:
    out: CreateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "CreateConnectorRequest.certificate_authority_arn required"
        )
    if data.get("MobileDeviceManagement") is not None:
        import capo_pca_connector_scep.types.mobile_device_management

        out["mobile_device_management"] = (
            capo_pca_connector_scep.types.mobile_device_management.deserialize_json(
                data["MobileDeviceManagement"]
            )
        )
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_pca_connector_scep.types.tags

        out["tags"] = capo_pca_connector_scep.types.tags.deserialize_json(data["Tags"])
    return out
