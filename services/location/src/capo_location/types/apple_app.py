"""Generated from Smithy shape ``com.amazonaws.location#AppleApp``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.apple_bundle_id


class AppleApp(TypedDict, closed=True):
    bundle_id: "capo_location.types.apple_bundle_id.AppleBundleId"
    """<p>The unique identifier of the app across all Apple platforms (iOS, macOS, tvOS and watchOS).</p> <p>Example: <code>com.mydomain.appname</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppleApp) -> dict:
    out: dict = {}
    out["BundleId"] = value["bundle_id"]
    return out


def deserialize_json(data: dict) -> AppleApp:
    out: AppleApp = {}  # type: ignore[typeddict-item]
    if data.get("BundleId") is not None:
        out["bundle_id"] = data["BundleId"]
    else:
        out["bundle_id"] = ""
    return out
