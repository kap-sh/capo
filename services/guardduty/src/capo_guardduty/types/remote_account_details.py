"""Generated from Smithy shape ``com.amazonaws.guardduty#RemoteAccountDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean
    import capo_guardduty.types.string


class RemoteAccountDetails(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID of the remote API caller.</p>"""
    affiliated: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Details on whether the Amazon Web Services account of the remote API caller is related to your GuardDuty environment. If this value is <code>True</code> the API caller is affiliated to your account in some way. If it is <code>False</code> the API caller is from outside your environment.</p>"""
    aws_service_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>If the remote account belongs to an Amazon Web Services service, this field indicates which service the remote account belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAccountDetails) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "affiliated" in value:
        out["affiliated"] = value["affiliated"]
    if "aws_service_name" in value:
        out["awsServiceName"] = value["aws_service_name"]
    return out


def deserialize_json(data: dict) -> RemoteAccountDetails:
    out: RemoteAccountDetails = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("affiliated") is not None:
        out["affiliated"] = data["affiliated"]
    if data.get("awsServiceName") is not None:
        out["aws_service_name"] = data["awsServiceName"]
    return out
