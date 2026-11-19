"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateThemeForStackResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.theme


class UpdateThemeForStackResult(TypedDict, closed=True):
    theme: NotRequired["capo_appstream.types.theme.Theme"]
    """<p> The theme object that contains the metadata of the custom branding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateThemeForStackResult) -> dict:
    out: dict = {}
    if "theme" in value:
        import capo_appstream.types.theme

        out["Theme"] = capo_appstream.types.theme.serialize_aws_json_1_1(value["theme"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateThemeForStackResult:
    out: UpdateThemeForStackResult = {}  # type: ignore[typeddict-item]
    if data.get("Theme") is not None:
        import capo_appstream.types.theme

        out["theme"] = capo_appstream.types.theme.deserialize_aws_json_1_1(
            data["Theme"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateThemeForStackResult) -> dict:
    out: dict = {}
    if "theme" in value:
        import capo_appstream.types.theme

        out["Theme"] = capo_appstream.types.theme.serialize_cbor(value["theme"])
    return out


def deserialize_cbor(data: dict) -> UpdateThemeForStackResult:
    out: UpdateThemeForStackResult = {}  # type: ignore[typeddict-item]
    if data.get("Theme") is not None:
        import capo_appstream.types.theme

        out["theme"] = capo_appstream.types.theme.deserialize_cbor(data["Theme"])
    return out
