"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SetupArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.setup_artifact_content
    import capo_observabilityadmin.types.setup_artifact_content_type
    import capo_observabilityadmin.types.setup_artifact_file_name
    import capo_observabilityadmin.types.setup_format


class SetupArtifact(TypedDict, closed=True):
    file_name: (
        "capo_observabilityadmin.types.setup_artifact_file_name.SetupArtifactFileName"
    )
    """<p>The suggested file name, for example <code>main.bicep</code>.</p>"""
    content: "capo_observabilityadmin.types.setup_artifact_content.SetupArtifactContent"
    """<p>The content of the artifact.</p>"""
    format: "capo_observabilityadmin.types.setup_format.SetupFormat"
    """<p>The format of the artifact.</p>"""
    content_type: NotRequired[
        "capo_observabilityadmin.types.setup_artifact_content_type.SetupArtifactContentType"
    ]
    """<p>The content type of the artifact, for example <code>text/plain</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetupArtifact) -> dict:
    out: dict = {}
    out["FileName"] = value["file_name"]
    out["Content"] = value["content"]
    import capo_observabilityadmin.types.setup_format

    out["Format"] = capo_observabilityadmin.types.setup_format.serialize_json(
        value["format"]
    )
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> SetupArtifact:
    out: SetupArtifact = {}  # type: ignore[typeddict-item]
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    else:
        out["file_name"] = ""
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        out["content"] = ""
    if data.get("Format") is not None:
        import capo_observabilityadmin.types.setup_format

        out["format"] = capo_observabilityadmin.types.setup_format.deserialize_json(
            data["Format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_observabilityadmin.types.setup_format.SetupFormat", ""
        )
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    return out
