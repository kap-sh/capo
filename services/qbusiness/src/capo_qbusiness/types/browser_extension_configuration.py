"""Generated from Smithy shape ``com.amazonaws.qbusiness#BrowserExtensionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.browser_extension_list


class BrowserExtensionConfiguration(TypedDict, closed=True):
    enabled_browser_extensions: (
        "capo_qbusiness.types.browser_extension_list.BrowserExtensionList"
    )
    """<p>Specify the browser extensions allowed for your Amazon Q web experience.</p> <ul> <li> <p> <code>CHROME</code> — Enables the extension for Chromium-based browsers (Google Chrome, Microsoft Edge, Opera, etc.).</p> </li> <li> <p> <code>FIREFOX</code> — Enables the extension for Mozilla Firefox.</p> </li> <li> <p> <code>CHROME</code> and <code>FIREFOX</code> — Enable the extension for Chromium-based browsers and Mozilla Firefox.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserExtensionConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.browser_extension_list

    out["enabledBrowserExtensions"] = (
        capo_qbusiness.types.browser_extension_list.serialize_json(
            value["enabled_browser_extensions"]
        )
    )
    return out


def deserialize_json(data: dict) -> BrowserExtensionConfiguration:
    out: BrowserExtensionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabledBrowserExtensions") is not None:
        import capo_qbusiness.types.browser_extension_list

        out["enabled_browser_extensions"] = (
            capo_qbusiness.types.browser_extension_list.deserialize_json(
                data["enabledBrowserExtensions"]
            )
        )
    else:
        out["enabled_browser_extensions"] = []
    return out
