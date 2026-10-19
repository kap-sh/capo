"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_tnb.types.function_artifact_meta


class GetSolFunctionPackageMetadata(TypedDict, closed=True):
    vnfd: NotRequired["capo_tnb.types.function_artifact_meta.FunctionArtifactMeta"]
    """<p>Metadata related to the function package descriptor of the function package.</p>"""
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageMetadata) -> dict:
    out: dict = {}
    if "vnfd" in value:
        import capo_tnb.types.function_artifact_meta

        out["vnfd"] = capo_tnb.types.function_artifact_meta.serialize_json(
            value["vnfd"]
        )
    import capo_tnb._protocol.serialize

    out["createdAt"] = capo_tnb._protocol.serialize.fmt_date_time(value["created_at"])
    import capo_tnb._protocol.serialize

    out["lastModified"] = capo_tnb._protocol.serialize.fmt_date_time(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageMetadata:
    out: GetSolFunctionPackageMetadata = {}  # type: ignore[typeddict-item]
    if data.get("vnfd") is not None:
        import capo_tnb.types.function_artifact_meta

        out["vnfd"] = capo_tnb.types.function_artifact_meta.deserialize_json(
            data["vnfd"]
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModified") is not None:
        import datetime

        out["last_modified"] = datetime.datetime.fromisoformat(
            data["lastModified"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["last_modified"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
