"""Generated from Smithy shape ``com.amazonaws.acmpca#Permission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.account_id
    import capo_acm_pca.types.action_list
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.aws_policy
    import capo_acm_pca.types.principal
    import capo_acm_pca.types.t_stamp


class Permission(TypedDict, closed=True):
    certificate_authority_arn: NotRequired["capo_acm_pca.types.arn.Arn"]
    """<p>The Amazon Resource Number (ARN) of the private CA from which the permission was issued.</p>"""
    created_at: NotRequired["capo_acm_pca.types.t_stamp.TStamp"]
    """<p>The time at which the permission was created.</p>"""
    principal: NotRequired["capo_acm_pca.types.principal.Principal"]
    """<p>The Amazon Web Services service or entity that holds the permission. At this time, the only valid principal is <code>acm.amazonaws.com</code>.</p>"""
    source_account: NotRequired["capo_acm_pca.types.account_id.AccountId"]
    """<p>The ID of the account that assigned the permission.</p>"""
    actions: NotRequired["capo_acm_pca.types.action_list.ActionList"]
    """<p>The private CA actions that can be performed by the designated Amazon Web Services service.</p>"""
    policy: NotRequired["capo_acm_pca.types.aws_policy.AWSPolicy"]
    """<p>The name of the policy that is associated with the permission.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Permission) -> dict:
    out: dict = {}
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "created_at" in value:
        import capo_acm_pca.types.t_stamp

        out["CreatedAt"] = capo_acm_pca.types.t_stamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "principal" in value:
        out["Principal"] = value["principal"]
    if "source_account" in value:
        out["SourceAccount"] = value["source_account"]
    if "actions" in value:
        import capo_acm_pca.types.action_list

        out["Actions"] = capo_acm_pca.types.action_list.serialize_aws_json_1_1(
            value["actions"]
        )
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if data.get("CreatedAt") is not None:
        import capo_acm_pca.types.t_stamp

        out["created_at"] = capo_acm_pca.types.t_stamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    if data.get("SourceAccount") is not None:
        out["source_account"] = data["SourceAccount"]
    if data.get("Actions") is not None:
        import capo_acm_pca.types.action_list

        out["actions"] = capo_acm_pca.types.action_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Permission) -> dict:
    out: dict = {}
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "created_at" in value:
        import capo_acm_pca.types.t_stamp

        out["CreatedAt"] = capo_acm_pca.types.t_stamp.serialize_cbor(
            value["created_at"]
        )
    if "principal" in value:
        out["Principal"] = value["principal"]
    if "source_account" in value:
        out["SourceAccount"] = value["source_account"]
    if "actions" in value:
        import capo_acm_pca.types.action_list

        out["Actions"] = capo_acm_pca.types.action_list.serialize_cbor(value["actions"])
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_cbor(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if data.get("CertificateAuthorityArn") is not None:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if data.get("CreatedAt") is not None:
        import capo_acm_pca.types.t_stamp

        out["created_at"] = capo_acm_pca.types.t_stamp.deserialize_cbor(
            data["CreatedAt"]
        )
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    if data.get("SourceAccount") is not None:
        out["source_account"] = data["SourceAccount"]
    if data.get("Actions") is not None:
        import capo_acm_pca.types.action_list

        out["actions"] = capo_acm_pca.types.action_list.deserialize_cbor(
            data["Actions"]
        )
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out
