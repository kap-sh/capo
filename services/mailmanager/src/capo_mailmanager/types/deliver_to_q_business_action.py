"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeliverToQBusinessAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.action_failure_policy
    import capo_mailmanager.types.iam_role_arn
    import capo_mailmanager.types.q_business_application_id
    import capo_mailmanager.types.q_business_index_id


class DeliverToQBusinessAction(TypedDict, closed=True):
    action_failure_policy: NotRequired[
        "capo_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified application has been deleted or the role lacks necessary permissions to call the <code>qbusiness:BatchPutDocument</code> API.</p>"""
    application_id: (
        "capo_mailmanager.types.q_business_application_id.QBusinessApplicationId"
    )
    """<p>The unique identifier of the Amazon Q Business application instance where the email content will be delivered.</p>"""
    index_id: "capo_mailmanager.types.q_business_index_id.QBusinessIndexId"
    """<p>The identifier of the knowledge base index within the Amazon Q Business application where the email content will be stored and indexed.</p>"""
    role_arn: "capo_mailmanager.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Role to use while delivering to Amazon Q Business. This role must have access to the <code>qbusiness:BatchPutDocument</code> API for the given application and index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeliverToQBusinessAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import capo_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            capo_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["ApplicationId"] = value["application_id"]
    out["IndexId"] = value["index_id"]
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeliverToQBusinessAction:
    out: DeliverToQBusinessAction = {}  # type: ignore[typeddict-item]
    if data.get("ActionFailurePolicy") is not None:
        import capo_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            capo_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    else:
        out["application_id"] = ""
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
