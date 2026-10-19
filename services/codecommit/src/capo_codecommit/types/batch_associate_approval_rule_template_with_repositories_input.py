"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchAssociateApprovalRuleTemplateWithRepositoriesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_template_name
    import capo_codecommit.types.repository_name_list


class BatchAssociateApprovalRuleTemplateWithRepositoriesInput(TypedDict, closed=True):
    approval_rule_template_name: (
        "capo_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the template you want to associate with one or more repositories.</p>"""
    repository_names: "capo_codecommit.types.repository_name_list.RepositoryNameList"
    """<p>The names of the repositories you want to associate with the template.</p> <note> <p>The length constraint limit is for each string in the array. The array itself can be empty.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchAssociateApprovalRuleTemplateWithRepositoriesInput,
) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    import capo_codecommit.types.repository_name_list

    out["repositoryNames"] = (
        capo_codecommit.types.repository_name_list.serialize_aws_json_1_1(
            value["repository_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchAssociateApprovalRuleTemplateWithRepositoriesInput:
    out: BatchAssociateApprovalRuleTemplateWithRepositoriesInput = {}  # type: ignore[typeddict-item]
    if data.get("approvalRuleTemplateName") is not None:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        out["approval_rule_template_name"] = ""
    if data.get("repositoryNames") is not None:
        import capo_codecommit.types.repository_name_list

        out["repository_names"] = (
            capo_codecommit.types.repository_name_list.deserialize_aws_json_1_1(
                data["repositoryNames"]
            )
        )
    else:
        out["repository_names"] = []
    return out
