"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlow``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.data_integration_flow_source_list
    import capo_supplychain.types.data_integration_flow_target
    import capo_supplychain.types.data_integration_flow_transformation
    import capo_supplychain.types.uuid


class DataIntegrationFlow(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The DataIntegrationFlow instance ID.</p>"""
    name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>The DataIntegrationFlow name.</p>"""
    sources: "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
    """<p>The DataIntegrationFlow source configurations.</p>"""
    transformation: "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
    """<p>The DataIntegrationFlow transformation configurations.</p>"""
    target: (
        "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
    )
    """<p>The DataIntegrationFlow target configuration.</p>"""
    created_time: "datetime.datetime"
    """<p>The DataIntegrationFlow creation timestamp.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The DataIntegrationFlow last modified timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlow) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["name"] = value["name"]
    import capo_supplychain.types.data_integration_flow_source_list

    out["sources"] = (
        capo_supplychain.types.data_integration_flow_source_list.serialize_json(
            value["sources"]
        )
    )
    import capo_supplychain.types.data_integration_flow_transformation

    out["transformation"] = (
        capo_supplychain.types.data_integration_flow_transformation.serialize_json(
            value["transformation"]
        )
    )
    import capo_supplychain.types.data_integration_flow_target

    out["target"] = capo_supplychain.types.data_integration_flow_target.serialize_json(
        value["target"]
    )
    import capo_supplychain.types._prelude.timestamp

    out["createdTime"] = capo_supplychain.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_supplychain.types._prelude.timestamp

    out["lastModifiedTime"] = capo_supplychain.types._prelude.timestamp.serialize_json(
        value["last_modified_time"]
    )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlow:
    out: DataIntegrationFlow = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        raise DeserializationError("DataIntegrationFlow.instance_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataIntegrationFlow.name required")
    if data.get("sources") is not None:
        import capo_supplychain.types.data_integration_flow_source_list

        out["sources"] = (
            capo_supplychain.types.data_integration_flow_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.sources required")
    if data.get("transformation") is not None:
        import capo_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            capo_supplychain.types.data_integration_flow_transformation.deserialize_json(
                data["transformation"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.transformation required")
    if data.get("target") is not None:
        import capo_supplychain.types.data_integration_flow_target

        out["target"] = (
            capo_supplychain.types.data_integration_flow_target.deserialize_json(
                data["target"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.target required")
    if data.get("createdTime") is not None:
        import capo_supplychain.types._prelude.timestamp

        out["created_time"] = (
            capo_supplychain.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.created_time required")
    if data.get("lastModifiedTime") is not None:
        import capo_supplychain.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_supplychain.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("DataIntegrationFlow.last_modified_time required")
    return out


def redact_sensitive(value: DataIntegrationFlow) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "transformation" in value:
        import capo_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            capo_supplychain.types.data_integration_flow_transformation.redact_sensitive(
                value["transformation"]
            )
        )
    return out
