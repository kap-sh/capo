"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowTransformation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_sql_transformation_configuration
    import capo_supplychain.types.data_integration_flow_transformation_type


class DataIntegrationFlowTransformation(TypedDict, closed=True):
    transformation_type: "capo_supplychain.types.data_integration_flow_transformation_type.DataIntegrationFlowTransformationType"
    """<p>The DataIntegrationFlow transformation type.</p>"""
    sql_transformation: NotRequired[
        "capo_supplychain.types.data_integration_flow_sql_transformation_configuration.DataIntegrationFlowSQLTransformationConfiguration"
    ]
    """<p>The SQL DataIntegrationFlow transformation configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowTransformation) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_flow_transformation_type

    out["transformationType"] = (
        capo_supplychain.types.data_integration_flow_transformation_type.serialize_json(
            value["transformation_type"]
        )
    )
    if "sql_transformation" in value:
        import capo_supplychain.types.data_integration_flow_sql_transformation_configuration

        out["sqlTransformation"] = (
            capo_supplychain.types.data_integration_flow_sql_transformation_configuration.serialize_json(
                value["sql_transformation"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowTransformation:
    out: DataIntegrationFlowTransformation = {}  # type: ignore[typeddict-item]
    if data.get("transformationType") is not None:
        import capo_supplychain.types.data_integration_flow_transformation_type

        out["transformation_type"] = (
            capo_supplychain.types.data_integration_flow_transformation_type.deserialize_json(
                data["transformationType"]
            )
        )
    else:
        raise DeserializationError(
            "DataIntegrationFlowTransformation.transformation_type required"
        )
    if data.get("sqlTransformation") is not None:
        import capo_supplychain.types.data_integration_flow_sql_transformation_configuration

        out["sql_transformation"] = (
            capo_supplychain.types.data_integration_flow_sql_transformation_configuration.deserialize_json(
                data["sqlTransformation"]
            )
        )
    return out


def redact_sensitive(value: DataIntegrationFlowTransformation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sql_transformation" in value:
        import capo_supplychain.types.data_integration_flow_sql_transformation_configuration

        out["sql_transformation"] = (
            capo_supplychain.types.data_integration_flow_sql_transformation_configuration.redact_sensitive(
                value["sql_transformation"]
            )
        )
    return out
