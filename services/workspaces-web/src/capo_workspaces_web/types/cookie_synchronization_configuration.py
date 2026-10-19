"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CookieSynchronizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.cookie_specifications


class CookieSynchronizationConfiguration(TypedDict, closed=True):
    allowlist: "capo_workspaces_web.types.cookie_specifications.CookieSpecifications"
    """<p>The list of cookie specifications that are allowed to be synchronized to the remote browser.</p>"""
    blocklist: NotRequired[
        "capo_workspaces_web.types.cookie_specifications.CookieSpecifications"
    ]
    """<p>The list of cookie specifications that are blocked from being synchronized to the remote browser.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CookieSynchronizationConfiguration) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.cookie_specifications

    out["allowlist"] = capo_workspaces_web.types.cookie_specifications.serialize_json(
        value["allowlist"]
    )
    if "blocklist" in value:
        import capo_workspaces_web.types.cookie_specifications

        out["blocklist"] = (
            capo_workspaces_web.types.cookie_specifications.serialize_json(
                value["blocklist"]
            )
        )
    return out


def deserialize_json(data: dict) -> CookieSynchronizationConfiguration:
    out: CookieSynchronizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("allowlist") is not None:
        import capo_workspaces_web.types.cookie_specifications

        out["allowlist"] = (
            capo_workspaces_web.types.cookie_specifications.deserialize_json(
                data["allowlist"]
            )
        )
    else:
        out["allowlist"] = []
    if data.get("blocklist") is not None:
        import capo_workspaces_web.types.cookie_specifications

        out["blocklist"] = (
            capo_workspaces_web.types.cookie_specifications.deserialize_json(
                data["blocklist"]
            )
        )
    return out
