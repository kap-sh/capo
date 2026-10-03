"""Generated from Smithy shape ``com.amazonaws.kms#CreateGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.grant_constraints
    import capo_kms.types.grant_name_type
    import capo_kms.types.grant_operation_list
    import capo_kms.types.grant_token_list
    import capo_kms.types.key_id_type
    import capo_kms.types.nullable_boolean_type
    import capo_kms.types.principal_id_type
    import capo_kms.types.service_principal_type


class CreateGrantRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Identifies the KMS key for the grant. The grant gives principals permission to use this KMS key.</p> <p>Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    grantee_principal: NotRequired["capo_kms.types.principal_id_type.PrincipalIdType"]
    """<p>The identity that gets the permissions specified in the grant.</p> <p>To specify the grantee principal, use the Amazon Resource Name (ARN) of an Amazon Web Services principal. Valid principals include Amazon Web Services accounts, IAM users, IAM roles, federated users, and assumed role users. For help with the ARN syntax for a principal, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a> in the <i> <i>Identity and Access Management User Guide</i> </i>.</p> <p>You must specify either <code>GranteePrincipal</code> or <code>GranteeServicePrincipal</code>, but not both.</p>"""
    retiring_principal: NotRequired["capo_kms.types.principal_id_type.PrincipalIdType"]
    """<p>The principal that has permission to use the <a>RetireGrant</a> operation to retire the grant. </p> <p>To specify the principal, use the <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of an Amazon Web Services principal. Valid principals include Amazon Web Services accounts, IAM users, IAM roles, federated users, and assumed role users. For help with the ARN syntax for a principal, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a> in the <i> <i>Identity and Access Management User Guide</i> </i>.</p> <p>The grant determines the retiring principal. Other principals might have permission to retire the grant or revoke the grant. For details, see <a>RevokeGrant</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grant-delete.html">Retiring and revoking grants</a> in the <i>Key Management Service Developer Guide</i>. </p> <p>You can specify either <code>RetiringPrincipal</code> or <code>RetiringServicePrincipal</code>, but not both.</p>"""
    operations: "capo_kms.types.grant_operation_list.GrantOperationList"
    """<p>A list of operations that the grant permits. </p> <p>This list must include only operations that are permitted in a grant. Also, the operation must be supported on the KMS key. For example, you cannot create a grant for a symmetric encryption KMS key that allows the <a>Sign</a> operation, or a grant for an asymmetric KMS key that allows the <a>GenerateDataKey</a> operation. If you try, KMS returns a <code>ValidationError</code> exception. For details, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations">Grant operations</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    constraints: NotRequired["capo_kms.types.grant_constraints.GrantConstraints"]
    """<p>Specifies a grant constraint.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>KMS supports the following grant constraints.</p> <ul> <li> <p> <code>EncryptionContextEquals</code> and <code>EncryptionContextSubset</code> — These encryption context grant constraints allow the permissions in the grant only when the encryption context in the request matches (<code>EncryptionContextEquals</code>) or includes (<code>EncryptionContextSubset</code>) the encryption context specified in the constraint.</p> <p>Encryption context grant constraints are supported only on <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations">grant operations</a> that include an <code>EncryptionContext</code> parameter, such as cryptographic operations on symmetric encryption KMS keys. You cannot use an encryption context grant constraint for cryptographic operations with asymmetric KMS keys or HMAC KMS keys. Operations with these keys don't support an encryption context. Grants with encryption context grant constraints can include the <a>DescribeKey</a> and <a>RetireGrant</a> operations, but the constraint doesn't apply to these operations. If a grant with an encryption context grant constraint includes the <code>CreateGrant</code> operation, the constraint requires that any grants created with the <code>CreateGrant</code> permission have an equally strict or stricter encryption context constraint. </p> <p>Each constraint value can include up to 8 encryption context pairs. The encryption context value in each constraint cannot exceed 384 characters. For more information about encryption context, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context">Encryption context</a> in the <i> <i>Key Management Service Developer Guide</i> </i>.</p> </li> <li> <p> <code>SourceArn</code> — This grant constraint allows the permissions in the grant only when the request is made on behalf of a specific Amazon Web Services resource, identified by its <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a>. This is effectively the same as having the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn">aws:SourceArn</a> global condition key in the grant. The SourceArn constraint is supported on grants for all types of KMS keys and can also be applied to the <a>DescribeKey</a> operation when specified in the request. However, it does not apply to <a>RetireGrant</a> operation.</p> </li> </ul> <p>For information about grant constraints, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-grant-overview.html#grant-constraints">Using grant constraints</a> in the <i>Key Management Service Developer Guide</i>. </p>"""
    grant_tokens: NotRequired["capo_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens. </p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token">Grant token</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    name: NotRequired["capo_kms.types.grant_name_type.GrantNameType"]
    """<p>A friendly name for the grant. Use this value to prevent the unintended creation of duplicate grants when retrying this request.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>When this value is absent, all <code>CreateGrant</code> requests result in a new grant with a unique <code>GrantId</code> even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the <code>CreateGrant</code> request.</p> <p>When this value is present, you can retry a <code>CreateGrant</code> request with identical parameters; if the grant already exists, the original <code>GrantId</code> is returned without creating a new grant. Note that the returned grant token is unique with every <code>CreateGrant</code> request, even when a duplicate <code>GrantId</code> is returned. All grant tokens for the same grant ID can be used interchangeably.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    grantee_service_principal: NotRequired[
        "capo_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>The Amazon Web Services <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services">service principal</a> that gets the permissions specified in the grant. </p> <p>When you specify a <code>GranteeServicePrincipal</code>, you must also specify a <code>SourceArn</code> grant constraint. In addition, you must specify either a <code>RetiringPrincipal</code> or a <code>RetiringServicePrincipal</code>. </p> <p>You must specify either <code>GranteePrincipal</code> or <code>GranteeServicePrincipal</code>, but not both.</p>"""
    retiring_service_principal: NotRequired[
        "capo_kms.types.service_principal_type.ServicePrincipalType"
    ]
    """<p>The Amazon Web Services <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services">service principal</a> that has permission to use the <a>RetireGrant</a> operation to retire the grant.</p> <p>You can specify either <code>RetiringPrincipal</code> or <code>RetiringServicePrincipal</code>, but not both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGrantRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    if "grantee_principal" in value:
        out["GranteePrincipal"] = value["grantee_principal"]
    if "retiring_principal" in value:
        out["RetiringPrincipal"] = value["retiring_principal"]
    import capo_kms.types.grant_operation_list

    out["Operations"] = capo_kms.types.grant_operation_list.serialize_aws_json_1_1(
        value["operations"]
    )
    if "constraints" in value:
        import capo_kms.types.grant_constraints

        out["Constraints"] = capo_kms.types.grant_constraints.serialize_aws_json_1_1(
            value["constraints"]
        )
    if "grant_tokens" in value:
        import capo_kms.types.grant_token_list

        out["GrantTokens"] = capo_kms.types.grant_token_list.serialize_aws_json_1_1(
            value["grant_tokens"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "grantee_service_principal" in value:
        out["GranteeServicePrincipal"] = value["grantee_service_principal"]
    if "retiring_service_principal" in value:
        out["RetiringServicePrincipal"] = value["retiring_service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGrantRequest:
    out: CreateGrantRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("CreateGrantRequest.key_id required")
    if data.get("GranteePrincipal") is not None:
        out["grantee_principal"] = data["GranteePrincipal"]
    if data.get("RetiringPrincipal") is not None:
        out["retiring_principal"] = data["RetiringPrincipal"]
    if data.get("Operations") is not None:
        import capo_kms.types.grant_operation_list

        out["operations"] = (
            capo_kms.types.grant_operation_list.deserialize_aws_json_1_1(
                data["Operations"]
            )
        )
    else:
        raise DeserializationError("CreateGrantRequest.operations required")
    if data.get("Constraints") is not None:
        import capo_kms.types.grant_constraints

        out["constraints"] = capo_kms.types.grant_constraints.deserialize_aws_json_1_1(
            data["Constraints"]
        )
    if data.get("GrantTokens") is not None:
        import capo_kms.types.grant_token_list

        out["grant_tokens"] = capo_kms.types.grant_token_list.deserialize_aws_json_1_1(
            data["GrantTokens"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("GranteeServicePrincipal") is not None:
        out["grantee_service_principal"] = data["GranteeServicePrincipal"]
    if data.get("RetiringServicePrincipal") is not None:
        out["retiring_service_principal"] = data["RetiringServicePrincipal"]
    return out
