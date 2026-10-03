"""Generated from Smithy shape ``com.amazonaws.iot#RegisterCACertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.allow_auto_registration
    import capo_iot.types.certificate_mode
    import capo_iot.types.certificate_pem
    import capo_iot.types.registration_config
    import capo_iot.types.set_as_active
    import capo_iot.types.tag_list


class RegisterCACertificateRequest(TypedDict, closed=True):
    ca_certificate: "capo_iot.types.certificate_pem.CertificatePem"
    """<p>The CA certificate.</p>"""
    verification_certificate: NotRequired[
        "capo_iot.types.certificate_pem.CertificatePem"
    ]
    """<p>The private key verification certificate. If <code>certificateMode</code> is <code>SNI_ONLY</code>, the <code>verificationCertificate</code> field must be empty. If <code>certificateMode</code> is <code>DEFAULT</code> or not provided, the <code>verificationCertificate</code> field must not be empty. </p>"""
    set_as_active: "capo_iot.types.set_as_active.SetAsActive"
    """<p>A boolean value that specifies if the CA certificate is set to active.</p> <p>Valid values: <code>ACTIVE | INACTIVE</code> </p>"""
    allow_auto_registration: (
        "capo_iot.types.allow_auto_registration.AllowAutoRegistration"
    )
    """<p>Allows this CA certificate to be used for auto registration of device certificates.</p>"""
    registration_config: NotRequired[
        "capo_iot.types.registration_config.RegistrationConfig"
    ]
    """<p>Information about the registration configuration.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the CA certificate.</p> <note> <p>For URI Request parameters use format: ...key1=value1&key2=value2...</p> <p>For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."</p> <p>For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."</p> </note>"""
    certificate_mode: NotRequired["capo_iot.types.certificate_mode.CertificateMode"]
    """<p>Describes the certificate mode in which the Certificate Authority (CA) will be registered. If the <code>verificationCertificate</code> field is not provided, set <code>certificateMode</code> to be <code>SNI_ONLY</code>. If the <code>verificationCertificate</code> field is provided, set <code>certificateMode</code> to be <code>DEFAULT</code>. When <code>certificateMode</code> is not provided, it defaults to <code>DEFAULT</code>. All the device certificates that are registered using this CA will be registered in the same certificate mode as the CA. For more information about certificate mode for device certificates, see <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode"> certificate mode</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCACertificateRequest) -> dict:
    out: dict = {}
    out["caCertificate"] = value["ca_certificate"]
    if "verification_certificate" in value:
        out["verificationCertificate"] = value["verification_certificate"]
    if "registration_config" in value:
        import capo_iot.types.registration_config

        out["registrationConfig"] = capo_iot.types.registration_config.serialize_json(
            value["registration_config"]
        )
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    if "certificate_mode" in value:
        import capo_iot.types.certificate_mode

        out["certificateMode"] = capo_iot.types.certificate_mode.serialize_json(
            value["certificate_mode"]
        )
    return out


def deserialize_json(data: dict) -> RegisterCACertificateRequest:
    out: RegisterCACertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("caCertificate") is not None:
        out["ca_certificate"] = data["caCertificate"]
    else:
        raise DeserializationError(
            "RegisterCACertificateRequest.ca_certificate required"
        )
    if data.get("verificationCertificate") is not None:
        out["verification_certificate"] = data["verificationCertificate"]
    if data.get("registrationConfig") is not None:
        import capo_iot.types.registration_config

        out["registration_config"] = (
            capo_iot.types.registration_config.deserialize_json(
                data["registrationConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    if data.get("certificateMode") is not None:
        import capo_iot.types.certificate_mode

        out["certificate_mode"] = capo_iot.types.certificate_mode.deserialize_json(
            data["certificateMode"]
        )
    return out
