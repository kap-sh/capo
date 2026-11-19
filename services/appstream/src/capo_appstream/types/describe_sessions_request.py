"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.authentication_type
    import capo_appstream.types.integer
    import capo_appstream.types.name
    import capo_appstream.types.string
    import capo_appstream.types.user_id


class DescribeSessionsRequest(TypedDict, closed=True):
    stack_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the stack. This value is case-sensitive.</p>"""
    fleet_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the fleet. This value is case-sensitive.</p>"""
    user_id: NotRequired["capo_appstream.types.user_id.UserId"]
    """<p>The user identifier (ID). If you specify a user ID, you must also specify the authentication type.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    limit: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The size of each page of results. The default value is 20 and the maximum value is 50.</p>"""
    authentication_type: NotRequired[
        "capo_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication method. Specify <code>API</code> for a user authenticated using a streaming URL or <code>SAML</code> for a SAML federated user. The default is to authenticate users using a streaming URL.</p>"""
    instance_id: NotRequired["capo_appstream.types.string.String"]
    """<p>The identifier for the instance hosting the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSessionsRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "authentication_type" in value:
        import capo_appstream.types.authentication_type

        out["AuthenticationType"] = (
            capo_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSessionsRequest:
    out: DescribeSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("AuthenticationType") is not None:
        import capo_appstream.types.authentication_type

        out["authentication_type"] = (
            capo_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSessionsRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "authentication_type" in value:
        import capo_appstream.types.authentication_type

        out["AuthenticationType"] = (
            capo_appstream.types.authentication_type.serialize_cbor(
                value["authentication_type"]
            )
        )
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    return out


def deserialize_cbor(data: dict) -> DescribeSessionsRequest:
    out: DescribeSessionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("AuthenticationType") is not None:
        import capo_appstream.types.authentication_type

        out["authentication_type"] = (
            capo_appstream.types.authentication_type.deserialize_cbor(
                data["AuthenticationType"]
            )
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    return out
