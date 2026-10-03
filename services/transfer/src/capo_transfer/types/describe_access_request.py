"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.external_id
    import capo_transfer.types.server_id


class DescribeAccessRequest(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server that has this access assigned.</p>"""
    external_id: "capo_transfer.types.external_id.ExternalId"
    """<p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like "<i>YourGroupName</i>*"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccessRequest) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["ExternalId"] = value["external_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccessRequest:
    out: DescribeAccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("DescribeAccessRequest.server_id required")
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    else:
        raise DeserializationError("DescribeAccessRequest.external_id required")
    return out
