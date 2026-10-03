"""Generated from Smithy shape ``com.amazonaws.eks#Provider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class Provider(TypedDict, closed=True):
    key_arn: NotRequired["capo_eks.types.string.String"]
    """<p>Amazon Resource Name (ARN) or alias of the KMS key. The KMS key must be symmetric and created in the same Amazon Web Services Region as the cluster. If the KMS key was created in a different account, the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html">IAM principal</a> must have access to the KMS key. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html">Allowing users in other accounts to use a KMS key</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Provider) -> dict:
    out: dict = {}
    if "key_arn" in value:
        out["keyArn"] = value["key_arn"]
    return out


def deserialize_json(data: dict) -> Provider:
    out: Provider = {}  # type: ignore[typeddict-item]
    if data.get("keyArn") is not None:
        out["key_arn"] = data["keyArn"]
    return out
