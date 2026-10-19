"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DescribeIdentityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_id


class DescribeIdentityInput(TypedDict, closed=True):
    identity_id: "capo_cognito_identity.types.identity_id.IdentityId"
    """<p>A unique identifier in the format REGION:GUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIdentityInput) -> dict:
    out: dict = {}
    out["IdentityId"] = value["identity_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIdentityInput:
    out: DescribeIdentityInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    else:
        out["identity_id"] = ""
    return out
