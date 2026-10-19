"""Generated from Smithy shape ``com.amazonaws.ssmincidents#SsmAutomation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.dynamic_ssm_parameters
    import capo_ssm_incidents.types.role_arn
    import capo_ssm_incidents.types.ssm_parameters
    import capo_ssm_incidents.types.ssm_target_account


class SsmAutomation(TypedDict, closed=True):
    role_arn: "capo_ssm_incidents.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the role that the automation document will assume when running commands.</p>"""
    document_name: "str"
    """<p>The automation document's name.</p>"""
    document_version: NotRequired["str"]
    """<p>The automation document's version to use when running.</p>"""
    target_account: NotRequired[
        "capo_ssm_incidents.types.ssm_target_account.SsmTargetAccount"
    ]
    """<p>The account that the automation document will be run in. This can be in either the management account or an application account.</p>"""
    parameters: NotRequired["capo_ssm_incidents.types.ssm_parameters.SsmParameters"]
    """<p>The key-value pair parameters to use when running the automation document.</p>"""
    dynamic_parameters: NotRequired[
        "capo_ssm_incidents.types.dynamic_ssm_parameters.DynamicSsmParameters"
    ]
    """<p>The key-value pair to resolve dynamic parameter values when processing a Systems Manager Automation runbook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SsmAutomation) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["documentName"] = value["document_name"]
    if "document_version" in value:
        out["documentVersion"] = value["document_version"]
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "parameters" in value:
        import capo_ssm_incidents.types.ssm_parameters

        out["parameters"] = capo_ssm_incidents.types.ssm_parameters.serialize_json(
            value["parameters"]
        )
    if "dynamic_parameters" in value:
        import capo_ssm_incidents.types.dynamic_ssm_parameters

        out["dynamicParameters"] = (
            capo_ssm_incidents.types.dynamic_ssm_parameters.serialize_json(
                value["dynamic_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SsmAutomation:
    out: SsmAutomation = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("documentName") is not None:
        out["document_name"] = data["documentName"]
    else:
        out["document_name"] = ""
    if data.get("documentVersion") is not None:
        out["document_version"] = data["documentVersion"]
    if data.get("targetAccount") is not None:
        out["target_account"] = data["targetAccount"]
    if data.get("parameters") is not None:
        import capo_ssm_incidents.types.ssm_parameters

        out["parameters"] = capo_ssm_incidents.types.ssm_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("dynamicParameters") is not None:
        import capo_ssm_incidents.types.dynamic_ssm_parameters

        out["dynamic_parameters"] = (
            capo_ssm_incidents.types.dynamic_ssm_parameters.deserialize_json(
                data["dynamicParameters"]
            )
        )
    return out
