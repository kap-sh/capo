"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LaunchPermissionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.account_list
    import capo_imagebuilder.types.organization_arn_list
    import capo_imagebuilder.types.organizational_unit_arn_list
    import capo_imagebuilder.types.string_list


class LaunchPermissionConfiguration(TypedDict, closed=True):
    user_ids: NotRequired["capo_imagebuilder.types.account_list.AccountList"]
    """<p>The Amazon Web Services account IDs to grant launch permission to. Each listed account can use the distributed AMI to launch instances.</p>"""
    user_groups: NotRequired["capo_imagebuilder.types.string_list.StringList"]
    """<p>The name of the group that you want to grant launch permission to. The only supported value is <code>all</code>, which makes the distributed AMI public.</p>"""
    organization_arns: NotRequired[
        "capo_imagebuilder.types.organization_arn_list.OrganizationArnList"
    ]
    """<p>The ARN for an Amazon Web Services Organization that you want to share your AMI with. For more information, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html">What is Organizations?</a>.</p>"""
    organizational_unit_arns: NotRequired[
        "capo_imagebuilder.types.organizational_unit_arn_list.OrganizationalUnitArnList"
    ]
    """<p>The ARN for an Organizations organizational unit (OU) that you want to share your AMI with. For more information about key concepts for Organizations, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html">Organizations terminology and concepts</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchPermissionConfiguration) -> dict:
    out: dict = {}
    if "user_ids" in value:
        import capo_imagebuilder.types.account_list

        out["userIds"] = capo_imagebuilder.types.account_list.serialize_json(
            value["user_ids"]
        )
    if "user_groups" in value:
        import capo_imagebuilder.types.string_list

        out["userGroups"] = capo_imagebuilder.types.string_list.serialize_json(
            value["user_groups"]
        )
    if "organization_arns" in value:
        import capo_imagebuilder.types.organization_arn_list

        out["organizationArns"] = (
            capo_imagebuilder.types.organization_arn_list.serialize_json(
                value["organization_arns"]
            )
        )
    if "organizational_unit_arns" in value:
        import capo_imagebuilder.types.organizational_unit_arn_list

        out["organizationalUnitArns"] = (
            capo_imagebuilder.types.organizational_unit_arn_list.serialize_json(
                value["organizational_unit_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> LaunchPermissionConfiguration:
    out: LaunchPermissionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("userIds") is not None:
        import capo_imagebuilder.types.account_list

        out["user_ids"] = capo_imagebuilder.types.account_list.deserialize_json(
            data["userIds"]
        )
    if data.get("userGroups") is not None:
        import capo_imagebuilder.types.string_list

        out["user_groups"] = capo_imagebuilder.types.string_list.deserialize_json(
            data["userGroups"]
        )
    if data.get("organizationArns") is not None:
        import capo_imagebuilder.types.organization_arn_list

        out["organization_arns"] = (
            capo_imagebuilder.types.organization_arn_list.deserialize_json(
                data["organizationArns"]
            )
        )
    if data.get("organizationalUnitArns") is not None:
        import capo_imagebuilder.types.organizational_unit_arn_list

        out["organizational_unit_arns"] = (
            capo_imagebuilder.types.organizational_unit_arn_list.deserialize_json(
                data["organizationalUnitArns"]
            )
        )
    return out
