"""Generated from Smithy shape ``com.amazonaws.mediatailor#HttpPackageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.type


class HttpPackageConfiguration(TypedDict, closed=True):
    path: "capo_mediatailor.types.__string.__string"
    """<p>The relative path to the URL for this VOD source. This is combined with <code>SourceLocation::HttpConfiguration::BaseUrl</code> to form a valid URL.</p>"""
    source_group: "capo_mediatailor.types.__string.__string"
    """<p>The name of the source group. This has to match one of the <code>Channel::Outputs::SourceGroup</code>.</p>"""
    type: "capo_mediatailor.types.type.Type"
    """<p>The streaming protocol for this package configuration. Supported values are <code>HLS</code> and <code>DASH</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpPackageConfiguration) -> dict:
    out: dict = {}
    out["Path"] = value["path"]
    out["SourceGroup"] = value["source_group"]
    import capo_mediatailor.types.type

    out["Type"] = capo_mediatailor.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> HttpPackageConfiguration:
    out: HttpPackageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    else:
        out["path"] = ""
    if data.get("SourceGroup") is not None:
        out["source_group"] = data["SourceGroup"]
    else:
        out["source_group"] = ""
    if data.get("Type") is not None:
        import capo_mediatailor.types.type

        out["type"] = capo_mediatailor.types.type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_mediatailor.types.type.Type", "")
    return out
