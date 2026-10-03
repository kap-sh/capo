"""Generated from Smithy shape ``com.amazonaws.appconfig#Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.blob
    import capo_appconfig.types.string
    import capo_appconfig.types.version


class Configuration(TypedDict, closed=True):
    content: NotRequired["capo_appconfig.types.blob.Blob"]
    """<p>The content of the configuration or the configuration data.</p> <important> <p>The <code>Content</code> attribute only contains data if the system finds new or updated configuration data. If there is no new or updated data and <code>ClientConfigurationVersion</code> matches the version of the current configuration, AppConfig returns a <code>204 No Content</code> HTTP response code and the <code>Content</code> value will be empty.</p> </important>"""
    configuration_version: NotRequired["capo_appconfig.types.version.Version"]
    """<p>The configuration version.</p>"""
    content_type: NotRequired["capo_appconfig.types.string.String"]
    """<p>A standard MIME type describing the format of the configuration content. For more information, see <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17">Content-Type</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_appconfig.types.blob

        out["Content"] = capo_appconfig.types.blob.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        import capo_appconfig.types.blob

        out["content"] = capo_appconfig.types.blob.deserialize_json(data["Content"])
    return out
