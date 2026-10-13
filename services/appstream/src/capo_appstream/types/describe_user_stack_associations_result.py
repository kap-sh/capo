"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeUserStackAssociationsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string
    import capo_appstream.types.user_stack_association_list


class DescribeUserStackAssociationsResult(TypedDict, closed=True):
    user_stack_associations: NotRequired[
        "capo_appstream.types.user_stack_association_list.UserStackAssociationList"
    ]
    """<p>The UserStackAssociation objects.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserStackAssociationsResult) -> dict:
    out: dict = {}
    if "user_stack_associations" in value:
        import capo_appstream.types.user_stack_association_list

        out["UserStackAssociations"] = (
            capo_appstream.types.user_stack_association_list.serialize_aws_json_1_1(
                value["user_stack_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserStackAssociationsResult:
    out: DescribeUserStackAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("UserStackAssociations") is not None:
        import capo_appstream.types.user_stack_association_list

        out["user_stack_associations"] = (
            capo_appstream.types.user_stack_association_list.deserialize_aws_json_1_1(
                data["UserStackAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeUserStackAssociationsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_stack_associations" in value:
        import capo_appstream.types.user_stack_association_list

        out["user_stack_associations"] = (
            capo_appstream.types.user_stack_association_list.redact_sensitive(
                value["user_stack_associations"]
            )
        )
    return out
