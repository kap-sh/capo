"""Generated from Smithy shape ``com.amazonaws.memorydb#EngineVersionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class EngineVersionInfo(TypedDict, closed=True):
    engine: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the engine for which version information is provided.</p>"""
    engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The engine version</p>"""
    engine_patch_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The patched engine version</p>"""
    parameter_group_family: NotRequired["capo_memorydb.types.string.String"]
    """<p>Specifies the name of the parameter group family to which the engine default parameters apply.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineVersionInfo) -> dict:
    out: dict = {}
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "engine_patch_version" in value:
        out["EnginePatchVersion"] = value["engine_patch_version"]
    if "parameter_group_family" in value:
        out["ParameterGroupFamily"] = value["parameter_group_family"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EngineVersionInfo:
    out: EngineVersionInfo = {}  # type: ignore[typeddict-item]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("EnginePatchVersion") is not None:
        out["engine_patch_version"] = data["EnginePatchVersion"]
    if data.get("ParameterGroupFamily") is not None:
        out["parameter_group_family"] = data["ParameterGroupFamily"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EngineVersionInfo) -> dict:
    out: dict = {}
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "engine_patch_version" in value:
        out["EnginePatchVersion"] = value["engine_patch_version"]
    if "parameter_group_family" in value:
        out["ParameterGroupFamily"] = value["parameter_group_family"]
    return out


def deserialize_cbor(data: dict) -> EngineVersionInfo:
    out: EngineVersionInfo = {}  # type: ignore[typeddict-item]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("EnginePatchVersion") is not None:
        out["engine_patch_version"] = data["EnginePatchVersion"]
    if data.get("ParameterGroupFamily") is not None:
        out["parameter_group_family"] = data["ParameterGroupFamily"]
    return out
