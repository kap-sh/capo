"""Generated from Smithy shape ``com.amazonaws.acmpca#PolicyInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.custom_object_identifier
    import capo_acm_pca.types.policy_qualifier_info_list


class PolicyInformation(TypedDict, closed=True):
    cert_policy_id: "capo_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    """<p>Specifies the object identifier (OID) of the certificate policy under which the certificate was issued. For more information, see NIST's definition of <a href="https://csrc.nist.gov/glossary/term/Object_Identifier">Object Identifier (OID)</a>.</p>"""
    policy_qualifiers: NotRequired[
        "capo_acm_pca.types.policy_qualifier_info_list.PolicyQualifierInfoList"
    ]
    """<p>Modifies the given <code>CertPolicyId</code> with a qualifier. Amazon Web Services Private CA supports the certification practice statement (CPS) qualifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyInformation) -> dict:
    out: dict = {}
    out["CertPolicyId"] = value["cert_policy_id"]
    if "policy_qualifiers" in value:
        import capo_acm_pca.types.policy_qualifier_info_list

        out["PolicyQualifiers"] = (
            capo_acm_pca.types.policy_qualifier_info_list.serialize_aws_json_1_1(
                value["policy_qualifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyInformation:
    out: PolicyInformation = {}  # type: ignore[typeddict-item]
    if data.get("CertPolicyId") is not None:
        out["cert_policy_id"] = data["CertPolicyId"]
    else:
        raise DeserializationError("PolicyInformation.cert_policy_id required")
    if data.get("PolicyQualifiers") is not None:
        import capo_acm_pca.types.policy_qualifier_info_list

        out["policy_qualifiers"] = (
            capo_acm_pca.types.policy_qualifier_info_list.deserialize_aws_json_1_1(
                data["PolicyQualifiers"]
            )
        )
    return out
