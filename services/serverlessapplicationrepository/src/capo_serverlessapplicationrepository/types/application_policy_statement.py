"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ApplicationPolicyStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__list_of__string
    import capo_serverlessapplicationrepository.types.__string


class ApplicationPolicyStatement(TypedDict, closed=True):
    actions: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    """<p>For the list of actions supported for this operation, see <a href="https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions">Application Permissions</a>.</p>"""
    principal_org_i_ds: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of PrinciplalOrgIDs, which corresponds to AWS IAM <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#principal-org-id">aws:PrincipalOrgID</a> global condition key.</p>"""
    principals: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    """<p>An array of AWS account IDs, or * to make the application public.</p>"""
    statement_id: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A unique ID for the statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPolicyStatement) -> dict:
    out: dict = {}
    if "actions" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["actions"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["actions"]
            )
        )
    if "principal_org_i_ds" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["principalOrgIDs"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["principal_org_i_ds"]
            )
        )
    if "principals" in value:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["principals"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["principals"]
            )
        )
    if "statement_id" in value:
        out["statementId"] = value["statement_id"]
    return out


def deserialize_json(data: dict) -> ApplicationPolicyStatement:
    out: ApplicationPolicyStatement = {}  # type: ignore[typeddict-item]
    if data.get("actions") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["actions"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["actions"]
            )
        )
    if data.get("principalOrgIDs") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["principal_org_i_ds"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["principalOrgIDs"]
            )
        )
    if data.get("principals") is not None:
        import capo_serverlessapplicationrepository.types.__list_of__string

        out["principals"] = (
            capo_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["principals"]
            )
        )
    if data.get("statementId") is not None:
        out["statement_id"] = data["statementId"]
    return out
