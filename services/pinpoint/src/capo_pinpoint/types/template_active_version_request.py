"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplateActiveVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class TemplateActiveVersionRequest(TypedDict, closed=True):
    version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The version of the message template to use as the active version of the template. Valid values are: latest, for the most recent version of the template; or, the unique identifier for any existing version of the template. If you specify an identifier, the value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateActiveVersionRequest) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> TemplateActiveVersionRequest:
    out: TemplateActiveVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
