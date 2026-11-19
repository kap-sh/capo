"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.resolved_artifact
    import capo_codebuild.types.resolved_secondary_artifacts
    import capo_codebuild.types.status_type
    import capo_codebuild.types.string
    import capo_codebuild.types.timestamp


class BuildSummary(TypedDict, closed=True):
    arn: NotRequired["capo_codebuild.types.string.String"]
    """<p>The batch build ARN.</p>"""
    requested_on: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the build was started, expressed in Unix time format.</p>"""
    build_status: NotRequired["capo_codebuild.types.status_type.StatusType"]
    """<p>The status of the build group.</p> <dl> <dt>FAILED</dt> <dd> <p>The build group failed.</p> </dd> <dt>FAULT</dt> <dd> <p>The build group faulted.</p> </dd> <dt>IN_PROGRESS</dt> <dd> <p>The build group is still in progress.</p> </dd> <dt>STOPPED</dt> <dd> <p>The build group stopped.</p> </dd> <dt>SUCCEEDED</dt> <dd> <p>The build group succeeded.</p> </dd> <dt>TIMED_OUT</dt> <dd> <p>The build group timed out.</p> </dd> </dl>"""
    primary_artifact: NotRequired[
        "capo_codebuild.types.resolved_artifact.ResolvedArtifact"
    ]
    """<p>A <code>ResolvedArtifact</code> object that represents the primary build artifacts for the build group.</p>"""
    secondary_artifacts: NotRequired[
        "capo_codebuild.types.resolved_secondary_artifacts.ResolvedSecondaryArtifacts"
    ]
    """<p>An array of <code>ResolvedArtifact</code> objects that represents the secondary build artifacts for the build group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "requested_on" in value:
        import capo_codebuild.types.timestamp

        out["requestedOn"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["requested_on"]
        )
    if "build_status" in value:
        import capo_codebuild.types.status_type

        out["buildStatus"] = capo_codebuild.types.status_type.serialize_aws_json_1_1(
            value["build_status"]
        )
    if "primary_artifact" in value:
        import capo_codebuild.types.resolved_artifact

        out["primaryArtifact"] = (
            capo_codebuild.types.resolved_artifact.serialize_aws_json_1_1(
                value["primary_artifact"]
            )
        )
    if "secondary_artifacts" in value:
        import capo_codebuild.types.resolved_secondary_artifacts

        out["secondaryArtifacts"] = (
            capo_codebuild.types.resolved_secondary_artifacts.serialize_aws_json_1_1(
                value["secondary_artifacts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildSummary:
    out: BuildSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("requestedOn") is not None:
        import capo_codebuild.types.timestamp

        out["requested_on"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["requestedOn"]
        )
    if data.get("buildStatus") is not None:
        import capo_codebuild.types.status_type

        out["build_status"] = capo_codebuild.types.status_type.deserialize_aws_json_1_1(
            data["buildStatus"]
        )
    if data.get("primaryArtifact") is not None:
        import capo_codebuild.types.resolved_artifact

        out["primary_artifact"] = (
            capo_codebuild.types.resolved_artifact.deserialize_aws_json_1_1(
                data["primaryArtifact"]
            )
        )
    if data.get("secondaryArtifacts") is not None:
        import capo_codebuild.types.resolved_secondary_artifacts

        out["secondary_artifacts"] = (
            capo_codebuild.types.resolved_secondary_artifacts.deserialize_aws_json_1_1(
                data["secondaryArtifacts"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "requested_on" in value:
        import capo_codebuild.types.timestamp

        out["requestedOn"] = capo_codebuild.types.timestamp.serialize_cbor(
            value["requested_on"]
        )
    if "build_status" in value:
        import capo_codebuild.types.status_type

        out["buildStatus"] = capo_codebuild.types.status_type.serialize_cbor(
            value["build_status"]
        )
    if "primary_artifact" in value:
        import capo_codebuild.types.resolved_artifact

        out["primaryArtifact"] = capo_codebuild.types.resolved_artifact.serialize_cbor(
            value["primary_artifact"]
        )
    if "secondary_artifacts" in value:
        import capo_codebuild.types.resolved_secondary_artifacts

        out["secondaryArtifacts"] = (
            capo_codebuild.types.resolved_secondary_artifacts.serialize_cbor(
                value["secondary_artifacts"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BuildSummary:
    out: BuildSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("requestedOn") is not None:
        import capo_codebuild.types.timestamp

        out["requested_on"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["requestedOn"]
        )
    if data.get("buildStatus") is not None:
        import capo_codebuild.types.status_type

        out["build_status"] = capo_codebuild.types.status_type.deserialize_cbor(
            data["buildStatus"]
        )
    if data.get("primaryArtifact") is not None:
        import capo_codebuild.types.resolved_artifact

        out["primary_artifact"] = (
            capo_codebuild.types.resolved_artifact.deserialize_cbor(
                data["primaryArtifact"]
            )
        )
    if data.get("secondaryArtifacts") is not None:
        import capo_codebuild.types.resolved_secondary_artifacts

        out["secondary_artifacts"] = (
            capo_codebuild.types.resolved_secondary_artifacts.deserialize_cbor(
                data["secondaryArtifacts"]
            )
        )
    return out
