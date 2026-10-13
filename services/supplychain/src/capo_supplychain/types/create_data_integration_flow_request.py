"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateDataIntegrationFlowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.data_integration_flow_source_list
    import capo_supplychain.types.data_integration_flow_target
    import capo_supplychain.types.data_integration_flow_transformation
    import capo_supplychain.types.tag_map
    import capo_supplychain.types.uuid


class CreateDataIntegrationFlowRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>Name of the DataIntegrationFlow.</p>"""
    sources: "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
    """<p>The source configurations for DataIntegrationFlow.</p>"""
    transformation: "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
    """<p>The transformation configurations for DataIntegrationFlow.</p>"""
    target: (
        "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
    )
    """<p>The target configurations for DataIntegrationFlow.</p>"""
    tags: NotRequired["capo_supplychain.types.tag_map.TagMap"]
    """<p>The tags of the DataIntegrationFlow to be created</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataIntegrationFlowRequest) -> dict:
    out: dict = {}
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
    if "tags" in value:
        import capo_supplychain.types.tag_map

        out["tags"] = capo_supplychain.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDataIntegrationFlowRequest:
    out: CreateDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("sources") is not None:
        import capo_supplychain.types.data_integration_flow_source_list

        out["sources"] = (
            capo_supplychain.types.data_integration_flow_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("CreateDataIntegrationFlowRequest.sources required")
    if data.get("transformation") is not None:
        import capo_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            capo_supplychain.types.data_integration_flow_transformation.deserialize_json(
                data["transformation"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataIntegrationFlowRequest.transformation required"
        )
    if data.get("target") is not None:
        import capo_supplychain.types.data_integration_flow_target

        out["target"] = (
            capo_supplychain.types.data_integration_flow_target.deserialize_json(
                data["target"]
            )
        )
    else:
        raise DeserializationError("CreateDataIntegrationFlowRequest.target required")
    if data.get("tags") is not None:
        import capo_supplychain.types.tag_map

        out["tags"] = capo_supplychain.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateDataIntegrationFlowRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "transformation" in value:
        import capo_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            capo_supplychain.types.data_integration_flow_transformation.redact_sensitive(
                value["transformation"]
            )
        )
    return out
