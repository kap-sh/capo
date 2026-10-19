"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorEntityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.connector_entity_field_list


class DescribeConnectorEntityResponse(TypedDict, closed=True):
    connector_entity_fields: (
        "capo_appflow.types.connector_entity_field_list.ConnectorEntityFieldList"
    )
    """<p> Describes the fields for that connector entity. For example, for an <i>account</i> entity, the fields would be <i>account name</i>, <i>account ID</i>, and so on. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorEntityResponse) -> dict:
    out: dict = {}
    import capo_appflow.types.connector_entity_field_list

    out["connectorEntityFields"] = (
        capo_appflow.types.connector_entity_field_list.serialize_json(
            value["connector_entity_fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeConnectorEntityResponse:
    out: DescribeConnectorEntityResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectorEntityFields") is not None:
        import capo_appflow.types.connector_entity_field_list

        out["connector_entity_fields"] = (
            capo_appflow.types.connector_entity_field_list.deserialize_json(
                data["connectorEntityFields"]
            )
        )
    else:
        out["connector_entity_fields"] = []
    return out
