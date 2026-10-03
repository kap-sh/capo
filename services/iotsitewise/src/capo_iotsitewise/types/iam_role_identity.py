"""Generated from Smithy shape ``com.amazonaws.iotsitewise#IAMRoleIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.iam_arn


class IAMRoleIdentity(TypedDict, closed=True):
    arn: "capo_iotsitewise.types.iam_arn.IamArn"
    """<p>The ARN of the IAM role. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM ARNs</a> in the <i>IAM User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMRoleIdentity) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> IAMRoleIdentity:
    out: IAMRoleIdentity = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IAMRoleIdentity.arn required")
    return out
