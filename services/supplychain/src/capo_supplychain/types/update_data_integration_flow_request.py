"""Generated from Smithy shape ``com.amazonaws.supplychain#UpdateDataIntegrationFlowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.data_integration_flow_source_list
    import capo_supplychain.types.data_integration_flow_target
    import capo_supplychain.types.data_integration_flow_transformation
    import capo_supplychain.types.uuid


class UpdateDataIntegrationFlowRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>The name of the DataIntegrationFlow to be updated.</p>"""
    sources: NotRequired[
        "capo_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
    ]
    """<p>The new source configurations for the DataIntegrationFlow.</p>"""
    transformation: NotRequired[
        "capo_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
    ]
    """<p>The new transformation configurations for the DataIntegrationFlow.</p>"""
    target: NotRequired[
        "capo_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
    ]
    """<p>The new target configurations for the DataIntegrationFlow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataIntegrationFlowRequest) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_supplychain.types.data_integration_flow_source_list

        out["sources"] = (
            capo_supplychain.types.data_integration_flow_source_list.serialize_json(
                value["sources"]
            )
        )
    if "transformation" in value:
        import capo_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            capo_supplychain.types.data_integration_flow_transformation.serialize_json(
                value["transformation"]
            )
        )
    if "target" in value:
        import capo_supplychain.types.data_integration_flow_target

        out["target"] = (
            capo_supplychain.types.data_integration_flow_target.serialize_json(
                value["target"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDataIntegrationFlowRequest:
    out: UpdateDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("sources") is not None:
        import capo_supplychain.types.data_integration_flow_source_list

        out["sources"] = (
            capo_supplychain.types.data_integration_flow_source_list.deserialize_json(
                data["sources"]
            )
        )
    if data.get("transformation") is not None:
        import capo_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            capo_supplychain.types.data_integration_flow_transformation.deserialize_json(
                data["transformation"]
            )
        )
    if data.get("target") is not None:
        import capo_supplychain.types.data_integration_flow_target

        out["target"] = (
            capo_supplychain.types.data_integration_flow_target.deserialize_json(
                data["target"]
            )
        )
    return out


def redact_sensitive(value: UpdateDataIntegrationFlowRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "transformation" in value:
        import capo_supplychain.types.data_integration_flow_transformation

        out["transformation"] = (
            capo_supplychain.types.data_integration_flow_transformation.redact_sensitive(
                value["transformation"]
            )
        )
    return out
