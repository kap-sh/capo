"""Generated from Smithy shape ``com.amazonaws.kendra#DeletePrincipalMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.group_id
    import capo_kendra.types.index_id
    import capo_kendra.types.principal_ordering_id


class DeletePrincipalMappingRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to delete a group from.</p>"""
    data_source_id: NotRequired["capo_kendra.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source you want to delete a group from.</p> <p>A group can be tied to multiple data sources. You can delete a group from accessing documents in a certain data source. For example, the groups "Research", "Engineering", and "Sales and Marketing" are all tied to the company's documents stored in the data sources Confluence and Salesforce. You want to delete "Research" and "Engineering" groups from Salesforce, so that these groups cannot access customer-related documents stored in Salesforce. Only "Sales and Marketing" should access documents in the Salesforce data source.</p>"""
    group_id: "capo_kendra.types.group_id.GroupId"
    """<p>The identifier of the group you want to delete.</p>"""
    ordering_id: NotRequired[
        "capo_kendra.types.principal_ordering_id.PrincipalOrderingId"
    ]
    """<p>The timestamp identifier you specify to ensure Amazon Kendra does not override the latest <code>DELETE</code> action with previous actions. The highest number ID, which is the ordering ID, is the latest action you want to process and apply on top of other actions with lower number IDs. This prevents previous actions with lower number IDs from possibly overriding the latest action.</p> <p>The ordering ID can be the Unix time of the last update you made to a group members list. You would then provide this list when calling <code>PutPrincipalMapping</code>. This ensures your <code>DELETE</code> action for that updated group with the latest members list doesn't get overwritten by earlier <code>DELETE</code> actions for the same group which are yet to be processed.</p> <p>The default ordering ID is the current Unix time in milliseconds that the action was received by Amazon Kendra. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePrincipalMappingRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    out["GroupId"] = value["group_id"]
    if "ordering_id" in value:
        out["OrderingId"] = value["ordering_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePrincipalMappingRequest:
    out: DeletePrincipalMappingRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("DeletePrincipalMappingRequest.index_id required")
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("DeletePrincipalMappingRequest.group_id required")
    if data.get("OrderingId") is not None:
        out["ordering_id"] = data["OrderingId"]
    return out
