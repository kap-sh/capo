"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.described_user
    import capo_transfer.types.server_id


class DescribeUserResponse(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that has this user assigned.</p>"""
    user: "capo_transfer.types.described_user.DescribedUser"
    """<p>An array containing the properties of the Transfer Family user for the <code>ServerID</code> value that you specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    import capo_transfer.types.described_user

    out["User"] = capo_transfer.types.described_user.serialize_aws_json_1_1(
        value["user"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserResponse:
    out: DescribeUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    if data.get("User") is not None:
        import capo_transfer.types.described_user

        out["user"] = capo_transfer.types.described_user.deserialize_aws_json_1_1(
            data["User"]
        )
    else:
        raise DeserializationError("DescribeUserResponse.user required")
    return out
