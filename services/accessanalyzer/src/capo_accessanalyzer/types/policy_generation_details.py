"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PolicyGenerationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.principal_arn


class PolicyGenerationDetails(TypedDict, closed=True):
    principal_arn: "capo_accessanalyzer.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM entity (user or role) for which you are generating a policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationDetails) -> dict:
    out: dict = {}
    out["principalArn"] = value["principal_arn"]
    return out


def deserialize_json(data: dict) -> PolicyGenerationDetails:
    out: PolicyGenerationDetails = {}  # type: ignore[typeddict-item]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    else:
        out["principal_arn"] = ""
    return out
