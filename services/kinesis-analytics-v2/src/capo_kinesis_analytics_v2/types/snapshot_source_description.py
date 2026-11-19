"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotSourceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.s3_prefix_location
    import capo_kinesis_analytics_v2.types.source_application_description


class SnapshotSourceDescription(TypedDict, closed=True):
    s3_prefix_location: NotRequired[
        "capo_kinesis_analytics_v2.types.s3_prefix_location.S3PrefixLocation"
    ]
    """<p>The Amazon S3 location that the snapshot was imported from. This field is present only if <code>SnapshotInitiatorOperation</code> is <code>ImportSnapshot</code>.</p>"""
    source_application_description: NotRequired[
        "capo_kinesis_analytics_v2.types.source_application_description.SourceApplicationDescription"
    ]
    """<p>Describes the application that the snapshot was created from. This field is not present for imported snapshots.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotSourceDescription) -> dict:
    out: dict = {}
    if "s3_prefix_location" in value:
        import capo_kinesis_analytics_v2.types.s3_prefix_location

        out["S3PrefixLocation"] = (
            capo_kinesis_analytics_v2.types.s3_prefix_location.serialize_aws_json_1_1(
                value["s3_prefix_location"]
            )
        )
    if "source_application_description" in value:
        import capo_kinesis_analytics_v2.types.source_application_description

        out["SourceApplicationDescription"] = (
            capo_kinesis_analytics_v2.types.source_application_description.serialize_aws_json_1_1(
                value["source_application_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotSourceDescription:
    out: SnapshotSourceDescription = {}  # type: ignore[typeddict-item]
    if data.get("S3PrefixLocation") is not None:
        import capo_kinesis_analytics_v2.types.s3_prefix_location

        out["s3_prefix_location"] = (
            capo_kinesis_analytics_v2.types.s3_prefix_location.deserialize_aws_json_1_1(
                data["S3PrefixLocation"]
            )
        )
    if data.get("SourceApplicationDescription") is not None:
        import capo_kinesis_analytics_v2.types.source_application_description

        out["source_application_description"] = (
            capo_kinesis_analytics_v2.types.source_application_description.deserialize_aws_json_1_1(
                data["SourceApplicationDescription"]
            )
        )
    return out
