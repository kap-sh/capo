"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GeneratedPolicyProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.cloud_trail_properties
    import capo_accessanalyzer.types.principal_arn


class GeneratedPolicyProperties(TypedDict, closed=True):
    is_complete: NotRequired["bool"]
    """<p>This value is set to <code>true</code> if the generated policy contains all possible actions for a service that IAM Access Analyzer identified from the CloudTrail trail that you specified, and <code>false</code> otherwise.</p>"""
    principal_arn: "capo_accessanalyzer.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM entity (user or role) for which you are generating a policy.</p>"""
    cloud_trail_properties: NotRequired[
        "capo_accessanalyzer.types.cloud_trail_properties.CloudTrailProperties"
    ]
    """<p>Lists details about the <code>Trail</code> used to generated policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedPolicyProperties) -> dict:
    out: dict = {}
    if "is_complete" in value:
        out["isComplete"] = value["is_complete"]
    out["principalArn"] = value["principal_arn"]
    if "cloud_trail_properties" in value:
        import capo_accessanalyzer.types.cloud_trail_properties

        out["cloudTrailProperties"] = (
            capo_accessanalyzer.types.cloud_trail_properties.serialize_json(
                value["cloud_trail_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeneratedPolicyProperties:
    out: GeneratedPolicyProperties = {}  # type: ignore[typeddict-item]
    if data.get("isComplete") is not None:
        out["is_complete"] = data["isComplete"]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    else:
        out["principal_arn"] = ""
    if data.get("cloudTrailProperties") is not None:
        import capo_accessanalyzer.types.cloud_trail_properties

        out["cloud_trail_properties"] = (
            capo_accessanalyzer.types.cloud_trail_properties.deserialize_json(
                data["cloudTrailProperties"]
            )
        )
    return out
