"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteLagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.lag_id


class DeleteLagRequest(TypedDict, closed=True):
    lag_id: "capo_direct_connect.types.lag_id.LagId"
    """<p>The ID of the LAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLagRequest) -> dict:
    out: dict = {}
    out["lagId"] = value["lag_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLagRequest:
    out: DeleteLagRequest = {}  # type: ignore[typeddict-item]
    if data.get("lagId") is not None:
        out["lag_id"] = data["lagId"]
    else:
        out["lag_id"] = ""
    return out
