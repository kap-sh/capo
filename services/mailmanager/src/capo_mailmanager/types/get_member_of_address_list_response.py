"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetMemberOfAddressListResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.address


class GetMemberOfAddressListResponse(TypedDict, closed=True):
    address: "capo_mailmanager.types.address.Address"
    """<p>The address retrieved from the address list.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The timestamp of when the address was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMemberOfAddressListResponse) -> dict:
    out: dict = {}
    out["Address"] = value["address"]
    import capo_mailmanager.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMemberOfAddressListResponse:
    out: GetMemberOfAddressListResponse = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    else:
        raise DeserializationError("GetMemberOfAddressListResponse.address required")
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "GetMemberOfAddressListResponse.created_timestamp required"
        )
    return out


def redact_sensitive(value: GetMemberOfAddressListResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "address" in value:
        out["address"] = "*** Sensitive Data Redacted ***"
    return out
