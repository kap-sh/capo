"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#GetMicrovmImageBuildOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_lambda_microvms.types.architecture
    import capo_lambda_microvms.types.build_state
    import capo_lambda_microvms.types.chipset
    import capo_lambda_microvms.types.non_blank_string
    import capo_lambda_microvms.types.snapshot_build


class GetMicrovmImageBuildOutput(TypedDict, closed=True):
    image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The ARN of the MicroVM image.</p>"""
    image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The version of the MicroVM image.</p>"""
    build_id: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The build request ID.</p>"""
    build_state: "capo_lambda_microvms.types.build_state.BuildState"
    """<p>The current state of the build.</p>"""
    architecture: "capo_lambda_microvms.types.architecture.Architecture"
    """<p>The target CPU architecture for the build. Supported value: ARM_64.</p>"""
    chipset: "capo_lambda_microvms.types.chipset.Chipset"
    """<p>The target chipset for the build.</p>"""
    chipset_generation: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The target chipset generation for the build.</p>"""
    state_reason: NotRequired["str"]
    """<p>The reason for the build state, if applicable.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the build was created.</p>"""
    snapshot_build: NotRequired[
        "capo_lambda_microvms.types.snapshot_build.SnapshotBuild"
    ]
    """<p>The snapshot build details, including memory and disk snapshot sizes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMicrovmImageBuildOutput) -> dict:
    out: dict = {}
    out["imageArn"] = value["image_arn"]
    out["imageVersion"] = value["image_version"]
    out["buildId"] = value["build_id"]
    import capo_lambda_microvms.types.build_state

    out["buildState"] = capo_lambda_microvms.types.build_state.serialize_json(
        value["build_state"]
    )
    import capo_lambda_microvms.types.architecture

    out["architecture"] = capo_lambda_microvms.types.architecture.serialize_json(
        value["architecture"]
    )
    import capo_lambda_microvms.types.chipset

    out["chipset"] = capo_lambda_microvms.types.chipset.serialize_json(value["chipset"])
    out["chipsetGeneration"] = value["chipset_generation"]
    if "state_reason" in value:
        out["stateReason"] = value["state_reason"]
    import capo_lambda_microvms.types._prelude.timestamp

    out["createdAt"] = capo_lambda_microvms.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "snapshot_build" in value:
        import capo_lambda_microvms.types.snapshot_build

        out["snapshotBuild"] = capo_lambda_microvms.types.snapshot_build.serialize_json(
            value["snapshot_build"]
        )
    return out


def deserialize_json(data: dict) -> GetMicrovmImageBuildOutput:
    out: GetMicrovmImageBuildOutput = {}  # type: ignore[typeddict-item]
    if data.get("imageArn") is not None:
        out["image_arn"] = data["imageArn"]
    else:
        raise DeserializationError("GetMicrovmImageBuildOutput.image_arn required")
    if data.get("imageVersion") is not None:
        out["image_version"] = data["imageVersion"]
    else:
        raise DeserializationError("GetMicrovmImageBuildOutput.image_version required")
    if data.get("buildId") is not None:
        out["build_id"] = data["buildId"]
    else:
        raise DeserializationError("GetMicrovmImageBuildOutput.build_id required")
    if data.get("buildState") is not None:
        import capo_lambda_microvms.types.build_state

        out["build_state"] = capo_lambda_microvms.types.build_state.deserialize_json(
            data["buildState"]
        )
    else:
        raise DeserializationError("GetMicrovmImageBuildOutput.build_state required")
    if data.get("architecture") is not None:
        import capo_lambda_microvms.types.architecture

        out["architecture"] = capo_lambda_microvms.types.architecture.deserialize_json(
            data["architecture"]
        )
    else:
        raise DeserializationError("GetMicrovmImageBuildOutput.architecture required")
    if data.get("chipset") is not None:
        import capo_lambda_microvms.types.chipset

        out["chipset"] = capo_lambda_microvms.types.chipset.deserialize_json(
            data["chipset"]
        )
    else:
        raise DeserializationError("GetMicrovmImageBuildOutput.chipset required")
    if data.get("chipsetGeneration") is not None:
        out["chipset_generation"] = data["chipsetGeneration"]
    else:
        raise DeserializationError(
            "GetMicrovmImageBuildOutput.chipset_generation required"
        )
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    if data.get("createdAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["created_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetMicrovmImageBuildOutput.created_at required")
    if data.get("snapshotBuild") is not None:
        import capo_lambda_microvms.types.snapshot_build

        out["snapshot_build"] = (
            capo_lambda_microvms.types.snapshot_build.deserialize_json(
                data["snapshotBuild"]
            )
        )
    return out
