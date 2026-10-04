"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationGuidanceExamples``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class RemediationGuidanceExamples(TypedDict, closed=True):
    aws_cli: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An AWS CLI snippet version of the example.</p>"""
    cli: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A CLI snippet version of the example.</p>"""
    python: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A Python snippet version of the example.</p>"""
    terraform: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A Terraform snippet version of the example.</p>"""
    cdk: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A CDK snippet version of the example.</p>"""
    cloud_formation: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A CloudFormation snippet version of the example.</p>"""
    ia_c: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An IaC snippet version of the example.</p>"""
    template: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A Template snippet version of the example.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationGuidanceExamples) -> dict:
    out: dict = {}
    if "aws_cli" in value:
        out["AwsCli"] = value["aws_cli"]
    if "cli" in value:
        out["Cli"] = value["cli"]
    if "python" in value:
        out["Python"] = value["python"]
    if "terraform" in value:
        out["Terraform"] = value["terraform"]
    if "cdk" in value:
        out["Cdk"] = value["cdk"]
    if "cloud_formation" in value:
        out["CloudFormation"] = value["cloud_formation"]
    if "ia_c" in value:
        out["IaC"] = value["ia_c"]
    if "template" in value:
        out["Template"] = value["template"]
    return out


def deserialize_json(data: dict) -> RemediationGuidanceExamples:
    out: RemediationGuidanceExamples = {}  # type: ignore[typeddict-item]
    if data.get("AwsCli") is not None:
        out["aws_cli"] = data["AwsCli"]
    if data.get("Cli") is not None:
        out["cli"] = data["Cli"]
    if data.get("Python") is not None:
        out["python"] = data["Python"]
    if data.get("Terraform") is not None:
        out["terraform"] = data["Terraform"]
    if data.get("Cdk") is not None:
        out["cdk"] = data["Cdk"]
    if data.get("CloudFormation") is not None:
        out["cloud_formation"] = data["CloudFormation"]
    if data.get("IaC") is not None:
        out["ia_c"] = data["IaC"]
    if data.get("Template") is not None:
        out["template"] = data["Template"]
    return out
