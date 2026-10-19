"""Generated from Smithy shape ``com.amazonaws.acmpca#PolicyQualifierInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.policy_qualifier_id
    import capo_acm_pca.types.qualifier


class PolicyQualifierInfo(TypedDict, closed=True):
    policy_qualifier_id: "capo_acm_pca.types.policy_qualifier_id.PolicyQualifierId"
    """<p>Identifies the qualifier modifying a <code>CertPolicyId</code>.</p>"""
    qualifier: "capo_acm_pca.types.qualifier.Qualifier"
    """<p>Defines the qualifier type. Amazon Web Services Private CA supports the use of a URI for a CPS qualifier in this field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyQualifierInfo) -> dict:
    out: dict = {}
    import capo_acm_pca.types.policy_qualifier_id

    out["PolicyQualifierId"] = (
        capo_acm_pca.types.policy_qualifier_id.serialize_aws_json_1_1(
            value["policy_qualifier_id"]
        )
    )
    import capo_acm_pca.types.qualifier

    out["Qualifier"] = capo_acm_pca.types.qualifier.serialize_aws_json_1_1(
        value["qualifier"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyQualifierInfo:
    out: PolicyQualifierInfo = {}  # type: ignore[typeddict-item]
    if data.get("PolicyQualifierId") is not None:
        import capo_acm_pca.types.policy_qualifier_id

        out["policy_qualifier_id"] = (
            capo_acm_pca.types.policy_qualifier_id.deserialize_aws_json_1_1(
                data["PolicyQualifierId"]
            )
        )
    else:
        import typing

        out["policy_qualifier_id"] = typing.cast(
            "capo_acm_pca.types.policy_qualifier_id.PolicyQualifierId", ""
        )
    if data.get("Qualifier") is not None:
        import capo_acm_pca.types.qualifier

        out["qualifier"] = capo_acm_pca.types.qualifier.deserialize_aws_json_1_1(
            data["Qualifier"]
        )
    else:
        raise DeserializationError("PolicyQualifierInfo.qualifier required")
    return out
