"""Generated from Smithy shape ``com.amazonaws.acmpca#Extensions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.certificate_policy_list
    import capo_acm_pca.types.custom_extension_list
    import capo_acm_pca.types.extended_key_usage_list
    import capo_acm_pca.types.general_name_list
    import capo_acm_pca.types.key_usage


class Extensions(TypedDict, closed=True):
    certificate_policies: NotRequired[
        "capo_acm_pca.types.certificate_policy_list.CertificatePolicyList"
    ]
    """<p>Contains a sequence of one or more policy information terms, each of which consists of an object identifier (OID) and optional qualifiers. For more information, see NIST's definition of <a href="https://csrc.nist.gov/glossary/term/Object_Identifier">Object Identifier (OID)</a>.</p> <p>In an end-entity certificate, these terms indicate the policy under which the certificate was issued and the purposes for which it may be used. In a CA certificate, these terms limit the set of policies for certification paths that include this certificate.</p>"""
    extended_key_usage: NotRequired[
        "capo_acm_pca.types.extended_key_usage_list.ExtendedKeyUsageList"
    ]
    """<p>Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the <code>KeyUsage</code> extension.</p>"""
    key_usage: NotRequired["capo_acm_pca.types.key_usage.KeyUsage"]
    subject_alternative_names: NotRequired[
        "capo_acm_pca.types.general_name_list.GeneralNameList"
    ]
    """<p>The subject alternative name extension allows identities to be bound to the subject of the certificate. These identities may be included in addition to or in place of the identity in the subject field of the certificate.</p>"""
    custom_extensions: NotRequired[
        "capo_acm_pca.types.custom_extension_list.CustomExtensionList"
    ]
    """<p/> <p>Contains a sequence of one or more X.509 extensions, each of which consists of an object identifier (OID), a base64-encoded value, and the critical flag. For more information, see the <a href="https://oidref.com/2.5.29">Global OID reference database.</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Extensions) -> dict:
    out: dict = {}
    if "certificate_policies" in value:
        import capo_acm_pca.types.certificate_policy_list

        out["CertificatePolicies"] = (
            capo_acm_pca.types.certificate_policy_list.serialize_aws_json_1_1(
                value["certificate_policies"]
            )
        )
    if "extended_key_usage" in value:
        import capo_acm_pca.types.extended_key_usage_list

        out["ExtendedKeyUsage"] = (
            capo_acm_pca.types.extended_key_usage_list.serialize_aws_json_1_1(
                value["extended_key_usage"]
            )
        )
    if "key_usage" in value:
        import capo_acm_pca.types.key_usage

        out["KeyUsage"] = capo_acm_pca.types.key_usage.serialize_aws_json_1_1(
            value["key_usage"]
        )
    if "subject_alternative_names" in value:
        import capo_acm_pca.types.general_name_list

        out["SubjectAlternativeNames"] = (
            capo_acm_pca.types.general_name_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "custom_extensions" in value:
        import capo_acm_pca.types.custom_extension_list

        out["CustomExtensions"] = (
            capo_acm_pca.types.custom_extension_list.serialize_aws_json_1_1(
                value["custom_extensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Extensions:
    out: Extensions = {}  # type: ignore[typeddict-item]
    if data.get("CertificatePolicies") is not None:
        import capo_acm_pca.types.certificate_policy_list

        out["certificate_policies"] = (
            capo_acm_pca.types.certificate_policy_list.deserialize_aws_json_1_1(
                data["CertificatePolicies"]
            )
        )
    if data.get("ExtendedKeyUsage") is not None:
        import capo_acm_pca.types.extended_key_usage_list

        out["extended_key_usage"] = (
            capo_acm_pca.types.extended_key_usage_list.deserialize_aws_json_1_1(
                data["ExtendedKeyUsage"]
            )
        )
    if data.get("KeyUsage") is not None:
        import capo_acm_pca.types.key_usage

        out["key_usage"] = capo_acm_pca.types.key_usage.deserialize_aws_json_1_1(
            data["KeyUsage"]
        )
    if data.get("SubjectAlternativeNames") is not None:
        import capo_acm_pca.types.general_name_list

        out["subject_alternative_names"] = (
            capo_acm_pca.types.general_name_list.deserialize_aws_json_1_1(
                data["SubjectAlternativeNames"]
            )
        )
    if data.get("CustomExtensions") is not None:
        import capo_acm_pca.types.custom_extension_list

        out["custom_extensions"] = (
            capo_acm_pca.types.custom_extension_list.deserialize_aws_json_1_1(
                data["CustomExtensions"]
            )
        )
    return out
