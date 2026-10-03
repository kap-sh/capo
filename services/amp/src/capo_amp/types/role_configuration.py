"""Generated from Smithy shape ``com.amazonaws.amp#RoleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.iam_role_arn


class RoleConfiguration(TypedDict, closed=True):
    source_role_arn: NotRequired["capo_amp.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role used in the source account to enable cross-account scraping. For information about the contents of this policy, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#cross-account-remote-write">Cross-account setup</a>.</p>"""
    target_role_arn: NotRequired["capo_amp.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role used in the target account to enable cross-account scraping. For information about the contents of this policy, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#cross-account-remote-write">Cross-account setup</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoleConfiguration) -> dict:
    out: dict = {}
    if "source_role_arn" in value:
        out["sourceRoleArn"] = value["source_role_arn"]
    if "target_role_arn" in value:
        out["targetRoleArn"] = value["target_role_arn"]
    return out


def deserialize_json(data: dict) -> RoleConfiguration:
    out: RoleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceRoleArn") is not None:
        out["source_role_arn"] = data["sourceRoleArn"]
    if data.get("targetRoleArn") is not None:
        out["target_role_arn"] = data["targetRoleArn"]
    return out
