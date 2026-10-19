"""Generated from Smithy shape ``com.amazonaws.m2#EnvironmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.arn
    import capo_m2.types.engine_type
    import capo_m2.types.engine_version
    import capo_m2.types.entity_name
    import capo_m2.types.environment_lifecycle
    import capo_m2.types.identifier
    import capo_m2.types.network_type
    import capo_m2.types.string20
    import capo_m2.types.timestamp


class EnvironmentSummary(TypedDict, closed=True):
    name: "capo_m2.types.entity_name.EntityName"
    """<p>The name of the runtime environment.</p>"""
    environment_arn: "capo_m2.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of a particular runtime environment.</p>"""
    environment_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of a particular runtime environment.</p>"""
    instance_type: "capo_m2.types.string20.String20"
    """<p>The instance type of the runtime environment.</p>"""
    status: "capo_m2.types.environment_lifecycle.EnvironmentLifecycle"
    """<p>The status of the runtime environment</p>"""
    engine_type: "capo_m2.types.engine_type.EngineType"
    """<p>The target platform for the runtime environment.</p>"""
    engine_version: "capo_m2.types.engine_version.EngineVersion"
    """<p>The version of the runtime engine.</p>"""
    creation_time: "capo_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the runtime environment was created.</p>"""
    network_type: NotRequired["capo_m2.types.network_type.NetworkType"]
    """<p>The network type supported by the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["environmentArn"] = value["environment_arn"]
    out["environmentId"] = value["environment_id"]
    out["instanceType"] = value["instance_type"]
    out["status"] = value["status"]
    out["engineType"] = value["engine_type"]
    out["engineVersion"] = value["engine_version"]
    import capo_m2.types.timestamp

    out["creationTime"] = capo_m2.types.timestamp.serialize_json(value["creation_time"])
    if "network_type" in value:
        out["networkType"] = value["network_type"]
    return out


def deserialize_json(data: dict) -> EnvironmentSummary:
    out: EnvironmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("environmentArn") is not None:
        out["environment_arn"] = data["environmentArn"]
    else:
        out["environment_arn"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    else:
        out["instance_type"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("engineType") is not None:
        out["engine_type"] = data["engineType"]
    else:
        out["engine_type"] = ""
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    else:
        out["engine_version"] = ""
    if data.get("creationTime") is not None:
        import capo_m2.types.timestamp

        out["creation_time"] = capo_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("networkType") is not None:
        out["network_type"] = data["networkType"]
    return out
