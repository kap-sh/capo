"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchAssociateApprovalRuleTemplateWithRepositoriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_errors_list
    import capo_codecommit.types.repository_name_list


class BatchAssociateApprovalRuleTemplateWithRepositoriesOutput(TypedDict, closed=True):
    associated_repository_names: (
        "capo_codecommit.types.repository_name_list.RepositoryNameList"
    )
    """<p>A list of names of the repositories that have been associated with the template.</p>"""
    errors: "capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_errors_list.BatchAssociateApprovalRuleTemplateWithRepositoriesErrorsList"
    """<p>A list of any errors that might have occurred while attempting to create the association between the template and the repositories.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchAssociateApprovalRuleTemplateWithRepositoriesOutput,
) -> dict:
    out: dict = {}
    import capo_codecommit.types.repository_name_list

    out["associatedRepositoryNames"] = (
        capo_codecommit.types.repository_name_list.serialize_aws_json_1_1(
            value["associated_repository_names"]
        )
    )
    import capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_errors_list

    out["errors"] = (
        capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_errors_list.serialize_aws_json_1_1(
            value["errors"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchAssociateApprovalRuleTemplateWithRepositoriesOutput:
    out: BatchAssociateApprovalRuleTemplateWithRepositoriesOutput = {}  # type: ignore[typeddict-item]
    if data.get("associatedRepositoryNames") is not None:
        import capo_codecommit.types.repository_name_list

        out["associated_repository_names"] = (
            capo_codecommit.types.repository_name_list.deserialize_aws_json_1_1(
                data["associatedRepositoryNames"]
            )
        )
    else:
        out["associated_repository_names"] = []
    if data.get("errors") is not None:
        import capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_errors_list

        out["errors"] = (
            capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_errors_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
