"""Generated from Smithy shape ``com.amazonaws.appsync#AppSyncRuntime``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.runtime_name
    import capo_appsync.types.string


class AppSyncRuntime(TypedDict, closed=True):
    name: "capo_appsync.types.runtime_name.RuntimeName"
    """<p>The <code>name</code> of the runtime to use. Currently, the only allowed value is <code>APPSYNC_JS</code>.</p>"""
    runtime_version: "capo_appsync.types.string.String"
    """<p>The <code>version</code> of the runtime to use. Currently, the only allowed version is <code>1.0.0</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppSyncRuntime) -> dict:
    out: dict = {}
    import capo_appsync.types.runtime_name

    out["name"] = capo_appsync.types.runtime_name.serialize_json(value["name"])
    out["runtimeVersion"] = value["runtime_version"]
    return out


def deserialize_json(data: dict) -> AppSyncRuntime:
    out: AppSyncRuntime = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_appsync.types.runtime_name

        out["name"] = capo_appsync.types.runtime_name.deserialize_json(data["name"])
    else:
        import typing

        out["name"] = typing.cast("capo_appsync.types.runtime_name.RuntimeName", "")
    if data.get("runtimeVersion") is not None:
        out["runtime_version"] = data["runtimeVersion"]
    else:
        out["runtime_version"] = ""
    return out
