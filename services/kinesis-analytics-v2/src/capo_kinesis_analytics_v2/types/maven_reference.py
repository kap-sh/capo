"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#MavenReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.maven_artifact_id
    import capo_kinesis_analytics_v2.types.maven_group_id
    import capo_kinesis_analytics_v2.types.maven_version


class MavenReference(TypedDict, closed=True):
    group_id: "capo_kinesis_analytics_v2.types.maven_group_id.MavenGroupId"
    """<p>The group ID of the Maven reference.</p>"""
    artifact_id: "capo_kinesis_analytics_v2.types.maven_artifact_id.MavenArtifactId"
    """<p>The artifact ID of the Maven reference.</p>"""
    version: "capo_kinesis_analytics_v2.types.maven_version.MavenVersion"
    """<p>The version of the Maven reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MavenReference) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    out["ArtifactId"] = value["artifact_id"]
    out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MavenReference:
    out: MavenReference = {}  # type: ignore[typeddict-item]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        out["group_id"] = ""
    if data.get("ArtifactId") is not None:
        out["artifact_id"] = data["ArtifactId"]
    else:
        out["artifact_id"] = ""
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = ""
    return out
