"""Generated from Smithy shape ``com.amazonaws.lambdacore#RestoreRuntimeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_alias_name
    import capo_lambda_core.types.runtime_arn
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_state
    import capo_lambda_core.types.runtime_timestamp
    import capo_lambda_core.types.runtime_version_name


class RestoreRuntimeResponse(TypedDict, closed=True):
    runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier"
    """The name or ARN of the runtime."""
    runtime_version: NotRequired[
        "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
    ]
    """Echoed back only when the request supplied a RuntimeVersion qualifier."""
    runtime_alias: NotRequired[
        "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName"
    ]
    """Echoed back only when the request supplied a RuntimeAlias qualifier."""
    arn: "capo_lambda_core.types.runtime_arn.RuntimeArn"
    """The fully qualified ARN of the resource that was restored (runtime, version, or alias)."""
    state: "capo_lambda_core.types.runtime_state.RuntimeState"
    """The state of the restored resource, ACTIVE on success."""
    last_modified: "capo_lambda_core.types.runtime_timestamp.RuntimeTimestamp"
    """The date and time when the restored resource was last modified."""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreRuntimeResponse) -> dict:
    out: dict = {}
    out["RuntimeName"] = value["runtime_name"]
    if "runtime_version" in value:
        out["RuntimeVersion"] = value["runtime_version"]
    if "runtime_alias" in value:
        out["RuntimeAlias"] = value["runtime_alias"]
    out["Arn"] = value["arn"]
    import capo_lambda_core.types.runtime_state

    out["State"] = capo_lambda_core.types.runtime_state.serialize_json(value["state"])
    out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> RestoreRuntimeResponse:
    out: RestoreRuntimeResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuntimeName") is not None:
        out["runtime_name"] = data["RuntimeName"]
    else:
        out["runtime_name"] = ""
    if data.get("RuntimeVersion") is not None:
        out["runtime_version"] = data["RuntimeVersion"]
    if data.get("RuntimeAlias") is not None:
        out["runtime_alias"] = data["RuntimeAlias"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("State") is not None:
        import capo_lambda_core.types.runtime_state

        out["state"] = capo_lambda_core.types.runtime_state.deserialize_json(
            data["State"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_lambda_core.types.runtime_state.RuntimeState", ""
        )
    if data.get("LastModified") is not None:
        out["last_modified"] = data["LastModified"]
    else:
        out["last_modified"] = ""
    return out
