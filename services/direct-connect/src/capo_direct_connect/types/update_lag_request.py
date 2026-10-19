"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateLagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_direct_connect.types.count
    import capo_direct_connect.types.encryption_mode
    import capo_direct_connect.types.lag_id
    import capo_direct_connect.types.lag_name


class UpdateLagRequest(TypedDict, closed=True):
    lag_id: "capo_direct_connect.types.lag_id.LagId"
    """<p>The ID of the LAG.</p>"""
    lag_name: NotRequired["capo_direct_connect.types.lag_name.LagName"]
    """<p>The name of the LAG.</p>"""
    minimum_links: NotRequired["capo_direct_connect.types.count.Count"]
    """<p>The minimum number of physical connections that must be operational for the LAG itself to be operational.</p>"""
    encryption_mode: NotRequired[
        "capo_direct_connect.types.encryption_mode.EncryptionMode"
    ]
    """<p>The LAG MAC Security (MACsec) encryption mode.</p> <p>Amazon Web Services applies the value to all connections which are part of the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLagRequest) -> dict:
    out: dict = {}
    out["lagId"] = value["lag_id"]
    if "lag_name" in value:
        out["lagName"] = value["lag_name"]
    if "minimum_links" in value:
        out["minimumLinks"] = value["minimum_links"]
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLagRequest:
    out: UpdateLagRequest = {}  # type: ignore[typeddict-item]
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    else:
        raise DeserializationError("UpdateLagRequest.lag_id required")
    if data.get("lagName") is not None:
        out["lag_name"] = data["lagName"]
    if data.get("minimumLinks") is not None:
        out["minimum_links"] = data["minimumLinks"]
    if data.get("encryptionMode") is not None:
        out["encryption_mode"] = data["encryptionMode"]
    return out
