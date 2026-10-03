"""Generated from Smithy shape ``com.amazonaws.kms#RevokeGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.grant_id_type
    import capo_kms.types.key_id_type
    import capo_kms.types.nullable_boolean_type


class RevokeGrantRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>A unique identifier for the KMS key associated with the grant. To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p> <p>Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    grant_id: "capo_kms.types.grant_id_type.GrantIdType"
    """<p>Identifies the grant to revoke. To get the grant ID, use <a>CreateGrant</a>, <a>ListGrants</a>, or <a>ListRetirableGrants</a>.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeGrantRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    out["GrantId"] = value["grant_id"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeGrantRequest:
    out: RevokeGrantRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("RevokeGrantRequest.key_id required")
    if data.get("GrantId") is not None:
        out["grant_id"] = data["GrantId"]
    else:
        raise DeserializationError("RevokeGrantRequest.grant_id required")
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
