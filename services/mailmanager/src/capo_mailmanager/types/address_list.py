"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddressList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.address_list_arn
    import capo_mailmanager.types.address_list_id
    import capo_mailmanager.types.address_list_name


class AddressList(TypedDict, closed=True):
    address_list_id: "capo_mailmanager.types.address_list_id.AddressListId"
    """<p>The identifier of the address list.</p>"""
    address_list_arn: "capo_mailmanager.types.address_list_arn.AddressListArn"
    """<p>The Amazon Resource Name (ARN) of the address list.</p>"""
    address_list_name: "capo_mailmanager.types.address_list_name.AddressListName"
    """<p>The user-friendly name of the address list.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The timestamp of when the address list was created.</p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p>The timestamp of when the address list was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddressList) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    out["AddressListArn"] = value["address_list_arn"]
    out["AddressListName"] = value["address_list_name"]
    import capo_mailmanager.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    import capo_mailmanager.types._prelude.timestamp

    out["LastUpdatedTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_updated_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AddressList:
    out: AddressList = {}  # type: ignore[typeddict-item]
    if data.get("AddressListId") is not None:
        out["address_list_id"] = data["AddressListId"]
    else:
        out["address_list_id"] = ""
    if data.get("AddressListArn") is not None:
        out["address_list_arn"] = data["AddressListArn"]
    else:
        out["address_list_arn"] = ""
    if data.get("AddressListName") is not None:
        out["address_list_name"] = data["AddressListName"]
    else:
        out["address_list_name"] = ""
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        import datetime

        out["created_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    else:
        import datetime

        out["last_updated_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
