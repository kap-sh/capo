"""Generated from Smithy shape ``com.amazonaws.odb#GetAutonomousDatabaseWalletDetailsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class GetAutonomousDatabaseWalletDetailsInput(TypedDict, closed=True):
    autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to retrieve wallet details for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutonomousDatabaseWalletDetailsInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutonomousDatabaseWalletDetailsInput:
    out: GetAutonomousDatabaseWalletDetailsInput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        out["autonomous_database_id"] = ""
    return out
