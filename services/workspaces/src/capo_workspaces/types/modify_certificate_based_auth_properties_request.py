"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyCertificateBasedAuthPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.certificate_based_auth_properties
    import capo_workspaces.types.deletable_certificate_based_auth_properties_list
    import capo_workspaces.types.directory_id


class ModifyCertificateBasedAuthPropertiesRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The resource identifiers, in the form of directory IDs.</p>"""
    certificate_based_auth_properties: NotRequired[
        "capo_workspaces.types.certificate_based_auth_properties.CertificateBasedAuthProperties"
    ]
    """<p>The properties of the certificate-based authentication.</p>"""
    properties_to_delete: NotRequired[
        "capo_workspaces.types.deletable_certificate_based_auth_properties_list.DeletableCertificateBasedAuthPropertiesList"
    ]
    """<p>The properties of the certificate-based authentication you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyCertificateBasedAuthPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "certificate_based_auth_properties" in value:
        import capo_workspaces.types.certificate_based_auth_properties

        out["CertificateBasedAuthProperties"] = (
            capo_workspaces.types.certificate_based_auth_properties.serialize_aws_json_1_1(
                value["certificate_based_auth_properties"]
            )
        )
    if "properties_to_delete" in value:
        import capo_workspaces.types.deletable_certificate_based_auth_properties_list

        out["PropertiesToDelete"] = (
            capo_workspaces.types.deletable_certificate_based_auth_properties_list.serialize_aws_json_1_1(
                value["properties_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyCertificateBasedAuthPropertiesRequest:
    out: ModifyCertificateBasedAuthPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("CertificateBasedAuthProperties") is not None:
        import capo_workspaces.types.certificate_based_auth_properties

        out["certificate_based_auth_properties"] = (
            capo_workspaces.types.certificate_based_auth_properties.deserialize_aws_json_1_1(
                data["CertificateBasedAuthProperties"]
            )
        )
    if data.get("PropertiesToDelete") is not None:
        import capo_workspaces.types.deletable_certificate_based_auth_properties_list

        out["properties_to_delete"] = (
            capo_workspaces.types.deletable_certificate_based_auth_properties_list.deserialize_aws_json_1_1(
                data["PropertiesToDelete"]
            )
        )
    return out
