"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_errors_list
    import capo_codecommit.types.repository_name_list


class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput(
    TypedDict, closed=True
):
    disassociated_repository_names: (
        "capo_codecommit.types.repository_name_list.RepositoryNameList"
    )
    """<p>A list of repository names that have had their association with the template removed.</p>"""
    errors: "capo_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_errors_list.BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorsList"
    """<p>A list of any errors that might have occurred while attempting to remove the association between the template and the repositories.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput,
) -> dict:
    out: dict = {}
    import capo_codecommit.types.repository_name_list

    out["disassociatedRepositoryNames"] = (
        capo_codecommit.types.repository_name_list.serialize_aws_json_1_1(
            value["disassociated_repository_names"]
        )
    )
    import capo_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_errors_list

    out["errors"] = (
        capo_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_errors_list.serialize_aws_json_1_1(
            value["errors"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput:
    out: BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput = {}  # type: ignore[typeddict-item]
    if data.get("disassociatedRepositoryNames") is not None:
        import capo_codecommit.types.repository_name_list

        out["disassociated_repository_names"] = (
            capo_codecommit.types.repository_name_list.deserialize_aws_json_1_1(
                data["disassociatedRepositoryNames"]
            )
        )
    else:
        out["disassociated_repository_names"] = []
    if data.get("errors") is not None:
        import capo_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_errors_list

        out["errors"] = (
            capo_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_errors_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
