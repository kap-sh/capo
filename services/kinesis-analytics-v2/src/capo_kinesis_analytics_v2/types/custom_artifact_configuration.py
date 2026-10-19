"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CustomArtifactConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.artifact_type
    import capo_kinesis_analytics_v2.types.maven_reference
    import capo_kinesis_analytics_v2.types.s3_content_location


class CustomArtifactConfiguration(TypedDict, closed=True):
    artifact_type: "capo_kinesis_analytics_v2.types.artifact_type.ArtifactType"
    """<p> <code>UDF</code> stands for user-defined functions. This type of artifact must be in an S3 bucket. A <code>DEPENDENCY_JAR</code> can be in either Maven or an S3 bucket.</p>"""
    s3_content_location: NotRequired[
        "capo_kinesis_analytics_v2.types.s3_content_location.S3ContentLocation"
    ]
    maven_reference: NotRequired[
        "capo_kinesis_analytics_v2.types.maven_reference.MavenReference"
    ]
    """<p>The parameters required to fully specify a Maven reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomArtifactConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.artifact_type

    out["ArtifactType"] = (
        capo_kinesis_analytics_v2.types.artifact_type.serialize_aws_json_1_1(
            value["artifact_type"]
        )
    )
    if "s3_content_location" in value:
        import capo_kinesis_analytics_v2.types.s3_content_location

        out["S3ContentLocation"] = (
            capo_kinesis_analytics_v2.types.s3_content_location.serialize_aws_json_1_1(
                value["s3_content_location"]
            )
        )
    if "maven_reference" in value:
        import capo_kinesis_analytics_v2.types.maven_reference

        out["MavenReference"] = (
            capo_kinesis_analytics_v2.types.maven_reference.serialize_aws_json_1_1(
                value["maven_reference"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomArtifactConfiguration:
    out: CustomArtifactConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ArtifactType") is not None:
        import capo_kinesis_analytics_v2.types.artifact_type

        out["artifact_type"] = (
            capo_kinesis_analytics_v2.types.artifact_type.deserialize_aws_json_1_1(
                data["ArtifactType"]
            )
        )
    else:
        import typing

        out["artifact_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.artifact_type.ArtifactType", ""
        )
    if data.get("S3ContentLocation") is not None:
        import capo_kinesis_analytics_v2.types.s3_content_location

        out["s3_content_location"] = (
            capo_kinesis_analytics_v2.types.s3_content_location.deserialize_aws_json_1_1(
                data["S3ContentLocation"]
            )
        )
    if data.get("MavenReference") is not None:
        import capo_kinesis_analytics_v2.types.maven_reference

        out["maven_reference"] = (
            capo_kinesis_analytics_v2.types.maven_reference.deserialize_aws_json_1_1(
                data["MavenReference"]
            )
        )
    return out
