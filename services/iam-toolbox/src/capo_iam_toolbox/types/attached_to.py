"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#AttachedTo``."""

from typing_extensions import NotRequired, TypedDict


class AttachedTo(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The ARN of the entity that the policy is attached to. The ARN format depends on the policy type:</p> <ul> <li> <p>For identity, session, and permissions boundary policies, this is the principal ARN (for example, an IAM role or user ARN).</p> </li> <li> <p>For resource-based policies, this is the resource ARN.</p> </li> <li> <p>For organization control policies (SCPs and RCPs), this is the AWS Organizations ARN of the account, organizational unit, or root.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachedTo) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AttachedTo:
    out: AttachedTo = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
