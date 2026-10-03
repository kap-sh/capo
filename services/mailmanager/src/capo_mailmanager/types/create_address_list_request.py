"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddressListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.address_list_name
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.tag_list


class CreateAddressListRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    address_list_name: "capo_mailmanager.types.address_list_name.AddressListName"
    """<p>A user-friendly name for the address list.</p>"""
    tags: NotRequired["capo_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddressListRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["AddressListName"] = value["address_list_name"]
    if "tags" in value:
        import capo_mailmanager.types.tag_list

        out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddressListRequest:
    out: CreateAddressListRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("AddressListName") is not None:
        out["address_list_name"] = data["AddressListName"]
    else:
        raise DeserializationError(
            "CreateAddressListRequest.address_list_name required"
        )
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
