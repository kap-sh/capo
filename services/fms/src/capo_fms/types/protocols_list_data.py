"""Generated from Smithy shape ``com.amazonaws.fms#ProtocolsListData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.list_id
    import capo_fms.types.previous_protocols_list
    import capo_fms.types.protocols_list
    import capo_fms.types.resource_name
    import capo_fms.types.time_stamp
    import capo_fms.types.update_token


class ProtocolsListData(TypedDict, closed=True):
    list_id: NotRequired["capo_fms.types.list_id.ListId"]
    """<p>The ID of the Firewall Manager protocols list.</p>"""
    list_name: "capo_fms.types.resource_name.ResourceName"
    """<p>The name of the Firewall Manager protocols list.</p>"""
    list_update_token: NotRequired["capo_fms.types.update_token.UpdateToken"]
    """<p>A unique identifier for each update to the list. When you update the list, the update token must match the token of the current version of the application list. You can retrieve the update token by getting the list. </p>"""
    create_time: NotRequired["capo_fms.types.time_stamp.TimeStamp"]
    """<p>The time that the Firewall Manager protocols list was created.</p>"""
    last_update_time: NotRequired["capo_fms.types.time_stamp.TimeStamp"]
    """<p>The time that the Firewall Manager protocols list was last updated.</p>"""
    protocols_list: "capo_fms.types.protocols_list.ProtocolsList"
    """<p>An array of protocols in the Firewall Manager protocols list.</p>"""
    previous_protocols_list: NotRequired[
        "capo_fms.types.previous_protocols_list.PreviousProtocolsList"
    ]
    """<p>A map of previous version numbers to their corresponding protocol arrays.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolsListData) -> dict:
    out: dict = {}
    if "list_id" in value:
        out["ListId"] = value["list_id"]
    out["ListName"] = value["list_name"]
    if "list_update_token" in value:
        out["ListUpdateToken"] = value["list_update_token"]
    if "create_time" in value:
        import capo_fms.types.time_stamp

        out["CreateTime"] = capo_fms.types.time_stamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "last_update_time" in value:
        import capo_fms.types.time_stamp

        out["LastUpdateTime"] = capo_fms.types.time_stamp.serialize_aws_json_1_1(
            value["last_update_time"]
        )
    import capo_fms.types.protocols_list

    out["ProtocolsList"] = capo_fms.types.protocols_list.serialize_aws_json_1_1(
        value["protocols_list"]
    )
    if "previous_protocols_list" in value:
        import capo_fms.types.previous_protocols_list

        out["PreviousProtocolsList"] = (
            capo_fms.types.previous_protocols_list.serialize_aws_json_1_1(
                value["previous_protocols_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtocolsListData:
    out: ProtocolsListData = {}  # type: ignore[typeddict-item]
    if data.get("ListId") is not None:
        out["list_id"] = data["ListId"]
    if data.get("ListName") is not None:
        out["list_name"] = data["ListName"]
    else:
        out["list_name"] = ""
    if data.get("ListUpdateToken") is not None:
        out["list_update_token"] = data["ListUpdateToken"]
    if data.get("CreateTime") is not None:
        import capo_fms.types.time_stamp

        out["create_time"] = capo_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if data.get("LastUpdateTime") is not None:
        import capo_fms.types.time_stamp

        out["last_update_time"] = capo_fms.types.time_stamp.deserialize_aws_json_1_1(
            data["LastUpdateTime"]
        )
    if data.get("ProtocolsList") is not None:
        import capo_fms.types.protocols_list

        out["protocols_list"] = capo_fms.types.protocols_list.deserialize_aws_json_1_1(
            data["ProtocolsList"]
        )
    else:
        out["protocols_list"] = []
    if data.get("PreviousProtocolsList") is not None:
        import capo_fms.types.previous_protocols_list

        out["previous_protocols_list"] = (
            capo_fms.types.previous_protocols_list.deserialize_aws_json_1_1(
                data["PreviousProtocolsList"]
            )
        )
    return out
