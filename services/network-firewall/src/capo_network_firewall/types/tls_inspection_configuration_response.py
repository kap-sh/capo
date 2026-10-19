"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TLSInspectionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.certificates
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.last_update_time
    import capo_network_firewall.types.number_of_associations
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_id
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.resource_status
    import capo_network_firewall.types.tag_list
    import capo_network_firewall.types.tls_certificate_data


class TLSInspectionConfigurationResponse(TypedDict, closed=True):
    tls_inspection_configuration_arn: (
        "capo_network_firewall.types.resource_arn.ResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p>"""
    tls_inspection_configuration_name: (
        "capo_network_firewall.types.resource_name.ResourceName"
    )
    """<p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p>"""
    tls_inspection_configuration_id: (
        "capo_network_firewall.types.resource_id.ResourceId"
    )
    """<p>A unique identifier for the TLS inspection configuration. This ID is returned in the responses to create and list commands. You provide it to operations such as update and delete.</p>"""
    tls_inspection_configuration_status: NotRequired[
        "capo_network_firewall.types.resource_status.ResourceStatus"
    ]
    """<p>Detailed information about the current status of a <a>TLSInspectionConfiguration</a>. You can retrieve this for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a> and providing the TLS inspection configuration name and ARN.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the TLS inspection configuration. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    last_modified_time: NotRequired[
        "capo_network_firewall.types.last_update_time.LastUpdateTime"
    ]
    """<p>The last time that the TLS inspection configuration was changed.</p>"""
    number_of_associations: NotRequired[
        "capo_network_firewall.types.number_of_associations.NumberOfAssociations"
    ]
    """<p>The number of firewall policies that use this TLS inspection configuration.</p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your TLS inspection configuration.</p>"""
    certificates: NotRequired["capo_network_firewall.types.certificates.Certificates"]
    """<p>A list of the certificates associated with the TLS inspection configuration.</p>"""
    certificate_authority: NotRequired[
        "capo_network_firewall.types.tls_certificate_data.TlsCertificateData"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TLSInspectionConfigurationResponse) -> dict:
    out: dict = {}
    out["TLSInspectionConfigurationArn"] = value["tls_inspection_configuration_arn"]
    out["TLSInspectionConfigurationName"] = value["tls_inspection_configuration_name"]
    out["TLSInspectionConfigurationId"] = value["tls_inspection_configuration_id"]
    if "tls_inspection_configuration_status" in value:
        import capo_network_firewall.types.resource_status

        out["TLSInspectionConfigurationStatus"] = (
            capo_network_firewall.types.resource_status.serialize_aws_json_1_0(
                value["tls_inspection_configuration_status"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "last_modified_time" in value:
        import capo_network_firewall.types.last_update_time

        out["LastModifiedTime"] = (
            capo_network_firewall.types.last_update_time.serialize_aws_json_1_0(
                value["last_modified_time"]
            )
        )
    if "number_of_associations" in value:
        out["NumberOfAssociations"] = value["number_of_associations"]
    if "encryption_configuration" in value:
        import capo_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "certificates" in value:
        import capo_network_firewall.types.certificates

        out["Certificates"] = (
            capo_network_firewall.types.certificates.serialize_aws_json_1_0(
                value["certificates"]
            )
        )
    if "certificate_authority" in value:
        import capo_network_firewall.types.tls_certificate_data

        out["CertificateAuthority"] = (
            capo_network_firewall.types.tls_certificate_data.serialize_aws_json_1_0(
                value["certificate_authority"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TLSInspectionConfigurationResponse:
    out: TLSInspectionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("TLSInspectionConfigurationArn") is not None:
        out["tls_inspection_configuration_arn"] = data["TLSInspectionConfigurationArn"]
    else:
        out["tls_inspection_configuration_arn"] = ""
    if data.get("TLSInspectionConfigurationName") is not None:
        out["tls_inspection_configuration_name"] = data[
            "TLSInspectionConfigurationName"
        ]
    else:
        out["tls_inspection_configuration_name"] = ""
    if data.get("TLSInspectionConfigurationId") is not None:
        out["tls_inspection_configuration_id"] = data["TLSInspectionConfigurationId"]
    else:
        out["tls_inspection_configuration_id"] = ""
    if data.get("TLSInspectionConfigurationStatus") is not None:
        import capo_network_firewall.types.resource_status

        out["tls_inspection_configuration_status"] = (
            capo_network_firewall.types.resource_status.deserialize_aws_json_1_0(
                data["TLSInspectionConfigurationStatus"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_network_firewall.types.last_update_time

        out["last_modified_time"] = (
            capo_network_firewall.types.last_update_time.deserialize_aws_json_1_0(
                data["LastModifiedTime"]
            )
        )
    if data.get("NumberOfAssociations") is not None:
        out["number_of_associations"] = data["NumberOfAssociations"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("Certificates") is not None:
        import capo_network_firewall.types.certificates

        out["certificates"] = (
            capo_network_firewall.types.certificates.deserialize_aws_json_1_0(
                data["Certificates"]
            )
        )
    if data.get("CertificateAuthority") is not None:
        import capo_network_firewall.types.tls_certificate_data

        out["certificate_authority"] = (
            capo_network_firewall.types.tls_certificate_data.deserialize_aws_json_1_0(
                data["CertificateAuthority"]
            )
        )
    return out
