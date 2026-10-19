"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateV3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.certificate_validity
    import capo_pca_connector_ad.types.enrollment_flags_v3
    import capo_pca_connector_ad.types.extensions_v3
    import capo_pca_connector_ad.types.general_flags_v3
    import capo_pca_connector_ad.types.hash_algorithm
    import capo_pca_connector_ad.types.private_key_attributes_v3
    import capo_pca_connector_ad.types.private_key_flags_v3
    import capo_pca_connector_ad.types.subject_name_flags_v3
    import capo_pca_connector_ad.types.template_name_list


class TemplateV3(TypedDict, closed=True):
    certificate_validity: (
        "capo_pca_connector_ad.types.certificate_validity.CertificateValidity"
    )
    """<p>Certificate validity describes the validity and renewal periods of a certificate.</p>"""
    superseded_templates: NotRequired[
        "capo_pca_connector_ad.types.template_name_list.TemplateNameList"
    ]
    """<p>List of templates in Active Directory that are superseded by this template.</p>"""
    private_key_attributes: (
        "capo_pca_connector_ad.types.private_key_attributes_v3.PrivateKeyAttributesV3"
    )
    """<p>Private key attributes allow you to specify the algorithm, minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v3 templates. V3 templates allow you to use Key Storage Providers.</p>"""
    private_key_flags: (
        "capo_pca_connector_ad.types.private_key_flags_v3.PrivateKeyFlagsV3"
    )
    """<p>Private key flags for v3 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, and if an alternate signature algorithm should be used.</p>"""
    enrollment_flags: (
        "capo_pca_connector_ad.types.enrollment_flags_v3.EnrollmentFlagsV3"
    )
    """<p>Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.</p>"""
    subject_name_flags: (
        "capo_pca_connector_ad.types.subject_name_flags_v3.SubjectNameFlagsV3"
    )
    """<p>Subject name flags describe the subject name and subject alternate name that is included in a certificate.</p>"""
    general_flags: "capo_pca_connector_ad.types.general_flags_v3.GeneralFlagsV3"
    """<p>General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.</p>"""
    hash_algorithm: "capo_pca_connector_ad.types.hash_algorithm.HashAlgorithm"
    """<p>Specifies the hash algorithm used to hash the private key.</p>"""
    extensions: "capo_pca_connector_ad.types.extensions_v3.ExtensionsV3"
    """<p>Extensions describe the key usage extensions and application policies for a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateV3) -> dict:
    out: dict = {}
    import capo_pca_connector_ad.types.certificate_validity

    out["CertificateValidity"] = (
        capo_pca_connector_ad.types.certificate_validity.serialize_json(
            value["certificate_validity"]
        )
    )
    if "superseded_templates" in value:
        import capo_pca_connector_ad.types.template_name_list

        out["SupersededTemplates"] = (
            capo_pca_connector_ad.types.template_name_list.serialize_json(
                value["superseded_templates"]
            )
        )
    import capo_pca_connector_ad.types.private_key_attributes_v3

    out["PrivateKeyAttributes"] = (
        capo_pca_connector_ad.types.private_key_attributes_v3.serialize_json(
            value["private_key_attributes"]
        )
    )
    import capo_pca_connector_ad.types.private_key_flags_v3

    out["PrivateKeyFlags"] = (
        capo_pca_connector_ad.types.private_key_flags_v3.serialize_json(
            value["private_key_flags"]
        )
    )
    import capo_pca_connector_ad.types.enrollment_flags_v3

    out["EnrollmentFlags"] = (
        capo_pca_connector_ad.types.enrollment_flags_v3.serialize_json(
            value["enrollment_flags"]
        )
    )
    import capo_pca_connector_ad.types.subject_name_flags_v3

    out["SubjectNameFlags"] = (
        capo_pca_connector_ad.types.subject_name_flags_v3.serialize_json(
            value["subject_name_flags"]
        )
    )
    import capo_pca_connector_ad.types.general_flags_v3

    out["GeneralFlags"] = capo_pca_connector_ad.types.general_flags_v3.serialize_json(
        value["general_flags"]
    )
    import capo_pca_connector_ad.types.hash_algorithm

    out["HashAlgorithm"] = capo_pca_connector_ad.types.hash_algorithm.serialize_json(
        value["hash_algorithm"]
    )
    import capo_pca_connector_ad.types.extensions_v3

    out["Extensions"] = capo_pca_connector_ad.types.extensions_v3.serialize_json(
        value["extensions"]
    )
    return out


def deserialize_json(data: dict) -> TemplateV3:
    out: TemplateV3 = {}  # type: ignore[typeddict-item]
    if data.get("CertificateValidity") is not None:
        import capo_pca_connector_ad.types.certificate_validity

        out["certificate_validity"] = (
            capo_pca_connector_ad.types.certificate_validity.deserialize_json(
                data["CertificateValidity"]
            )
        )
    else:
        raise DeserializationError("TemplateV3.certificate_validity required")
    if data.get("SupersededTemplates") is not None:
        import capo_pca_connector_ad.types.template_name_list

        out["superseded_templates"] = (
            capo_pca_connector_ad.types.template_name_list.deserialize_json(
                data["SupersededTemplates"]
            )
        )
    if data.get("PrivateKeyAttributes") is not None:
        import capo_pca_connector_ad.types.private_key_attributes_v3

        out["private_key_attributes"] = (
            capo_pca_connector_ad.types.private_key_attributes_v3.deserialize_json(
                data["PrivateKeyAttributes"]
            )
        )
    else:
        raise DeserializationError("TemplateV3.private_key_attributes required")
    if data.get("PrivateKeyFlags") is not None:
        import capo_pca_connector_ad.types.private_key_flags_v3

        out["private_key_flags"] = (
            capo_pca_connector_ad.types.private_key_flags_v3.deserialize_json(
                data["PrivateKeyFlags"]
            )
        )
    else:
        raise DeserializationError("TemplateV3.private_key_flags required")
    if data.get("EnrollmentFlags") is not None:
        import capo_pca_connector_ad.types.enrollment_flags_v3

        out["enrollment_flags"] = (
            capo_pca_connector_ad.types.enrollment_flags_v3.deserialize_json(
                data["EnrollmentFlags"]
            )
        )
    else:
        raise DeserializationError("TemplateV3.enrollment_flags required")
    if data.get("SubjectNameFlags") is not None:
        import capo_pca_connector_ad.types.subject_name_flags_v3

        out["subject_name_flags"] = (
            capo_pca_connector_ad.types.subject_name_flags_v3.deserialize_json(
                data["SubjectNameFlags"]
            )
        )
    else:
        raise DeserializationError("TemplateV3.subject_name_flags required")
    if data.get("GeneralFlags") is not None:
        import capo_pca_connector_ad.types.general_flags_v3

        out["general_flags"] = (
            capo_pca_connector_ad.types.general_flags_v3.deserialize_json(
                data["GeneralFlags"]
            )
        )
    else:
        raise DeserializationError("TemplateV3.general_flags required")
    if data.get("HashAlgorithm") is not None:
        import capo_pca_connector_ad.types.hash_algorithm

        out["hash_algorithm"] = (
            capo_pca_connector_ad.types.hash_algorithm.deserialize_json(
                data["HashAlgorithm"]
            )
        )
    else:
        import typing

        out["hash_algorithm"] = typing.cast(
            "capo_pca_connector_ad.types.hash_algorithm.HashAlgorithm", ""
        )
    if data.get("Extensions") is not None:
        import capo_pca_connector_ad.types.extensions_v3

        out["extensions"] = capo_pca_connector_ad.types.extensions_v3.deserialize_json(
            data["Extensions"]
        )
    else:
        raise DeserializationError("TemplateV3.extensions required")
    return out
