"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAccessPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.id


class CreateAccessPolicyResponse(TypedDict, closed=True):
    access_policy_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the access policy.</p>"""
    access_policy_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the access policy, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId}</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessPolicyResponse) -> dict:
    out: dict = {}
    out["accessPolicyId"] = value["access_policy_id"]
    out["accessPolicyArn"] = value["access_policy_arn"]
    return out


def deserialize_json(data: dict) -> CreateAccessPolicyResponse:
    out: CreateAccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("accessPolicyId") is not None:
        out["access_policy_id"] = data["accessPolicyId"]
    else:
        raise DeserializationError(
            "CreateAccessPolicyResponse.access_policy_id required"
        )
    if data.get("accessPolicyArn") is not None:
        out["access_policy_arn"] = data["accessPolicyArn"]
    else:
        raise DeserializationError(
            "CreateAccessPolicyResponse.access_policy_arn required"
        )
    return out
