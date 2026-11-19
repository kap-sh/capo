"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeHybridADUpdateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.hybrid_update_activities
    import capo_directory_service.types.next_token


class DescribeHybridADUpdateResult(TypedDict, closed=True):
    update_activities: NotRequired[
        "capo_directory_service.types.hybrid_update_activities.HybridUpdateActivities"
    ]
    """<p>Information about update activities for the hybrid directory, organized by update type.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent request to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHybridADUpdateResult) -> dict:
    out: dict = {}
    if "update_activities" in value:
        import capo_directory_service.types.hybrid_update_activities

        out["UpdateActivities"] = (
            capo_directory_service.types.hybrid_update_activities.serialize_aws_json_1_1(
                value["update_activities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHybridADUpdateResult:
    out: DescribeHybridADUpdateResult = {}  # type: ignore[typeddict-item]
    if data.get("UpdateActivities") is not None:
        import capo_directory_service.types.hybrid_update_activities

        out["update_activities"] = (
            capo_directory_service.types.hybrid_update_activities.deserialize_aws_json_1_1(
                data["UpdateActivities"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeHybridADUpdateResult) -> dict:
    out: dict = {}
    if "update_activities" in value:
        import capo_directory_service.types.hybrid_update_activities

        out["UpdateActivities"] = (
            capo_directory_service.types.hybrid_update_activities.serialize_cbor(
                value["update_activities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeHybridADUpdateResult:
    out: DescribeHybridADUpdateResult = {}  # type: ignore[typeddict-item]
    if data.get("UpdateActivities") is not None:
        import capo_directory_service.types.hybrid_update_activities

        out["update_activities"] = (
            capo_directory_service.types.hybrid_update_activities.deserialize_cbor(
                data["UpdateActivities"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
