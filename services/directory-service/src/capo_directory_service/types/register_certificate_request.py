"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegisterCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.certificate_data
    import capo_directory_service.types.certificate_type
    import capo_directory_service.types.client_cert_auth_settings
    import capo_directory_service.types.directory_id


class RegisterCertificateRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    certificate_data: "capo_directory_service.types.certificate_data.CertificateData"
    """<p>The certificate PEM string that needs to be registered.</p>"""
    type: NotRequired["capo_directory_service.types.certificate_type.CertificateType"]
    """<p>The function that the registered certificate performs. Valid values include <code>ClientLDAPS</code> or <code>ClientCertAuth</code>. The default value is <code>ClientLDAPS</code>.</p>"""
    client_cert_auth_settings: NotRequired[
        "capo_directory_service.types.client_cert_auth_settings.ClientCertAuthSettings"
    ]
    """<p>A <code>ClientCertAuthSettings</code> object that contains client certificate authentication settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterCertificateRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["CertificateData"] = value["certificate_data"]
    if "type" in value:
        import capo_directory_service.types.certificate_type

        out["Type"] = (
            capo_directory_service.types.certificate_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "client_cert_auth_settings" in value:
        import capo_directory_service.types.client_cert_auth_settings

        out["ClientCertAuthSettings"] = (
            capo_directory_service.types.client_cert_auth_settings.serialize_aws_json_1_1(
                value["client_cert_auth_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterCertificateRequest:
    out: RegisterCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("CertificateData") is not None:
        out["certificate_data"] = data["CertificateData"]
    else:
        out["certificate_data"] = ""
    if data.get("Type") is not None:
        import capo_directory_service.types.certificate_type

        out["type"] = (
            capo_directory_service.types.certificate_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("ClientCertAuthSettings") is not None:
        import capo_directory_service.types.client_cert_auth_settings

        out["client_cert_auth_settings"] = (
            capo_directory_service.types.client_cert_auth_settings.deserialize_aws_json_1_1(
                data["ClientCertAuthSettings"]
            )
        )
    return out
