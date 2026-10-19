"""Generated from Smithy shape ``com.amazonaws.budgets#IamActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.groups
    import capo_budgets.types.policy_arn
    import capo_budgets.types.roles
    import capo_budgets.types.users


class IamActionDefinition(TypedDict, closed=True):
    policy_arn: "capo_budgets.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy to be attached. </p>"""
    roles: NotRequired["capo_budgets.types.roles.Roles"]
    """<p>A list of roles to be attached. There must be at least one role. </p>"""
    groups: NotRequired["capo_budgets.types.groups.Groups"]
    """<p>A list of groups to be attached. There must be at least one group. </p>"""
    users: NotRequired["capo_budgets.types.users.Users"]
    """<p>A list of users to be attached. There must be at least one user. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IamActionDefinition) -> dict:
    out: dict = {}
    out["PolicyArn"] = value["policy_arn"]
    if "roles" in value:
        import capo_budgets.types.roles

        out["Roles"] = capo_budgets.types.roles.serialize_aws_json_1_1(value["roles"])
    if "groups" in value:
        import capo_budgets.types.groups

        out["Groups"] = capo_budgets.types.groups.serialize_aws_json_1_1(
            value["groups"]
        )
    if "users" in value:
        import capo_budgets.types.users

        out["Users"] = capo_budgets.types.users.serialize_aws_json_1_1(value["users"])
    return out


def deserialize_aws_json_1_1(data: dict) -> IamActionDefinition:
    out: IamActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("Roles") is not None:
        import capo_budgets.types.roles

        out["roles"] = capo_budgets.types.roles.deserialize_aws_json_1_1(data["Roles"])
    if data.get("Groups") is not None:
        import capo_budgets.types.groups

        out["groups"] = capo_budgets.types.groups.deserialize_aws_json_1_1(
            data["Groups"]
        )
    if data.get("Users") is not None:
        import capo_budgets.types.users

        out["users"] = capo_budgets.types.users.deserialize_aws_json_1_1(data["Users"])
    return out
