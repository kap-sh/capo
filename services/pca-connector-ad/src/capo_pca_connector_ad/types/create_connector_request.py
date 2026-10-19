"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.certificate_authority_arn
    import capo_pca_connector_ad.types.client_token
    import capo_pca_connector_ad.types.directory_id
    import capo_pca_connector_ad.types.tags
    import capo_pca_connector_ad.types.vpc_information


class CreateConnectorRequest(TypedDict, closed=True):
    directory_id: "capo_pca_connector_ad.types.directory_id.DirectoryId"
    """<p>The identifier of the Active Directory.</p>"""
    certificate_authority_arn: (
        "capo_pca_connector_ad.types.certificate_authority_arn.CertificateAuthorityArn"
    )
    """<p> The Amazon Resource Name (ARN) of the certificate authority being used.</p>"""
    vpc_information: "capo_pca_connector_ad.types.vpc_information.VpcInformation"
    """<p>Information about your VPC and security groups used with the connector.</p>"""
    client_token: NotRequired["capo_pca_connector_ad.types.client_token.ClientToken"]
    """<p>Idempotency token.</p>"""
    tags: NotRequired["capo_pca_connector_ad.types.tags.Tags"]
    """<p>Metadata assigned to a connector consisting of a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    import capo_pca_connector_ad.types.vpc_information

    out["VpcInformation"] = capo_pca_connector_ad.types.vpc_information.serialize_json(
        value["vpc_information"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_pca_connector_ad.types.tags

        out["Tags"] = capo_pca_connector_ad.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConnectorRequest:
    out: CreateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        out["certificate_authority_arn"] = ""
    if data.get("VpcInformation") is not None:
        import capo_pca_connector_ad.types.vpc_information

        out["vpc_information"] = (
            capo_pca_connector_ad.types.vpc_information.deserialize_json(
                data["VpcInformation"]
            )
        )
    else:
        raise DeserializationError("CreateConnectorRequest.vpc_information required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_pca_connector_ad.types.tags

        out["tags"] = capo_pca_connector_ad.types.tags.deserialize_json(data["Tags"])
    return out
