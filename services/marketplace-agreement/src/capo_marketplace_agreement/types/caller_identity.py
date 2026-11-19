"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CallerIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.principal_arn


class CallerIdentity(TypedDict, closed=True):
    principal_arn: "capo_marketplace_agreement.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM principal that made the call.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CallerIdentity) -> dict:
    out: dict = {}
    out["principalArn"] = value["principal_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CallerIdentity:
    out: CallerIdentity = {}  # type: ignore[typeddict-item]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    else:
        out["principal_arn"] = ""
    return out
