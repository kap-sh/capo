"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ListInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.instance_summary_list
    import capo_servicediscovery.types.next_token


class ListInstancesResponse(TypedDict, closed=True):
    resource_owner: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that created the namespace that contains the specified service. If this isn't your account ID, it's the ID of the account that shared the namespace with your account.</p>"""
    instances: NotRequired[
        "capo_servicediscovery.types.instance_summary_list.InstanceSummaryList"
    ]
    """<p>Summary information about the instances that are associated with the specified service.</p>"""
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>If more than <code>MaxResults</code> instances match the specified criteria, you can submit another <code>ListInstances</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstancesResponse) -> dict:
    out: dict = {}
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "instances" in value:
        import capo_servicediscovery.types.instance_summary_list

        out["Instances"] = (
            capo_servicediscovery.types.instance_summary_list.serialize_aws_json_1_1(
                value["instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstancesResponse:
    out: ListInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceOwner") is not None:
        out["resource_owner"] = data["ResourceOwner"]
    if data.get("Instances") is not None:
        import capo_servicediscovery.types.instance_summary_list

        out["instances"] = (
            capo_servicediscovery.types.instance_summary_list.deserialize_aws_json_1_1(
                data["Instances"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListInstancesResponse) -> dict:
    out: dict = {}
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "instances" in value:
        import capo_servicediscovery.types.instance_summary_list

        out["Instances"] = (
            capo_servicediscovery.types.instance_summary_list.serialize_cbor(
                value["instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListInstancesResponse:
    out: ListInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceOwner") is not None:
        out["resource_owner"] = data["ResourceOwner"]
    if data.get("Instances") is not None:
        import capo_servicediscovery.types.instance_summary_list

        out["instances"] = (
            capo_servicediscovery.types.instance_summary_list.deserialize_cbor(
                data["Instances"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
