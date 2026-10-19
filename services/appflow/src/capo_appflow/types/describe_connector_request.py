"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.connector_label
    import capo_appflow.types.connector_type


class DescribeConnectorRequest(TypedDict, closed=True):
    connector_type: "capo_appflow.types.connector_type.ConnectorType"
    """<p>The connector type, such as CUSTOMCONNECTOR, Saleforce, Marketo. Please choose CUSTOMCONNECTOR for Lambda based custom connectors.</p>"""
    connector_label: NotRequired["capo_appflow.types.connector_label.ConnectorLabel"]
    """<p>The label of the connector. The label is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorRequest) -> dict:
    out: dict = {}
    import capo_appflow.types.connector_type

    out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
        value["connector_type"]
    )
    if "connector_label" in value:
        out["connectorLabel"] = value["connector_label"]
    return out


def deserialize_json(data: dict) -> DescribeConnectorRequest:
    out: DescribeConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectorType") is not None:
        import capo_appflow.types.connector_type

        out["connector_type"] = capo_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    else:
        import typing

        out["connector_type"] = typing.cast(
            "capo_appflow.types.connector_type.ConnectorType", ""
        )
    if data.get("connectorLabel") is not None:
        out["connector_label"] = data["connectorLabel"]
    return out
