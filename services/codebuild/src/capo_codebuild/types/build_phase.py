"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildPhase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_phase_type
    import capo_codebuild.types.phase_contexts
    import capo_codebuild.types.status_type
    import capo_codebuild.types.timestamp
    import capo_codebuild.types.wrapper_long


class BuildPhase(TypedDict, closed=True):
    phase_type: NotRequired["capo_codebuild.types.build_phase_type.BuildPhaseType"]
    """<p>The name of the build phase. Valid values include:</p> <dl> <dt>BUILD</dt> <dd> <p>Core build activities typically occur in this build phase.</p> </dd> <dt>COMPLETED</dt> <dd> <p>The build has been completed.</p> </dd> <dt>DOWNLOAD_SOURCE</dt> <dd> <p>Source code is being downloaded in this build phase.</p> </dd> <dt>FINALIZING</dt> <dd> <p>The build process is completing in this build phase.</p> </dd> <dt>INSTALL</dt> <dd> <p>Installation activities typically occur in this build phase.</p> </dd> <dt>POST_BUILD</dt> <dd> <p>Post-build activities typically occur in this build phase.</p> </dd> <dt>PRE_BUILD</dt> <dd> <p>Pre-build activities typically occur in this build phase.</p> </dd> <dt>PROVISIONING</dt> <dd> <p>The build environment is being set up.</p> </dd> <dt>QUEUED</dt> <dd> <p>The build has been submitted and is queued behind other submitted builds.</p> </dd> <dt>SUBMITTED</dt> <dd> <p>The build has been submitted.</p> </dd> <dt>UPLOAD_ARTIFACTS</dt> <dd> <p>Build output artifacts are being uploaded to the output location.</p> </dd> </dl>"""
    phase_status: NotRequired["capo_codebuild.types.status_type.StatusType"]
    """<p>The current status of the build phase. Valid values include:</p> <dl> <dt>FAILED</dt> <dd> <p>The build phase failed.</p> </dd> <dt>FAULT</dt> <dd> <p>The build phase faulted.</p> </dd> <dt>IN_PROGRESS</dt> <dd> <p>The build phase is still in progress.</p> </dd> <dt>STOPPED</dt> <dd> <p>The build phase stopped.</p> </dd> <dt>SUCCEEDED</dt> <dd> <p>The build phase succeeded.</p> </dd> <dt>TIMED_OUT</dt> <dd> <p>The build phase timed out.</p> </dd> </dl>"""
    start_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the build phase started, expressed in Unix time format.</p>"""
    end_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the build phase ended, expressed in Unix time format.</p>"""
    duration_in_seconds: NotRequired["capo_codebuild.types.wrapper_long.WrapperLong"]
    """<p>How long, in seconds, between the starting and ending times of the build's phase.</p>"""
    contexts: NotRequired["capo_codebuild.types.phase_contexts.PhaseContexts"]
    """<p>Additional information about a build phase, especially to help troubleshoot a failed build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildPhase) -> dict:
    out: dict = {}
    if "phase_type" in value:
        import capo_codebuild.types.build_phase_type

        out["phaseType"] = capo_codebuild.types.build_phase_type.serialize_aws_json_1_1(
            value["phase_type"]
        )
    if "phase_status" in value:
        import capo_codebuild.types.status_type

        out["phaseStatus"] = capo_codebuild.types.status_type.serialize_aws_json_1_1(
            value["phase_status"]
        )
    if "start_time" in value:
        import capo_codebuild.types.timestamp

        out["startTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codebuild.types.timestamp

        out["endTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "duration_in_seconds" in value:
        out["durationInSeconds"] = value["duration_in_seconds"]
    if "contexts" in value:
        import capo_codebuild.types.phase_contexts

        out["contexts"] = capo_codebuild.types.phase_contexts.serialize_aws_json_1_1(
            value["contexts"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildPhase:
    out: BuildPhase = {}  # type: ignore[typeddict-item]
    if data.get("phaseType") is not None:
        import capo_codebuild.types.build_phase_type

        out["phase_type"] = (
            capo_codebuild.types.build_phase_type.deserialize_aws_json_1_1(
                data["phaseType"]
            )
        )
    if data.get("phaseStatus") is not None:
        import capo_codebuild.types.status_type

        out["phase_status"] = capo_codebuild.types.status_type.deserialize_aws_json_1_1(
            data["phaseStatus"]
        )
    if data.get("startTime") is not None:
        import capo_codebuild.types.timestamp

        out["start_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_codebuild.types.timestamp

        out["end_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if data.get("durationInSeconds") is not None:
        out["duration_in_seconds"] = data["durationInSeconds"]
    if data.get("contexts") is not None:
        import capo_codebuild.types.phase_contexts

        out["contexts"] = capo_codebuild.types.phase_contexts.deserialize_aws_json_1_1(
            data["contexts"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildPhase) -> dict:
    out: dict = {}
    if "phase_type" in value:
        import capo_codebuild.types.build_phase_type

        out["phaseType"] = capo_codebuild.types.build_phase_type.serialize_cbor(
            value["phase_type"]
        )
    if "phase_status" in value:
        import capo_codebuild.types.status_type

        out["phaseStatus"] = capo_codebuild.types.status_type.serialize_cbor(
            value["phase_status"]
        )
    if "start_time" in value:
        import capo_codebuild.types.timestamp

        out["startTime"] = capo_codebuild.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codebuild.types.timestamp

        out["endTime"] = capo_codebuild.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "duration_in_seconds" in value:
        out["durationInSeconds"] = value["duration_in_seconds"]
    if "contexts" in value:
        import capo_codebuild.types.phase_contexts

        out["contexts"] = capo_codebuild.types.phase_contexts.serialize_cbor(
            value["contexts"]
        )
    return out


def deserialize_cbor(data: dict) -> BuildPhase:
    out: BuildPhase = {}  # type: ignore[typeddict-item]
    if data.get("phaseType") is not None:
        import capo_codebuild.types.build_phase_type

        out["phase_type"] = capo_codebuild.types.build_phase_type.deserialize_cbor(
            data["phaseType"]
        )
    if data.get("phaseStatus") is not None:
        import capo_codebuild.types.status_type

        out["phase_status"] = capo_codebuild.types.status_type.deserialize_cbor(
            data["phaseStatus"]
        )
    if data.get("startTime") is not None:
        import capo_codebuild.types.timestamp

        out["start_time"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_codebuild.types.timestamp

        out["end_time"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["endTime"]
        )
    if data.get("durationInSeconds") is not None:
        out["duration_in_seconds"] = data["durationInSeconds"]
    if data.get("contexts") is not None:
        import capo_codebuild.types.phase_contexts

        out["contexts"] = capo_codebuild.types.phase_contexts.deserialize_cbor(
            data["contexts"]
        )
    return out
