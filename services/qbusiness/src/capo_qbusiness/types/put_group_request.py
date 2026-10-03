"""Generated from Smithy shape ``com.amazonaws.qbusiness#PutGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.group_members
    import capo_qbusiness.types.group_name
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.membership_type
    import capo_qbusiness.types.role_arn


class PutGroupRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application in which the user and group mapping belongs.</p>"""
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index in which you want to map users to their groups.</p>"""
    group_name: "capo_qbusiness.types.group_name.GroupName"
    """<p>The list that contains your users or sub groups that belong the same group. For example, the group "Company" includes the user "CEO" and the sub groups "Research", "Engineering", and "Sales and Marketing".</p>"""
    data_source_id: NotRequired["capo_qbusiness.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source for which you want to map users to their groups. This is useful if a group is tied to multiple data sources, but you only want the group to access documents of a certain data source. For example, the groups "Research", "Engineering", and "Sales and Marketing" are all tied to the company's documents stored in the data sources Confluence and Salesforce. However, "Sales and Marketing" team only needs access to customer-related documents stored in Salesforce.</p>"""
    type: "capo_qbusiness.types.membership_type.MembershipType"
    """<p>The type of the group.</p>"""
    group_members: "capo_qbusiness.types.group_members.GroupMembers"
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has access to the S3 file that contains your list of users that belong to a group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutGroupRequest) -> dict:
    out: dict = {}
    out["groupName"] = value["group_name"]
    if "data_source_id" in value:
        out["dataSourceId"] = value["data_source_id"]
    import capo_qbusiness.types.membership_type

    out["type"] = capo_qbusiness.types.membership_type.serialize_json(value["type"])
    import capo_qbusiness.types.group_members

    out["groupMembers"] = capo_qbusiness.types.group_members.serialize_json(
        value["group_members"]
    )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> PutGroupRequest:
    out: PutGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("groupName") is not None:
        out["group_name"] = data["groupName"]
    else:
        raise DeserializationError("PutGroupRequest.group_name required")
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    if data.get("type") is not None:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("PutGroupRequest.type required")
    if data.get("groupMembers") is not None:
        import capo_qbusiness.types.group_members

        out["group_members"] = capo_qbusiness.types.group_members.deserialize_json(
            data["groupMembers"]
        )
    else:
        raise DeserializationError("PutGroupRequest.group_members required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
