"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateVodSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.http_package_configurations


class UpdateVodSourceRequest(TypedDict, closed=True):
    http_package_configurations: (
        "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    )
    """<p>A list of HTTP package configurations for the VOD source on this account.</p>"""
    source_location_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the source location associated with this VOD Source.</p>"""
    vod_source_name: "capo_mediatailor.types.__string.__string"
    """<p>The name of the VOD source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVodSourceRequest) -> dict:
    out: dict = {}
    import capo_mediatailor.types.http_package_configurations

    out["HttpPackageConfigurations"] = (
        capo_mediatailor.types.http_package_configurations.serialize_json(
            value["http_package_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateVodSourceRequest:
    out: UpdateVodSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("HttpPackageConfigurations") is not None:
        import capo_mediatailor.types.http_package_configurations

        out["http_package_configurations"] = (
            capo_mediatailor.types.http_package_configurations.deserialize_json(
                data["HttpPackageConfigurations"]
            )
        )
    else:
        out["http_package_configurations"] = []
    return out
