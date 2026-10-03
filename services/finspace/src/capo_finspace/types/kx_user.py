"""Generated from Smithy shape ``com.amazonaws.finspace#KxUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_user_arn
    import capo_finspace.types.kx_user_name_string
    import capo_finspace.types.role_arn
    import capo_finspace.types.timestamp


class KxUser(TypedDict, closed=True):
    user_arn: NotRequired["capo_finspace.types.kx_user_arn.KxUserArn"]
    """<p> The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    user_name: NotRequired["capo_finspace.types.kx_user_name_string.KxUserNameString"]
    """<p>A unique identifier for the user.</p>"""
    iam_role: NotRequired["capo_finspace.types.role_arn.RoleArn"]
    """<p>The IAM role ARN that is associated with the user.</p>"""
    create_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb user was created. </p>"""
    update_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb user was updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxUser) -> dict:
    out: dict = {}
    if "user_arn" in value:
        out["userArn"] = value["user_arn"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "iam_role" in value:
        out["iamRole"] = value["iam_role"]
    if "create_timestamp" in value:
        import capo_finspace.types.timestamp

        out["createTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["create_timestamp"]
        )
    if "update_timestamp" in value:
        import capo_finspace.types.timestamp

        out["updateTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["update_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> KxUser:
    out: KxUser = {}  # type: ignore[typeddict-item]
    if data.get("userArn") is not None:
        out["user_arn"] = data["userArn"]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    if data.get("iamRole") is not None:
        out["iam_role"] = data["iamRole"]
    if data.get("createTimestamp") is not None:
        import capo_finspace.types.timestamp

        out["create_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["createTimestamp"]
        )
    if data.get("updateTimestamp") is not None:
        import capo_finspace.types.timestamp

        out["update_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["updateTimestamp"]
        )
    return out
