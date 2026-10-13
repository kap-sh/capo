"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionArtifacts``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.test_grid_session_artifact

TestGridSessionArtifacts: TypeAlias = list[
    "capo_device_farm.types.test_grid_session_artifact.TestGridSessionArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessionArtifacts) -> list:
    import capo_device_farm.types.test_grid_session_artifact

    out: list = []
    for item in value:
        out.append(
            capo_device_farm.types.test_grid_session_artifact.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TestGridSessionArtifacts:
    import capo_device_farm.types.test_grid_session_artifact

    out: TestGridSessionArtifacts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_device_farm.types.test_grid_session_artifact.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: TestGridSessionArtifacts) -> list[Any]:
    import capo_device_farm.types.test_grid_session_artifact

    return [
        capo_device_farm.types.test_grid_session_artifact.redact_sensitive(item)
        for item in value
    ]
