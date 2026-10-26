"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotPayload``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError, SerializationError
from capo_partnercentral_selling.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_opportunity_summary_full_view
    import capo_partnercentral_selling.types.opportunity_summary_view


class _ResourceSnapshotPayload_OpportunitySummary(TypedDict, closed=True):
    OpportunitySummary: "capo_partnercentral_selling.types.opportunity_summary_view.OpportunitySummaryView"


class _ResourceSnapshotPayload_AwsOpportunitySummaryFullView(TypedDict, closed=True):
    AwsOpportunitySummaryFullView: "capo_partnercentral_selling.types.aws_opportunity_summary_full_view.AwsOpportunitySummaryFullView"


ResourceSnapshotPayload: TypeAlias = (
    _ResourceSnapshotPayload_OpportunitySummary
    | _ResourceSnapshotPayload_AwsOpportunitySummaryFullView
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSnapshotPayload) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResourceSnapshotPayload: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "OpportunitySummary" in value:
        import capo_partnercentral_selling.types.opportunity_summary_view

        return {
            "OpportunitySummary": capo_partnercentral_selling.types.opportunity_summary_view.serialize_aws_json_1_0(
                value["OpportunitySummary"]
            )
        }
    elif "AwsOpportunitySummaryFullView" in value:
        import capo_partnercentral_selling.types.aws_opportunity_summary_full_view

        return {
            "AwsOpportunitySummaryFullView": capo_partnercentral_selling.types.aws_opportunity_summary_full_view.serialize_aws_json_1_0(
                value["AwsOpportunitySummaryFullView"]
            )
        }
    else:
        raise SerializationError("ResourceSnapshotPayload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ResourceSnapshotPayload:
    if data.get("OpportunitySummary") is not None:
        import capo_partnercentral_selling.types.opportunity_summary_view

        return {
            "OpportunitySummary": capo_partnercentral_selling.types.opportunity_summary_view.deserialize_aws_json_1_0(
                data["OpportunitySummary"]
            )
        }
    elif data.get("AwsOpportunitySummaryFullView") is not None:
        import capo_partnercentral_selling.types.aws_opportunity_summary_full_view

        return {
            "AwsOpportunitySummaryFullView": capo_partnercentral_selling.types.aws_opportunity_summary_full_view.deserialize_aws_json_1_0(
                data["AwsOpportunitySummaryFullView"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ResourceSnapshotPayload: no recognized variant key")


def redact_sensitive(value: ResourceSnapshotPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "OpportunitySummary" in value:
        import capo_partnercentral_selling.types.opportunity_summary_view

        out["OpportunitySummary"] = (
            capo_partnercentral_selling.types.opportunity_summary_view.redact_sensitive(
                value["OpportunitySummary"]
            )
        )
    if "AwsOpportunitySummaryFullView" in value:
        import capo_partnercentral_selling.types.aws_opportunity_summary_full_view

        out["AwsOpportunitySummaryFullView"] = (
            capo_partnercentral_selling.types.aws_opportunity_summary_full_view.redact_sensitive(
                value["AwsOpportunitySummaryFullView"]
            )
        )
    return out
