"""Generated from Smithy shape ``com.amazonaws.connect#ExtensionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.allowed_extensions_list


class ExtensionConfiguration(TypedDict, closed=True):
    allowed_extensions: (
        "capo_connect.types.allowed_extensions_list.AllowedExtensionsList"
    )
    """<p>The list of allowed file extensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.allowed_extensions_list

    out["AllowedExtensions"] = (
        capo_connect.types.allowed_extensions_list.serialize_json(
            value["allowed_extensions"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExtensionConfiguration:
    out: ExtensionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AllowedExtensions") is not None:
        import capo_connect.types.allowed_extensions_list

        out["allowed_extensions"] = (
            capo_connect.types.allowed_extensions_list.deserialize_json(
                data["AllowedExtensions"]
            )
        )
    else:
        out["allowed_extensions"] = []
    return out
