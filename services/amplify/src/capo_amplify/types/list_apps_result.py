"""Generated from Smithy shape ``com.amazonaws.amplify#ListAppsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.apps
    import capo_amplify.types.next_token


class ListAppsResult(TypedDict, closed=True):
    apps: "capo_amplify.types.apps.Apps"
    """<p>A list of Amplify apps. </p>"""
    next_token: NotRequired["capo_amplify.types.next_token.NextToken"]
    """<p>A pagination token. Set to null to start listing apps from start. If non-null, the pagination token is returned in a result. Pass its value in here to list more projects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsResult) -> dict:
    out: dict = {}
    import capo_amplify.types.apps

    out["apps"] = capo_amplify.types.apps.serialize_json(value["apps"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppsResult:
    out: ListAppsResult = {}  # type: ignore[typeddict-item]
    if data.get("apps") is not None:
        import capo_amplify.types.apps

        out["apps"] = capo_amplify.types.apps.deserialize_json(data["apps"])
    else:
        raise DeserializationError("ListAppsResult.apps required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAppsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "apps" in value:
        import capo_amplify.types.apps

        out["apps"] = capo_amplify.types.apps.redact_sensitive(value["apps"])
    return out
