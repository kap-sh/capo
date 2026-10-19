"""Generated from Smithy shape ``com.amazonaws.glue#StartBlueprintRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.blueprint_parameters
    import capo_glue.types.orchestration_iam_role_arn
    import capo_glue.types.orchestration_name_string


class StartBlueprintRunRequest(TypedDict, closed=True):
    blueprint_name: "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    """<p>The name of the blueprint.</p>"""
    parameters: NotRequired["capo_glue.types.blueprint_parameters.BlueprintParameters"]
    """<p>Specifies the parameters as a <code>BlueprintParameters</code> object.</p>"""
    role_arn: "capo_glue.types.orchestration_iam_role_arn.OrchestrationIAMRoleArn"
    """<p>Specifies the IAM role used to create the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBlueprintRunRequest) -> dict:
    out: dict = {}
    out["BlueprintName"] = value["blueprint_name"]
    if "parameters" in value:
        out["Parameters"] = value["parameters"]
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBlueprintRunRequest:
    out: StartBlueprintRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("BlueprintName") is not None:
        out["blueprint_name"] = data["BlueprintName"]
    else:
        out["blueprint_name"] = ""
    if data.get("Parameters") is not None:
        out["parameters"] = data["Parameters"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
