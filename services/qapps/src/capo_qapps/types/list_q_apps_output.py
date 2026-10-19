"""Generated from Smithy shape ``com.amazonaws.qapps#ListQAppsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.user_apps_list


class ListQAppsOutput(TypedDict, closed=True):
    apps: "capo_qapps.types.user_apps_list.UserAppsList"
    """<p>The list of Amazon Q Apps meeting the request criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQAppsOutput) -> dict:
    out: dict = {}
    import capo_qapps.types.user_apps_list

    out["apps"] = capo_qapps.types.user_apps_list.serialize_json(value["apps"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQAppsOutput:
    out: ListQAppsOutput = {}  # type: ignore[typeddict-item]
    if data.get("apps") is not None:
        import capo_qapps.types.user_apps_list

        out["apps"] = capo_qapps.types.user_apps_list.deserialize_json(data["apps"])
    else:
        out["apps"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
