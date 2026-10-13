"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionArtifact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.sensitive_string
    import capo_device_farm.types.string
    import capo_device_farm.types.test_grid_session_artifact_type


class TestGridSessionArtifact(TypedDict, closed=True):
    filename: NotRequired["capo_device_farm.types.string.String"]
    """<p>The file name of the artifact.</p>"""
    type: NotRequired[
        "capo_device_farm.types.test_grid_session_artifact_type.TestGridSessionArtifactType"
    ]
    """<p>The kind of artifact.</p>"""
    url: NotRequired["capo_device_farm.types.sensitive_string.SensitiveString"]
    """<p>A semi-stable URL to the content of the object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestGridSessionArtifact) -> dict:
    out: dict = {}
    if "filename" in value:
        out["filename"] = value["filename"]
    if "type" in value:
        import capo_device_farm.types.test_grid_session_artifact_type

        out["type"] = (
            capo_device_farm.types.test_grid_session_artifact_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestGridSessionArtifact:
    out: TestGridSessionArtifact = {}  # type: ignore[typeddict-item]
    if data.get("filename") is not None:
        out["filename"] = data["filename"]
    if data.get("type") is not None:
        import capo_device_farm.types.test_grid_session_artifact_type

        out["type"] = (
            capo_device_farm.types.test_grid_session_artifact_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("url") is not None:
        out["url"] = data["url"]
    return out


def redact_sensitive(value: TestGridSessionArtifact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
